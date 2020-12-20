# IOT Aquaponics in NYC; a thrilling & expensive romaine lettuce.

## Goal
I want to serve my friends lettuce that I grew myself, fertilized by fish-poop generated nitrates from a Recirculating Aquaculture System in my bedroom, and managed by the internet (of things!). 

If you're like most people I've said this to, you probably just thought "Lol, why?"

Simply put: It's an opportunity to dig into the role technology can play in a key challenge of our generation. Plus, it may turn out to be really, really fun.

## Prototype motivation
This section is boring if you just care about the tech or what a $$$$$ piece of lettuce looks like, I just need to get it off my chest. 

You would call me stubborn if I didn't explore the ag-tech and aquaculture industries: they tackle **a key challenge of our generation**, are **full of technical opportunities and challenges**, and may be a way to **re-kindle my aquarist addiction**. 

### 1. A key challenge: Feeding a growing, changing planet.

By 2050, we'll have to feed more than 2.5 billion more people in a world whose climate is uncertain. That's like suddenly seeing 7.6 more USAs pop up, all crying for more more MORE food. Best of all, this exponentially growing food requirement will exist while we collectively realize the impact of decades of unsustainable ecological practices. How fun. Luckily, the avenues to tackle this problem are plentiful and you can niche out -- supply chain, genetic engineering, environmental control, robotics & automation, monitoring & alerting, etc. 
	
