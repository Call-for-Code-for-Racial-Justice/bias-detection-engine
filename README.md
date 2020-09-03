# Bias Diagnostics Engine 

This solution starter was created by technologists from IBM.

## Table of Content

1. [The Team](#1-team---working-team-for-cfc-embrace-phase-ii-externalization)
2. [Overview](#2-overview---ibm-racial-disparity--bias-diagnostics-engine)
3. [The idea](#3-idea)
4. [How it works](#4-functionality---how-it-works--how-ibm-technology-can-help-detect-diagnois-and-remediate-implicit-racial-bias)
5. [Architecture Diagrams](#5-architecture----bias-diagnostics-engine-architecture)
6. [Prototype](#6-prototype)
7. [Datasets](#7-datasets)
8. [Technology](#8-technology)
9. [Vision](#9-vision---fully-scaled-ibm-disparity-detection-and-bias-diagnostics-engine)
10. [Getting started](#10-getting-started)
11. [Resources](#11-resources)
12. [License](#12-license)


## 1. Team - Working Team for CFC EmbRACE Phase-II Externalization 

* Denise Knorr - Product Manager
* Boz Handy Bosman - AoT Master Inventor (AIF360)
* Sam Hoffman - AIF360 Developer
* Margriet Groenendijk - Data & AI Developer Advocate   
* Hema Veeradhi - Red Hat Software Engineer    
* Kate Tereshchenko - Cloud Data Scientist 
* Ann Marie Fred - CFC Sentencing Reform Team 
* Demi Ajayi - Prod Designer – AI Natural Language 
* Otis Smart - AI Data Scientist - Machine Learning 

## 2. Overview - IBM Racial Disparity & Bias Diagnostics Engine

* The Dispairity Detection and Bias Diagnostics Engine will be powered by IBM’s [AI Fairness 360](https://github.com/Trusted-AI/AIF360) sourced functionality refined to specifically isolate racial disparity in technology enabled outcomes
* The Engine diagnoses bias related causes for the disparity that is detected and isolated to recommend remediation
* Bias Engine will also monitor outcomes and measure alignment of outcomes to the desired objective of being a fair outcome that is free of racially biased influence 

### Problem Statement - Reason why deployment of this technology is a so critial need

A new class of “anti-bias / anti-systemic Racism” solutions, apps and platforms (aka IBM's EmbRACE Call-for-Code) strives to have outcomes that can be mathematically assessed, validated verifiabially and attributed to be “Bias-Free”. 

1. This new class of solutions that prioritize the minimization of outcomes infected by implicit racial bias, will need leading edge technology and newly developed interface protocols to effectively serve as a universally accepted fair and “Credible Arbiter” of bias and other discrimininatory variables that might negatively contribute to negative racial disparity in outcomes associated with the objectives of the solution or application.

2. Without validated and benchmarked models for consistent attribution and remediation of implicit racial bias, the full range of new and innovative anti-bias solutions will have diminished ability to deliver outcomes that can be universally seen as mathematically and repeatably accurate in diagnosing and remediating that racial bias. 
    *	A random / one-off approach to detecting and remediating implicit racial bias will not be sufficient to drive outcomes accepted / acknowledged as bias-free across a large ecosystem of a new class of anti-bias solutions.

3.	Furthering the problem is that effects of bias can be fed into a single solution’s outcomes via multiple inputs / steps in that single solution’s processes, while at the same time some steps or processes associated with the solution’s outcome may be mathematically bias-free or neutral.  
    *	This means that the bias diagnostics capabilities need to be sufficient to assess the *cumulative* effect of *multiple* sources of bias throughout the entire “process pipeline” within a single solution, so that if any single “bias-infected” input source or data set within the solution’s process pipeline goes undiagnosed, the outcome may still reflect elements of racial bias. In other words, neutral processes are not sufficient in-and-of themselves to prevent implicit racial bias from infecting a solution’s outcomes. 

These problems are hardened by fact that many bodies of authority (governmental / corporate / financial) may continue to deny the existence of Implicit bias and Systemic Racism.  Therefore mathmatically grounded technology like the Dispairity Detection and Bias Diagnostics Engine will be extremely critical to ensure proper progress can be made in efforts to address societal and structural factors that lend themselves to racially biased outcomes.  

## 3. Idea

![Elevator pitch](https://github.com/MargrietGroenendijk/bias-detection-engine/blob/master/figures/Bias%20Engine%20-%20How%20it%20Works%20Sep%201.png)

## 4. Functionality - How it works & How IBM Technology can help Detect, Diagnois and Remediate Implicit Racial Bias 

1. By leveraging existing (enhanced) IBM technologies like AI Fairness 360, IBM can provide benchmarked hardened models and interface protocols for disparity and bias diagnostics functionality (**aka a full functioning Bias Diagnostics Engine**) that can be universally applied via Open Source cloud enablement by a varied range of internal and external 3rd party solutions targeting bias-free outcomes.

2. IBM technology can serve as a scientifically sourced “CREDIBLE-ARIBITER" of disparity and racial bias by leveraging IBM’s unique and deep brain-trust of research and expertise needed to adequately assign algorithms sufficient to digitize and quantify bias infused context and concepts. 

3. PRIVACY PRESERVING will be required due to the nature of most data sets, so IBM Cloud Security will be a critical technology enabler for this new class of anti-bias / anti-racism solutions and required for the Bias Engine to function optimally, since many of the most relevant data sets needed are those that will require maximum levels of security and privacy similar to the levels of security IBM provides to Financial and Public Sector solutions and platforms. 

![How it works](https://github.com/MargrietGroenendijk/bias-detection-engine/blob/master/figures/Screen%20Shot%202020-09-01%20at%2012.45.58%20PM.png)

### Success & Proof Points - What proves success 
The Disparity Detection and Bias Diagnostics Engine will have a cloud based API that will receive datasets and process pipelines from multiple types of anti-bias focused solutions and apps in a way that will provision the engine to execute query, selection, presentation, and visualization functions against that data. 

Critical components of the engine's outputs will be fed back to the requesting solutions via APIs and will provide analyical and contextual insights that include:

1. A visualization of the process pipeline for the served app or solution showing how and where dispairity was detected
2. A statistical analysis to indicate where and how bias informed the dispairity
3. A simulation to model what fair results would look like

![Architecture](https://user-images.githubusercontent.com/7343099/90186448-2c7d8080-dd86-11ea-9fe2-e5e12a181888.png)

## 5. Architecture -  Bias Diagnostics Engine Architecture

### The Racial Dispairity Funnel 
Implicit Bias and vairables leading to racial disparity are structural inputs into the decision making process pipeline that leads to outcomes. As such disparity and bias can work their way through the process pipeline to filter out equitable or racially fair analysis along the process pipeline resulting in racial disparity in the outcome.  This is the case regardless of whether individual processes or inputs are in-and-of themselves neutral.  As long as there is any input source or data element that is infected with implicit bias or other variables that lead to racial dispairity that work their way through hiring funnel, willl lead to disparities in the outputs. The hiring process is a seven-step process that includes: sourcing, application, screening, shortlist, hiring manager/interview, offer/negotiation, and candidate decision. In this solution we are not directly addressing the sourcing step, but rather focusing on the pipeline from application to being hired or dispositioned. Our hope is that by showing bias at each step along the pipeline, we can help companies understand why they may not be achieving the diversity they desire in their employee base.  

![Hiring Funnel](https://github.com/MargrietGroenendijk/bias-detection-engine/blob/master/figures/Funnel%20-%20Bias%20Filtering%20processes%20-%20Sep%201.png)

## 6. Prototype

We have created some initial data science exploratory Jupyter notebooks [here.](https://github.com/embrace-call-for-code/bias-detection-engine/tree/master/notebooks)
The notebooks analyze simulated HR and Judicial data sets to depict the bias in various stages of either HR recruiting process or legal procedure for the Black community.

## 7. Datasets

The data sets used in our initial analysis/notebooks can be found [here.](https://github.com/embrace-call-for-code/bias-detection-engine/tree/master/data)
Initial input data sets will be generated by the requesting anti-bias solution or app. 

## EXAMPLE - Sentencing Reform "Outcaracation" Solution API Interface with Bias Detection Engine
Sentencing Reform solution can give the bias detection engine information about the desired outputs with objective of receiving back recommendations, links to data, reasons the system gave the recommendations, plus the ability to annotate documents to explain its reasoning and show evidence.  

Data relevant to public defenders' tool including: 
- How well does the crime fit a charge? (AI - bias detection engine)
- How extreme is that charge compared to the reality of the crime?
- Statistical component - 90% like this crime, 45% like this one
- Have similar crimes in the jurisdiction been charged the same way?
- Case precedent  - what other cases are similar to this one? (AI - bias detection engine)

OUTCOMES 
- Give me a group of similar crimes to compare this to (AI - bias detection engine)
- Average sentencing data by conviction (not AI - federal sentencing data)
- Disparities in sentencing by race (not AI - federal sentencing data)
- How bias is currently showing up in the charging outcomes (AI - bias detection engine) - Especially for crimes similar to this one
- Lesser charges for privileged groups?
- The "priors" of the person accused: prior convictions (not AI - from our questionnaire) Ideally, we could get some data on how fair the previous outcomes were! could just be the questionnaire as a start
- Demographic information about the defendant (not AI - from our questionnaire))
- Personal history information about the defendant (not AI - from our questionnaire or other data that's already been entered into the system)
- Factors that will help the accused decide whether to go to trial - hard data based on the charges (not AI)
- Likely outcome of bail hearing - what percentage get bail, what percentage sit in jail and for how long
- If you plead not guilty, what are your chances of being found guilty vs. innocent
- If you're found guilty, what are the usual sentences?
- Strength of evidence?
- How likely is it that they're actually innocent?
- At least from the initial data, victim factors,keywords or tone flags that might indicate bias in the case documents (AI)
- What happens after people serve their sentence? By sentence type.  (not AI)
- Likelihood to re-offend or be rehabilitated
- Help the public defender argue for a different option
- What sentence could make them less likely to re-offend?
- Mental health treatment for example
- Routing homeless people to social services
- Jail time
- Probation
- Home Arrest
- School-to-prison pipeline


## Data relevant to public dashboard
Using the datasets and outcomes of the Bias Detection Engine, we would like to create public dashboards including visualizations to explain the following:
- How bias is currently showing up in the sentencing outcomes: aggregate data (Some AI, some not)
- Ideally, show the data per specific judge, prosector to help voters
- Are the judges acting in accordance with their public statements?
- Less ideally, show the data per jurisdiction
- Show the data by type of crime
- Some kind of "bias score"?
- Evidence and sources
- Are there other types of sentences that would have a better impact/prevent the crime from occurring again? (Some AI, some not)

##  Help with policy
- Are mandatory sentencing guidelines contributing to biased outcomes?
- Did the person convicted have good legal representation?
- Type of representation: self, public defender, private attorney
- Disparities in sentencing by type of representation (Some AI, some not)
- What happens after people serve their sentence? By sentence type.   (Some AI, some not)
- Likelihood to re-offend or be rehabilitated
- What sentence could make them less likely to re-offend
- Mental health treatment for example
- Routing homeless people to social services
- Jail time
- Probation
- Home arrest
- School-to-prison pipeline?


## 8. Technology

1. [AI Fairness 360](https://github.com/Trusted-AI/AIF360)
1. Blockchain to establish consensus about data sharing
2. Accountability Scoring
3. Privacy Preserving
4. Clean Media Ecosystem Container – Bias detection + Misinformation flagging + Misinformation filters + Accountability Scores

## 9. Vision - Fully Scaled IBM Disparity Detection and Bias Diagnostics Engine 
Boz please add Denise fuure vision diagram here 

## 10. Getting Started
TBD

## 11. Resources
TBD

## 12. License
TBD


















