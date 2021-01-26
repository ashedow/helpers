# Data Anonymization

Data anonymization is the process of protecting private and sensitive data. This can be done by applying the secured Personally Identifiable Information (PII), which enables the organizations to build an information security environment for masking or anonymizing the information of the user or the source, without losing the business value.

## Directory replacement
The directory replacement method involves making changes to the names of individuals within the data but maintaining consistent relations between other values. For example, you can use a postcode and an ID to identify an individual. In a separate location, you store the information that directly identifies the individual. The data is pseudonymized in this way. To anonymize, you delete the separately stored information that identifies the individual.

## Masking out
This technique allows you to hide part of the data by placing random characters or other data instead. You can pseudonymize by masking identities or important identifiers, and thus still be able to identify the data without manipulating the actual identities. This technique is typical for billing scenarios; the most common example includes the masking of credit card information that is then displayed in the form XXXX XXXX XXXX 4321.

# Scrambling/Shuffling
Scrambling or shuffling simply entails the mixing of letters or digits in the personal data. For example, #458912 may become #298514. Ideally, the process is irreversible so that the original data cannot be retrieved from the scrambled data. The most popular methods here include cryptographic data scrambling, network security data scrambling, as well as the so-called nearest neighbor data substitution (NeNDS). 

## Generalization
This technique has the purpose of reducing the granularity of the data. As a result, the data that is disclosed is less precise than the original data and therefore makes it difficult if not impossible to retrieve the exact values associated with an individual. For example, if you have a database containing the age of certain types of patients, the exact ages of the concrete individuals would be replaced with age groups, e.g. 55-65, 65-75, etc. 

## Blurring
Similar to generalization, this technique reduces the precision of the disclosed data to minimize the possibility of identification. As the name suggests, blurring uses an approximation of data values instead of the original identifiers, making it difficult to identify individuals with absolute certainty. For example, a natural person might be identifiable by an exact account balance at a point in time. Adding small random values to this balance does not introduce significant error into the data but provides anonymity for the affected person.

## Data encryption
This technique translates the personal data into another form or code so that the data that is deemed sensitive is replaced with data in an unreadable format. Authorized users have access to a secret key or a password that makes it possible for them to retrieve the data in its original form. Data encryption brings a variety of benefits when moving to the cloud. These include helping you meet regulatory requirements and providing safe harbor from breach notifications. It allows you to secure your remote locations and sets the ground for secure outsourcing and licensing. It can also prevent service providers from accessing or inadvertently exposing your data.

## Substitution
As the name suggests, this technique allows you to replace the contents of a database column with data from a predefined list of fake data so that the data cannot be traced back to an identifiable individual. This technique has the advantage of keeping the integrity of the original information intact. 

## Nulling out 
In this case, the sensitive data is simply removed and deleted from the data set. All pieces of sensitive information, such as customer name, address, or age, become null values. 

## Number and date variance 
If specifically dealing with numeric and date columns, this anonymization technique may come in question: in this case, each value in a column is modified by a random percentage of its real value. In this way, the data is altered to such an extent that it can no longer be traced back to its original form. 

## Custom anonymization
The method of custom or personalized anonymization is simply about creating and implementing your own anonymization technique or a combination of several techniques. You can do this by using scripts or an application.


***

## Data Masking           
Since the data is exposed to many networks simultaneously, masking it by making altered changes in its value would prevent the source from being detected. These alternations in value can be in the form of modifying database techniques such as shuffling of characters, encryption, or substitution of a character or a word.

This technique, also known as “Swap and replace,” helps replicate the data source for testing, or training purposes, while maintaining the original user security.

## Pseudonymization
As the name suggests, this technique involves data management by replacing the original user name with a pseudonym or swapping the personal identity with the fake identifiers. This helps in data training, data security, data training, and data management by preserving the accuracy and integrity of the data.

## Generalization
Data Generalisation involves removal of the precision from the data set, to make it less identifiable. However, this technique can weaken the statistical accuracy of data but helps in securing the privacy of the people it represents. Google uses Data Generalization before sharing its PII across various services. This can be elucidated in the following manner: removing the house numbers from a particular address or area so that statistical accuracy can be maintained, without breaching the security.

## Data Swapping
Also known as Data Permutation or Shuffing, it applies the principle of Permutation and combination. This technique involves shuffling the attributes of various dataset values across different rows and columns so that the data can be available, without disclosing the name of the user.

## Data Perturbation
This is done by slightly modifying the original dataset by multiplication, subtraction, or adding a numerical value.

## Synthetic Data
This technique utilizes the creation of artificial datasets instead of altering the original ones, without risking privacy or security. The statistical model is created based on the patterns from the original dataset.

***

## k-anonymity

k-anonymity is a property possessed by certain anonymized data. The concept of k-anonymity was first introduced by Latanya Sweeney and Pierangela Samarati in a paper published in 1998[1] as an attempt to solve the problem: "Given person-specific field-structured data, produce a release of the data with scientific guarantees that the individuals who are the subjects of the data cannot be re-identified while the data remain practically useful."[2][3][4] A release of data is said to have the k-anonymity property if the information for each person contained in the release cannot be distinguished from at least {\displaystyle k-1}k - 1 individuals whose information also appear in the release.

***

# Stsandarts

## HIPAA PMI

# Data Privacy Services

## AWS HIPAA


## Links
https://www.analyticsinsight.net/data-anonymization-step-towards-securing-data-organizations/
