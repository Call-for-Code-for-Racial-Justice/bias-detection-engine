# Bias & Disparity Detection Engine
(for analysis of Federal US Sentencing Commission Datasets only)

This solution starter was created by technologists from IBM.

## Table of Contents

1. [The Team](#1-team)
2. [Overview](#2-overview---bias--disparity-detection-engine-bdde-for-open-sentencing-solution-federal-us-sentencing-commission-data-sets-only)
3. [The Idea](#3-whats-the-idea-behind-the-bias--disparity-detection-engine)
4. [Functionality](#4-functionality---how-the-bias--disparity-detection-engine-works-with-the-open-sentencing-solution)
5. [Architecture](#5-architecture----bias--disparity-detection-engine-process-flow)
6. [Prototype-Working Code](#6-prototype---working-code-notebooks)
7. [Datasets](#7-datasets---data-model-examples-and-links-to-dataset-notebooks)
8. [Technology](#8-technology)
9. [Vision](#9-vision)
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

## 2. Overview - Bias & Disparity Detection Engine (BDDE) for Open Sentencing Solution Federal US Sentencing Commission Data Sets Only
The Bias & Disparity Detection Engine (BDDE) will be powered by IBM’s AI Fairness 360 functionality, refined to specifically isolate disparity in Federal sentencing outcomes of Black vs. White defendants. The BDDE assesses disparity by comparing the average months of incarceration, prescribed in Federal Sentencing Guidelines, against a historical profile of actual sentences for similar Federal charges, aggregated by racial demographics


### Problem Statement - Why deployment of this type of disparity detection technology is critical
A new class of  “Tech for Good" solutions, apps and platforms will strive to inform outcomes that can be quantifiably assessed, and be validated as free of racial bias and disparity.

1.	This new class of solutions prioritizes the minimization of outcomes infected by implicit racial bias and replicated disparities. Such solutions will need leading edge technology and newly developed interface protocols to effectively serve as credible arbiters of bias and other discriminatory variables.

2.	Without validated and benchmarked models for consistent attribution of implicit racial bias, solutions like CFCFRJ Open Sentencing could not deliver the insight and outcomes users need in order to minimize the impact of disparity and bias on outcomes for their clients.
    *	A random / one-off approach to detecting racial bias and disparity in processes and algorithms will not be sufficient for solutions like Open Sentencing, and may lead to ethics exposures related to how the science of bias detection is applied in solution-specific scenarios

3. These problems are made more difficult by the fact that some bodies of authority continue to deny the existence of implicit bias and systemic racism. Therefore, mathematically grounded technology, such as that presented by the Bias and Disparity Detection Engine, will be critical to ensuring that proper progress can be made in efforts to address societal and structural factors that contribute to racially biased outcomes.

## 3. The ideas behind the Bias & Disparity Detection Engine
This technology can detect and highlight racial disparities in datasets related to the Call for Code Open Sentencing Solution process pipeline.

![Architecture](/images/Diagram%20%231%20for%20ReadMe%20-%20BDDE%20Architecture%20Data%20Set%20Flow%20-%20Oct%2017.png)

## 4. Functionality - How the Bias & Disparity Detection Engine works with the Open Sentencing Solution
The Bias & Disparity Detection Engine (BDDE) analyzes available historical data against case specific data, provided by the Open Sentencing Public Defender, to give the public defense attorney (user) insights and bias/disparity indicators for each case. Public Defenders can then act immediately on the insight provided by the BDDE to negotiate a better plea or sentence for the defendant.

The BDDE functional scope, as related to an original use case presented by the interfaced Open Sentencing Solution, is centered on analysis of one type of Federal Drug Possession / Trafficking charge. This restricted scope narrowly demonstrates functionality that may later be used to analyze a broader set of charges and jurisdictions.

By leveraging existing and enhanced IBM technologies, such as AI Fairness 360 and Big Data Analytics, the BDDE will provide benchmarked hardened data analysis protocols. The protocols will detect disparity by isolating deviations in how Federal Sentencing Guidelines are applied in final sentencing outcomes, based on aggregation of historical sentencing outcomes by race.


### Use Case Proof Points
The BDDE will have a cloud-based API that will receive a single, case-specific dataset from the Open Sentencing Solution Aggregator, to determine which Federal Sentencing Guidelines might be relevant for the defendant being charged. The BDDE then compares the appropriate Federal Sentencing Guidelines midpoint against historical outcomes of similarly charged defendants. Success is achieved when the BDDE detects / isolates deviations (in number of months) historically applied in actual sentencing outcomes in that jurisdiction. BDDE then passes the results of that analysis back to the Open Sentencing Solution Aggregator, for presentation to the Public Defender via the solution's Report Generator.

![Architecture](/images/BDDE%20Sample%20Input%20-%20Output%20REPORT%20-%20Oct%2017%20%20.png)

## 5. Architecture -  Bias & Disparity Detection Engine Process Flow
![Process Flow](/images/Open%20Sentencing%20Architecture%20Process%20Flow%20-%20Oct%2017.png)


## 6. Prototype - Working Code Notebooks
Initial data science exploratory Jupyter notebooks are available and show structure and analysis protocols used for gathering and analyzing publicly accessed and simulated Federal Sentencing Guidelines and sentencing outcomes data sets

**Notebook #A** BDDE prototype [code outline](https://github.com/Call-for-Code-for-Racial-Justice/bias-detection-engine/blob/master/server/routes/engine.py)

**Notebook #B** BDDE [data analysis code](https://github.com/Call-for-Code-for-Racial-Justice/bias-detection-engine/blob/master/notebooks/open_sentencing_demo.ipynb)

<!-- **Notebook #C** BDDE [Disparity Detection demo dode](https://nbviewer.jupyter.org/github/embrace-call-for-code/bias-detection-engine/blob/master/notebooks/judicial_bias.ipynb). Todo:  addd this back when 404 error is resolved. (from Boz) -->

## 7. Datasets - Data Model Examples and Links to Dataset Notebooks
The data sets used in our initial analysis were sourced from publicly available interactive data found in the United States Sentencing Commission public domain.

**BDDE Dataset #1** - Input to BDDE from Open Sentencing Solution Aggregator Bias & Disparity Detection Engine accepts initial dataset from Open Sentencing Solution Aggregator which will pass the BDDE the initial dataset describing the defendants' charges, race, gender, and prior history based on data input into the solutions questionnaire by the user Public Defendant or Defense Attorney

**BDDE Dataset #2 Notebook**  Sentencing Guidelines and [historical sentencing outcomes](https://github.com/embrace-call-for-code/bias-detection-engine/tree/master/notebooks) Data for analysis captured from Federal Sentencing Commission domain to isolate specific actual sentencing deviation fact paterns This dataset capures Federal Sentencing Guidelines and actual historical sentencing outcomes pulled from interactive data accessed via United States Sentencing Commission interactive datasets
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
- At least from the initial data, victim factors, keywords or tone flags that might indicate bias in the case documents
- What happens after people serve their sentence? By sentence type. 

**BDDE Dataset #3 Notebook** [Simulated historical data to supplement actual historical data collected from US Sentencing Commission](https://github.com/embrace-call-for-code/bias-detection-engine/blob/master/notebooks/weighted_drug_trafficking_data.ipynb) Due to compressed Call for Code timeline, a set of simulated historical datasets were created to reflect trends indicated in smaller amount of actual historical sentencing data captured in Dataset #2 collected from publicly available interactive data found on United States Sentencing Commission public portal. This dataset shows a view of simulated data that replicate fact patterns discerned in limited actual historical data collected from United States Sentencing Commission interactive historical outcomes datasets sufficient to reveal that a large proportion of black defendants are offered and take a plea bargain deal which results in a disproportionately negative deviation from the Federal Sentencing Guidelines mid-point

![Judicial Bias](/images/Judicial_Bias.png)

 **BDE Dataset #4 Notebook** [BDDE Data output dashboard analysis results to be passed back to Open Sentencing Solution Aggregator](https://github.com/Call-for-Code-for-Racial-Justice/bias-detection-engine/blob/master/notebooks/open_sentencing_demo.ipynb)
Critical findings generated by BDDE outputs will be fed back to the Open Sentencing Aggregator via the BDDE API and will provide analytic and contextual insights that include:
1. \# of similarly charged Sentencing Documents evaluated
2. % white male vs % black male reflected in the historical pull of Sentencing documents
3. % white males with positive and negative deviations from sentencing guidelines
4. % black males with positive and negative  deviations
5. Nature of deviations by demographics (ie plea deals, min vs max judgments, fines assessed, etc) 

## 8. Technology
- [AI Fairness 360](https://github.com/Trusted-AI/AIF360).
-This version of the Bias & Disparity Detection Engine uses a set of python programs with a Flask front end and APIs for organizations to provide metamodel and instance to be assessed for systemic disparities and biased outcomes.
-The APIs will enable specification of a steps in a structured process, and to provide sets of data to be a analyzed. Python code is used to generate both unbiased and biased data in order to simulate outcomes for a given metamodel.
-Additional security controls can be added to allow organizations to assess only their own data.
-Hooks are provided into one or more IBM Cloud AI offerings such that unstructured data can be uploaded for analysis using the chosen training method. This will enable adopters of the code base to provide keys that will enable use of a trial or production version of the AI offering and to provide training.
-IBM Carbon Framework used with Github Pages (likely Gatsby) to provide content for developers.
-Existing python scripts were enhanced to provide general way to identify the set of data with number of steps and the labels for the steps
-Created a flask application with a front end to give developers specs for metamodel
-Jupyter Notebooks and D3 Visualization Library using


## 9. Vision
- Additional selected AI Fairness 360 features may be integrated into the BDDE to provide an automated front end for selected AI Fairness 360 algorithms.
- Future version may include privacy preserving features, as well as guidance in Github pages and the readme.
- GraphQL for integrating data sets from multiple organizations may also be explored for integration. This likely will be a contributed feature or a different standard providing aggregated queries.
- Due to time constraints, IBM Blockchain was not included in this version of BDDE structure but there is vast potential for integrating blockchain


## 10. Getting Started
### Calling the Open Sentencing API
If the service is cloud-deployed, be sure to point to the IP and port associated with the deployment. Examples here are provided for deployment on `localhost:5000`.

You can then use [Postman app](https://www.postman.com/downloads/) to send json formatted POST HTTP requests to the model at the URL `http://127.0.0.1:5000/sentencing-disparity`
Here is an example JSON data you can use to test the model.
```
{
	"charge_code": "Drug trafficking",
    "race": "Black",
    "gender": "Male",
    "controlled_substance_quantity_level": 6,
}
```
#### From the Command Line
Run the following command line curl command

```asciidoc
curl -X POST -H "Content-Type: application/json" -d '{"charge_code":"Drug trafficking","race":"Black","gender":"Male","controlled_substance_quantity_level":6,}' localhost:5000/sentencing-disparity
```

You should get the following result

```asciidoc
{
    "charge_code": "Drug trafficking",
    "controlled_substance_quantity_level": 6,
    "deviations": [{"charge_code": "Drug trafficking",
    "sentence_deviations": [{"commitmentTerm": 39.72043010752688,
        "commitmentUnit": "Months",
        "sentence_type": "Prison Only"}]}],
    "gender": "Male",
    "race": "Black",
    "success": True
 }
```

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
- Legislators who strive to leverage technology to help them ensure that new laws and legislation is free of bias that can lead to disparity in how the laws / legislation impact minorities constituents / citizens
- **United States Sentencing Commission** - created by Congress in 1984 to reduce sentencing disparities and promote transparency and proportionality in sentencing. The Commission collects, analyzes, and distributes a broad array of information on federal sentencing practices.  The Commission also continuously establishes and amends sentencing guidelines for the judicial branch and assists the other branches in developing effective and efficient crime policy .


## 11. Resources
- **United States Sentencing Commission**: Created by Congress in 1984 to reduce sentencing disparities and promote transparency and proportionality in sentencing. The Commission collects, analyzes, and distributes a broad array of information on federal sentencing practices.  The Commission also continuously establishes and amends sentencing guidelines for the judicial branch and assists the other branches in developing effective and efficient crime policy .

- Measuring Bias in Machine Learning: The Statistical Bias Test - https://www.datacamp.com/community/blog/measuring-bias-in-ml
a defining statistical bias in a machine learning model and demonstrate how to perform the test on synthetic data.

- 5 Types of bias & how to eliminate them in your machine learning project: - Sample, Exclusion, Observer, Prejudice, Measurement bias. An introduction and an example to each   https://towardsdatascience.com/5-types-of-bias-how-to-eliminate-them-in-your-machine-learning-project-75959af9d3a0

## 12. License
This project is licensed under the Apache 2 License - see the [LICENSE](/LICENSE) file for details.

