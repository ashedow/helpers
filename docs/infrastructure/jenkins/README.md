# Jenkins

> www.jenkins.io
> Jenkins is an open-source automation tool written in Java with plugins built for Continuous Integration purposes. Jenkins is used to build and test your software projects continuously making it easier for developers to integrate changes to the project, and making it easier for users to obtain a fresh build. It also allows you to continuously deliver your software by integrating with a large number of testing and deployment technologies.
* It is an open-source tool with great community support.
* It is easy to install.
* It has 1000+ plugins to ease your work. If a plugin does not exist, you can code it and share it with the community.
* It is free of cost.
* It is built with Java and hence, it is portable to all the major platforms.


* Adoption: Jenkins is widespread, with more than 147,000 active installations and over 1 million users around the world.
* Plugins: Jenkins is interconnected with well over 1,000 plugins that allow it to integrate with most of the development, testing and deployment tools.

## Jenkins Architecture

Jenkins uses a Master-Slave architecture to manage distributed builds. In this architecture, Master and Slave communicate through TCP/IP protocol.

### Jenkins Master

Your main Jenkins server is the Master. The Master’s job is to handle:
* Scheduling build jobs.
* Dispatching builds to the slaves for the actual execution.
* Monitor the slaves (possibly taking them online and offline as required).
* Recording and presenting the build results.
* A Master instance of Jenkins can also execute build jobs directly.

### Jenkins Slave

A Slave is a Java executable that runs on a remote machine. Following are the characteristics of Jenkins Slaves:
* It hears requests from the Jenkins Master instance.
* Slaves can run on a variety of operating systems.
* The job of a Slave is to do as they are told to, which involves executing build jobs dispatched by the Master.
* You can configure a project to always run on a particular Slave machine, or a particular type of Slave machine, or simply let Jenkins pick the next available Slave.

![jenkins diagram 1](./jenkins_diagram_1.png)

Jenkins checks the Git repository at periodic intervals for any changes made in the source code.
Each builds requires a different testing environment which is not possible for a single Jenkins server. In order to perform testing in different environments Jenkins uses various Slaves as shown in the diagram.
Jenkins Master requests these Slaves to perform testing and to generate test reports.

##  Pipeline
> https://www.jenkins.io/doc/book/pipeline/syntax/

Can be created from UI or like file.

Sections:
 * `agent` - The agent section specifies where the entire Pipeline, or a specific stage, will execute in the Jenkins environment depending on where the agent section is placed. The section must be defined at the top-level inside the pipeline block, but stage-level usage is optional.

 * `post` - The post section defines one or more additional steps that are run upon the completion of a Pipeline’s or stage’s run (depending on the location of the post section within the Pipeline). post can support any of the following post-condition blocks: always, changed, fixed, regression, aborted, failure, success, unstable, unsuccessful, and cleanup. These condition blocks allow the execution of steps inside each condition depending on the completion status of the Pipeline or stage. The condition blocks are executed in the order shown below.

 * `stages` - Containing a sequence of one or more stage directives, the stages section is where the bulk of the "work" described by a Pipeline will be located. At a minimum, it is recommended that stages contain at least one stage directive for each discrete part of the continuous delivery process, such as Build, Test, and Deploy.

 * `steps` - The steps section defines a series of one or more steps to be executed in a given stage directive.

## Blue Ocean
> https://www.jenkins.io/doc/book/blueocean/

Blue Ocean rethinks the user experience of Jenkins. Designed from the ground up for Jenkins Pipeline, but still compatible with freestyle jobs, Blue Ocean reduces clutter and increases clarity for every member of the team. Blue Ocean’s main features include:
* Sophisticated visualizations of continuous delivery (CD) Pipelines, allowing for fast and intuitive comprehension of your Pipeline’s status.
* Pipeline editor - makes creation of Pipelines approachable by guiding the user through an intuitive and visual process to create a Pipeline.
* Personalization to suit the role-based needs of each member of the team.
* Pinpoint precision when intervention is needed and/or issues arise. Blue Ocean shows where in the pipeline attention is needed, facilitating exception handling and increasing productivity.
* Native integration for branch and pull requests, enables maximum developer productivity when collaborating on code with others in GitHub and Bitbucket.


# Jenkins X

Jenkins X was first introduced by James Strachan (creator of Groovy, Apache Camel) in March 2018. It’s designed from the ground up to be a cloud-native, Kubernetes-only application that not only supports CI/CD but also makes working with Kubernetes as simple as possible. With one command you can create a Kubernetes cluster, install all the tools you’ll need to manage your application. You can also create build and deployment pipelines, and deploy your application to various environments.

## Jenkins Vs Jenkins X
| Jenkins	|  Jenkins X |
| :------------- | :----------: | -----------: |
| Jenkins takes an unopinionated view   |  Jenkins X takes an opinionated view |
| In Jenkins, you require several integrations and plugins to configure	| It simplifies the configuration |
| Jenkins adapts to the process according to the requirement |	Defines the process |
| It uses the first GUI approach with the configuration via UI and depending heavily on plugins. |	It adopts a CLI/API first approach and relies on the configuration as code to embraces external tools |
