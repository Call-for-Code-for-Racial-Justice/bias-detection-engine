# Bias and Disparity Detection Engine for Open Sentencing Solution  
(for analysis of Federal US Sentencing Comission Datasets only)

This solution starter was created by technologists from IBM.

## Table of Content

1. [The Team](#1-team)
2. [Overview](#2-overview---racial-disparity--bias-diagnostics-engine)
3. [The idea](#3-idea)
4. [How it works](#4-functionality---how-it-works--how-ibm-technology-can-help-detect-diagnosis-and-remediate-implicit-racial-bias)
5. [Architecture Diagrams](#5-architecture----bias-diagnostics-engine-architecture)
6. [Prototype-Working Code](#6-prototype-working-code)
7. [Datasets](#7-datasets)
8. [Technology](#8-technology)
9. [Vision](#9-vision---fully-scaled-ibm-disparity-detection-and-bias-diagnostics-engine)
10. [Getting started](#10-getting-started)
11. [Resources](#11-resources)
12. [License](#12-license)


## 1. Team

* Denise Knorr - Product Manager
* Boz Handy Bosma PhD - Vice-President IBM Academy of Technology
* Sam Hoffman - AIF360 Developer
* Margriet Groenendijk PhD - Data & AI Developer Advocate   
* Hema Veeradhi - Red Hat Software Engineer    
* Kate Tereshchenko - Cloud Data Scientist
* Ann Marie Fred - CFC Sentencing Reform Team
* Demi Ajayi PhD - Prod Designer – AI Natural Language
* Otis Smart PhD - AI Data Scientist - Machine Learning

## 2. Overview - Bias & Disparity Detection Engine (BDDE) for Open Sentencing Solution Federal US Sentencing Comission Data Sets Only 

* The Bias & Disparity Detection Engine (BDDE) will be powered by IBM’s [AI Fairness 360](https://github.com/Trusted-AI/AIF360) sourced functionality refined to specifically isolate disparity in Federal sentecning outcomes between black and white defendants 
* The BDDE accesses disparity by comparing the average months of encarceration perscribed in Federal Sentencing Guidelines against a historical profile of actual sentences for similiar Federal charges aggregated by racial demographics

### Problem Statement - Reason why deployment of this type of Bias detection technology is a so critical at this moment in time

A new class of “Tech for Good" solutions, apps and platforms will strive to inform outcomes that can be mathematically assessed and validated as being free of racial bias.

1. This new class of solutions prioritizes the minimization of outcomes infected by implicit racial bias and replicated disparities. This will need leading edge technology and newly developed interface protocols to effectively serve as a universally accepted fair and “Credible Arbiter” of bias and other discriminatory variables.

2. Without validated and benchmarked models for consistent attribution and remediation of implicit racial bias, solutions like CFCRF Open Sentencing might have diminished ability to deliver insight and outcomes that can be universally seen as mathematically and repeatably accurate in identifying and diagnosing racial bias as it may exist in the process pipeline and datasets associated with the functions of the solution.
    *	A random / one-off approach to detecting and remediating implicit racial bias in processes and code will not be sufficient for solutions like Open Sentencing and may lead to ethics exposures related to how the sicence of bias detection is applied.

3. These problems are hardened by fact that many bodies of authority (governmental / corporate / financial) may continue to deny the existence of Implicit bias and Systemic Racism.  Therefore mathematically grounded technology like the Bias and Disparity Detection Engine will be extremely critical to ensure proper progress can be made in efforts to address societal and structural factors that lend themselves to racially biased outcomes.

## 3. Idea

![Architecture](/images/Open%20Sentencing%20Architecture%20Process%20Flow%20-%20Oct%2017.png)

## 4. Functionality - How it works - how technology can help detect and highlight racial disparities in datasets related to the Open Sentencing process pipeline 
The Bias & Disparity Detection Engine analyzes available historical data and case specific data provided by the Open Sentencing Public Defender to provide the public defense attorney user with insights and bias/disparity indicators for each case. Public defenders can then act immediately on that information to negotiate a better plea or sentence for the defendant.  Scope is currently focused on anlysis of one crime type related to Drug Posession / Trafficking. 

By leveraging existing and enhanced IBM technologies like AI Fairness 360 and Big Data Analytics  the Bias & Disparity Detection Engine will provide benchmarked hardened data analysis protocols detecting disparity in how Federal Sentencing Guidelines are applied in final sentencing outcomes based on aggregation of historical sentencing outcomes by race.

### Success & Proof Points - What proves success
The BDDE will have a cloud based API that will receive a case specific dataset from the Open Sentencing Solution Aggregator in order to determine which Federal Sentencing Guidelines should be applied as relevant for the defendant being charged. The BDDE compares the Federal Sentencing Guidelines midpoint against historical outcomes of similiarly charged defendants. Success is achieved when the BDDE isolates the positive or negative devidation (in number of months) historially applied in actual sentening outcomes in that jurisdiction and passes the results of that analysis back to the Open Sentencing Solution Aggregator for presentation to the Public Defender via the solution's Report Generator.

Critical components of the BDDE outputs will be fed back to the Open Sentencing Aggregator via APIs and will provide analytic and contextual insights that include:
1. \# of similarly charged Sentencing Documents evaluated
2. % white male vs % black male reflected in the historical pull of Sentencing documents
3. % white males with positive and negative deviations from sentencing guidelines
4. % black males with positive and negative  deviations 
5. Nature of deviations by demographics (ie plea deals, min vs max judgments, fines assessed, etc) 


## 5. Architecture -  Bias & Disparity Detection Engine Architecture

![Architecture](/images/Diagram%20%231%20for%20ReadMe%20-%20BDDE%20Architecture%20Data%20Set%20Flow%20-%20Oct%2017.png)


## 6. Prototype - Working Code

Initial data science exploratory Jupyter notebooks are available and show analyze of simulated Federal Sentencing Outcomes data sets as comopared to Federal Sentencing Guidelines. [here.](/notebooks)

Notebook #1 shows actual Federal judicial sentencing hostorical datasets and describes the disparity in historical outcomes by race and gender. 
[Judicial Bias Notebook](/notebooks/judicial_bias.ipynb) - 

Notebook #2 shows a view of simulated data fact patterns that reveal that a large proportion of black defendants are offered and take a plea bargain deal which results in a disportionately negative deviation from the Federal Sentencing Guidelines mid-point.
![Judicial Bias](/images/Judicial_Bias.png)


## 7. Datasets - Data Model Examples and Links to related Notebooks
The data sets used in our initial analysis/notebooks can be sourced from publically available data found in the United States Sentencing Commissioni public domain [here.](/data)

Initial input dataset describing the charges against the defendant will be provided to the BDDE by the Aggregator in the OpenSentencing Solutioin as provided by the Public Defender user of the solution. 

**Dataset #1 Example : Bias & Disparity Detection Engine acccepts initial dataset from Open Sentencing Solutioin Aggregator**
The Open Sentencing solution will pass the BDDE the initial dataset describing the defendants' charges, race, gender, and prior history based on data input into the solutions questionnaire by the user Public Defendant or Defense Attorney  


**Dataset #2 Example : Sentencing Guidelines and actual historical sentencing outcomes captured from Federal Sentencing Commission domain to isolate specific fact paterns**
XXXXXXXX NOTE TO John / Boz...  put Hema Notebook url here-----   https://github.com/embrace-call-for-code/bias-detection-engine/tree/master/notebooks
- Similar crimes to compare
- Average sentencing data by conviction
- Disparities in sentencing by race
- How deviation from guidelines is currently showing up in the charging outcomes - Especially for crimes similar to this one
- Lesser charges for privileged groups?
- The "priors" of the person accused: prior convictions
- Demographic information about the defendant
- Factors that will help the accused decide whether to go to trial - hard data based on the charges
- Likely outcome of bail hearing - what percentage get bail, what percentage sit in jail and for how long
- If you plead not guilty, what are your chances of being found guilty vs. innocent
- If you're found guilty, what are the usual sentences?
- Strength of evidence?
- At least from the initial data, victim factors,keywords or tone flags that might indicate bias in the case documents
- What happens after people serve their sentence? By sentence type. 

**Example 3: Federal Sentencing Data Simulated historical data to supplement actual historical data collected from US Sentencingi Commission **   

XXXXXXXX NOTE TO John / Boz...  put KateNotebook url here----- https://github.com/Call-for-Code-for-Racial-Justice/bias-detection-engine/blob/master/notebooks/weighted_drug_trafficking_data.ipynb
Due to compressed Call for Code timeline, a set of simulated historical datasets were created to reflect trends indicated in smaller amount of actual historical sentencing data captured in Dataset #2 collected from publically available interactive data found on United States Sentencing Commissioni public portal.   

**Example 4: BDDE Data output dashboard analysis results to be passed back to Open Sentencing Solution Aggregrator**
XXXXXXXXXXX  NOTE to John / Box   put Sam Notebook link here https://github.com/Call-for-Code-for-Racial-Justice/bias-detection-engine/blob/master/notebooks/open_sentencing_demo.ipynb
1. # of similarly charged Sentencing Documents evaluated
2. Show the data by type of crime2. 
3. % white male vs % black male reflected in the historical pull of Sentencing documents
4. % white males with positive and negative deviations from sentencing guidelines
5. % black males with positive and negative  deviations 
6. Nature of deviations by demographics (ie plea deals, min vs max judgments, fines assessed, etc)  show the data per jurisdiction


## 8. Technology
Main Code for BDDE for Open Sentencing Solution is located here
XXXXX  John / Box... please add link here ----  https://github.com/Call-for-Code-for-Racial-Justice/bias-detection-engine/blob/master/server/routes/engine.py

- For initial version, we are creating a set of python programs with a Flask front end and APIs for organnizations to provide metamodel and instance to be assessed for systemic disparities and biased outcomes.
- The APIs will enable specification of a steps in a structured process, and to provide sets of data to be analyzed.  We also currently provide python code to generate both unbiased and biased data in order to simulate outcomes for a given metamodel.
- We will add additional security controls to allow organizations to assess only their own data.
- We will provide hooks into one or more IBM Cloud AI offerings such that unstructured data can be uploaded for analysis using the chosen training method.  This will enable adopters of the code base to provide keys that will enable use of a trial or production version of the AI offering and to provide training.
- We will use IBM Carbon Framework with Github Pages (likely Gatsby) to provide content for developers.  (we will edit this statement to update what has been completed during the fortification period).
- Enhance the existing python scripts so we have a general way to identify the set of data with number of steps and the labels for the steps
- Create a flask application with a front end so we can give developers specs for their metamodel (list of name value pairs)
- Jupyter Notebooks and D3 Visualization Library using

## 9. Vision - Fully Scaled IBM Disparity Detection and Bias Diagnostics Engine
- IBM Cloud will play a prominent role in our solution, though we will use Openshift to ensure multi-cloud capability. IBM Data and AI capabilities such as natural language understanding, geospatial analysis, and big data analytics will play a critical role in an overall solution to end systemic racism. By providing bindings into key IBM cloud capabilities like machine learning, we will be able to analyze structured data in any sequential pipeline or funnel affecting black lives, identifying key areas of disparity for each step, end to end. Moreover, we will provide a solution to collect and bind semi-structured and unstructured text associated with any step in a structured process we analyze. Using IBM storage and database technology, we will be able to accept and federate large data volumes in a secure fashion and perform any and all forms of analysis that might be required to analyze that process. IBM data analysis capabilities will then position users to analyze relationships among pipelines, quantifying their cumulative effect in distilling and amplifying systemic racism and its impact on the lives experience of black persons. We have established relationships with advanced practitioners who would be interested in approaching this topic of mathematically quantifying racial bias from an AI Big Data and quantification perspective.

- [AI Fairness 360](https://github.com/Trusted-AI/AIF360). As a stretch goal, during the fortification period, we will add selected features to provide an automated front end for selected AI Fairness 360 algorithms.  Alternatively, on the advice of the CFC Core Team, DE's, and IBM Fairness 360 owners, we may receive data and process it to allow for Fairness 360 to use existing APIs and data access methods.

- We will include privacy preserving features, as well as guidance in Github pages and the readme.  
Depending on legal review, we may offer a license for contributed data to be provided to peer organizations to allow for benchmarking, for example across an industry or profession.

- We will explore GraphQL for integrating data sets from multiple organizations. This likely will be a contributed feature or we may choose a different standard or way of providing aggregated queries. Due to time constraints, we omitted IBM Blockchain from this solution, but we see vast potential for integrating blockchain with this solution. We are exploring these options with technical leaders in IBM Research and the IBM Blockchain business unit.

- We intend to create the basis to measure racial disparity and diagnosis when, where and how racial bias contributes to those disparities. This detection and diagnostics capability can be applied to structured processes relevant to full range of processes currently plagued by effects of Systemic Racism worldwide including hiring & promotion processes, education and school application screening and testing processes, home loans, business loans, professional certifications, civil reforms, and policing and criminal justice reforms.  This will better position organizations that currently exhibit or pass through systemic racism to remedy their processes and  hold themselves and their peers accountable for making tangible progress toward eliminating the effects of systemic racism. Each of these processes currently takes racially flawed input, and in almost all cases does not improve substantially on those inputs when the processes are complete. The organizations who own those processes often assert that their processes are unbiased or neutral; they blame their disparate outcomes on disparate inputs inherited from other processes. This is a central defining feature of systemic racism. Using open source and the unique abilities of IBM data and AI, we will provide the basis for owners of these processes and these stakeholder to identify specific areas of greatest systemic disparity, to define experiments and remediations to address those disparities, and to demonstrate tangible progress.

## Future state of the engine will also fully integrate the following technologies
- Blockchain to establish consensus about data sharing
- Accountability Scoring
- Privacy Preserving
![Future Vision](/images/Bias%20Engine%20%20future%20Vision%20-%20Sep%203%20%20.png)

## 10. Getting Started -
### To use current scripts:
1. Clone repo
2. Define steps for structured process
3. Create data file to be analyzed
4. In Jupyter Notebook, adapt script to apply to structure process and data file
5. If generating data, use data generation python script.
### To contribute functionality:
1. Clone repo
2. Consult readme file and gh pages (pending)
3. Develop feature
4. Contribute via Github Pull Request
5. Contact developers via Github ID

### What preferred external partners you could work with to test solution?
A.	Legislators who strive to leverage technology to help them ensure that new laws and legislation is free of bias that can lead to disparity in how the laws / legislation impact minorities constituents / citizens  
- **United States Sentencing Commission** - created by Congress in 1984 to reduce sentencing disparities and promote transparency and proportionality in sentencing. The Commission collects, analyzes, and distributes a broad array of information on federal sentencing practices.  The Commission also continuously establishes and amends sentencing guidelines for the judicial branch and assists the other branches in developing effective and efficient crime policy .

B.	Pioneers in deploying solutions that feature avoidance of implicit bias, racist algorithms and processes, and misinformation … especially when solutions are related to Diversity & Representation / Police and Judicial Reform / Policy & Legislation
- **A Starting Point** - a channel of communication and connectivity between Americans and their elected officials with the goal of creating a more informed electorate.

C.	Corporate enterprises who strive to strip racial disparity and implicit bias from their internal technology enabled processes
- **SHRM** - the Society for Human Resource Management, creates better workplaces where employers and employees thrive together. As the voice of all things work, workers and the workplace, SHRM is the foremost expert, convener and thought leader on issues impacting today’s evolving workplaces

D.	Jurisdictions who strive to demonstrate efforts to respond to public calls to cleanse racial bias from outcomes
- **Minneapolis City Council** – working to redefine policies / structures for policing going forward after George Floyd reckoning

E.	**Polling enterprises** that may have data sets that are optimal for testing how racial or implicit bias in questions can impact the outcomes

F.	**Social Scientists, Researchers, Academicians** who want to contribute to the science of AI being used to detect disparity and implicit bias tied to Systemic Racism  



## 11. Resources
- **United States Sentencing Commission**: Created by Congress in 1984 to reduce sentencing disparities and promote transparency and proportionality in sentencing. The Commission collects, analyzes, and distributes a broad array of information on federal sentencing practices.  The Commission also continuously establishes and amends sentencing guidelines for the judicial branch and assists the other branches in developing effective and efficient crime policy .

- Measuring Bias in Machine Learning: The Statistical Bias Test - https://www.datacamp.com/community/blog/measuring-bias-in-ml
a defining statistical bias in a machine learning model and demonstrate how to perform the test on synthetic data.

- 5 Types of bias & how to eliminate them in your machine learning project: - Sample, Exclusion, Observer, Prejudice, Measurement bias. An introduction and an example to each   https://towardsdatascience.com/5-types-of-bias-how-to-eliminate-them-in-your-machine-learning-project-75959af9d3a0

## 12. License
This project is licensed under the Apache 2 License - see the [LICENSE](/LICENSE) file for details.

- Content license pending legal guidance
