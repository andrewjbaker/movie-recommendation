# Movie recommendation model
### L3T12 University of Edinburgh HyperionDev Software Engineering Online Bootcamp - compulsory task 2

## About
This repo contains a Python program which takes a pre-defined movie title and description, and recommends the best match for the next movie to watch based on a list of movies and descriptions provided.
The solution makes use of the `spaCy` package with the `en_core_web_md` model.

## Installation and setup requirements
This repository includes a Dockerfile to support containerisation.  To create and run the Docker image, you must download Docker on your machine from [here](https://www.docker.com).

Clone the repository locally, navigate to the root and in the terminal/ command line you can build the image using
```docker build -t movie ./```

To run the program, enter the following command in the terminal:
```docker run movie```

## Credits
Developed by Andrew Baker (GitHub: andrewjbaker) as part of the University of 
Edinburgh and HyperionDev Software Engineering Online Bootcamp (2023).

## URL
You can access the repository for this project [here](https://github.com/andrewjbaker/movie-recommendation).
