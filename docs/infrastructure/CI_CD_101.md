# CI/CD

* Continuous Integration
* Continuous Delivery
* Continuous Deployment

## Continuous Integration

* Check-in code
* Build
* Run autontion test

Merge code to main branch erly and often.
test faaster than 5 mins or t least shorter thn 15 mins

### Testing

* Sttic Analysis
* Unit tests
* Regression tests
* Acceptance e2e tests
* Performance tests

### Artifact management

Artifact storge
* Repository
* Metatdata
* Package
* Repo server

Docker registry (store docker image)
* Registry - hosts Docker repo
* Repository - continer for particular Docer image versiobs

## Continuous Delivery

* Deploy to env
* Acceptance test
* Promotion

Every change is proven to be deployable at any time.
Visibility - all aspects of the system are visible to every team member
Feedback - Team members are notified about CD problems ASAP and fix them ASAP.
Automted deployment - any version can be deployed to any env.

## Continuous Deployment

* Change management
* Deploy to production

Means that every change is automaticlly deployed to prod. In order to do so CD relies on the results of Continious Delivery  vallidation.

## Pipelines

PreCommit stage
* Change/Pull Request
* Code review
Min build stage
* Merge
* Build
* Test
    * Prepare
    * Deploy
    * Run tests
    * Teardown
* Promote
    * Optional Nightly stage
* Deploy

## CD practices

* Sanity check
* Validation
* Automated rollback
