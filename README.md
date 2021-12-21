# Web-Portfolio
This is a simple personal web portfolio. If you notice any issues, from grammar to browser display issues, submit a pull request and I'll see what I can do about it.


## How it's built
From a technical standpoint, it's pretty basic: HTML, CSS, and JavaScript. Django is the site's backbone.

Hosted by Heroku at https://olamilekan.herokuapp.com/ and deployed from the "main" branch. As part of continuous delivery, any changes to "main" will be reflected in the live site.

## Repository structure
### Branches
* **main.** This is the Master branch, and the branch Heroku uses to deploy. I don't do any development work here, as I want it to be stable.
* **dev.** Where the magic happens. Here, I sort out bugs and build new features. They get merged with "prod" as they're ready.
