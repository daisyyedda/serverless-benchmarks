# UW Serverless Benchmarks
This repository contains code that rewrites a portion of the existing popular benchmark [DeathStarBench/socialNetwork](https://github.com/delimitrou/DeathStarBench/tree/master/socialNetwork) into a serverless way.

## Application Structure
Supported actions:
- Register using user credentials
- Login using user credentials
- Create text post 
- Create media post (supported media: image, video, shortened URL, user tag)
- Receive recommendations on which users to follow
- Database Storage (RDS) of User Information
