# Notes During Test

## Running Thoughts
That is a lot of stuff I need to accomplish. I actually haven't set up this computer for terraform or anything (Using non-work computer), so lets do that first.

Ok that is done, Windows machines are weird to install Terraform and Python.

They use Flask/Terraform/Ansible/Nomad. Haven't used a lot of Nomad so lets use ElasticBeanstalk as I know that a little better. Haven't had to write my own microservice in a while.

Nice tutorial, lets use this as jumping off point: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

Error spinning up Env. It is because I have used python 3.9 (default download when you go to python) but they need 3.7. So all my packages are 3.9 and can't be installed in 3.7. Going to download/change that now.

The requirements are for the flask app, you will need to install awsebcli to run eb commands

Make sure you have your aws credentials where they should be for aws commands to run correctly

Had to recreate my Beanstalk environment because of the failure earlier. Hope this time it works, already burned almost 1.5 hours just trying to set this up.

Getting a 502, most likely due to the load balancer not able to talk to the instance behind it.

Heh, Forgot that EB expects the object instance to be called `application`, changing that now.

Woot! Application is loading correctly now. The next choice is do I work on the application or the CI/CD? 

My view in almost everything I do can be boiled down to 3 steps: `get it working, get it right, get it fast`. So following this the application isn't working yet and that is the most important part as the CI/CD I would argue is part of getting it right.

Got the application to reverse and uppercase, but not using the shoutcloud.io, so changing that now

Ok, got shoutcloud to work for me. Going to clean up the application code a bit and then see if I can automate the EB work.

Need to write down steps for how to spin up the EB via commandline.

Currently editing WriteUp file for what my next steps would be. This file is for seeing my thoughts and work as I progressed, while that file would be the professional "Readme" and future steps of the project.