Some emerging solutions remove the need for or tackle several avenues at once. One very promising example are the automated, indoor vertical farms utilizing highly controlled [hydroponic environments](https://en.wikipedia.org/wiki/Hydroponics#:~:text=Hydroponics%20is%20a%20type%20of,solutions%20in%20an%20aqueous%20solvent). [Bowery Farming](https://www.youtube.com/watch?v=-Epa1jEwMwk&ab_channel=GoldmanSachs) is a key example, they're growing leafy greens without pesticides, 95% less water than traditional farming methods, and see 100x yields on the same acreage of land. Oh, the (now first of several) farm is in BROOKLYN, so forget about needing to ship across country for fresh produce. So, how do they do it, what challenges might they face, and can I create a tiny prototype to understand more? 
	
###	2. Technical speaking, it's rife out here. 

Farming is as old as dust, and it's become obvious that tech is helping farmers become as productive as possible. You probably guessed it, but ag-tech is the technologization of agriculture industry and it's happening now. AgFunderNews estimates that in [*each* of 2018 and 2019, global VC investment in ag-tech passed $4 Billion and is up 370% since 2012](https://agfundernews.com/farm-tech-investment-up-370-in-6-years-how-will-covid-19-impact-2020-trends.html). 

![Annual Farm Tech Financings](https://i.imgur.com/h4VF0oU.png)
  
Ventures funded are as interesting as it gets, from growing meat in a lab to creating autonomous vehicles for crop management, and it's hard to wrap my head around all the roles tech can play in the space. As a PM-in-tech-for-4-years, missing the boat is awesome, right?  
	
Ok, up next: Dude, what is up the with the fish? 

### 3. Fun in the sun: Aquaculture as a productive & creative outlet

Fish (the only pets my parents let me keep in my shared NYC Bedroom) have been an obsession of mine since I could pick my nose. It's hard to express how fast you'll lose me if we walk to an aquarium store together or if we're snorkeling around a reef. Well, is fish keeping just a childhood hobby? It turns out that there's a whole industry around it. 

	
When I discovered that [farmed aquatic products now account for MORE THAN HALF of the world's consumed seafood](http://www.fao.org/3/I9540EN/i9540en.pdf), my jaw dropped. Aquaculture, aka fish farming, has steadily grown in production, innovation, and demand since I've been alive. What opportunities exist in this new normal that I could start learning about today, and do I like them enough to turn this interest into a passion? 

![World Capture Fisheries and Aquaculture Production](https://i.imgur.com/3AOCYeE.png)

So what can tie feeding the world, ag-tech, and fish keeping together? It turns out that fish poop decomposes into Nitrates, which is key ingredient in commercial fertilizers, and can be delivered to plants via hydroponics. This well established method is called Aquaponics, and can provide insights into each of these three motivations. What better way to learn than to try? 

Aaaabd gere we are. This first stab at home-grown fish poop salad is meant to be all wrong (or right, depending on your outlook); it's filled with hacks, peer borrowing, inconsistent design patterns, cut corners, wilted lettuce, ugly on the eyes, cost inefficient. Thankfully, it's educational for the enthusiast in me.

## Requirements
Because this project is to explore more about the role technology can play in ag & aquaculture, you'll notice that there are no strict data or yield requirements, so the "results" section is going to be seriously subjective and lacking to the data-inclined. This makes the PM in me gasp, but I'm not trying to build a system that produces the fastest / tastiest / prettiest lettuce, so I'm cool with it.  

**Functional: An aquaponic system**
1. Grow lettuce or other leafy greens from seed to harvest 
2. Monitors & alerts on at least 1 system parameter
3. No additional fertilizers for plants (e.g. soil, nutrients)
4. When functioning successfully, does not require human intervention to operate
	
**Technical: IOT, please.**
1. No technology restrictions -- can use any platform(s) for communication
2. Sensor input drives mechanical behavior of the system
3. Microcontrollers/computers (Arduino, Raspberry Pi) are in the party 
4. No hardware-based schedulers (i.e. timer-based outlets)
	
**Product: Leafy greens, for friends.**
1. At least 1 piece of edible lettuce
2. At least 1 friend eats #1
	
By intentionally overcomplicating the requirements I get to learn a bit more about designing & engineering in this space. For example, technical requirement #4 means I have to code up time-based control, which can be both dangerous (i.e. pump never turns off and I flood the beds) and complicated (why not just use a timer?), but helps me understand how this may work at scale. 

## Design 
I decided to build an [Ebb & Flow](https://en.wikipedia.org/wiki/Ebb_and_flow#In_Hydroponics) aquaponic system with goldfish (and a pleco), as this lets me engineer for the above requirements while generating data surrounding my project motivations. [Other hydroponic solutions](https://sensorex.com/blog/2019/10/29/hydroponic-systems-explained/)(deep water culture, NFT, Aeroponic, Drip, etc.) seemed like there would not be enough variables to play with and would provide inadequate filtration opportunities for the water. 

Here's the 5 minute, pen and paper science fair design (I have lots of cool colored pens now, it's awesome):

![Basic design sketch of aquaponic system](https://i.imgur.com/OK3ab98.png?1)

1. **Fish tank / poop factory:** 12 baby goldfish and one pleco live in this 27 gallon tote from Home Depot. Some substrate should be in here for ammonia-eating bacteria growth. Most of the "systems" engineering happens here (pumping, water monitoring, etc), and this supplies key nutrients to the grow bed (after the nitrogen cycle completes, of course). 
2. **Water highways:** Ebb & Flow systems supply nutrient-rich water to a grow bed several times a day. My system does this 4 times throughout the waking hours (it was really loud at night!) for 15 minutes, and then allows the water to drain through each tube back into the poop factory.
3. **Grow bed & plants:** I used an old storage container for this, and fitted the water highways using ebb & flow connectors that I found online. The plants were the cheapest romaine lettuce seeds I could find on Amazon.
4. **Photosynthesis generators:** I used the smallest, cheapest T5 bulbs. 
5. **Computer & microcontrollers:** The heart of the project is the brains -- how to communicate instructions between sensors, pumps, and lights. Here, we'll use a Raspberry Pi communicating to several Wyze Wifi plugs for system control, and do local data processing for monitoring through the cheapest sensors money could buy. 

***This is not novel at all.*** It's actually probably laughable to the hydroponics & aquaponics communities. There are incredible examples online that blow this one out of the water (hah, get it?), below are some that influenced and motivated me to get this prototype up and running: 
- [Hydroponic Flood and Drain "How-To" Custom Build!! On The Grow](https://www.youtube.com/watch?v=K4rb5pGYQdU&ab_channel=OnTheGrow)
- [Starting an Aquaponics System | How to Start & What You Need](https://www.youtube.com/watch?v=1q_MN4kZRlY&t=934s&ab_channel=RobBob%27sAquaponics%26BackyardFarm)
- [Kyle Gabriel's Automated Hydroponic System Build](https://kylegabriel.com/projects/2020/06/automated-hydroponic-system-build.html)
- https://farmerfrog.org/about/ (I got to volunteer here a few times to help build the 2nd aquaponics greenhouse!)
- https://eatupwardfarms.com/our-story
- The [r/aquaponics](https://www.reddit.com/r/aquaponics) community
- [And many, many more.](https://en.wikipedia.org/wiki/Aquaponics#Current_examples)

## System in action
Not all requirements have been fulfilled yet, but the system has been up and running for the month f November & December. I'll film a video when I'm home from a lil vacation (oh, what?! It's working?! Yeaaaaaahhh!!!), but for now here are a few pictures of the system & growth. 

*Whole system:*

![System selfie](https://i.imgur.com/DawOkqA.png)

*Seed germination:*

![Seed germination](https://i.imgur.com/fucwPgS.png)

*First planting:*

![First planting](https://i.imgur.com/xc6t5HS.jpg?1)

*Growth so far:*

![My best grower](https://i.imgur.com/kHlQGqE.jpg?1)

*What I'd do differently:*
- I was originally planning on just flooding until the grow bed flooded, and stop after water flow was detected. This would have been cool but the plants definitely did not get enough nutrients so I scrapped that idea.
- I bought grow lights for $12 from someone on FB marketplace and the lettuce just could not grow. It was stringy and weird! I ended up purchasing way stronger lights and that fixed it.
- I put the plants in too early into the nitrogen cycle that was happening, and some really withered from too little nutrient supply. I'd wait for an established tank before planting greens. 
- Butter lettuce is probably better for this application -- maximizing vertical space is required for compact growth. 
- I suck at germination and propagation, I should push the seeds deeper into the rockwool cubes so their roots can support the weight of the plant. 


## Insights & takeaways (so far)

*Industry*
- **Raising fish and lettuce isn't just another software product -- there's an actual lead time?** 4 years working in software took me out of the world where you actually need to create a PHYSICAL product to get the moniez, and it's not on your own timetable or requirements. System malfunctions can be super costly to production (if you're raising fish and your oxygen supply dies, all fish are dead fish in minutes!). This will be an interesting challenge for tech people entering the agriculture space, unless their product isn't the end product of agriculture itself.
- **[RAS](https://en.wikipedia.org/wiki/Recirculating_aquaculture_system) is a controlled, tech-centered way to go, if we can get it going.** If the aquaculture industry wants to do what Bowery & Aerofarms is doing to the leafy greens industry, it seems interesting to continue down the RAS path and eliminate climate & environmental factors from their production. The upfront cost and long lead times though is pretty intense so I'm interested in exploring this more. ([Atlantic Sapphire](https://www.bizjournals.com/southflorida/news/2020/09/18/atlantic-sapphire-bets-on-south-florida.html) is a great example of what the current state of RAS looks like, both from upfront costs, opportunity, and hiccups, but why limit to salmon?).
- **Growth optimization is everywhere.** The data you can collect to optimize growing conditions is abundant, and will provide a competitive advantage on yield. Companies that store & have plans for optimization with this data are likely to succeed in the indoor farming space. I'd like to explore it more, and specifically didn't in this project because things like an automatic pH sensor can cost hundreds of dollars. 
- **Efficiently converting energy to light will be a key challenge for indoor farming.** It seems like grow environments for these systems balance between greenhouses and indoor vertical. When land is expensive, vertical will be required, but operational costs in terms of energy required may put a limit to scale. Where is the Elon Musk of LED lighting? 

*Tech:*
- **Low-code platforms for event-driven functionality are fun and dramatically cut down dev costs.** I got to play with two in this project: [IFTTT](https://ifttt.com/) for water and light control & [Node Red](https://github.com/node-red) for temperature and heating. This feels like a better way to connect services, apps and devices, though I am concerned about scale, reliability, and responsiveness for commercial systems. 
- **At-home hydro/aquaponic systems have a low barrier to entry and can be great educational tools.** It's hard to predict whether small in-home systems will be adopted by consumers as the effort and cost to grow from scratch is wildly higher than just ordering online from a grocery delivery service. It's definitely possible however for small businesses to adopt these systems successfully and with seemingly low upfront and management costs, so I hope to see these everywhere in a few years. 
- **Monitoring & alerting will play a much larger role at scale:** it's easy when you have one grow bed in your bedroom to make sure everything is functioning correctly. At scale, it does not seem like system design will be the biggest question but rather how fast you can identify and mitigate issues to preserve your yields. 
- **WiFi plugs & appliances should be programmable, without compromising security.** I was scared shitless to set up a system of relays right above a splashing water source, and my bud @SamBroner suggested to use WiFi-connected plugs instead. I got some Wyze plugs at 9.99 which were the closest to programmable (through IFTT), but if we want to promote the IOT revolution, it would be way better if people could use them with open APIs to encourage more tinkering, especially with the cost of entry to the industry diminishing. 
- **Open source is dope.** You know this, you're on Github! It was just one of my first experiences getting something built up & running so fast because so many other people contributed to projects I got to use. Thank u!

*Personal:*
- **Blending the physical & digital world is exhilarating.** I have never been more excited to overcomplicate how hard it is to turn on a light bulb. Controlling the physical environment with code was really fun, and I opportunities pop up all over the place (especially living in NYC). I hope I can dive into more future projects to do this in a way that could actually benefit more people than just my learning. 
- **I don't know anything about growing greens.** I think I got lucky with getting a yield so far, and that nature has just optimized itself against idiots like me. This part was something I did not want to dive deeper on, I think I was more interested in the systems behind growing these plants than the plants themselves. It will probably be WAY cooler when optimizations come in.
- **Failing fast is better than overthinking <3.** I have spent months researching aquaculture, ag-tech, RAS, hydroponics, etc. But it only took a few weekends to put this prototype together. I'm excited to take this learning to all aspects of my life as it matches my internal drive a bunch.  

## Next steps

For this system:
- Complete water monitoring dashboards 
- Trigger water heater when temp drops 
- Feed 1 piece of lettuce to a friend and film it for this report 
- ----------------------- Project's done ----------------------- 
- Diversify greens grown, include propagating houseplants
- Expand water parameter measurements

For my interests:
- Design an indoor vertical aquaponic system at 50x scale
- Understand energy requirements & technologies for commercial operations
- Join a "grown by the future" community in NYC
- Understand consumer segments, requirements and motivations


