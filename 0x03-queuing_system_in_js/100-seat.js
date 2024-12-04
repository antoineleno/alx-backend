const express = require('express');
const redis = require('redis');
const kue = require('kue');
const util = require('util');

const redisClient = redis.createClient();
const getAsync = util.promisify(redisClient.get).bind(redisClient);
const setAsync = util.promisify(redisClient.set).bind(redisClient);

const queue = kue.createQueue();

const app = express();
const port = 1245;

let reservationEnabled = true;
let availableSeats = 50;

async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

app.get('/available_seats', async (req, res) => {
  const currentSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: currentSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {})
    .save((err) => {
      if (err) {
        return res.json({ status: 'Reservation failed' });
      }
      res.json({ status: 'Reservation in process' });
    });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      let currentSeats = await getCurrentAvailableSeats();
      if (currentSeats > 0) {
        currentSeats -= 1;
        await reserveSeat(currentSeats);

        if (currentSeats === 0) {
          reservationEnabled = false;
        }

        done();
        console.log(`Seat reservation job ${job.id} completed`);
      } else {
        done(new Error('Not enough seats available'));
        console.log(`Seat reservation job ${job.id} failed: Not enough seats available`);
      }
    } catch (error) {
      done(error);
      console.log(`Seat reservation job ${job.id} failed: ${error.message}`);
    }
  });
});

(async () => {
  await reserveSeat(availableSeats);

  app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
  });
})();
