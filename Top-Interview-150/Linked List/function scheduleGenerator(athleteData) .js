function scheduleGenerator(athleteData) {
  let eventSchedule = []
    for (let i = 0; i < athleteData.length; i++) {
      let currentAthlete = athleteData[i];
      for (let j = 0; j < athletes[i].events.length; j++) {
        let currentEvent = athletes[i].events[j];
        let eventExists = false;
  
        for (let k = 0; k < eventSchedule.length; k++) {
          let SchedEvent = eventSchedule[k];
          if (SchedEvent.event === currentEvent) {
              eventExists = true;
  
              SchedEvent.athletes.push(currentAthlete.name);
  
              break;
            }
          } if (eventExists === false) {
          eventSchedule.push({ event: currentEvent, athletes: [currentAthlete.name] });
        }
      }
    }
  return eventSchedule
  }

  let athletes = [
    {
      name: "Simone Biles",
      countryRepresenting: "USA",
      sport: "Gymnastics",
      events: ["floor", "balance beam", "vault"],
      age: 22
    },
      {
      name: "Kohei Uchimura",
      countryRepresenting: "Japan",
      sport: "Gymnastics",
      events: ["vault", "floor", "rings"],
      age: 28,
    },
      /* ...and so on */
    ]


console.log(scheduleGenerator(athletes))