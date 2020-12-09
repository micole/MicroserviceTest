#Flask Test Documentation
##Setup:
Follow the instructions to set up your AWS credentials if you haven't already: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

```commandline
$ git clone [repolocation]
$ cd [localrepo]
```

If you want to run the flask app locally:
```commandline
$ virtualenv devenv
$ source devenv/bin/activate
$ pip install -r requirements.txt
```

Make sure you have the EB CLI tool installed in (hopefully separate environment) pip:
```commandline
$ pip install awsebcli
```

Run through creating your EB setup:
```commandline
# Do it in one line:
$ eb init -p python-3.7 flask-test --region us-east-2
# Do it in interactive mode
$ eb init

# Create your flask Env
$ eb create flask-env
```

Every time you want to update your application in EB (make sure you have everything committed first):
```commandline
$ eb deploy
```

##Things to improve and next steps
- Not hooked into ci/cd pipeline at all, everything is manual.
- Would hook into GitHub actions to deploy on commit.
- No error handling for things like not able to hit the Shout api.
- Default notifications for EB, would want to send those to slack/pagerduty.
- No configuration on scaling, however EB does a decent default job: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.managing.as.html
- No route53 record (would either do this in Terraform or see if EB has a way of making/updating one)
- Application has pretty generic names for things and not laid out very well for adding more functionality. If needed to add more api endpoints I would make application.py a gateway for the flask application and have the other endpoints modules/files that the application.py calls out to.
- Would look into having two requirement files, one for deployment/testing and one for production (seeing as how you don't need the EB CLI in the requirements file, but we want to make it easy for people to setup to test)
- Haven't tested it on a Mac yet, so the requirements might not be the same/easy to install.
- No automated rollback if you upload a broken configuration to EB. Would want to make it deploy to a test environment first instead of prod.

##End Thoughts
All in all there are lots of things I would like to do to fix/edit this project. Didn't get around to setting up the CI/CD which is personally upsetting but hope that the CLI tool is easy enough for people to set up and deploy as EB is very easy to deploy for testing like this.
