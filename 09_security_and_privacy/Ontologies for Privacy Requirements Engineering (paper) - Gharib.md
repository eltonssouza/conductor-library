# Ontologies for Privacy Requirements Engineering (paper)

> **Author(s):** Gharib · **Category:** 09_security_and_privacy · **Language:** English

---

Ontologies for Privacy Requirements Engineering: A Systematic Literature Review
Mohamad Gharib1, Paolo Giorgini2, and John Mylopoulos2
1 University of Florence - DiMaI, Viale Morgagni 65, Florence, Italy mohamad.gharib@unifi.it
2 University of Trento - DISI, 38123, Povo, Trento, Italy {paolo.giorgini,john.mylopoulos}@unitn.it
Abstract. Privacy has been frequently identified as a main concern for system developers while dealing with/managing personal information. Despite this, most existing work on privacy requirements deals with them as a special case of security requirements. Therefore, key aspects of privacy are, usually, overlooked. In this context, wrong design decisions might be made due to insufficient understanding of privacy concerns. In this paper, we address this problem with a systematic literature review whose main purpose is to identify the main concepts/relations for capturing privacy requirements. In addition, the identified concepts/relations are further analyzed to propose a novel privacy ontology to be used by software engineers when dealing with privacy requirements.
Keywords
Privacy Ontology, Privacy Requirements, Privacy by Design (PbD), Requirements Engineering
1 Introduction
Increasing numbers of today's systems deal with personal information (e.g., information about citizens, customers, etc.), where such information is protected by privacy laws [99]. Therefore, privacy has become a main concern for system designers. In other words, dealing with privacy related concerns is a must these days because privacy breaches may result in huge costs as well as a long-term consequences [2,97,114,33,34]. Privacy breaches might be due lack of appropriate security policies, bad security practices, attacks, data thefts, etc. [2,144]. However, most of these breaches can be avoided if privacy requirements of the system-to-be were captured properly during system design (e.g., Privacy by Design (PbD)) [37,36,144], where privacy requirements aim to capture the types and levels of protection necessary to meet the privacy needs of the users.
Nevertheless, just few works focused on considering privacy during the system design [104]. More specifically, most existing work on privacy requirements often deal with them either as non-functional requirements (NFRs) with no specific

criteria on how such requirements can be met [10,261,179], or as a part of security [263,130], i.e., focusing mainly on confidentiality and overlooking important privacy aspects such as anonymity, pseudonymity, unlinkability, unobservability, etc.
On the other hand, privacy is an elusive and vague concept [213,214,130]. Although several efforts have been made to clarify the privacy concept by linking it to more refined concepts such as secrecy, person-hood, control of personal information, etc., there is no consensus on the definition of these concepts or which of them should be used to analyze privacy [214]. This has resulted in a lot of confusion among designers and stakeholders, which has led in turn to wrong design decisions. In this context, a well-defined privacy ontology that captures privacy related concepts along with their interrelations would constitute a great step forward in designing privacy-aware systems.
Ontologies have been proven to be a key success factor for eliciting highquality requirements, and it can facilitate and improve the job of requirements engineers [217,128,65], since it can reduce the conceptual vagueness and terminological confusion by providing a shared understanding of the related concepts between designers and stakeholders [238].
In addition, the ontology should capture privacy requirements in their social and organizational context. Since most complex systems these days (e.g., healthcare systems, smart cities, etc.) are socio-technical systems [75], which consist not only of technical components but also of humans along with their interrelations, where different kinds of vulnerabilities might manifest themselves [155,99]. Focusing on the technical aspects and leaving the social and organizational aspects outside the system's boundary leaves the system open to different kinds of vulnerabilities that might manifest themselves in the social interactions and/or the organizational structure of the system [155]. The Flash Crash [215] and the Allied Irish Bank scandal [166] are good examples, where problems were not caused by mere technical failures, but it were also due to several socio-technical related vulnerabilities of the system.
This paper applies systematic review techniques to survey available literature to identify the most mature studies that propose privacy ontologies/concepts. In addition, we further analyze the selected privacy related concepts/relations to identify the main ones in order to propose a novel ontology that can be used to capture privacy requirements. This paper is therefore intended to be a starting point to address the problem of identifying a core privacy ontology.
The rest of the paper is organized as follows; Section (�2) describes the review process and the protocol underlining this systematic review. We present and discuss the review results and findings in Section (�3). In Section (�4) we propose a novel ontology for privacy requirements engineering. We discuss threats to validity in Section (�5). Related work is presented in Section (�6), and we conclude and discuss future work in Section (�7).

2 Review Process
A systematic review can be defined as a systematic process for defining research questions, searching the literature for the best available resources to answer such questions, and collecting available data from the resources for answering the research questions. Following [139,136], the review process (depicted in Figure 1) consists of three main phases:
1. Planning the review, in which we formulate the research questions and we define the review protocol.
2. Conducting the review, in which we conduct the search process after identifying the search terms and the literature sources, and then we perform the study selection activity.
3. Reporting the results of the review, in which we collect detailed information from the selected studies in order to answer the research questions, and then we use the obtained data to answer the research questions, which we discuss in the following section.
2.1 Planning the review
This phase is very important for the success of the review, for it is here that we define the research objectives and the way in which the review will be carried out. This includes two main activities: (1) formulating the research questions that the systematic review will answer; and (2) defining the review protocol that specifies the main procedures to be taken during the review.
Research questions Formulating the review questions is a very critical activity since these questions are used to derive the entire systematic review methodology [139]. Therefore, we formulate the following four Research Questions (RQ) to identify the main privacy concepts that have been presented in the literature:
RQ1 What are the privacy concepts/relations that have been used to capture privacy concerns?
RQ2 What are the main concepts/relations that have been used for capturing privacy requirements?
RQ3 Do existing privacy studies cover the main privacy concepts/relations? RQ4 What are the limitations of existing privacy studies?
Define the review protocol The review protocol specifies the methods to be followed while conducting the systematic review. Based on [139,136], a review protocol should specify the following: the strategy that will be used to search for primary studies selection; study selection criteria; study quality assessment criteria; data extraction and dissemination strategies. In the rest of this section, we discuss how we specify and perform each of these activities.

1. Planning the review
1.1. Formulating the research questions
1.2. Define the review protocol

2. Conducting the review

2.1. Search strategy
Identify the Identify the search terms search sources

2.2. Study selection
Primary selection

Conduct the search process

Quality assessment

Fig. 1: The systematic review process

3. Reporting the results
3.1 Data Synthesis
3.2 Results and discussion

2.2 Conducting the review
This phase is composed of two main activities: 1- search strategy; and 2- study selection, where each of them is composed of several sub-activities. In what follows, we discuss them.
Search strategy The search strategy aims to find as many studies relating to the research questions as possible using an objective and repeatable search strategy [139]. The search activity consists of three main sub-activities: 1- identify the search terms, 2- identify the literature resources, and 3- conduct the search process.
Identify the search terms. Following [139,136], we derived the main search terms from the research questions. In particular, we used the Boolean AND to link the major terms, and we use the Boolean OR to incorporate alternative synonyms of such terms. The resulting search terms are: (Privacy AND (ontology OR ontologies OR taxonomy OR taxonomies ) OR (Privacy requirements).
Identify the literature resources. Six electronic database resources were used to primarily extract data for this research. These include: IEEE Xplore, ACM Digital Library, Springer, ACM library, Google Scholar, and Citseerx.
Conduct the search process. The search process (shown in Figure 2) consists of two main stages:
Search stage 1. We have used the search terms to search the six electronic database sources, and only papers with relevant titles have been selected;
Search stage 2. The reference lists of all primary selected papers were carefully checked, and several relevant papers (25 papers) were identified and added to the list of the primary selected papers.
Study selection. The selection process (shown in Figure 2) consists of two main stages.
Selection stage 1 (primary selection). Searching the electronic database source returned 240 relevant papers, among which we have identified and removed 33 duplicated papers. Next, we have applied the primary selection

Search stage 1
IEEE 62 Xplore
60 Springer
ACM 40 Library
Google 43 Scholar
Citeseerx 35 library

Selection stage 1

240 papers

References

-33

search

remove

references

duplicated papers

+25

Search stage 2

207 papers

132 papers

-100

apply primary selection criteria

107 papers

-98

apply QA
criteria Selection

stage 2

34 papers

Fig. 2: Paper search and selection process

criteria on the remaining 207 papers. In particular, we have read the abstract, introduction, and then we skimmed through the rest of paper. We removed all the papers that are not published in the English language, and we excluded all papers that are not related to any of our research questions. Moreover, when we were able to identify multiple version of the same paper, only the most complete one was included. Finally, we excluded any paper that has been published before 1996, since we were not able to find any concrete work related to our research before 1996. The primary selection inclusion and exclusion criteria are shown in Table 1. The outcome of this selection stage was 107 papers, i.e., we have excluded 100 papers.
Selection stage 2 (Quality Assessment (QA)). At this stage, the QA criteria has been applied to the papers that have resulted from the first selection stage (107 papers) along with the papers that have resulted from the second search stage (25 papers), for a total of 132 papers. In order to identify the most relevant studies that can be used to answer our research questions, we formulated five QA questions (shown in Table 2) to evaluate the relevance, completeness, and quality of the studies, where each question has only two answers: Yes = 1 or No= 0. The quality score for each study is computed by summing the scores of its QA questions, and the paper is selected only if it scored at least 4. As a result, 98 papers were excluded and 34 studies were selected. The result of the QA of the studies is presented in Table 7 in Appendix A.

2.3 Reporting the results
The final phase of the systematic review involves summarizing the results, and it consists of two main activities: 1- data synthesis; and 2- results and discussion.

Table 1: Primary selection inclusion and exclusion criteria

Inclusion criteria

Exclusion criteria

a. All papers published in the English lan- a. Papers that are not published in the En-

guage

glish language

b. Papers related to at least one of the re- b. Papers that do not have any link with the

search questions

research questions

c. Relevant papers that are published from c. If a paper has several versions only the

1996 to 2016

most complete one is included

Data synthesis In what follows, we describe how data syntheses were executed: Data related to RQ1 can be extracted directly from the list of selected papers (shown in Table 3). To answer RQ2, the contents of the 34 selected studies were further analyzed to identify privacy related concepts along with their interrelations, and list them in a comprehensive table (Table 4). Moreover, we identify the main concepts/relations for capturing privacy requirements based on Table 4 & Table 5 that shows the frequency of concepts/relations appearance in the selected studies. To answer RQ3 data can be derived from Table 6, which summaries the percentage of the main concepts/relations categories that each selected study cover. RQ4 can be answered by categorizing the studies into four group based on the concepts categories they do not cover.
3 Review results and discussion
This section presents and discusses the findings of this review. First, we start by presenting an overview of the selected studies, and then, we present the findings of this review concerning the research questions.
Overview of selected studies3. 34 studies were selected, where 5 studies were from book chapters, 10 papers were published in journals, 11 papers appeared in conference proceedings, 6 papers came from workshops, and 2 papers were extracted from symposiums. The number of papers by year of publication is presented in Figure 3; while the percentages of the selected studies based on their publishing type are represented in Figure 4.
3 An overview of all considered studies is shown in Table 8 in Appendix B

Table 2: Quality assessment questions
Quality assessment questions Q1 Are the objectives of the proposed work clearly justified? Q2 Are the proposed concepts/relations clearly defined? Q3 Does the work propose sufficient concepts/relations to deal with privacy aspects? Q4 Have the concepts/relations been applied to project/case study, or have they
been justified by appropriate examples? Q5 Does the work add value to the state-of-the-art1? 1Evaluated based on the number of citations taking into consideration the year of publication

    
���� ���� ���� ���� ���� ���� ���� ���� ��� �� ��� ��� ���
Fig. 3: Number of papers by year of publication
RQ1: What are the privacy concepts/relations that have been used to capture privacy concerns? The review has identified 34 studies that provide concepts and relations that can be used for capturing privacy requirements. The list of the selected studies that answers our first research question (RQ1 ) is presented in Table 3, where each paper is described by its identifier, title, author(s), publication year and number of citation. In what follows, we present a summary of the contributions of each selected study.
ACM 03 [240], "Elaborating Security Requirements by Construction of Intentional Anti-Models". Lamsweerde [240] proposed a goal-oriented approach that extends the KAOS framework for modeling and analyzing security requirements. The framework focus on generating and resolving obstacles/anti-

29% 15%
6% 32%
18%

Book chapters Journals Conferences Workshops Symposiums

Fig. 4: Percentages of selected studies

Table 3: The list of the selected studies

Study ID ACM 03 [240]
ACM 14 [144]
ACM 16 [28]

Title of the study

Author(s) Year#Cite

Elaborating Security Requirements by Construction of Intentional V. Lam- 2004 337

Anti-Models

sweerde

Modeling of privacy-aware business processes in BPMN to protect per- Labda et al. 2014 0

sonal data

Introducing privacy in a hospital information system

Braghin et al. 2008 9

ACM 35 [211] ACM 40 [248] IEEE 12 [221] IEEE 15 [235]

Ontologies for Modeling Enterprise Level Security Metrics

A. Singhal, 2010 7

D. Wijesekera

OVM: an ontology for vulnerability management

J. Wang and 2009 40

G. Minzhe

Using Security and Domain ontologies for Security Requirements Anal- Souag et al. 2013 4

ysis

Towards an Ontology-based Security Management

B. Tsoumas, 2006 88

D. Gritzalis

IEEE 50 [100]
IEEE 57 [132]
CIT 07 [241]
CIT 33 [155] Spgr 07 [162]

Modeling security requirements through ownership, permission and Giorgini et al. 2005 198

delegation

A Security Ontology with MDA for Software Development

W. Kang, 2013 1

Y. Liang

Modeling Reusable Security Requirements Based on an Ontology Lasheras et al. 2009 30

Framework

Security and Privacy Requirements Analysis within a Social Setting Liu et al. 2006 75

An Extended Ontology for Security Requirements

Massacci et al. 2011 16

Spgr 13 [71] SCH 18 [208] SCH 24 [130] SCH 28 [179]

A Modeling Ontology for Integrating Vulnerabilities into Security Re- Elahi et al. 2009 21

quirements Conceptual Foundation

Eliciting security requirements with misuse cases

G. Sindre and 2005 830

A. Opdahl

Addressing privacy requirements in system design: the PriS method Kalloniatis 2008 76

et al.

Secure Tropos: a security-oriented extension of the Tropos methodol- H. Mouratidis, 2007 193

ogy

P. Giorgini

SCH 41 [214] A taxonomy of privacy Spgr 18 03 [81] Formalizing information security knowledge
Spgr 13 01 [15] Risk as dependability metrics for the evaluation of business solutions: a model-driven approach

D. Solove S. Fenz, A.
Ekelhart Asnar et al.

2006 967 2009 144
2008 30

Spgr 13 02 [59] Spgr 13 03 [72]

The CORAS methodology. model-based risk assessment using UML and UP A vulnerability-centric requirements engineering framework. analyzing security attacks, countermeasures, and requirements based on vulnerabilities

Braber et al. Elahi et al.

2003 66 2010 73

Spgr 13 04 [123] UMLsec: Extending UML for secure systems development

J. Ju�rjens 2002 583

Spgr 13 05 [167] Adapting Secure Tropos for security risk management in the early Matulevicius 2008 60

phases of information systems development

et al.

Spgr 13 07 [199] An extended misuse case notation: Including vulnerabilities and the L. R�stad 2006 46 insider threat

Spgr 08 01 [169] Model-based management of information system security risk

N. Mayer 2009 70

Spgr 08 03 [63] A knowledge-based approach to security requirements for e-health ap- Dritsas et al. 2006 17

plications

Spgr 07 02 [263] A requirements engineering methodology for trust, security, and pri- N. Zannone 2007 17

vacy

Spgr 07 03 [152] Introducing abuse frames for analysing security requirements

Lin et al. 2003 73

Spgr 03 01 [16] Basic Concepts and Taxonomy of Dependable and Secure

Avizienis 2004 3703 et al.

Spgr 02 01 [13] From trust to dependability through risk analysis Spgr 02 02 [14] Risk modelling and reasoning in goal models SCH 24 02 [114] Privacy risk models for designing privacy-sensitive ubiquitous comput-
ing systems SCH 28 01 [186] STS-Tool Security Requirements Engineering for Socio-Technical Sys-
tems

Asnar et al. Asnar et al. Hong et al.
Paja et al.

2007 57 2006 17 2004 218
2014 2

SCH 43 01 [239] Handbook of privacy and privacy-enhancing technologies

Blarkom et al. 2003 69

goals to goal satisfaction, i.e., it addresses malicious obstacles/anti-goals (threats) set up by attackers to threaten security goals, and the new security requirements are obtained as countermeasures to resolve these obstacles/anti-goals (threats). The framework adopts several main concepts from KAOS (e.g., agents, goals, etc.) and proposes concepts for building intentional threat models (e.g., obstacles, anti-goal, anti-requirements, attacker, etc.). ACM 14 [144], "Modeling of Privacy-aware Business Processes in BPMN to Protect Personal Data". Labda et al. [144] propose a privacy-aware Business Processes (BP) framework for modeling, reasoning and enforcing privacy constraints. They have identified several privacy-related concepts, including: Data, User, Action, Purpose, and Permissions. In addition, they identify five concepts that can be used for analysis privacy in BP: (1) Access control, (2) Separation of Tasks (SoT), (3) Binding of Tasks (BoT), (4) User consent, (5) Necessity to know (NtK). ACM 16 [28], "Introducing Privacy in a Hospital Information System". Braghin et al. [28] presented an approach that supports expressing and enforcing privacy-related policies. The approach extends the conceptual model of an open source hospital information system (Care2x) with concepts for role-based privacy management (e.g., subject, processor, and controller), and concepts for supporting the privacy enforcement mechanisms (actions), where such actions can be either inactive or declarative, where the former includes actions that require to access and process data, while the latter includes simple statements representing activities that do not require to interact with the system. ACM 35 [211], "Ontologies for Modeling Enterprise Level Security Metrics". Singhal and Wijesekera [211] provide a security ontology that supports IT security risk analysis. The ontology identifies which threats endanger which assets and what countermeasures can reduce the probability of the occurrence of a related attack. The concepts of the ontology, includes: threat, a potential violation of security, an attack exploits vulnerabilities to realize a threat, where vulnerabilities are characteristics of target assets that make them prone to attack, and a risk is an expectation of loss expressed as a probability that a particular threat will exploit a certain vulnerability, which will result in a harmful result. Finally, security mechanisms are designed to prevent threats from happening or mitigating their impact when they occur. ACM 40 [248], "OVM: An Ontology for Vulnerability Management". Wang and Guo [248] propose an ontology for vulnerability management (OVM) that capture the fundamental concepts in information security and their relationship, retrieve vulnerable assets (data) and reason about the cause and impact of such vulnerabilities. The ontology has been built based on the Common Vulnerabilities and Exposures (CVE), Common Weakness Enumeration (CWE), Common Platform Enumeration (CPE), and Common Attack Pattern Enumeration and Classification (CAPEC). The top level concepts of the ontology includes, a Vulnerability existing in an IT Product that can be exploited by an Attacker through an Attack that compromises

the IT Product and cause Consequence. Moreover, Countermeasures can be used to protect the IT Product through mitigating the Vulnerability. CIT 07 [241], "Modeling Reusable Security Requirements Based on an Ontology Framework ". Velasco et al. [241] propose an ontology-based framework for representing and reusing security requirements based on risk analysis. The ontology is based on two ontologies: 1- the risk analysis ontology that is developed based on MAGERIT [159], and identifies five types of risk elements: asset, threat, safeguard, valuation dimension, valuation criteria, and 2- the requirements ontology that models reusable requirements along with their relationships. CIT 33 [155], "Security and Privacy Requirements Analysis within a Social Setting". Liu et al. [155] propose a framework for dealing with security and privacy requirements within an agent-oriented modeling framework. They extend i * modeling language to deal with security and privacy requirements, where i * language allows for analyzing security/privacy issues within their social context, which enables for a systematic way of deriving vulnerabilities and threats. Moreover, i * models make it possible to conduct different countermeasure analyses for addressing vulnerabilities and suggesting countermeasures for them. IEEE 12 [221], "Using Security and Domain ontologies for Security Requirements Analysis". Souag et al. [221] introduce an ontology-based method for discovering Security Requirements (SR). The process that underlies this method has three main steps, and it starts with the elicitation step that constructs an initial i * requirements model from the stakeholders' needs/concerns about security. The second step is the SR analysis that depends on production rules to exploit the security-specific ontology to discover threats, vulnerabilities, countermeasures, and resources. These concepts are used to enrich the requirements model by adding new elements (malicious tasks, vulnerability points, etc.). Finally, the domain specific SR analysis step, in which another set of rules explores the domain ontology to improve the requirements model with resources, actors and other concepts that are more specific to the domain at hand. IEEE 15 [235], "Towards an Ontology-based Security Management". Tsoumas and Gritzalis [235] introduce a security management framework that proposes a Security Ontology (SO), which contains the following concepts, a stakeholder possesses an asset, which in turn can be compromised by a vulnerability. While a threat initiated by a threat agent targets an asset and exploits a vulnerability of the asset in order to achieve its goal. Exploitation of a vulnerability leads to the realization of an unwanted incident, which has a certain impact. Furthermore, countermeasures reduce the impact of the threat with the use of controls. Finally, security policy formulates the controls into a manageable security framework possessed by stakeholders. IEEE 50 [100], "Modeling Security Requirements through Ownership, Permission and Delegation". Giorgini et al. [100] introduce Secure Tropos, a formal framework for modeling and analyzing security requirements in their social and organizational context. Secure Tropos proposes several concepts includ-

ing, an actor that covers two concepts (a role and an agent), a goal that can be refined through and/or-decompositions of a root goal into finer sub-goals, a task, and a resource. Secure Tropos adopts the notion of delegation to model the transfer of objectives (goals and tasks) from one actor to another, and it adopts resource provision among actors. Moreover, it introduces the ownership concept that capture the relation between actors and resources they own. Finally, it provides the trust concept to capture the actors' expectations in one another concerning their social dependencies, and it introduce the monitoring concept to compensate the lack of trust/distrust among actors concerning social dependencies.
IEEE 57 [132], "A Security Ontology with MDA for Software Development". Kang and Liang [132] propose security ontology for software development based on Model Driven Architecture (MDA) paradigm. The ontology includes most popular security concerns mentioned in literature such as auditing, threats, accountability, non-repudiation, risk, attacks, availability, frauds, confidentiality, asset, integrity, prevention, and Reputation.
SCH 18 [132], "Eliciting Security Requirements with Misuse Cases". Sindre and Opdahl [132] present a systematic approach to eliciting security requirements based on use cases. They extend the traditional use case approach to also consider misuse cases that represent unwanted behavior in the system to be developed. In particular, a use case diagram contains both, use cases and actors, as well as misuse cases and misusers. In addition, misuse cases adopts the ordinary use case relationships such as include, extend, and generalize. A use case is related to a misuse case using a directed association, which means that a misuse case threatens the use case. Moreover, a use case diagram can contain security use cases, which are special use cases that can mitigate misuse cases. In summary, an ordinary use cases represent requirements, security cases represent security requirements, and misuse cases represent security threats.
SCH 24 [130], "Addressing Privacy Requirements in System Design. the PriS Method ". Kalloniatis et al. [130] introduce PriS, a security requirements engineering method that consider users' privacy requirements. PriS considers privacy requirements as business goals and provides a methodological approach for analysing their effect onto the organizational processes. The conceptual model of PriS is based on the Enterprise Knowledge Development (EKD) framework [156], and it includes a set of concepts for modeling privacy requirements, such as: stakeholders, goals that can be either strategic goals or operational goals, and goals can be realized by processes. On the other hand, privacy requirements are a special type of goals (privacy goals), which constraint the causal transformation of organizational goals into processes. Privacy goals may be decomposed in simpler goals or may support/ conflict the achievement of other goals. Moreover, eight types of privacy goals have been identified corresponding to the eight privacy concerns namely, authentication, authorisation, identification, data protection, anonymity, pseydonymity, unlinkability, and unobservability.

SCH 28 [179], "Secure Tropos: a Security-oriented Extension of the Tropos Methodology". Mouratidis and Giorgini [179] introduce extensions to the Tropos methodology [32] to model security concerns throughout the whole development process. Secure Tropos adopts from Tropos methodology concepts for modeling actors, goals, resources, along with their different relations and social dependencies. In addition, it introduces concepts for modeling security requirements, such as a security constraint (e.g., privacy, integrity, and availability), which can be decomposed into one or more security subconstraints. Security constraint modeling is divided into security constraint delegation, security constraint assignment, and security constraint analysis. Secure Tropos also introduces secure entity, security features, security mechanisms, a secure capability, a secure dependency, and the threat concept.
SCH 41 [214], "A Taxonomy of Privacy". Solove [214] provides taxonomy for understanding a wide range of privacy related problems. The taxonomy specifies four main groups of possible harmful activities: (i) information collection: creates disruption based on the process of data gathering Two sub-classifications of information collection have been identified, surveillance and interrogation. (ii) information processing: refers to the use, storage, and manipulation of data that has been collected. Five different subclassifications of information processing have been identified: aggregation, identification, insecurity, secondary use, and Exclusion. (iii) information dissemination: in which the data holders transfer the information to others. Seven different sub-classifications of information dissemination have been identified: breach of confidentiality, disclosure, exposure, increased accessibility, blackmail, appropriation, and 7- distortion. (iv) invasion: involves impingements directly on the individual. Two different sub-classifications of information invasion have been identified: intrusion and 2-decisional interference.
Spgr 07 [162], "An Extended Ontology for Security Requirements. Massacci et al. [162] propose ontology for security requirements engineering, the ontology adopts concepts from Secure Tropos methodology [163], Problem Frame [107], and several industrial case studies. The most general concept in the ontology is Thing. An object is a thing that persists, and an event is an instantaneous happening that changes some objects. The object concept can be specialized into proposition, situation, entity and relationship. A proposition is an object representing a true/false statement. A situation is a partial world described by a proposition. An entity is an object that has a distinct, separate existence from all other things, though that existence need not be material. Entity is specialized into Actor, Action, Process, Resource, and Asset. Relationship can be specialized into do-dependency, can-dependency, trust-dependency, and/or refinement, contributes, provides, uses. In addition, damages is a relationship between an attack and an asset, where the attack causes harm to the asset. Exploits is a relationship between attack and vulnerability. Protects relates a security goal to an asset. Finally, denies relates an anti-goal to a requirement. Finally, a specification is an entity consisting of actions, quality propositions, and domain assumptions. Vulnerability is a

specialization of Situation and is adopted from the Security domain. While a threatconsists of a situation that includes an attacker and one or more vulnerabilities. Spgr 13 [71], "A Modeling Ontology for Integrating Vulnerabilities into Security Requirements Conceptual Foundation". Elahi et al. [71] propose a vulnerability-centric modeling ontology, which integrates empirical knowledge of vulnerabilities into the system development process. They identify a set of core concepts for security requirements elicitation, and they identify another set of concepts for capturing vulnerabilities and their effects on the system. The ontology contains several concepts, including: a concrete element that is a tangible entity (e.g., an activity, task, etc.), and it may bring a vulnerability into the system. Exploitation of vulnerabilities can have effects on other elements (affected elements), where the effect relation is characterized by the severity attribute. An attack involves the execution of malicious actions that one or more actors perform to satisfy some malicious goal. A concrete element may have a security impact on attacks, which can be interpreted as a security countermeasure that can be used to patch vulnerabilities. Spgr 02 01 [13], "From Trust to Dependability Through Risk Analysis". Asnar et al. [13] present an extension of the Tropos Goal-Risk framework. In particular, they introduce an approach to assess risk on the basis of trust relations among actors. In particular, they introduce the notion of trust to extend the risk assessment process. Using this framework, an actor can assess the risk in delegating the fulfillment of his objectives and decide whether or not the risk is acceptable. They also introduce the notion of trust level proposing three trust levels: Trust, Distrust, and NTrust (i.e., neither trust nor distrust), where a low level of trust increases the risk perceived by the depender about the achievement of his objectives. Spgr 02 02 [14], "Risk Modeling and Reasoning in Goal Models". Asnar et al. [14] propose a goal-oriented approach for modeling and reasoning about risks at requirements level, where risks are introduced and analyzed along the stakeholders goals and countermeasures. Their proposed framework is based on the Tropos methodology and extends it with new concepts and qualitative reasoning mechanisms to consider risks since the early phases of the requirements analysis. In their framework, a risk is an event that has a negative impact on the satisfaction of a goal, while a treatment is a countermeasure that can be adopted in order to mitigate the effects of the risk. Moreover, they consider likelihood as a property of the event, and they capture the likelihood by the level of evidence that supports and prevents the occurrence of the event (SAT and DEN). On the other hand, impact is used to capture the influence of an event to the goal fulfillment, and they classify impact under: strong positive, positive, negative, and strong negative. Spgr 03 01 [16], "Basic Concepts and Taxonomy of Dependable and Secure Computing". Avizienis et al. [16] propose a new taxonomy for dependable and secure computing based on an extensive analysis of the related literature. The authors provide precise definitions characterizing the various concepts

that come into play when addressing the dependability and security of computing and communication systems. The three top-level dimensions of this taxonomy are: attribute, threat, and means. The concept of attribute is analyzed in terms of: availability; reliability; safety; confidentiality; integrity; and maintainability. The concept of threat is further refined in terms of fault, error, and failure. While the concept of means is used to attain the various attributes of dependability and security, where these means can be grouped into four main categories: fault prevention; fault tolerance; fault removal ; and fault forecasting. Spgr 07 02 [263], "A Requirements Engineering Methodology for Trust, Security, and Privacy". Zannone [263] introduces the Secure i* (SI*) methodology that adopts from Secure Tropos the concepts of actors, goals, resources, along with their different relations and social dependencies, and it proposes new relation among roles, namely supervision. In SI*, an actor is defined along with a set of objectives, capabilities, and entitlements, which can be modeled through relations between actors and services (goals, tasks, and resources), namely: (1) require indicates that an actor intends to achieve a service, (2) be entitled indicates that an actor is the legitimate owner of a service, and (3) provide indicates that the actor has the capability to achieve a service. The delegation concept is refined in SI* into: (1) Delegation of execution (De), and (2) Delegation of permission (De). In addition, the trust concept is refined to cope with the refinement of delegation they propose into: (1) Trust of execution (Te), and (2) Trust of permission (Tp). Spgr 07 03 [152], "Introducing Abuse Frames for Analysing Security Requirements". Lin et al. [152] develop an approach using Problem Frames to analyze security problems in order to determine security vulnerabilities. In particular, they introduce the notion of an anti-requirement as the requirement of a malicious user that can subvert an existing requirement, and they incorporate anti-requirements into abuse frames to represent the notion of a security threat that is imposed by malicious users in a particular problem context. Spgr 08 01 [169], "Model-based Management of Information System Security Risk ". Mayer [169] proposes ISSRM (Information System Security Risk Management), a security risk management model. The ISSRM reference model addresses risk management at three different levels, combining together asset, risk, and risk treatment views, and it proposes concepts that are ordered in three main groups: (i) Asset-related concepts describe what assets are important to protect, and what criteria guarantee asset security; (ii) Risk-related concepts present how the risk itself is defined. A risk is the combination of a threat with one or more vulnerabilities leading to a negative impact harming the assets; and (iii) Risk treatment-related concepts describe what decisions, requirements and controls should be defined and implemented in order to mitigate possible risks. Spgr 08 03 [63], "A Knowledge-based Approach to Security Requirements for E-health Applications". Dritsas et al. [63] propose an ontology that includes the main security related concepts, and use the ontology for designing and

developing a set of security patterns that address a subset of these requirements for applications that provide e-health services. The concepts used in the proposed ontology includes: stakeholder, objective, threat, countermeasure, asset, vulnerability, deliberate attack, security pattern and security pattern context. A security pattern provides a specific set of countermeasures, and a security pattern context is defined as a set of asset, vulnerability, and deliberate attack triplets. Therefore, one can start from the generic security objectives, find the security pattern contexts that match them and choose specific security pattern, which ensures that the high level security objectives can be fulfilled by implementing the respective countermeasures. Spgr 13 01 [15], "Risk as Dependability Metrics for the Evaluation of Business Solutions: a Model-driven Approach". Asnar et al. [15] adopt and extend the Tropos Goal Model [14,13] by considering also the interdependency among the actors within an organization. Through this extension analysts can assess the risk perceived by each actor, taking into account the organizational environment where the actor acts. Based on such analysis, we have provided a method to assist analysts in determining the treatments to be introduced in order to make risks be acceptable by all actors. Spgr 13 02 [59], "The CORAS Methodology: Model-based Risk Assessment Using UML and UP ". Braber [59] introduces the CORAS methodology in which the Unified Modeling Language (UML) and Unified Process (UP) are combined to support a model-based risk assessment of security-critical systems. The CORAS ontology propose several concepts, such as context that influences the target, which contains assets and has its security requirements. Security requirements lead to security policies, which protect assets by reducing its related vulnerabilities that can be exploited by threats, which might reduce the value of the asset. A Risk contains an unwanted incident that has a certain consequence and frequency of occurrence. Spgr 13 03 [72], "A Vulnerability-centric Requirements Engineering Framework: Analyzing Security Attacks, Countermeasures, and Requirements based on Vulnerabilities. Elahi et al. [72] adopt and extend their previous work [71] by proposing an agent- and goal-oriented framework for eliciting and analyzing security requirements. They refined the goal model evaluation method that helps analysts verifying whether top goals are satisfied with the risk of vulnerabilities and attacks and assess the efficacy of security countermeasures against such risks. More specifically, the evaluation does not only specify if the goals are satisfied, but also makes it possible to understand why and how the goals are satisfied (or denied) by tracing back the evaluation to vulnerabilities, attacks, and countermeasures. Spgr 13 04 [123], "UMLsec: Extending UML for Secure Systems Development". Ju�rjens [123] proposes UMLsec that is an extension to UML modeling language, which allows for integrating security requirements modeling and analysis within the system development process. UMLsec is able to model security related features such as secrecy, integrity, access control, etc. It represents security feature on UML diagrams by providing several extension mechanisms, namely: (1) stereotypes: a new types of modeling elements that

extends the semantics of existing types in the UML meta-model; (2) tagged values: that is used to associate data with model elements and (3) constraints: that are used to define criteria to determine whether requirements are met or not by the system design. In UMLsec, integrity is modeled as a constraint, which can restrict unwanted modification (e.g., insert), but information quality can be affected in several other ways that cannot be captured by this approach.
Spgr 13 05 [167], "Adapting Secure Tropos for Security Risk Management in the Early Phases of Information Systems Development". Matulevicius et al. [167] have analyzed how Secure Tropos can be applied to analyze security risks at the early IS development phases. Their analysis suggested a number of improvements for Secure Tropos in order to deal better with security risk management activities. In particular, Secure Tropos could be improved with additional constructs adopted from existing security risk management models (e.g., ISSRM (Information System Security Risk Management)) such as risk, risk treatment, and control. More specifically, among the suggested risk-related concepts is a risk that presents how the risk itself is defined, what are the major principles that should be taken into account when defining the possible risks. The risk is described by the cause of the risk, and the impact of the risk captures the potential negative consequence of the risk, which can be represented by a negative contribution link between the attack and the related security constraint, i.e., the impact negates the security criteria.
Spgr 13 07 [199], "An Extended Misuse Case Notation: Including Vulnerabilities". R�stad [199] proposes an extended misuse case notation that includes the ability to represent vulnerabilities and the insider threat. In particular, beside the main concepts of misuse case notation (e.g., actors, use cases, misuse cases, misusers, etc.). R�stad introduce the insider concept to capture inside attackers, since the misuser concept in misuse cases was mainly proposed to address outside attackers. More specifically, an insider is a misusers that is also member of an authorized group for the entity being attacked. In addition, she introduce the vulnerability concept that is a weakness in the system, which can be exploited by the insider.
Spgr 18 03 [81], "Formalizing Information Security Knowledge". Fenz and Ekelhar [81] introduce security ontology for information security domain knowledge. In their ontology, a vulnerability is the absence of a proper safeguard,which could be exploited by a threat. A threat might threaten an asset, and it can be exploited by predefined threat, and mitigation is achieved by the implementation of one or more control. In addition, the severity of each vulnerability is rated by a three-point scale (high, medium, and low). A threat has a source, and a related security objectives. An asset is categorized either as a tangible or an intangible asset. While the data concept comprises metadata on the knowledge of an organization. The person concept is used to model physical persons in the ontology, and the organization concept comprises organizations in the broadest sense and assigns roles to them. A role is a physical person or organization relevant to the organization. Finally, a

location is used to relate location and threat information in order to assign a priori threat probabilities.
SCH 24 02 [114], "Privacy Risk Models for Designing Privacy-sensitive Ubiquitous Computing Systems". Hong et al. [114] propose a privacy risk model that captures privacy concerns at high abstraction level, and then refining them into concrete issues for specific applications. The privacy risk model consists of two parts: (1) a privacy risk analysis that poses a series of questions to help designers think about the social and organizational context in which an application will be used, the technology used to implement that application, and control and feedback mechanisms that end-users will use; and (2) privacy risk management that takes the unordered list of privacy risks from the privacy risk analysis, prioritizes them, and helps design teams identify solutions for helping end-users manage those issues.
SCH 28 01 [186], "STS-Tool: Security Requirements Engineering for SocioTechnical ". Paja et al. [186] present the STS-Tool, a modeling and analysis support tool for STS-ml (Socio-Technical Security modeling language), a security requirements modeling language for socio-technical systems. STS-ml consists of three complementary views: 1- The social view, 2- The information view, 3- The authorization view. Through these views, STS-ml supports different types of security needs: (1) Interaction (security) needs are securityrelated constraints on goal delegations and document provisions; (2) Authorisation needs determine which information can be used, how, for which purpose, and by whom; (3) Organisational constraints constrain the adoption of roles and the uptake of responsibilities. In addition, STS-ml supports the following interaction security needs: 1. Over goal delegations: (a) Noredelegation, (b) Non-repudiation, (c) Redundancy, (d) Trustworthiness, and (e) Availability. 2. Over-document provisions: (a) Integrity of transmission, (b) Confidentiality of transmission, (c) Availability. 3. From organizational constraints: (a) Separation of duties (SoD), and (b) Combination of duties (CoD).
SCH 43 01 [239], "Handbook of Privacy and Privacy-enhancing Technologies". Van Blarkom et al. [239] investigate several active areas related to privacy, Privacy-Enhancing Technologies (PET), intelligent software agents, and the inter-relations among these areas. Furthermore, they discussed the concepts of privacy and data protection, the European Directives that rule the protection of personal data and the relevant definitions. In particular, they investigate when personal data items become non-identifiable, the sensitivity of data, automated decisions, privacy preferences, and policies. In addition, they discussed existing technological solutions that offer agent user privacy protection, known under the name Privacy-Enhancing Technologies (PETs), the set of technologies/ principles that underlying PETs, and the legal basis for PET. Moreover, they discussed the Common Criteria for Information Technology Security Evaluation (CC) supplies important information for building privacy secure agents.

RQ2: What are the main concepts/relations that have been used for capturing privacy requirements? Each of the 34 selected studies has been deeply investigated to identify any concept/relation that can be used for capturing privacy requirements. We have focused on identifying any concept/relation that can be used for capturing privacy requirements in their social and organizational context. More specifically, we tried to identify any concept that is related to privacy, social and organizational threats that might threaten privacy needs, treatment/countermeasures that can be used to mitigate threats concerning privacy needs. The result is shown in Table 4, which presents the concepts/relations that have been identified in each selected studies. In particular, 55 concepts and relations4 have been identified, which have been grouped into four main groups based on their types:
Organizational. 27 concepts and relations have been identified for capturing the agentive entities of the system in terms of their objectives, entitlements, dependencies and their expectations concerning such dependencies. The organizational concepts and relations are further grouped into four sub-categories:
Agentive entities. 8 concepts and relations have been identified for capturing the active entities of the system (e.g., actor, user, etc. ).
Intentional entities. 5 concepts and relations have been identified for capturing objectives that active entities aim for achieve/want to perform (e.g., goal, task, activity, etc. ).
Informational entities. 8 concepts and relations have been identified for capturing informational assets (e.g., data, asset, information, etc.).
Entities interactions. 6 concepts and relations have been identified for capturing the entities dependencies and expectations concerning such dependencies (e.g., delegation, dependency, provision, trust, etc. ).
Risk. 10 concepts and relations have been identified for capturing risk related aspects (e.g., risk, threat, vulnerabilities, attack, etc.).
Treatment. 8 concepts and relations have been identified for capturing treatment related aspects (e.g., treatment, countermeasure, mitigate etc.).
Privacy. 9 concepts and relations have been identified for capturing privacy related aspects (e.g., anonymity, confidentiality, etc.).
Among the 55 identified concepts and relations, we have selected 38 main concepts and relations that can be used for capturing privacy requirements in their social and organizational context. In particular, these concepts and relations are 17 organizational, 9 risk, 5 treatment, and 7 privacy concepts, and they are shown in Bold typeset in Table 4. Each of the selected concepts and relations has been chosen based on the following two criteria: (1) its importance for capturing privacy requirements; and (2) the frequency of its appearance in the selected studies, which is shown in Table 5.
RQ3: Do existing privacy studies cover the main privacy concepts/relations? We answer RQ3 by comparing the privacy related concepts/relations presented in each selected study with the main privacy concepts/relations identified while answering RQ2. In Table 4, we use ( ) when the study presents a main privacy concept/relation, and (-)
4 When there are more than one concept with very close meaning, we have chosen the most appropriate one to represent all

Table 4: Summary of the privacy related concepts and relations identified in the studies

[240] [144] [28] [211] [248] [241] [155] [221] [235] [100] [132] [162] [71] [208] [130] [179] [214] [81] [15] [59] [72] [123] [167] [199] [169] [63] [263] [152] [16] [13] [14] [114] [186] [239]

Agentive

Intentional

Organizational

Informational

Interaction

actor

XXXXXX

XX

X

XXX XX XX XX XX

role

XXXXXX

X XXXXX X XX X XXX XXXXX

agent

XXXXX

X XXXXX XX X X X X XXXXX

user

--

-

--

stakeholder

-

-

-

-

-

person

-

is a

XXXXXX XX XXXXX XXXX X XXX XXXXX X

plays

XXXXXX XX XXXXX XXXX X XXX XXXXX X

goal

XX XX

XX

XX XX X X XXX XX

XX

objective

--

--

task

-- -

-

-

---

-

-- -

action

--

---

-

-

refinement

XXXXX

X XXXXX XX X X XXX XX XX X

asset

-

- - -- --

-- -

- -- -

informational X

XX

XX XXXXXX XXXX XXX XXXX

data

--

--

--

resource

-

-- - --

-

-

personal info X

XXXXXXXXXXXXX XXXXXXXXXXXXXX X

sensitive info

-

-

-

part of

XXXXXXXXXXXXXXXX XXXXXXXXXXXXXXX X

own

X XXXX X XXXXXX

XXXX XXX XXXXX X

obj deleg. X X X X X X X X X X X X X X X X X X X X X X X X X X X

perm. deleg. X X X X X X X X X X X X X X X X X X X X X X X X X X X X

info provision X X X X X X X X X X X X X X X X X X X X X X X X X X X

monitor

XXXXXXXX XXXXXXXXXXXXXXX XXXXXX X

obj trust X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

perm trust X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

risk

-

--

--

-

-----

threat

XXXXXXX

X

XX XX X

X

XX XX

inten. threat X X X X

XXXXX XXXX XXXX X XXXXXXXXX

casual threat X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

vulnerability X X

X

XX

XX X X

XX

XX XXXXXX

attack

-- - - ---

-

--

-

attacker

XXX X

XX

XXXXXX

X XXX XX

attack method X X X X X

XXXXXXXXXXXX XXX XXXXXXXXX

impact

XXXX X XXXX

XXXX X

X X XXXXXX XX

threaten

XXXXX

XXXX XXXX XXXXX XXX XXXX X

exploit

XXXX X

XX XXXXX X

XX

XXXXXXXXX

countermeasure -

----- -

-- --- -

--

mitigate

XXX XX

XXXXXXXX

XXXX

XXXX

XXX

control

--

-

--

-

treatment

-

s/p goal

XX XX

X

X

XX

X

XXXXX X

s/p constraint X X X X X X X X X X X X X X X X X X X

XXXXXXXXXXX

s/p policy X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

s/p mechanism X X

XX X XXXXXX XXXXXXXXXXXXXXXXXX

sec/priv req.

XXXX X

XX XXX XX

X

XXX

confidentiality X X X X X

XXXXX XXX

XXX

XXXX

integrity -

-----

-

--

-- -

-

availability -

- ---

-

--

-- -

-

non-repudiation X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

notice

X XXXXXXXXXXXXX

XXXXXXXXXXXXXXXX

anonymity X X X X X X X X X X X X X X X

XXXXXXXXXXXXXX X

transparency X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

accountability X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X

Risk

Treatment

Privacy

Table 5: The frequency of concepts/relations appearance in the selected studies

Conc./rel. actor stakeholder goal refinement resource own monitor

# Conc./rel.

# Conc./rel.

14 role

10 agent

5

person

1

is a

15 objective

3

task

12 asset

14 information

8

personal info. 5

sensitive info.

4 obj. deleg.

7 perm. deleg.

4 obj. trust

5 perm. trust

# Conc./rel.

#

12 user

5

7 plays

7

12 action

7

12 data

6

3 part of

2

6 info. provision 6

3 risk

11

threat attack threaten control s/p policy integrity anonymity

16 intin. threat 7 casual threat 4 vulnerability 15

11 attacker

16 attack method 5 impact

10

8 exploits

10 countermeasure 15 mitigate

10

6

treatment

1 s/p goal

19 s/p constraint 4

4 s/p mechanism 5 sec/priv req. 18 confidentiality 14

13 availability

12 non-repudiation 3 notice

4

4 transparency 3 accountability 2

when the study presents a normal privacy concept/relation. In addition, we use (X) to mark when a study misses a main concept/relation. Table 6 summarizes the percentage of the main privacy concepts/relations identified in each selected study with respect to the main four categories (organizational, risk, treatment, and privacy). Considering Table 4 and Table 6, it is easy to note that most studies miss main privacy related concepts/relations, i.e., none of them cover all the main privacy related concepts/relations. In RQ4, we discuss the limitation of each selected study.
RQ4: RQ4 What are the limitations of existing privacy studies? We answer this question by categorizing the studies into four groups (Group1-4) 5 based on the concepts categories (e.g., organizational, risk, treatment, and privacy) that the studies do not appropriately cover:
5 These groups are not mutually exclusive, i.e., a study may belong to all of them

Table 6: The percentage of the main privacy concepts/relations captured by each

selected study

Study

Org. Risk Tre. Pri. All Study

Org. Risk Tre. Pri. All

ACM 03 [240] 5/17 5/9 2/5 3/7 15/38 ACM 14 [144] 2/17 0/9 0/5 2/7 4/38

ACM 16 [28] 3/17 0/9 2/5 0/7 5/38 ACM 35 [211] 1/17 1/9 2/5 0/7 4/38

ACM 40 [248] 0/17 5/9 1/5 0/7 6/38 CIT 07 [241] 1/17 1/9 0/5 0/7 2/38

CIT 33 [155] 11/17 7/9 4/5 2/7 24/38 IEEE 12 [221] 6/17 6/9 2/5 1/7 15/38

IEEE 15[235] 0/17 5/9 3/5 2/7 10/38 IEEE 50 [100] 15/17 0/9 1/5 2/7 18/38

IEEE 57 [132] 0/17 1/9 1/5 4/7 6/38 Spgr 7 [162] 4/17 5/9 1/5 1/7 11/38

Spgr 13 [71] 2/17 6/9 1/5 1/7 10/38 SCH 18 [208] 1/17 1/9 0/5 0/7 2/38

SCH 24 [130] 0/17 1/9 1/5 0/7 2/38 SCH 28 [179] 8/17 1/9 4/5 3/7 16/38

SCH 41 [214] 5/17 0/9 0/5 3/7 8/38 Spgr 18 03 [81] 2/17 7/9 2/5 0/7 11/38

Spgr 13 01 [15] 3/17 0/9 1/5 0/7 4/38 Spgr 13 02 [59] 0/17 4/9 1/5 1/7 6/38

Spgr 13 03 [72] 10/17 5/9 1/5 1/7 17/38 Spgr 13 04 [123] 1/17 2/9 1/5 1/7 4/38

Spgr 13 05 [167] 10/17 4/9 2/5 1/7 17/38 Spgr 13 07 [199] 1/17 5/9 2/5 1/7 9/38

Spgr 08 01 [169] 1/17 7/9 2/5 1/7 11/38 Spgr 08 03 [63] 4/17 2/9 1/5 2/7 9/38

Spgr 07 02 [263] 11/17 0/9 1/5 2/7 14/38 Spgr 07 03 [152] 0/17 4/9 0/5 1/7 5/38

Spgr 03 01 [16] 0/17 1/9 0/5 1/7 2/38 Spgr 02 01 [13] 5/17 0/9 1/5 0/7 6/38

Spgr 02 02 [14] 2/17 0/9 1/5 0/7 3/38 SCH 24 02 [114] 2/17 3/9 0/5 3/7 8/38

SCH 28 01 [186] 15/17 1/9 1/5 5/7 22/38 SCH 43 01 [239] 5/17 0/9 0/5 5/7 10/38

Group 1, contains studies that do not appropriately cover the organizational concepts. In this group, we have identified 25 studies out of the 34 selected ones, including: ACM 03 Lamsweerde [240], ACM 14 Labda et al. [144], ACM 16 Braghin et al. [28], ACM 35 Singhal and Wijesekera [211], ACM 40 Wang and Guo [248], CIT 07 Lasheras et al. [241], IEEE 12 Souag et al. [221], IEEE 15 Tsoumas and Gritzalis [235], IEEE 57 Kang and Liang [132], Spgr 7 Massacci et al. [162], Spgr 13 Elahi et al. [71], SCH 18 Sindre and Opdahl [208], SCH 24 Kalloniatis et al. [130], Spgr 18 03 Fenz and Ekelhart [81], Spgr 13 01 Asnar et al. [15], Spgr 13 02 Braber et al. [59], Spgr 13 04 Ju�rjens [123], Spgr 13 07 R�stad [199], Spgr 08 01 Mayer [169], Spgr 08 03 Dritsas et al. [63], Spgr 07 03 Lin et al. [152], Spgr 03 01 Avizienis et al. [16], Spgr 02 01 Asnar et al. [13], Spgr 02 02 Asnar et al. [14], SCH 24 02 Hong et al. [114], SCH 43 01 Blarkom et al. [239].
Group 2, contains studies that do not appropriately cover risk concepts. In this group, we have identified 22 studies out of the 34 selected ones, including: ACM 14 Labda et al. [144], ACM 16 Braghin et al. [28], ACM 35 Singhal and Wijesekera [211], CIT 07 Lasheras et al. [241], IEEE 50 Giorgini et al. [100], IEEE 57 Kang and Liang [132], SCH 18 Sindre and Opdahl [208], SCH 24 Kalloniatis et al. [130], SCH 28 Mouratidis and Giorgini [179], SCH 41 Solove [214], Spgr 13 01 Asnar et al. [15], Spgr 13 02 Braber et al. [59], Spgr 13 04 Ju�rjens [123], Spgr 08 03 Dritsas et al. [63], Spgr 07 02 Zannone [263], Spgr 07 03 Lin et al. [152], Spgr 03 01 Avizienis et al. [16], Spgr 02 01 Asnar et al. [13], Spgr 02 02 Asnar et al. [14], SCH 24 02 Hong et al. [114], SCH 28 01 Paja et al. [186], SCH 43 01 Blarkom et al. [239].
Group 3, contains studies that do not appropriately cover treatment concepts. In this group, we have identified 31 studies out of the 34 selected ones, including: ACM 03 Lamsweerde [240], ACM 14 Labda et al. [144], ACM 16 Braghin et al. [28], ACM 35 Singhal and Wijesekera [211], ACM 40 Wang and Guo [248], CIT 07 Lasheras et al. [241], IEEE 12 Souag et al. [221], IEEE 50 Giorgini et al. [100], IEEE 57 Kang and Liang [132], Spgr 7 Massacci et al. [162], Spgr 13 Elahi et al. [71], SCH 18 Sindre and Opdahl [208], SCH 24 Kalloniatis et al. [130], SCH 41 Solove [214], Spgr 18 03 Fenz and Ekelhart [81], Spgr 13 01 Asnar et al. [15], Spgr 13 02 Braber et al. [59], Spgr 13 03 Elahi et al. [72], Spgr 13 04 Ju�rjens [123], Spgr 13 05 Matulevicius et al. [167], Spgr 13 07 R�stad [199], Spgr 08 01 Mayer [169], Spgr 08 03 Dritsas et al. [63], Spgr 07 02 Zannone [263], Spgr 07 03 Lin et al. [152], Spgr 03 01 Avizienis et al. [16], Spgr 02 01 Asnar et al. [13], Spgr 02 02 Asnar et al. [14], SCH 24 02 Hong et al. [114], SCH 28 01 Paja et al. [186], SCH 43 01 Blarkom et al. [239].
Group 4, contains studies that do not appropriately cover the privacy concepts. In this group, we have identified 31 studies out of the 34 selected ones, including: ACM 03 Lamsweerde [240], ACM 14 Labda et al. [144], ACM 16 Braghin et al. [28], ACM 35 Singhal and Wijesekera [211], ACM 40 Wang and Guo [248], CIT 07 Lasheras et al. [241], CIT 33 Liu et al. [155], IEEE 12 Souag et al. [221], IEEE 15 Tsoumas and Gritzalis [235], IEEE 50 Giorgini et al. [100], Spgr 7 Massacci et al. [162], Spgr 13 Elahi et al. [71], SCH 18 Sindre and Opdahl [208], SCH 24 Kalloniatis et al. [130], SCH 28 Mouratidis and Giorgini [179], SCH 41 Solove [214], Spgr 18 03 Fenz and Ekelhart [81], Spgr 13 01 Asnar et al. [15], Spgr 13 02 Braber et al. [59], Spgr 13 03 Elahi et al. [72], Spgr 13 04 Ju�rjens [123], Spgr 13 05 Matulevicius et al. [167], Spgr 13 07 R�stad [199], Spgr 08 01 Mayer [169], Spgr 08 03 Dritsas et al. [63], Spgr 07 02 Zannone [263], Spgr 07 03 Lin et al. [152], Spgr 03 01 Avizienis et al. [16], Spgr 02 01 Asnar et al. [13], Spgr 02 02 Asnar et al. [14], SCH 24 02 Hong et al. [114].

Based on the previous categories, we have 15 studies that do not appropriately cover all the four concepts categories, and 13 studies that do not appropriately cover three categories. 5 studies do not appropriately cover two categories, and one study does not appropriately cover only one categories. A detailed description of the concepts and relations that each of these studies does not cover can be obtained from Table 4.
Note that most of these studies have not been developed to address privacy related issues. Therefore, it is not a negative thing when they do not cover privacy related concepts. RQ4 has been considered in this study to assist authors of selected studies, if they aim to extend their frameworks and approaches to cover privacy concerns.
4 A novel privacy ontology
Several resent studies stress the need for addressing privacy concerns during the system design (e.g., Privacy by Design (PbD) [130,144]). Nevertheless, based on the results of this review, it is easy to note that no existing study covers all the main privacy concepts/relations that have been identified in the review, i.e., no existing ontology enables for capturing main privacy aspects and without such ontology it is almost impossible to address privacy concerns during the system design. Therefore, proposing such ontology would be a viable solution for this problem. To this end, we propose a novel privacy ontology based on the main privacy concepts/relations identified in Table 4. The meta-model of our ontology is depicted in Figure 5, and the concepts of the ontology are organized into four main dimensions:
Organizational dimension: proposes concepts to capture the social and technical components of the system in terms of their capabilities, objectives, and dependencies.
Risk dimension: proposes concepts to capture risks that might endanger privacy needs at the social and organizational levels.
Treatment dimension: proposes concepts to capture countermeasure techniques to mitigate risks to privacy needs.
Privacy dimension: proposes concepts to capture the stakeholders' (actors) privacy requirements/needs concerning their personal information.
In what follows, we define each of these dimensions in terms of their concepts and relations
(1) Organizational dimension. Most current complex systems consist of several autonomous components that interact and depend on one another for achieving their objectives. Therefore, this dimension includes the organizational concepts of the system, which have been further organized into several categories, including: intentional entities, entities' objectives, informational assets, entities interactions, and entities expectations concerning such interactions (social trust). In what follows, we define each of these dimensions along with their concepts and relations.
Agentive entities: represent the active entities of the system, we have selected three concepts along with two relations:
Actor represents an autonomous entity that has intentionality and strategic goals within the system. Actor can be decomposed into sub-units:
Role is an abstract characterization of an actor in terms of a set of behaviors and functionalities within some specialized context. A role can be a specialization (is a) of one another.

Agent is an autonomous entity that has a specific manifestation in the system. An agent can plays a role or more within the system, i.e., an agent inherits the properties of the roles it plays.
Intentional entities: the behavior of actors is, usually, determined by the objectives they aim to achieve. Therefore, we adopted the goal concept and and/or decomposition (refinement) relations to represent such objectives.
Goal is a state of affairs that an actor intends to achieve. When a goal is too coarse to be achieved, it can be refined through and/or-decompositions of a root goal into finer sub-goals.
And-decomposition implies that the achievement of the root-goal requires the achievement of all its sub-goals.
Or-decomposition is used to provide different alternatives to achieve the root goal, and it implies that the achievement of the root-goal requires the achievement of any of its sub-goals.
Informational entities: information is one of the most important concepts when we speak about privacy. Among the available concepts for capturing informational asset, e.g., data [144], a resource (physical or informational) [100,263,179,162], asset [132,72], etc., we have adopted the following concepts and relations:
Information represents any informational entity without intentionality. Information can be atomic or composite (composed of several parts), and we rely on part of relation to capture the relation between an information entity and its sub-parts. In the context of this work, we differentiate between two main types of information: Personal information any information that can be related (directly or indirectly) to an identified or identifiable legal entity (e.g., names, addresses, medical records, etc.), who has the right to control how such information can be used by others [28,239]. Public information any information that cannot be related (directly or indirectly) to an identified or identifiable legal entity, or personal information that has been made public by its legal entity [144].
Information type of use: actors may use information to achieve their goals. Our ontology adopts three relations between goals and information(e.g., produce, read, and modify), where each of these relations can be defined as follows:
Produce indicates that information can be created by achieving the goal that is responsible for its production;
Read indicates that the goal achievement depends on consuming such information; Modify indicates that the goal achievement depends on modifying such information.
Information ownership & permissions: as previously mentioned, we differentiate between personal and public information if it can be related (directly or indirectly) to an identified or identifiable legal entity. In what follows, we define the own concept that relates personal information to its legal entity, and we specify how information owner controls the usage to its personal information.
Own indicates that an actor is the legitimate owner of information, where information owner has full control over the use of information it owns.

trustor trustee delegator del eg at ee aims
Fig. 5: The meta-model of the proposed privacy ontology A permission is consent of a particular use of a particular object in a system [203],
i.e., the holder of the permission is allowed to perform some action(s) in the system. Information owner has the authority to control the use of its own information, i.e.,

Agent
1..n plays 1..n
Role
is_a

provideTo

1..n Provision 1..n of 1 Information

[Non-]Confidential providedBy 1..n

1..n

Public Information

Privacy Requirement

part of related acquire

1

0..n

1..n Personal 1..n Information

has

Vulnerability mitigates

own

0..n

Privacy

1

Goal

thre ate n exploits

0..n 0..n 1 1 1
Actor 1 monitor 1..n

Monitor 1..n

of

1 monitoree 1..n

1..n of

0..n

{XOR}

01 1 1 1

.

0

.

.

n

.

n

1

Permission

has 1..n

1..n

ToP:[P][R ][M]

1
Use
ToU:[P][R][M ]
1

over

Impact

implies

severity level

Threat

over

realizedBy
Privacy Constraint

aims

1

11 .. ..
nn

1..n Trust
1..n [dis]trust

1..n trustum 1..n trustum
{XOR}

Delegation 1..n [Non-]redelegate
1..n [Non-]repudiation

delegatum delegatum
{XOR}

1
1 1 0..n

Intentional
1..n
Threat

and/ or decomposed
1 0..n 1
Goal
2..n

1
1
Attack Method

Casual Threat

Privacy Privacy Mechanism Policy

Confidentiality Notice
Anonymity Transparency Accountability

the owner can control the delegated permissions over information it owns. In our ontology, information permissions are classified under (P)roduce, (R)ead, (M)odify permissions, which covers the three relations between goals and information that our ontology propose.
Entities interactions: actors may not have the required capabilities to achieve their own objectives by themselves (e.g., achieve a goal, furnish information, etc.). Therefore, they depend on one another for such objectives. In what follows, we discuss the concepts that are used for capturing the different actors' social interactions and dependencies.
Information provision indicates that an actor has the capability to deliver information to another one, where the source of the provision relation is the provider and the destination is the requester. Information provision has one attribute that describes the provisioning type, which can be either confidential or non-confidential, where the first guarantee the confidentiality of the transmitted information while the last does not.
Goal delegation indicates that one actor delegates the responsibility to achieve a goal to other actors, where the source of delegation called the delegator , the destination is called delegatee, and the subject of delegation is called delegatum.
Permissions delegation indicates that an actor delegates the permissions to produce, read and/or modify over a specific information to another actor.
Entities social trust: the need for trust arises when actors depend on one another for goals or permissions since such dependencies might entail risk [47,98]. More specifically, a delegator has no warranty that the delegated goal will be achieved or the delegated permissions will not be misused by the delegatee. Therefore, our ontology adopts the notion of trust and distrust to capture the actors' expectations of one another concerning their delegations:
Trust indicates the expectation of trustor that the trustee will behave as expected considering the trustum (e.g., trustee will achieve the delegated goal, or it will not misuse the delegated permission);
Distrust indicates the expectation of trustor that the trustee will not behave as expected considering the trustum (e.g., trustee will not achieve the delegated goal, or it will misuse the delegated permission).
Monitoring: we rely on monitoring to compensate the lack of trust or distrust in the trustee concerning the trustum [94,263].
Monitoring can be defined as the process of observing and analyzing the performance of an actor in order to detect any undesirable performance [103], where the source of monitoring is called the monitor and the destination is called monitoree.
(2) Risk dimension. Risk can be defined as an event that has a negative impact on the system, i.e., it is the possibility that a particular threat will harm one or more asset of a system by exploiting a vulnerability [132,211,169,71]. In our ontology, risk is not a primitive concept and we do not include it into the ontology, since it can be captured by other concepts such as threat, vulnerabilities, attack, etc. In what follows, we define the risk dimension related concepts along with their interrelations:

A threat is a potential incident that threaten an asset (personal information) by exploiting a vulnerability concerning such asset [169,211,132]. A threat can be either natural (e.g. earthquake, etc.), accidental (e.g. hardware/software failure, etc.), or intentional (e.g. theft of personal information, etc.)[81,241,220]. Therefore, the ontology differentiates between two types of threat:
Casual threat (natural or accidental): a threat that does not require a threat actor nor an attack method.
Intentional threat a threat that require a threat actor and a presumed attack method [152,162].
Threat actor is an actor that aims for achieving the intentional threat [199,169,71]. Attack method is a standard means by which a threat actor carries out an intentional
threat [169,72,220]. Impact is the consequence of the threat over the asset, and it can be characterized
by a severity attribute that captures the level of the impact (e.g. high, medium or low) [248,220]. A vulnerability is a weakness in the system, asset (personal information), etc. that can be exploited by a threat [199,169,211].
(3) Treatment dimension. This dimension introduces countermeasure concepts to mitigate risks, we adopted a high abstraction level countermeasure concepts to capture the required protection/treatment level (e.g., privacy goal), which can be refined into concrete protection/treatment constraints (e.g., mechanisms or policies) that can be implemented. The concepts of the treatment dimension are:
A privacy goal is an aim to counter threats and prevents harm to personal information by satisfying privacy criteria concerning such information.
A privacy constraint is a restriction that is used to realize/satisfy a privacy goal, constraints can be either a privacy policy or privacy mechanism.
A privacy policy is a privacy statement that defines the permitted and/or forbidden actions to be carried out by actors of the system toward information.
A privacy mechanism is a concrete technique to be implemented for helping towards the satisfaction of privacy goal (attribute).
(4) Privacy dimension. Introduce concepts to capture the stakeholders' (actors) privacy requirements/needs concerning their personal information. The concepts of the privacy dimension are:
Privacy requirement is used to capture the actors' (personal information owner/subject) privacy needs at a high abstraction level, and it is specialized from the privacy goal concept. Moreover, privacy requirement concept is further specialized into five more refined concepts.
Confidentiality, means personal information should be kept secure from any potential leaks and improper access [214,63,144]. We rely on the following principles to analyze confidentiality: Non-disclosure, personal information can only be disclosed if the owner's consent is provided, i.e., the disclosure of the personal information should be under the control of its legitimate owner [214,63,28,144]. Note that non-disclosure also cover information transmission that is why we differentiate between two types of information provision (confidential and non-confidential). Need to know (NtK), an actor should only use information if it is strictly necessary for completing a certain task [144,186].

Purpose of use, personal information should only be used for specific, explicit, legitimate purposes and not further used in a way that is incompatible with those purposes [239,214,63]. Purpose of use is able to address situations where an actor might be granted a permission to use some personal information for a legitimate purpose, yet after accessing it, he/she might use the information for some other purpose.
Notice, the data subject (information owner) should be notified when its information is being collected [239,214,63]. Notice is considered mainly to address situations where personal information related to a legitimate entity (data subject) is being collected without his/her knowledge.
Anonymity, the identity of the information owner should not be disclosed unless it is required [63,214], i.e., the primary/secondary identifiers of the data subject (e.g., name, social security number, address, etc. ) should be removed if they are not required and information still can be used for the same purpose after their removal. We rely on part of relation to model the internal structure of personal information, i.e., we link the identifiers of the data subject with the rest of the information item by the part of relation. If the identifiers are not required for the task, they can be easily removed, and information can be used without linking it back to its owner/data subject (unlinkability).
Transparency, information owner should be able to know who is using his/her information and for what purposes [239,63,132]. We rely on the following principles to analyze transparency:
Authentication, a mechanism that aims at verifying whether actors are who they claim they are [186].
Authorization, a mechanism that aims at verifying whether actors can use information in accordance with their credentials [63].
Accountability, information owner should have a mechanism available to them to hold information users accountable for their actions concerning information [63,132]. We rely on the following principles to analyze accountability:
Non-repudiation, the delegator cannot repudiate he/she delegated; and the delegatee cannot repudiate he/she accepted the delegation [132,186].
Not-re-delegation, the delegatee is requested by the delegator not to re-delegate the delegatum, i.e., the re-delegation of a goal/permission is forbidden [186].
5 Threats to validity
After presenting and discussing our systematic literature review, we discuss the threats to its validity in this section. Following Runeson et al. [200], we classify threats to validity under four types: construct, internal, external and reliability:
1- Construct threats: is concerned with to what extent a test measures what it claims to be measuring [200]. Construct validity is particularly important, since it might influence the internal validity as well [158]. We have identified the following threats:
Poor conceptualization of the construct: occurs when the predicted outcome of the study is defined too narrowly [158], i.e., using only one factor to analyze the subject of the study. To avoid this threat, the research objective has been transformed into several research questions and for each of these questions, several factors were

specified to evaluate whether they have been properly answered. In addition, we followed the best practices in the area to define the criteria while searching for and selecting the related studies (e.g., inclusion and exclusion criteria, quality assessment criteria, etc.). Systematic error: may occur while designing and conducting the review. To avoid such threat, the review protocol has been carefully designed based on well-adopted methods, and it has been strictly followed during the different phases of the review.
2- Internal threats: is concerned with factors that have not been considered in the study, and they could have influenced the investigated factors in the study [233,200]. One internal threat has been identified:
Publication bias: publication bias is a common threat to the validity of systematic reviews, and it refers to a situation where positive research results are more likely to be reported than negatives ones [136]. Our review focused on finding privacy related concepts/relations by reviewing the related literature, and there are no positive nor negative research results in such case. Despite this, we have specified very clear inclusion and exclusion criteria, and quality assessment criteria while searching for and selecting the related studies.
3- External threats: is concerned with to what extent the results of the study can be generalized [200]. One internal threat has been identified:
Completeness: it is almost impossible to capture all related studies, yet our review protocol and search strategy were very carefully designed to cover as much as possible of the related studies. In addition, we might exclude some relevant nonEnglish published studies since we only considered English studies in this review. To mitigate this limitation we performed a manual scan of the references of all the primary selected studies in order to identify those studies that were missed during the first search stage. However, we cannot guarantee that we have identified all the main available studies, which can be used to answer our research questions.
4- Reliability threats: is concerned with to what extent the study is dependent on the researcher(s), i.e., if another researcher(s) conducted the same study, the result should be the same. The search terms, search sources, inclusion and exclusion criteria, quality assessment questions, etc. are all available, and any researcher can repeat the review and he should get similar results. However, the researcher should take into consideration the time when the studies search process was performed, i.e., the researcher should limit the search time to March 2016.
6 Related work
There are few systematic reviews concerning privacy/securities ontologies. For instance, Souag et al. [219] performed a systematic review that proposes an analysis and a typology of existing security ontologies. While Blanco et al. [24] conducted a systematic review with a main aim for identifying, extracting and analyzing the main proposals for security ontologies. Fabian et al. [78] present a conceptual framework for security requirements engineering by mapping the diverse terminologies of different security requirements engineering methods to that framework. Moreover, a security ontology

for capturing security requirements have been presented in [220]. However, the focus of all the previously mentioned studies was security ontology.
On the other hand, Blanco et al. [23] conduct a systematic review for extracting the key requirements that an integrated and unified security ontology should have. While Mellado et al. [172] carried out a systematic review of the existing literature concerning security requirements engineering in order to summarize the current contributions and to provide a road map for future research in this area. Iankoulova and Daneva [117] performed a systematic review concerning the security requirements of cloud computing. In particular, they have classified the main identified security requirements under nine sub-areas: access control, attack/harm detection, non-repudiation, integrity, security auditing, physical protection, privacy, recovery, and prosecution. Li [150] conducted a systematic review concerning online information privacy concerns, consequences, and moderating effects. Based on the review outcome, he proposed a framework to illustrate the relationships between the previously mentioned factors and to highlight opportunities for further improvement. Finally, Ferna�ndez-Alema�n et al. [83] performed systematic literature review for identifying and analyzing critical privacy and security aspects of the electronic health record systems.
7 Conclusions and Future Work
In this paper, we argued that many wrong design decisions might be made due to the insufficient knowledge about the privacy-related concepts, and we advocate that a welldefined privacy ontology that captures the privacy related concepts along with their interrelations can solve this problem. Therefore, we conduct a systematic review concerning the existing privacy/security literature with a main purpose of identifying the main concepts along with their interrelation for capturing privacy requirements. The objectives of the research were considered to have been achieved since the research questions posed have been answered. Moreover, we used the identified concepts/relations for proposing a privacy ontology to be used by software engineers while dealing with privacy requirements.
For future work, we aim to develop core privacy ontology to be used by software/security engineers when dealing with privacy requirements. To achieve that, we are planning to contact the authors of the selected studies to get their feedback concerning the proposed privacy ontology. In addition, we will conduct a controlled experiment with software/security engineers to evaluate the usability of the ontology. Finally, we plan to evaluate the completeness and validity of the ontology by deploying it to capture the privacy requirements for two real case studies that belong to different domains (e.g., medical sector and public administration).
References
1. Abulaish, M., Nabi, S. I., Alghathbar, K., and Chikh, A. Simont: A security information management ontology framework. In Secure and Trust Computing, Data Management and Applications. Springer, 2011, pp. 201�208.
2. Acquisti, A., Friedman, A., and Telang, R. Is there a cost to privacy breaches? an event study. ICIS 2006 Proceedings (2006), 94.
3. Ahamed, S. I., Monjur, M., and Islam, M. S. CCTB: Context correlation for trust bootstrapping in pervasive environment. In 4th International Conference on Intelligent Environments (IET) (2008), IET, pp. 1�8.

4. Akmayeva, G., and Shoniregun, C. Ontology of e-learning security. In Information Society (i-Society), 2010 International Conference on (2010), IEEE, pp. 652�655.
5. Alam, M. Model driven security engineering for the realization of dynamic security requirements in collaborative systems. In Models in Software Engineering. Springer, 2006, pp. 278�287.
6. Albers, M., Jonker, C. M., Karami, M., and Treur, J. Agent models and different user ontologies for an electronic market place. Knowledge and Information Systems 6, 1 (2004), 1�41.
7. Alliance, S. C. Hipaa compliance and smart cards: Solutions to privacy and security requirements. Online at http://www. datakey. com/resources/HIPAA Compliance and Smart Cards FINAL. pdf (2003).
8. Amagasa, T., Zhang, F., Sakuma, J., and Kitagawa, H. A scheme for privacy-preserving ontology mapping. In Proceedings of the 18th International Database Engineering & Applications Symposium (2014), ACM, pp. 87�95.
9. Analyti, A., Antoniou, G., Dama�sio, C. V., and Pachoulakis, I. A framework for modular erdf ontologies. Annals of mathematics and artificial intelligence 67, 3-4 (2013), 189�249.
10. Anto�n, A. I., Earp, J. B., and Reese, A. Analyzing website privacy requirements using a privacy goal taxonomy. In Requirements Engineering, 2002. Proceedings. IEEE Joint International Conference on (2002), IEEE, pp. 23�31.
11. Ashburner, M., Ball, C. A., Blake, J. A., Botstein, D., Butler, H.,
Cherry, J. M., Davis, A. P., Dolinski, K., Dwight, S. S., Eppig, J. T.,
et al. Gene ontology: tool for the unification of biology. Nature genetics 25, 1 (2000), 25�29. 12. Asim, M., Petkovic�, M., Qu, M., and Wang, C. An interoperable security framework for connected healthcare. In Consumer Communications and Networking Conference (CCNC), 2011 IEEE (2011), IEEE, pp. 116�120. 13. Asnar, Y., Giorgini, P., Massacci, F., and Zannone, N. From trust to dependability through risk analysis. In The Second InternationalConference on Availability, Reliability and Security, ARES'07. (2007), IEEE, pp. 19�26. 14. Asnar, Y., Giorgini, P., and Mylopoulos, J. Risk modelling and reasoning in goal models, technical report DIT-06-008. Tech. rep., Universit�a degli studi di Trento, 2006. 15. Asnar, Y., Moretti, R., Sebastianis, M., and Zannone, N. Risk as dependability metrics for the evaluation of business solutions: a model-driven approach. In Third Conference on Availability, Reliability and Security, ARES08 (2008), IEEE, pp. 1240�1247. 16. Avizienis, A., Laprie, J.-C., Randell, B., and Landwehr, C. Basic concepts and taxonomy of dependable and secure computing. Dependable and Secure Computing, IEEE Transactions on 1, 1 (2004), 11�33. 17. Balopoulos, T., Gymnopoulos, L., Karyda, M., Kokolakis, S., Gritzalis, S., and Katsikas, S. A framework for exploiting security expertise in application development. In Trust and Privacy in Digital Business. Springer, 2006, pp. 62�70. 18. Bao, J., Slutzki, G., and Honavar, V. Privacy-preserving reasoning on the semanticweb. In International Conference on Web Intelligence, IEEE/WIC/ACM (2007), IEEE, pp. 791�797. 19. Beckers, K., Eicker, S., Fa�bender, S., Heisel, M., Schmidt, H., and Schwittek, W. Ontology-based identification of research gaps and immature research areas. In Multidisciplinary Research and Practice for Information Systems. Springer, 2012, pp. 1�16.

20. Ben Brahim, M., Chaari, T., Ben Jemaa, M., and Jmaiel, M. Semantic matching of web services security policies. In Risk and Security of Internet and Systems (CRiSIS), 2012 7th International Conference on (2012), IEEE, pp. 1�8.
21. Bishop, M. What is computer security? Security & Privacy, IEEE 1, 1 (2003), 67�69.
22. Blackwell, C. A security ontology for incident analysis. In Proceedings of the Sixth Annual Workshop on Cyber Security and Information Intelligence Research (2010), ACM, p. 46.
23. Blanco, C., Lasheras, J., Ferna�ndez-Medina, E., Valencia-Garc�ia, R., and Toval, A. Basis for an integrated security ontology according to a systematic review of existing proposals. Computer Standards & Interfaces 33, 4 (2011), 372� 388.
24. Blanco, C., Lasheras, J., Valencia-Garc�ia, R., Ferna�ndez-Medina, E., Toval, A., and Piattini, M. A systematic review and comparison of security ontologies. In 3rd Conference on Availability, Reliability and Security, ARES '08 (2008), IEEE, pp. 813�820.
25. Blanquer, I., Herna�ndez, V., Segrelles, D., and Torres, E. Enhancing privacy and authorization control scalability in the grid through ontologies. Information Technology in Biomedicine, IEEE Transactions on 13, 1 (2009), 16�24.
26. Blobel, B. Intelligent security and privacy solutions for enabling personalized telepathology. Diagnostic pathology 6, Suppl 1 (2011), S4.
27. Bouna, B. A., Chbeir, R., and Gabillon, A. The image protector-a flexible security rule specification toolkit. In Security and Cryptography (SECRYPT), 2011 Proceedings of the International Conference on (2011), IEEE, pp. 345�350.
28. Braghin, S., Coen-Porisini, A., Colombo, P., Sicari, S., and Trombetta, A. Introducing privacy in a hospital information system. In Proceedings of the fourth international workshop on Software engineering for secure systems (2008), ACM, pp. 9�16.
29. Brar, A., and Kay, J. Privacy and security in ubiquitous personalized applications. School of Information Technologies, University of Sydney, 2004.
30. Breaux, T. D., and Anto�n, A. I. Analyzing regulatory rules for privacy and security requirements. Software Engineering, IEEE Transactions on 34, 1 (2008), 5�20.
31. Breaux, T. D., Hibshi, H., and Rao, A. Eddy, a formal language for specifying and analyzing data flow specifications for conflicting privacy requirements. Requirements Engineering 19, 3 (2014), 281�307.
32. Bresciani, P., Perini, A., Giorgini, P., Giunchiglia, F., and Mylopoulos, J. Tropos: An agent-oriented software development methodology. Autonomous Agents and Multi-Agent Systems 8, 3 (2004), 203�236.
33. Camp, L. J. Designing for trust. In Trust, reputation, and security: Theories and practice. Springer, 2002, pp. 15�29.
34. Campbell, K., Gordon, L. A., Loeb, M. P., and Zhou, L. The economic cost of publicly announced information security breaches: empirical evidence from the stock market. Journal of Computer Security 11, 3 (2003), 431�448.
35. Carminati, B., Ferrari, E., and Hung, P. C. Security conscious web service composition. In International Conference on Web Services ICWS'06 (2006), IEEE, pp. 489�496.
36. Cavoukian, A. Privacy by design: Origins, meaning, and prospects. Privacy Protection Measures and Technologies in Business Organizations: Aspects and Standards: Aspects and Standards (2011), 170.

37. Cavoukian, A., et al. Privacy by design: The 7 foundational principles. Information and Privacy Commissioner of Ontario, Canada (2009).
38. Ceravolo, P. Managing identities via interactions between ontologies. In On The Move to Meaningful Internet Systems OTM Workshops (2003), Springer, pp. 732�740.
39. Chandramouli, K., Fernandez Arguedas, V., and Izquierdo, E. Knowledge modeling for privacy-by-design in smart surveillance solution. In Advanced Video and Signal Based Surveillance (AVSS), 2013 10th IEEE International Conference on (2013), IEEE, pp. 171�176.
40. Chase, M., and Chow, S. S. Improving privacy and security in multi-authority attribute-based encryption. In Proceedings of the 16th ACM conference on Computer and communications security (2009), ACM, pp. 121�130.
41. Chen, H., Finin, T., and Joshi, A. An ontology for context-aware pervasive computing environments. The Knowledge Engineering Review 18, 03 (2003), 197� 207.
42. Chen, H., Finin, T., and Joshi, A. The SOUPA ontology for pervasive computing. In Ontologies for agents: Theory and experiences. Springer, 2005, pp. 233�258.
43. Chen, H., Finin, T., Joshi, A., Kagal, L., Perich, F., and Chakraborty, D. Intelligent agents meet the semantic web in smart spaces. Internet Computing, IEEE 8, 6 (2004), 69�79.
44. Chen, H., Perich, F., Finin, T., and Joshi, A. Soupa: Standard ontology for ubiquitous and pervasive applications. In Mobile and Ubiquitous Systems: Networking and Services, 2004. MOBIQUITOUS 2004. The First Annual International Conference on (2004), IEEE, pp. 258�267.
45. Chen, S., and Williams, M.-A. An ontological study of data purpose for privacy policy enforcement. In Privacy, Security, Risk and Trust (PASSAT) and Third Inernational Conference on Social Computing (SocialCom) (2011), IEEE, pp. 1208�1213.
46. Chen, S.-W., Tseng, Y.-T., and Lai, T.-Y. The design of an ontology-based service-oriented architecture framework for traditional chinese medicine healthcare. In 14th International Conference on e-Health Networking, Applications and Services (Healthcom) (2012), IEEE, pp. 353�356.
47. Chopra, K., and Wallace, W. Trust in electronic environments. In System Sciences, 2003. Proceedings of the 36th Annual Hawaii International Conference on (2003), Ieee, pp. 10�pp.
48. Chor, B., Kushilevitz, E., Goldreich, O., and Sudan, M. Private information retrieval. Journal of the ACM (JACM) 45, 6 (1998), 965�981.
49. Chowdhury, M. M., Chamizo, J., Noll, J., and Go�mez, J. M. Capturing semantics for information security and privacy assurance. In Ubiquitous Intelligence and Computing. Springer, 2008, pp. 105�118.
50. Chowdhury, M. M., Noll, J., and Gomez, J. M. Enabling access control and privacy through ontology. In Innovations in Information Technology, 2007. IIT'07. 4th International Conference on (2007), IEEE, pp. 168�172.
51. Ciuciu, I., Claerhout, B., Schilders, L., and Meersman, R. Ontology-based matching of security attributes for personal data access in e-health. In On the Move to Meaningful Internet Systems: OTM 2011. Springer, 2011, pp. 605�616.
52. Coma, C., Cuppens-Boulahia, N., Cuppens, F., and Cavalli, A. R. Context ontology for secure interoperability. In Availability, Reliability and Security, 2008. ARES 08. Third International Conference on (2008), IEEE, pp. 821�827.

53. Compagna, L., Khoury, P. E., Massacci, F., Thomas, R., and Zannone, N. How to capture, model, and verify the knowledge of legal, security, and privacy experts: a pattern-based approach. In Proceedings of the 11th international conference on Artificial intelligence and law (2007), ACM, pp. 149�153.
54. Da Silva, G., Rademaker, A., Vasconcelos, D., Amaral, F., Baz�ilio, C., Costa, V., and Haeusler, E. Dealing with the formal analysis of information security policies through ontologies: A case study. In Proceedings of the Third Australasian Workshop on Advances in Ontologies-Volume 85 (2007), Australian Computer Society, Inc., pp. 55�60.
55. D'Agostini, S., Di Giacomo, V., Pandolfo, C., and Presenza, D. An ontology for run-time verification of security certificates for soa. In 7th International Conference on Availability, Reliability and Security (ARES) (2012), IEEE, pp. 525�533.
56. Daramola, O., Sindre, G., and Stalhane, T. Pattern-based security requirements specification using ontologies and boilerplates. In Requirements Patterns (RePa), 2012 IEEE Second International Workshop on (2012), IEEE, pp. 54�59.
57. de Azevedo, R. R., Freitas, F., de Almeida, S. C., Almeida, M. J. S., de Barros C Filho, E. C., and Veras, W. C. Coresec: an ontology of security aplied to the business process of management. In Proceedings of the 2008 Euro American Conference on Telematics and Information Systems (2008), ACM, p. 13.
58. Delgado, J., Gallego, I., Llorente, S., and Garc�ia, R. Regulatory ontologies: An intellectual property rights approach. In On The Move to Meaningful Internet Systems 2003: OTM 2003 Workshops (2003), Springer, pp. 621�634.
59. den Braber, F., Dimitrakos, T., Gran, B. A., Lund, M. S., St�len, K., and Aagedal, J. �. The CORAS methodology: model-based risk assessment using UML and up. UML and the Unified Process (2003), 332�357.
60. Denker, G., Kagal, L., Finin, T., Paolucci, M., and Sycara, K. Security for daml web services: Annotation and matchmaking. In The Semantic WebISWC. Springer, 2003, pp. 335�350.
61. Dhiah el Diehn, I., and Berlik, S. An ontology-based approach for managing and maintaining privacy in information systems. Springer, 2006.
62. Donner, M. Toward a security ontology. IEEE Security & Privacy 1, 3 (2003), 0006�7.
63. Dritsas, S., Gymnopoulos, L., Karyda, M., Balopoulos, T., Kokolakis, S., Lambrinoudakis, C., and Katsikas, S. A knowledge-based approach to security requirements for e-health applications. Electronic Journal for E-Commerce Tools and Applications (2006).
64. Du�rbeck, S., Schillinger, R., and Kolter, J. Security requirements for a semantic service-oriented architecture. In Availability, Reliability and Security, 2007. ARES 2007. The Second International Conference on (2007), IEEE, pp. 366�373.
65. Dzung, D. V., and Ohnishi, A. Ontology-based reasoning in requirements elicitation. In Software Engineering and Formal Methods, 2009 Seventh IEEE International Conference on (2009), IEEE, pp. 263�272.
66. Eiter, T., Ianni, G., Polleres, A., Schindlauer, R., and Tompits, H. Reasoning with rules and ontologies. In Reasoning web. Springer, 2006, pp. 93�127.
67. Ekclhart, A., Fenz, S., Goluch, G., and Weippl, E. Ontological mapping of common criterias security assurance requirements. In New Approaches for Security, Privacy and Trust in Complex Environments. Springer, 2007, pp. 85� 95.

68. Ekelhart, A., Fenz, S., Klemen, M., and Weippl, E. Security ontologies: Improving quantitative risk analysis. In System Sciences, 2007. HICSS 2007. 40th Annual Hawaii International Conference on (2007), IEEE, pp. 156a�156a.
69. Ekelhart, A., Fenz, S., Klemen, M. D., and Weippl, E. R. Security ontology: Simulating threats to corporate assets. In International Conference on Information Systems Security (2006), Springer, pp. 249�259.
70. El-Khatib, K., Korba, L., Xu, Y., and Yee, G. Privacy and security in elearning. International Journal of Distance Education Technologies (IJDET) 1, 4 (2003), 1�19.
71. Elahi, G., Yu, E., and Zannone, N. A modeling ontology for integrating vulnerabilities into security requirements conceptual foundations. In ER 2009. Springer, 2009, pp. 99�114.
72. Elahi, G., Yu, E., and Zannone, N. A vulnerability-centric requirements engineering framework: analyzing security attacks, countermeasures, and requirements based on vulnerabilities. Requirements engineering 15, 1 (2010), 41�62.
73. Elahi, N., Chowdhury, M. M., and Noll, J. Semantic access control in web based communities. In Computing in the Global Information Technology, 2008. ICCGI'08. The Third International Multi-Conference on (2008), IEEE, pp. 131� 136.
74. Elc�i, A. Isn't the time ripe for a standard ontology on security of information and networks? In Proceedings of the 7th International Conference on Security of Information and Networks (2014), ACM, p. 1.
75. Emery, F., and Trist, E. Socio-technical systems. management sciences, models and techniques. churchman cw et al, 1960.
76. Evesti, A., and Ovaska, E. Ontology-based security adaptation at run-time. In 4th IEEE International Conference on Self-Adaptive and Self-Organizing Systems (SASO) (2010), IEEE, pp. 204�212.
77. Evfimievski, A., Gehrke, J., and Srikant, R. Limiting privacy breaches in privacy preserving data mining. In Proceedings of the twenty-second ACM SIGMOD-SIGACT-SIGART symposium on Principles of database systems (2003), ACM, pp. 211�222.
78. Fabian, B., Gu�rses, S., Heisel, M., Santen, T., and Schmidt, H. A comparison of security requirements engineering methods. Requirements engineering 15, 1 (2010), 7�40.
79. Fensel, D. Ontologies: A silver bullet for knowledge management and electroniccommerce (2000). Berlin: Spring-Verlag.
80. Fenz, S. Ontology-based generation of it-security metrics. In Proceedings of the 2010 ACM Symposium on Applied Computing (2010), ACM, pp. 1833�1839.
81. Fenz, S., and Ekelhart, A. Formalizing information security knowledge. In Proceedings of the 4th international Symposium on information, Computer, and Communications Security (2009), ACM, pp. 183�194.
82. Fenz, S., Goluch, G., Ekelhart, A., Riedl, B., and Weippl, E. Information security fortification by ontological mapping of the iso/iec 27001 standard. In Dependable Computing, 2007. PRDC 2007. 13th Pacific Rim International Symposium on (2007), IEEE, pp. 381�388.
83. Ferna�ndez-Alema�n, J. L., Sen~or, I. C., Lozoya, P. A� . O., and Toval, A. Security and privacy in electronic health records: A systematic literature review. Journal of biomedical informatics 46, 3 (2013), 541�562.
84. Fernandez Arguedas, V., Izquierdo, E., and Chandramouli, K. Surveillance ontology for legal, ethical and privacy protection based on skos. In Digital

Signal Processing (DSP), 2013 18th International Conference on (2013), IEEE, pp. 1�5. 85. Ferrari, E., and Thuraisingham, B. Security and privacy for web databases and services. In Advances in Database Technology-EDBT 2004. Springer, 2004, pp. 17�28. 86. Firesmith, D. Engineering safety and security related requirements for software intensive systems. In ICSE Companion (2007), p. 169. 87. Firesmith, D. G. Security use cases. Journal of object technology 2, 3 (2003). 88. Firesmith, D. G. A taxonomy of security-related requirements. In International Workshop on High Assurance Systems (RHAS'05) (2005), Citeseer. 89. Floridi, L. The ontological interpretation of informational privacy. Ethics and Information Technology 7, 4 (2005), 185�200. 90. Foster, I., Kesselman, C., Tsudik, G., and Tuecke, S. A security architecture for computational grids. In Proceedings of the 5th ACM conference on Computer and communications security (1998), ACM, pp. 83�92. 91. Gandhi, R., and Lee, S.-W. Ontology guided risk analysis: From informal specifications to formal metrics. In Advances in Information and Intelligent Systems. Springer, 2009, pp. 227�249. 92. Gandhi, R. A., and Lee, S. W. Discovering multidimensional correlations among regulatory requirements to understand risk. ACM Transactions on Software Engineering and Methodology (TOSEM) 20, 4 (2011), 16. 93. Gandon, F. L., and Sadeh, N. M. Semantic web technologies to reconcile privacy and context awareness. Web Semantics: Science, Services and Agents on the World Wide Web 1, 3 (2004), 241�260. 94. Gans, G., Jarke, M., Kethers, S., and Lakemeyer, G. Modeling the impact of trust and distrust in agent networks. In Proc. of AOIS'01 (2001), pp. 45�58. 95. Gao, F., He, J., Peng, S., Wu, X., and Liu, X. An approach for privacy protection based-on ontology. In Networks Security Wireless Communications
and Trusted Computing (NSWCTC), 2010 Second International Conference on (2010), vol. 2, IEEE, pp. 397�400. 96. Garcia, D., Toledo, M. B. F., Capretz, M. A., Allison, D. S., Blair, G. S., Grace, P., and Flores, C. Towards a base ontology for privacy protection in service-oriented architecture. In Service-Oriented Computing and Applications (SOCA), 2009 IEEE International Conference on (2009), IEEE, pp. 1�8. 97. Gellman, R. Privacy, consumers, and costs: How the lack of privacy costs consumers and why business studies of privacy costs are biased and incomplete. In Ford Foundation (2002). 98. Gharib, M., and Giorgini, P. Analyzing trust requirements in socio-technical systems: A belief-based approach. In IFIP Working Conference on The Practice of Enterprise Modeling (2015), Springer, pp. 254�270. 99. Gharib, M., Salnitri, M., Paja, E., Giorgini, P., Mouratidis, H., Pavlidis, M., Ruizz, J. F., Fernandez, S., and Della Siria, A. Privacy requirements: Findings and lessons learned in developing a privacy platform. In 24nd International Requirements Engineering Conference (RE), to appear (2016), IEEE. 100. Giorgini, P., Massacci, F., Mylopoulos, J., and Zannone, N. Modeling security requirements through ownership, permission and delegation. In 13th International Conference on Requirements Engineering (2005), IEEE, pp. 167� 176. 101. Guan, H., Wang, X., and Yang, H. A framework for security driven software evolution. In Automation and Computing (ICAC), 2014 20th International Conference on (2014), IEEE, pp. 194�199.

102. Guarino, N. Formal ontology in information systems: Proceedings of the first international conference (FOIS'98), June 6-8, Trento, Italy, vol. 46. IOS press, 1998.
103. Guessoum, Z., Ziane, M., and Faci, N. Monitoring and organizational-level adaptation of multi-agent systems. In Proceedings of the Third International Joint Conference on Autonomous Agents and Multiagent Systems-Volume 2 (2004), IEEE Computer Society, pp. 514�521.
104. Gu�rses, S., Troncoso, C., and Diaz, C. Engineering privacy by design. Computers, Privacy & Data Protection 14 (2011).
105. Hadzic, M., Dillon, T., and Chang, E. Use of ontology technology for standardization of medical records and dealing with associated privacy issues. In Industrial Technology, 2006. ICIT 2006. IEEE International Conference on (2006), IEEE, pp. 2839�2845.
106. Hadzic, M., Wongthongtham, P., Dillon, T., and Chang, E. Case study I: Ontology-based multi-agent system for human disease studies. In Ontology-Based Multi-Agent Systems. Springer, 2009, pp. 179�216.
107. Haley, C. B., Laney, R., Moffett, J. D., and Nuseibeh, B. Security requirements engineering: A framework for representation and analysis. Software Engineering, IEEE Transactions on 34, 1 (2008), 133�153.
108. He, Q., Anto�n, A. I., et al. A framework for modeling privacy requirements in role engineering. In Proc. of REFSQ (2003), vol. 3, pp. 137�146.
109. Hecker, M., and Dillon, T. Privacy support and evaluation on an ontological basis. In 23rd International Conference on Data Engineering Workshop (2007), IEEE, pp. 221�227.
110. Hecker, M., Dillon, T. S., and Chang, E. Privacy ontology support for e-commerce. Internet Computing, IEEE 12, 2 (2008), 54�61.
111. Hentea, M. Multi-agent security service architecture for mobile learning. In
Information Technology: Research and Education, 2004. ITRE 2004. 2nd International Conference on (2004), IEEE, pp. 91�95. 112. Heupel, M., Fischer, L., Bourimi, M., and Scerri, S. Ontology-enabled access control and privacy recommendations. In Mining, Modeling, and Recommending'Things' in Social Media. Springer, 2015, pp. 35�54. 113. Hinze, A., Sachs, K., and Buchmann, A. Event-based applications and enabling technologies. In Proceedings of the Third ACM International Conference on Distributed Event-Based Systems (2009), ACM, p. 1. 114. Hong, J. I., Ng, J. D., Lederer, S., and Landay, J. A. Privacy risk models for designing privacy-sensitive ubiquitous computing systems. In Proceedings of
the 5th conference on Designing interactive systems: processes, practices, methods, and techniques (2004), ACM, pp. 91�100. 115. Hoss, A. M., and Carver, D. L. Towards combining ontologies and model weaving for the evolution of requirements models. In Innovations for requirement analysis. From stakeholders needs to formal designs. Springer, 2007, pp. 85�102. 116. Hsieh, C.-F., Huang, Y.-F., and Chen, R.-C. A light-weight ranger intrusion detection system on wireless sensor networks. In Fifth International Conference on Genetic and Evolutionary Computing (ICGEC) (2011), IEEE, pp. 49�52. 117. Iankoulova, I., and Daneva, M. Cloud computing security requirements: A systematic review. In 2012 Sixth International Conference on Research Challenges in Information Science (RCIS) (2012), IEEE, pp. 1�7. 118. Ionita, C. M., and Osborn, S. L. Specifying an access control model for ontologies for the semantic web. In Secure Data Management. Springer, 2005, pp. 73�85.

119. Isaza, G., Castillo, A., Lo�pez, M., Castillo, L., and Lo�pez, M. Intrusion correlation using ontologies and multi-agent systems. In Information Security and Assurance. Springer, 2010, pp. 51�63.
120. Iwaihara, M., Murakami, K., Ahn, G.-J., and Yoshikawa, M. Risk evaluation for personal identity management based on privacy attribute ontology. In Conceptual Modeling-ER 2008. Springer, 2008, pp. 183�198.
121. Jansen, W., Grance, T., et al. Guidelines on security and privacy in public cloud computing. NIST special publication 800 (2011), 144.
122. Juan-Verdejo, A., and Baars, H. Decision support for partially moving applications to the cloud: the example of business intelligence. In Proceedings of the 2013 international workshop on Hot topics in cloud services (2013), ACM, pp. 35�42.
123. Ju�rjens, J. Umlsec: Extending UML for secure systems development. In UML The Unified Modeling Language. Springer, 2002, pp. 412�425.
124. Kabilan, V., Johannesson, P., Ruohomaa, S., Moen, P., Herrmann, A., �Ahlfeldt, R.-M., and Weigand, H. Introducing the common non-functional ontology. In Enterprise Interoperability II. Springer, 2007, pp. 633�645.
125. Kabir, M. A., Han, J., Yu, J., and Colman, A. User-centric social context information management: an ontology-based approach and platform. Personal and Ubiquitous Computing 18, 5 (2014), 1061�1083.
126. Kagal, L., Finin, T., Joshi, A., and Greenspan, S. Security and privacy challenges in open and dynamic environments. Computer 39, 6 (2006), 89�91.
127. Kagal, L., Finin, T., Paolucci, M., Srinivasan, N., Sycara, K., and Denker, G. Authorization and privacy for semantic web services. Intelligent Systems, IEEE 19, 4 (2004), 50�56.
128. Kaiya, H., and Saeki, M. Using domain ontology as domain knowledge for requirements elicitation. In Requirements Engineering, 14th IEEE International Conference (2006), IEEE, pp. 189�198.
129. Kalloniatis, C., Kavakli, E., and Gritzalis, S. Dealing with privacy issues during the system design process. In Signal Processing and Information Technology, 2005. Proceedings of the Fifth IEEE International Symposium on (2005), IEEE, pp. 546�551.
130. Kalloniatis, C., Kavakli, E., and Gritzalis, S. Addressing privacy requirements in system design: the PriS method. Requirements Engineering 13, 3 (2008), 241�255.
131. Kanbe, M., and Yamamoto, S. Ontology alignment in rfid privacy protection. In Complex, Intelligent and Software Intensive Systems, 2009. CISIS'09. International Conference on (2009), IEEE, pp. 718�723.
132. Kang, W., and Liang, Y. A security ontology with mda for software development. In Cyber-Enabled Distributed Computing and Knowledge Discovery (CyberC), 2013 International Conference on (2013), IEEE, pp. 67�74.
133. Karyda, M., Balopoulos, T., Dritsas, S., Gymnopoulos, L., Kokolakis, S., Lambrinoudakis, C., and Gritzalis, S. An ontology for secure egovernment applications. In Availability, Reliability and Security, 2006. ARES 2006. The First International Conference on (2006), IEEE, pp. 5�pp.
134. Kayes, A., Han, J., and Colman, A. An ontology-based approach to context-aware access control for software services. In Web Information Systems Engineering�WISE 2013. Springer, 2013, pp. 410�420.
135. Kayes, A., Han, J., and Colman, A. A semantic policy framework for contextaware access control applications. In 12th International Conference on Trust,

Security and Privacy in Computing and Communications (TrustCom) (2013), IEEE, pp. 753�762. 136. Keele University. Guidelines for performing systematic literature reviews in software engineering. Tech. rep., Keele University, 2007. 137. Khan, K. M., Erradi, A., Alhazbi, S., and Han, J. Security oriented service composition: A framework. In Innovations in Information Technology (IIT), 2012 International Conference on (2012), IEEE, pp. 48�53. 138. Kim, A., Luo, J., and Kang, M. Security ontology for annotating resources. In OTM Confederated International Conferences" On the Move to Meaningful Internet Systems" (2005), Springer, pp. 1483�1499. 139. Kitchenham, B. Procedures for performing systematic reviews. Keele, UK, Keele University 33, 2004 (2004), 1�26. 140. Koinig, U., Tjoa, S., and Ryoo, J. Contrology-an ontology-based cloud assurance approach. In 4th International Conference on Enabling Technologies: Infrastructure for Collaborative Enterprises (WETICE) (2015), IEEE, pp. 105� 107. 141. Kost, M., and Freytag, J. C. Privacy analysis using ontologies. In Proceedings
of the second ACM conference on Data and Application Security and Privacy (2012), ACM, pp. 205�216. 142. Kost, M., Freytag, J.-C., Kargl, F., and Kung, A. Privacy verification using ontologies. In Availability, Reliability and Security (ARES), 2011 Sixth International Conference on (2011), IEEE, pp. 627�632. 143. Kumari, P., and Pretschner, A. Deriving implementation-level policies for usage control enforcement. In Proceedings of the second ACM conference on Data and Application Security and Privacy (2012), ACM, pp. 83�94. 144. Labda, W., Mehandjiev, N., and Sampaio, P. Modeling of privacy-aware business processes in bpmn to protect personal data. In Proceedings of the 29th Annual ACM Symposium on Applied Computing (2014), ACM, pp. 1399�1405. 145. Lammari, N., Bucumi, J.-S., Akoka, J., and Comyn-Wattiau, I. A conceptual meta-model for secured information systems. In Proceedings of the 7th International Workshop on Software Engineering for Secure Systems (2011), ACM, pp. 22�28. 146. Langheinrich, M. Privacy by designprinciples of privacy-aware ubiquitous systems. In Ubicomp 2001: Ubiquitous Computing (2001), Springer, pp. 273�291. 147. Lee, C.-Y., Kavi, K. M., Paul, R. A., and Gomathisankaran, M. Ontology of secure service level agreement. In High Assurance Systems Engineering (HASE), 2015 IEEE 16th International Symposium on (2015), IEEE, pp. 166� 172. 148. Lee, S.-W., Gandhi, R., Muthurajan, D., Yavagal, D., and Ahn, G.-J. Building problem domain ontology from security requirements in regulatory documents. In Proceedings of the 2006 international workshop on Software engineering for secure systems (2006), ACM, pp. 43�50. 149. Li, M., Lou, W., and Ren, K. Data security and privacy in wireless body area networks. Wireless Communications, IEEE 17, 1 (2010), 51�58. 150. Li, Y. Empirical studies on online information privacy concerns: literature review and an integrative framework. Communications of the Association for Information Systems 28, 1 (2011), 453�496. 151. Liccardo, L., Rak, M., Di Modica, G., and Tomarchio, O. Ontologybased negotiation of security requirements in cloud. In Computational Aspects of Social Networks (CASoN), 2012 Fourth International Conference on (2012), IEEE, pp. 192�197.

152. Lin, L., Nuseibeh, B., Ince, D., Jackson, M., and Moffett, J. Introducing abuse frames for analysing security requirements. In 11th Requirements Engineering International Conference (2003), IEEE, pp. 371�372.
153. Lioudakis, G. V., Koutsoloukas, E. A., Dellas, N., Kapellaki, S., Prezerakos, G. N., Kaklamani, D. I., and Venieris, I. S. A proxy for privacy: the discreet box. In The International Conference on Computer as a Tool, EUROCON (2007), IEEE, pp. 966�973.
154. Liu, C.-L. Ontology-based requirements conflicts analysis in activity diagrams. In Computational Science and Its Applications�ICCSA 2009. Springer, 2009, pp. 1� 12.
155. Liu, L., Yu, E., and Mylopoulos, J. Security and privacy requirements analysis within a social setting. In 11th International Requirements Engineering Conference (2003), IEEE, pp. 151�161.
156. Loucopoulos, P., and Kavakli, V. Enterprise knowledge management and conceptual modelling. In Conceptual Modeling. Springer, 1999, pp. 123�143.
157. Mace, J. C., Parkin, S., and van Moorsel, A. A collaborative ontology development tool for information security managers. In Proceedings of the 4th Symposium on Computer Human Interaction for the Management of Information Technology (2010), ACM, p. 5.
158. MacKenzie, S. B. The dangers of poor construct conceptualization. Journal of the Academy of Marketing Science 31, 3 (2003), 323�326.
159. MAGERIT, P. Methodology for information systems risk analysis and management, 2006.
160. Maisonnasse, J., Gourier, N., Brdiczka, O., Reignier, P., and Crowley, J. L. Detecting privacy in attention aware system. In Intelligent Environments, 2006. IE 06. 2nd IET International Conference on (2006), vol. 2, IET, pp. 231� 239.
161. Man, J., Yang, A., and Sun, X. Retracted: shared ontology for pervasive computing. In Advances in Computer Science�ASIAN 2005. Data Management on the Web. Springer, 2005, pp. 64�78.
162. Massacci, F., Mylopoulos, J., Paci, F., Tun, T. T., and Yu, Y. An extended ontology for security requirements. In Advanced Information Systems Engineering Workshops (2011), Springer, pp. 622�636.
163. Massacci, F., Mylopoulos, J., and Zannone, N. Computer-aided support for secure tropos. Automated Software Engineering 14, 3 (2007), 341�364.
164. Massacci, F., Mylopoulos, J., and Zannone, N. An ontology for secure socio-technical systems. Handbook of ontologies for business interaction 1 (2007), 469.
165. Massacci, F., Prest, M., and Zannone, N. Using a security requirements engineering methodology in practice: the compliance with the italian data protection legislation. Computer Standards & Interfaces 27, 5 (2005), 445�455.
166. Massacci, F., and Zannone, N. Detecting conflicts between functional and security requirements with secure tropos: John rusnak and the allied irish bank. Social Modeling for Requirements Engineering. MIT Press, Cambridge (2008).
167. Matulevicius, R., Mayer, N., Mouratidis, H., Dubois, E., Heymans, P., and Genon, N. Adapting Secure Tropos for security risk management in the early phases of information systems development. In Advanced Information Systems Engineering (2008), Springer, pp. 541�555.
168. Maxwell, J. C., and Anto�n, A. I. The production rule framework: developing a canonical set of software requirements for compliance with law. In proceedings of

the 1st ACM International Health Informatics Symposium (2010), ACM, pp. 629� 636. 169. Mayer, N. Model-based management of information system security risk. PhD thesis, University of Namur, 2009. 170. Mayer, N., Rifaut, A., Dubois, E., et al. Towards a risk-based security requirements engineering framework. In Workshop on Requirements Engineering for Software Quality. In Proc. of REFSQ (2005), vol. 5. 171. McGrath, R. E., Ranganathan, A., Campbell, R. H., and Mickunas, M. D. Use of ontologies in pervasive computing environments. Report number: UIUCDCS (2003). 172. Mellado, D., Blanco, C., Sa�nchez, L. E., and Ferna�ndez-Medina, E. A systematic review of security requirements engineering. Computer Standards & Interfaces 32, 4 (2010), 153�165. 173. Mezga�r, I., and Kincses, Z. Development of an ontology-based smart card system reference architecture. In Ontologies. Springer, 2007, pp. 841�863. 174. Milicevic, D., and Goeken, M. Ontology-based evaluation of iso 27001. In I3E (2010), Springer, pp. 93�102. 175. Mitra, P., Liu, P., and Pan, C.-C. Privacy-preserving ontology matching. In AAAI Workshop on Context and Ontologies (2005). 176. Mitra, P., Pan, C.-C., Liu, P., and Atluri, V. Privacy-preserving semantic interoperation and access control of heterogeneous databases. In Proceedings of the 2006 ACM Symposium on Information, computer and communications security (2006), ACM, pp. 66�77. 177. Mitre, H. A., Gonza�lez-Tablas, A. I., Ramos, B., and Ribagorda, A. A legal ontology to support privacy preservation in location-based services. In On the Move to Meaningful Internet Systems: OTM Workshops (2006), Springer, pp. 1755�1764. 178. Modica, G. D., and Tomarchio, O. Semantic annotations for security policy matching in ws-policy. In Security and Cryptography (SECRYPT), 2011 Proceedings of the International Conference on (2011), IEEE, pp. 443�449. 179. Mouratidis, H., and Giorgini, P. Secure Tropos: A security-oriented extension of the Tropos methodology. Journal of Software Engineering and Knowledge Engineering 17, 2 (2007), 285�309. 180. Mouratidis, H., Giorgini, P., and Manson, G. An ontology for modelling security: The tropos approach. In Knowledge-Based Intelligent Information and Engineering Systems (2003), Springer, pp. 1387�1394. 181. Mun~oz, J. C., Tamura, G., Villegas, N. M., and Mu�ller, H. A. Surprise: user-controlled granular privacy and security for personal data in smartercontext. In Proceedings of the 2012 Conference of the Center for Advanced Studies on Collaborative Research (2012), IBM Corp., pp. 131�145. 182. Nissan, E. Accounting for social, spatial, and textual interconnections. In Computer Applications for Handling Legal Evidence, Police Investigation and Case Argumentation. Springer, 2012, pp. 483�765. 183. Ohkubo, M., Suzuki, K., Kinoshita, S., et al. Cryptographic approach to privacy-friendly tags. In RFID privacy workshop (2003), vol. 82, Cambridge, USA. 184. Oladimeji, E. A., Chung, L., Jung, H. T., and Kim, J. Managing security and privacy in ubiquitous ehealth information interchange. In Proceedings of the 5th International Conference on Ubiquitous Information Management and Communication (2011), ACM, p. 26.

185. Olivier, M. S. Database privacy: balancing confidentiality, integrity and availability. ACM SIGKDD Explorations Newsletter 4, 2 (2002), 20�27.
186. Paja, E., Dalpiaz, F., and Giorgini, P. STS-tool: Security requirements engineering for socio-technical systems. In Engineering Secure Future Internet Services and Systems. Springer, 2014, pp. 65�96.
187. Panetto, H., Dillon, T., Eder, J., Bellahsene, Z., Ritter, N., and De Leenheer, P. Efficient projection of ontologies.
188. Papagiannakopoulou, E. I., Koukovini, M. N., Lioudakis, G. V., Dellas, N., Garcia-Alfaro, J., Kaklamani, D. I., Venieris, I. S., CuppensBoulahia, N., and Cuppens, F. Leveraging ontologies upon a holistic privacyaware access control model. In Foundations and Practice of Security. Springer, 2014, pp. 209�226.
189. Parkin, S. E., van Moorsel, A., and Coles, R. An information security ontology incorporating human-behavioural implications. In Proceedings of the 2nd International Conference on Security of Information and Networks (2009), ACM, pp. 46�55.
190. Pereira, T., and Santos, H. An ontology based approach to information security. In Metadata and Semantic Research. Springer, 2009, pp. 183�192.
191. Perrig, A., Szewczyk, R., Tygar, J. D., Wen, V., and Culler, D. E. Spins: Security protocols for sensor networks. Wireless networks 8, 5 (2002), 521�534.
192. Poritz, J., Schunter, M., Van Herreweghen, E., and Waidner, M. Property attestationscalable and privacy-friendly security assessment of peer computers.
193. Rahmouni, H. B., Solomonides, T., Mont, M. C., and Shiu, S. Privacy compliance in european healthgrid domains: An ontology-based approach. In Computer-Based Medical Systems, 2009. CBMS 2009. 22nd IEEE International Symposium on (2009), IEEE, pp. 1�8.
194. Rajugan, R., Chang, E., and Dillon, T. S. Ontology views: a theoretical perspective. In On the Move to Meaningful Internet Systems 2006: OTM 2006 Workshops (2006), Springer, pp. 1814�1824.
195. Ranganathan, A., McGrath, R. E., Campbell, R. H., and Mickunas, M. D. Ontologies in a pervasive computing environment. In Workshop on Ontologies in Distributed Systems at IJCAI, Acapulco, Mexico (2003), Citeseer.
196. Raskin, V., Hempelmann, C. F., Triezenberg, K. E., and Nirenburg, S. Ontology in information security: a useful theoretical foundation and methodological tool. In Proceedings of the 2001 workshop on New security paradigms (2001), ACM, pp. 53�59.
197. Rezgui, A., Ouzzani, M., Bouguettaya, A., and Medjahed, B. Preserving privacy in web services. In Proceedings of the 4th international workshop on Web information and data management (2002), ACM, pp. 56�62.
198. Rodr�iguez, N. D., Cue�llar, M. P., Lilius, J., and Calvo-Flores, M. D. A survey on ontologies for human behavior recognition. ACM Computing Surveys (CSUR) 46, 4 (2014), 43.
199. R�stad, L. An extended misuse case notation: Including vulnerabilities and the insider threat. In International Working Conference on Requirements Engineering: Foundation for Software Quality (2006), Springer, pp. 33�34.
200. Runeson, P., and Ho�st, M. Guidelines for conducting and reporting case study research in software engineering. Empirical software engineering 14, 2 (2009), 131�164.

201. Ryan, H., Spyns, P., De Leenheer, P., and Leary, R. Ontology-based platform for trusted regulatory compliance services. In On The Move to Meaningful Internet Systems Workshops OTM (2003), Springer, pp. 675�689.
202. Sacco, O., and Passant, A. A privacy preference ontology (ppo) for linked data. In LDOW (2011), Citeseer.
203. Sandhu, R. S., Coynek, E. J., Feinsteink, H. L., and Youmank, C. E. Role-based access control models yz. IEEE computer 29, 2 (1996), 38�47.
204. Sardis, E., Gogouvitis, S. V., Bouras, T., Gouvas, P., and Varvarigou, T. Secure enterprise interoperability ontology for semantic integration of business to business applications. In P2P, Parallel, Grid, Cloud and Internet Computing (3PGCIC), 2013 Eighth International Conference on (2013), IEEE, pp. 68�75.
205. Saripalle, R. K., De La Rosa Algarin, A., and Ziminski, T. B. Towards knowledge level privacy and security using rdf/rdfs and rbac. In Semantic Computing (ICSC), 2015 IEEE International Conference on (2015), IEEE, pp. 264� 267.
206. Schaefer, R. The epistemology of computer security. ACM SIGSOFT Software Engineering Notes 34, 6 (2009), 8�10.
207. Sicilia, M.-A., Garc�ia-Barriocanal, E., Bermejo-Higuera, J., and Sa�nchez-Alonso, S. What are information security ontologies useful for? In Metadata and Semantics Research. Springer, 2015, pp. 51�61.
208. Sindre, G., and Opdahl, A. L. Eliciting security requirements with misuse cases. Requirements engineering 10, 1 (2005), 34�44.
209. Singh, V., and Pandey, S. A comparative study of cloud security ontologies. In Reliability, Infocom Technologies and Optimization (ICRITO)(Trends and Future Directions), 2014 3rd International Conference on (2014), IEEE, pp. 1�6.
210. Singh, V., and Pandey, S. Revisiting security ontologies. IETE Technical Review Journal, Taylor & Francis Online, submitted (2014).
211. Singhal, A., and Wijesekera, D. Ontologies for modeling enterprise level security metrics. In Proceedings of the Sixth Annual Workshop on Cyber Security and Information Intelligence Research (2010), ACM, p. 58.
212. Skinner, G., Han, S., and Chang, E. An information privacy taxonomy for collaborative environments. Information management & computer security 14, 4 (2006), 382�394.
213. Solove, D. J. Conceptualizing privacy. California Law Review (2002), 1087� 1155.
214. Solove, D. J. A taxonomy of privacy. University of Pennsylvania law review (2006), 477�564.
215. Sommerville, I., Cliff, D., Calinescu, R., Keen, J., Kelly, T., Kwiatkowska, M., Mcdermid, J., and Paige, R. Large-scale complex IT systems. Communications of the ACM 55, 7 (2012), 71�77.
216. Sorli, M., and Stokic, D. Ict tools and systems supporting innovation in product/process development. Innovating in Product/Process Development: Gaining Pace in New Product Development (2009), 113�152.
217. Souag, A. Towards a new generation of security requirements definition methodology using ontologies. In 24th International Conference on Advanced Information Systems Engineering (CAiSE'12) (2012), pp. 1�8.
218. Souag, A., Mazo, R., Salinesi, C., and Comyn-Wattiau, I. Reusable knowledge in security requirements engineering: a systematic mapping study. Requirements Engineering (2015), 1�33.

219. Souag, A., Salinesi, C., and Comyn-Wattiau, I. Ontologies for security requirements: A literature survey and classification. In Advanced Information Systems Engineering Workshops (2012), Springer, pp. 61�69.
220. Souag, A., Salinesi, C., Mazo, R., and Comyn-Wattiau, I. A security ontology for security requirements elicitation. In Engineering Secure Software and Systems. Springer, 2015, pp. 157�177.
221. Souag, A., Salinesi, C., Wattiau, I., and Mouratidis, H. Using security and domain ontologies for security requirements analysis. In Computer Software and Applications Conference Workshops (COMPSACW), 2013 IEEE 37th Annual (2013), IEEE, pp. 101�107.
222. Spyns, P. Evaluating automatically a text miner for ontologies: a catch-22 situation? In On the Move to Meaningful Internet Systems: OTM 2008. Springer, 2008, pp. 1404�1422.
223. Squicciarini, A. C., Bertino, E., Ferrari, E., and Ray, I. Achieving privacy in trust negotiations with an ontology-based approach. Dependable and Secure Computing, IEEE Transactions on 3, 1 (2006), 13�30.
224. Srinivasan, A., Wu, J., and Zhu, W. Safe: Secure and big data-adaptive framework for efficient cross-domain communication. In Proceedings of the First International Workshop on Privacy and Secuirty of Big Data (2014), ACM, pp. 19�28.
225. Stoica, A., and Farkas, C. Ontology guided xml security engine. Journal of Intelligent Information Systems 23, 3 (2004), 209�223.
226. Studer, T. Privacy preserving modules for ontologies. In Perspectives of Systems Informatics. Springer, 2009, pp. 380�387.
227. Sullivan, K., Clarke, J., and Mulcahy, B. P. Trust-terms ontology for defining security requirements and metrics. In Proceedings of the Fourth European Conference on Software Architecture: Companion Volume (2010), ACM, pp. 175� 180.
228. Sure, Y., and Haller, J. Towards cross-domain security properties supported by ontologies. In Web Information Systems (WISE) Workshops (2004), Springer, pp. 58�69.
229. Takabi, H., Joshi, J. B., and Ahn, G.-J. Security and privacy challenges in cloud computing environments. IEEE Security & Privacy, 6 (2010), 24�31.
230. Tan, V., Groth, P., Miles, S., Jiang, S., Munroe, S., Tsasakou, S., and Moreau, L. Security issues in a soa-based provenance system. In Provenance and Annotation of Data. Springer, 2006, pp. 203�211.
231. Torrellas, G. A. S. A framework for multi-agent system engineering using ontology domain modelling for security architecture risk assessment in e-commerce security services. In 3rd IEEE International Symposium on Network Computing and Applications(NCA) (2004), IEEE, pp. 409�412.
232. Torres-Urquidy, M. H., Powell, V. J., Din, F. M., Diehl, M., BertaudGounot, V., Klein, W. T., Mishra, S., Geist, S.-M. R. Y., Chaudhari, M., and Allen, M. Hit considerations: Informatics and technology needs and considerations. In Integration of Medical and Dental Care and Patient Data. Springer, 2012, pp. 25�137.
233. Trochim, W., and Donnelly, J. The Research Methods Knowledge Base. Cengage Learning, 2006.
234. Tropea, G., Lioudakis, G. V., Blefari-Melazzi, N., Kaklamani, D. I., and Venieris, I. S. Introducing privacy awareness in network monitoring ontologies. In Trustworthy Internet. Springer, 2011, pp. 317�331.

235. Tsoumas, B., and Gritzalis, D. Towards an ontology-based security management. In 20th International Conference on Advanced Information Networking and Applications (AINA) (2006), vol. 1, IEEE, pp. 985�992.
236. Tsoumas, B., Papagiannakopoulos, P., Dritsas, S., and Gritzalis, D. Security-by-ontology: A knowledge-centric approach. In Security and Privacy in Dynamic Environments. Springer, 2006, pp. 99�110.
237. Undercoffer, J., Joshi, A., and Pinkston, J. Modeling computer attacks: An ontology for intrusion detection. In Recent Advances in Intrusion Detection (2003), Springer, pp. 113�135.
238. Uschold, M., and Gruninger, M. Ontologies: Principles, methods and applications. The knowledge engineering review 11, 02 (1996), 93�136.
239. Van Blarkom, G., Borking, J., and Olk, J. Handbook of privacy and privacyenhancing technologies. Privacy Incorporated Software Agent (PISA) Consortium, The Hague (2003).
240. Van Lamsweerde, A. Elaborating security requirements by construction of intentional anti-models. In Proceedings of the 26th International Conference on Software Engineering (2004), IEEE Computer Society, pp. 148�157.
241. Velasco, J. L., Valencia-Garc�ia, R., Ferna�ndez-Breis, J. T., Toval, A., et al. Modelling reusable security requirements based on an ontology framework. Journal of Research and Practice in Information Technology 41, 2 (2009), 119.
242. Vincent, J., Porquet, C., Borsali, M., and Leboulanger, H. Privacy protection for smartphones: an ontology-based firewall. In Information Security Theory and Practice. Security and Privacy of Mobile Devices in Wireless Communication. Springer, 2011, pp. 371�380.
243. Vorobiev, A., and Bekmamedova, N. An ontological approach applied to information security and trust. ACIS 2007 Proceedings (2007), 114.
244. Vorobiev, A., and Han, J. Security attack ontology for web services. In Semantics, Knowledge and Grid, 2006. SKG'06. Second International Conference on (2006), IEEE, pp. 42�42.
245. Vorobiev, A., and Han, J. Specifying dynamic security properties of web service based systems. In Semantics, Knowledge and Grid, 2006. SKG'06. Second International Conference on (2006), IEEE, pp. 34�34.
246. Vorobiev, A., Han, J., and Bekmamedova, N. An ontology framework for managing security attacks and defences in component based software systems. In Software Engineering, 2008. ASWEC 2008. 19th Australian Conference on (2008), IEEE, pp. 552�561.
247. Vorobiev, V. I., Fedorchenko, L. N., Zabolotsky, V. P., and Lyubimov, A. V. Ontology-based analysis of information security standards and capabilities for their harmonization. In Proceedings of the 3rd international conference on Security of information and networks (2010), ACM, pp. 137�141.
248. Wang, J. A., and Guo, M. OVM: an ontology for vulnerability management. In Proceedings of the 5th Annual Workshop on Cyber Security and Information Intelligence Research (2009), ACM, p. 34.
249. Wang, J. A., Guo, M., Wang, H., Xia, M., and Zhou, L. Environmental metrics for software security based on a vulnerability ontology. In Secure Software Integration and Reliability Improvement, 2009. SSIRI 2009. Third IEEE International Conference on (2009), IEEE, pp. 159�168.
250. Wang, P., Chao, K.-M., Lo, C.-C., and Wang, Y.-S. Using ontologies to perform threat analysis and develop defensive strategies for mobile security. Information Technology and Management, 1�25.

251. Ware, W. H. A taxonomy for privacy. Tech. rep., DTIC Document, 1981. 252. Weber, R. H. Internet of things - new security and privacy challenges. Computer
Law & Security Review 26, 1 (2010), 23�30. 253. Weber-Jahnke, J. H., and Onabajo, A. Mining and analysing security goal
models in health information systems. In Software Engineering in Health Care, 2009. SEHC'09. ICSE Workshop on (2009), IEEE, pp. 42�52. 254. Wei, C., Chen, G., and Ge, Q. Research on semantic-based security services model of soa. In E-Business and Information System Security, 2009. EBISS'09. International Conference on (2009), IEEE, pp. 1�4. 255. Wei, W., and Yu, T. The design and enforcement of a rule-based constraint policy language for service composition. In Social Computing (SocialCom), 2010 IEEE Second International Conference on (2010), IEEE, pp. 873�880. 256. Weippl, E. R., Schatten, A., Karim, S., and Tjoa, A. M. SemanticLIFE Collaboration: Security Requirements and solutions�security aspects of semantic knowledge management. Springer, 2004. 257. Yan, P., Zhao, Y., and Sanxing, C. Ontology-based information content security analysis. In Fuzzy Systems and Knowledge Discovery, 2008. FSKD'08. Fifth International Conference on (2008), vol. 5, IEEE, pp. 479�483. 258. Yau, S. S., and Chen, Z. A framework for specifying and managing security requirements in collaborative systems. In Autonomic and Trusted Computing. Springer, 2006, pp. 500�510. 259. Yau, S. S., and Liu, J. Hierarchical situation modeling and reasoning for pervasive computing. In Software Technologies for Future Embedded and Ubiquitous Systems, 2006 and the 2006 Second International Workshop on Collaborative Computing, Integration, and Assurance. SEUS 2006/WCCIA 2006. The Fourth IEEE Workshop on (2006), IEEE, pp. 6�pp. 260. Yau, S. S., Yao, Y., Chen, Z., and Zhu, L. An adaptable security framework for service-based systems. In 10th International Workshop on Object-Oriented Real-Time Dependable Systems (WORDS) (2005), IEEE, pp. 28�35. 261. Yu, E., and Cysneiros, L. Designing for privacy and other competing requirements. In 2nd Symposium on Requirements Engineering for Information Security (SREIS02), Raleigh, North Carolina (2002), Citeseer, pp. 15�16. 262. Yu, Y., Kaiya, H., Washizaki, H., Xiong, Y., Hu, Z., and Yoshioka, N. Enforcing a security pattern in stakeholder goal models. In Proceedings of the 4th ACM Workshop on Quality of Protection (2008), ACM, pp. 9�14. 263. Zannone, N. A requirements engineering methodology for trust, security, and privacy. PhD thesis, University of Trento, 2006. 264. Zhang, N., and Todd, C. Developing a privacy ontology for privacy control in context-aware systems. Tech. rep., 2006.

Appendix A: Quality assessment application

Table 7: Quality assessment (selection stage 2) application

N

ID

1 ACM 02 [40]

3 ACM 04 [197]

5 ACM 06 [92]

7 ACM 08 [184]

9 ACM 11 [253]

11 ACM 14 [144]

13 ACM 17 [53]

15 ACM 19 [168]

17 ACM 23 [176]

19 ACM 26 [157]

21 ACM 30 [258]

23 ACM 34 [80]

25 ACM 36 [22]

27 ACM 40 [248]

29 IEEE 09 [193]

31 IEEE 12 [221]

33 IEEE 14 [259]

35 IEEE 18 [223]

37 IEEE 21 [249]

39 IEEE 26 [4]

41 IEEE 30 [160]

43 IEEE 35 [39]

45 IEEE 38 [147]

47 IEEE 42 [82]

49 IEEE 49 [21]

51 IEEE 51 [110]

53 IEEE 54 [25]

55 IEEE 57 [132]

57 IEEE 59 [257]

59 CIT 01 [192]

61 CIT 09 [30]

63 CIT 13 [217]

65 CIT 18 [164]

67 CIT 26 [146]

69 CIT 31 [195]

71 Spgr 01 [138]

73 Spgr 03 [219]

75 Spgr 08 [220]

77 Spgr 14 [236]

79 Spgr 19 [61]

81 Spgr 22 [91]

83 Spgr 31 [42]

85 Spgr 34 [177]

87 Spgr 36 [190]

Q1 Q2 Q3 Q4 Q5 S. N

ID

- - - 1 1 2 2 ACM 03 [240]

- - - 1 1 2 4 ACM 05 [141]

1 - - - 1 2 6 ACM 07 [113]

1 - - - 1 2 8 ACM 10 [224]

- - - - 1 1 10 ACM 13 [181]

1 1 1 1 - 4 12 ACM 16 [28]

1 - - - - 1 14 ACM 18 [262]

1 - - - - 1 16 ACM 22 [226]

1 - - 1 1 3 18 ACM 24 [227]

1 - - - - 1 20 ACM 28 [206]

1 1 - 1 - 3 22 ACM 32 [5]

- - - - - - 24 ACM 35 [211]

- - 1 - - 1 26 ACM 37 [54]

1 1 1 - 1 4 28 IEEE 03 [142]

1 - - 1 - 2 30 IEEE 11 [151]

1 1 1 1 1 5 32 IEEE 13 [56]

1 - - - 1 2 34 IEEE 15 [235]

1 1 - 1 - 3 36 IEEE 19 [86]

1 - 1 1 - 3 38 IEEE 25 [44]

- - - - - 0 40 IEEE 28 [52]

1 - - 1 - 2 42 IEEE 33 [95]

1 1 - 1 - 3 44 IEEE 36 [209]

1 - - 1 - 2 46 IEEE 41 [96]

1 - - 1 1 3 48 IEEE 48 [50]

1 - - - 1 2 50 IEEE 50 [100]

1 1 1 - - 3 52 IEEE 52 [105]

1 - - 1 1 3 54 IEEE 56 [231]

1 1 1 1 - 4 56 IEEE 58 [244]

1 - - 1 - 2 58 IEEE 60 [68]

1 - - 1 1 3 60 CIT 07 [241]

1 - - 1 1 3 62 CIT 12 [48]

- - - - - - 64 CIT 15 [67]

1 1 1 1 1 5 66 CIT 23 [264]

1 - - 1 1 3 68 CIT 29 [246]

1 - - - 1 2 70 CIT 33 [155]

1 - - - 1 2 72 Spgr 02 [78]

- - - - - - 74 Spgr 07 [162]

- - - - - - 76 Spgr 13 [71]

1 - - 1 - 2 78 Spgr 18 [174]

1 - - - - 1 80 Spgr 20 [242]

1 - - 1 - 2 82 Spgr 28 [112]

1 - - - 1 2 84 Spgr 32 [180]

1 - - - - 1 86 Spgr 35 [49]

1 - - - - 1 88 Spgr 38 [58]

Q1 Q2 Q3 Q4 Q5 S 1 1 1 1 15 1 1 - - -2 1 - - 1 13 1 - - - -1 1 - - 1 -2 1 1 1 1 -4 1 - - - -1 1 1 - 1 -3 - - - - -0 - - - - -0 1 1 - - -2 1 1 1 1 -4 - - - - -0 1 1 - - -2 1 - - - -1 - 1 - - -1 1 1 1 - 14 1 1 - - -2 1 - - 1 13 1 - - - -1 - - - - -0 1 - - - -1 1 - - - -1 1 - - 1 -3 1 1 1 1 15 1 - - - -1 1 - - 1 13 1 - - 1 13 1 1 - 1 14 1 1 1 1 15 1 - - 1 13 1 - - 1 -2 1 - - - -1 1 - - 1 -2 1 1 1 1 15 - - - - -1 1 1 1 -4 1 1 1 1 -4 1 - - - -1 - - - - -1 1 - - 1 -2 1 - - - 12 1 - - - -1 1 - - - -1

N

ID

Q1 Q2 Q3 Q4 Q5 S N

ID

Q1 Q2 Q3 Q4 Q5 S

89 Spgr 41 [120] 1 - - 1 - 2 90 Spgr 55 [69]

1 - - - -1

91 Spgr 56 [1]

1 - - - 1 2 92 Spgr 58 [51]

1 - - - -1

93 Spgr 60 [31]

1 - - 1 1 3 94 SCH 02 [41]

1 1 - - 13

95 SCH 03 [165] 1 1 1 1 1 5 96 SCH 06 [202] 1 - - - 1 2

97 SCH 16 [87]

1 - - 1 1 3 98 SCH 18 [208] 1 - 1 1 1 4

99 SCH 20 [10]

1 1 - - 1 3 100 SCH 24 [130] 1 1 1 1 1 5

101 SCH 26 [107] 1 - - 1 1 3 102 SCH 27 [108] 1 - - 1 1 3

103 SCH 28 [179] 1 1 1 1 1 5 104 SCH 32 [62]

- - - - -0

105 SCH 36 [7]

1 - - 1 - 2 106 SCH 41 [214] 1 1 1 1 1 5

107 SCH 43 [212] 1 - - 1 - 2 108 Spgr 18 01 [133] 1 - - 1 - 3

109 Spgr 18 02 [196] - - - - 1 1 110 Spgr 18 03 [81] 1 1 1 - 1 4

111 Spgr 13 01 [15] 1 1 1 1 1 5 112 Spgr 13 02 [59] 1 1 - 1 1 4

113 Spgr 13 03 [72] 1 1 1 1 1 5 114 Spgr 13 04 [123] 1 1 - 1 1 4

115 Spgr 13 05 [167] 1 1 1 1 1 5 116 Spgr 13 06 [170] 1 1 1 1 1 5

117 Spgr 13 07 [199] 1 - - 1 1 3 118 Spgr 13 08 [210] 1 1 - - 1 3

117 Spgr 13 07 [199] 1 - - 1 1 3 118 Spgr 13 08 [210] 1 1 - - 1 3

119 Spgr 08 01 [169] 1 1 1 1 1 5 120 Spgr 08 02 [241] 1 1 1 1 - 4

121 Spgr 08 03 [63] 1 1 1 1 - 4 122 Spgr 07 01 [24] - - - - - -

123 Spgr 07 02 [263] 1 1 1 1 - 4 124 Spgr 07 03 [152] 1 - - - 1 2

125 Spgr 03 01 [16] 1 1 - 1 1 4 126 Spgr 03 02 [88] 1 - - - 1 2

127 Spgr 02 01 [13] 1 1 - 1 1 4 128 Spgr 02 02 [14] 1 1 - 1 1 4

129 SCH 24 01 [129] 1 - - 1 - 2 130 SCH 24 02 [114] 1 1 1 1 1 5

131 SCH 28 01 [186] 1 1 1 1 - 4 132 SCH 43 01 [239] 1 1 1 1 - 4

Appendix B: Overview of all the considered studies

Table 8: Overview of all the considered studies

N

ID

Title

Author(s)

Pub # Decision

Year Cited

001 ACM 01 Database Privacy, Martin S Olivier 2002 30 Excluded

[185] Balancing Conden-

stage 1

tiality, Integrity

and Availability

002 ACM 02 Improving privacy Melissa Chase, 2009 375 Excluded

[40]

and security in

Sherman

stage 2

multi-authority

S.M. Chow

attribute-based

encryption

003 ACM 03 Elaborating Security

Axel van

2004 337 Selected

[240]

Requirements

Lamsweerde

by Construction

of Intentional

Anti-Models

004 ACM 04 Preserving Privacy Abdelmounaam 2002 102 Excluded

[197]

in Web Services Rezgui, Mourad

stage 2

Ouzzani, Athman

Bouguettaya,

Medjahed Brahim

005 ACM 05 Privacy analysis

Martin Kost, 2012 9 Excluded

[141]

using ontologies Johann Christoph

stage 2

Freytag

006 ACM 06

Discovering

Robin A. Gandhi, 2011 7 Excluded

[92]

Multidimensional Seok Won Lee

stage 2

Correlations

among Regulatory

Requirements to

Understand Risk

007 ACM 07

Event-based

Hinze Annika Kai 2009 110 Excluded

[113]

applications

Sachs, Alejandro

stage 2

and enabling

Buchmann

technologies

008 ACM 08 Managing security

Ebenezer A.

2011 12 Excluded

[184]

and privacy in

Oladimeji,

stage 2

ubiquitous eHealth Lawrence Chung,

information

Hyo Taeg Jung,

interchange

Kim Jaehyoun

009 ACM 09

Deriving

Prachi Ku-

2012 18 Excluded

[143] implementation-level mari, Alexander

stage 1

policies for usage

Pretschner

control enforcement

010 ACM 10

SAFE: Secure Avinash Srinivasan, 2014 1 Excluded

[224]

and Big Data- Wu Jie, Zhu Wen

stage 2

Adaptive Framework

for Efficient

Cross-Domain

Communication

011 ACM 11

Mining and

Jens H. Weber- 2009 6 Excluded

[253]

Analysing Secu-

Jahnke, On-

stage 2

rity Goal Models

abajo Adeniyi

in Health Infor-

mation Systems

012 ACM 12 Decision support

Adrian Juan- 2013 10 Excluded

[122]

for partially

Verdejo, Hen-

stage 2

moving applications

ning Baars

to the cloud:

the example of

business intelligence

013 ACM 13 Surprise: user-

Juan C. Mun~oz, 2012 5 Excluded

[181] controlled granular Tamura Gabriel,

stage 2

privacy and security Norha M. Ville-

for personal data gas, and Hausi

in Smarter Context

A. Mu�ller

014 ACM 14

Modeling of

Wadha JLabda, 2014 0 Selected

[144]

privacy-aware

Nikolay Mehand-

business processes jiev, Pedro Sampaio

in BPMN to protect

personal data

015 ACM 15 A conceptual meta- Nadira Lammari, 2011 2 Excluded

[145]

model for secured

Jean-Sylvain

stage 1

information systems Bucumi, Jacky

Akoka, Isabelle

Comyn-Wattiau

016 ACM 16 Introducing privacy Stefano Braghin, 2008 9 Selected

[28]

in a hospital

Alberto Coen-

information system Porisini, Pietro

Colombo, Sabrina

Sicari, Alberto

Trombetta

017 ACM 17 How to capture, Luca Compagna, 2007 29 Excluded

[53]

model, and verify Paul El Khoury,

stage 2

the knowledge

Fabio Massacci,

of legal, security, Thomas Reshma,

and privacy

Nicola Zannone

experts: a pattern-

based approach

018 ACM 18

Enforcing a

Yijun Yu, Kaiya

[262]

Security Pattern

Haruhiko,

in Stakeholder Washizaki Hironori,

Goal Models

Xiong Yingfei,

Hu Zhenjiang,

Yoshioka Nobukazu

019 ACM 19 The production Jeremy C. Maxwell,

[168]

rule framework:

Annie I. Ant�on

developing a canon-

ical set of software

requirements for

compliance with law

020 ACM 20 Security issues Victor Tan, Paul

[230]

in a SOA-Based

Groth, Simon

provenance system Miles, Sheng Jiang,

Steve Munroe,

Sofia Tsasakou,

Luc Moreau

021 ACM 21 [8] A scheme for

Toshiyuki Ama-

privacy-preserving gasa,Fan Zhang,

ontology mapping

Jun Sakuma,

Hiroyuki Kitagawa

022 ACM 22

Privacy pre-

Thomas Studer

[226]

serving modules

for ontologies

023 ACM 23 Privacy-preserving Prasenjit Mitra,

[176]

semantic interop- Chi-Chun Pan,

eration and access Peng Liu, and Vi-

control of hetero- jayalakshmi Atluri

geneous databases

024 ACM 24 Trust-terms ontology Kieran Sullivan,

[227] for defining security Jim Clarke,

requirements

Barry P. Mulcahy

and metrics

025 ACM 25 User-centric social

Muhammad

[125] context information Ashad Kabir,

management:

Jun Han, Jian

an ontology-

Yu, Alan Colman

based approach

and platform

026 ACM 26 A collaborative on- John C. Mace,

[157] tology development Simon Parkin,

tool for information Aad van Moorsel

security managers

027 ACM 27 Privacy-Preserving Jie Bao, Giora

[18]

Reasoning on the

Slutzki, Vas-

Semantic Web

ant Honavar

2008
2010
2006
2014 2010 2006 2010 2014
2010 2007

17 Excluded stage 2
15 Excluded stage 2
73 Excluded stage 1
0 Excluded stage 1
4 Excluded stage 2
35 Excluded stage 2
3 Excluded stage 2
9 Excluded stage 1
6 Excluded stage 2
37 Duplicated

028 ACM 28 The Epistemology of Robert Schaefer 2009 6 Excluded

[206] Computer Security

stage 2

029 ACM 29

A Survey on Rodr�iguez, Natalia 2014 17 Excluded

[198]

Ontologies for D�iaz and Cu�ellar,

stage 1

Human Behavior Manuel P Lilius,

Recognition Johan Calvo-Flores,

Miguel Delgado

030 ACM 30 A framework for Stephen S. Yau, 2006 17 Excluded

[258]

specifying and

Chen Zhaoji

stage 2

managing security

requirements in col-

laborative systems

031 ACM 31 Isn't the Time Ripe

Atilla Elc�i

2014 3 Excluded

[74]

for a Standard

stage 1

Ontology on Secu-

rity of Information

and Networks?

032 ACM 32 [5] Model driven se- Muhammad Alam 2007 14 Excluded

curity engineering

stage 1

for the realization

of dynamic security

requirements in col-

laborative systems

033 ACM 33

CoreSec: an

Ryan Ribeiro 2008 1 Excluded

[57] ontology of security de Azevedo,

stage 1

applied to the

Fred Freitas,

business process Silas Cardoso de

of management Almeida, Marcelo

Jos SC Almeida,

Edson C. de Barros

C Filho, Wendell

Campos Veras

034 ACM 34 Ontology-based

Stefan Fenz

2010 21 Excluded

[80]

generation of

stage 2

IT-security metrics

035 ACM 35

Ontologies for Singhal Anoop, Wi- 2010 7 Selected

[211]

Modeling En- jesekera Duminda

terprise Level

Security Metrics

036 ACM 36 A Security Ontology Clive Blackwell 2007 7 Excluded

[22] for Incident Analysis

stage 2

037 ACM 37 Dealing with the Da Silva, G. M. 2007 3 Excluded

[54]

formal analysis

H., Rademaker,

stage 2

of Information

A., Vasconcelos,

Security policies

D. R., Amaral,

through ontologies: F. N., Baz�ilio,

a case study

C., Costa, V. G.,

Haeusler, E. H

038 ACM 38 Building problem Lee, Seok-Won, 2006 42 Excluded

[148]

domain ontology Robin Gandhi,

stage 1

from security Divya Muthurajan,

requirements in reg- Yavagal Deepak.

ulatory documents Ahn Gail-Joon

039 ACM 39 Ontology-based Vladimir I Voro- 2010 2 Excluded

[247]

analysis of infor-

biev, Ludmila

stage 1

mation security

Fedorchenko,

standards and Vadim P Zabolot-

capabilities for

sky, Alexander

their harmonization V Lyubimov

040 ACM 40 OVM: an ontology Ju An Wang, 2009 40 Selected

[248]

for vulnerability

Guo Minzhe

management

041 IEEE 01 Authorization and Lalana Kagal, Tim 2004 242 Excluded

[127] privacy for semantic Finin, Massimo

stage 1

Web services

Paolucci, Naveen

Srinivasan, Katia

Sycara, Grit Denker

042 IEEE 02

Surveillance

Virginia Fernandez 2013 1 Excluded

[84]

ontology for

Arguedas, Ebroul

stage 1

legal, ethical and Izquierdo, Krishna

privacy protection Chandramouli

based on SKOS

043 IEEE 03 Privacy Verification Martin Kost, 2011 10 Excluded

[142]

Using Ontologies Johann-Christoph

stage 2

Freytag, Frank

Kargl, An-

tonio Kung

044 IEEE 04 A Semantic Policy ASM Kayes, Jun 2013 1 Excluded

[135]

Framework for Han, Alan Colman

stage 1

Context-Aware

Access Control

Applications

045 IEEE 05 A Proxy for Privacy: Georgios V. Li- 2007 9 Excluded

[153]

the Discreet Box oudakis, Eleftherios

stage 1

A. Koutsoloukas,

Nikolaos Dellas,

Sofia Kapellaki,

George N. Prez-

erakos, Dimitra

I. Kaklamani,

Iakovos S. Venieris

046 IEEE 06 Semantic annota-

Giuseppe Di

2011 1 Excluded

[178]

tions for security Modica, Orazio

stage 1

policy matching

Tomarchio

in WS-Policy

047 IEEE 07 Semantic Security

Giuseppe Di

2011 4 Excluded

[178] Policy Matching in Modica, Orazio

stage 1

Service Oriented

Tomarchio

Architectures

048 IEEE 08 Security Require- Stefan Du�rbeck, 2007 14 Excluded

[64] ments for a Seman- Rolf Schillinger,

stage 1

tic Service-oriented

Jan Kolter

Architecture

049 IEEE 09 Privacy compliance Hanene Boussi 2009 9 Excluded

[193] in European health Rahmouni, Tony

stage 2

grid domains:

Solomonides,

An ontology-

Marco Casassa

based approach Mont, Simon Shiu

050 IEEE 10 An Ontological Shan Chen, Mary- 2011 0 Excluded

[45]

Study of Data

Anne Williams

stage 1

Purpose for Privacy

Policy Enforcement

051 IEEE 11 Ontology-based Loredana Liccardo, 2012 2 Excluded

[151]

Negotiation of

Massimiliano

stage 2

Security Require- Rak, Giuseppe

ments in Cloud

Di Modica,

Orazio Tomarchio

052 IEEE 12 Using Security and Amina Souag, 2013 4 Selected

[221] Domain ontologies Camille Salinesi,

for Security Re- Isabelle Wattiau,

quirements Analysis Haris Mouratidis

053 IEEE 13

Pattern-based

Olawande

2012 4 Excluded

[56]

security require- Daramola, Gut-

stage 2

ments specification torm Sindre,

using ontologies

Tor Stalhane

and boilerplates

054 IEEE 14 Hierarchical Situa- Stephen S Yau, 2006 83 Excluded

[259] tion Modeling and

Junwei Liu

stage 2

Reasoning for Per-

vasive Computing

055 IEEE 15

Towards an

TSOUMAS

2006 88 Selected

[235] Ontology-based Se- Bill, GRITZA-

curity Management LIS Dimitris

056 IEEE 16 Security oriented Khaled M Khan, 2012 3 Excluded

[137] service composition: Abdelkarim

stage 1

A framework

Erradi, Saleh

Alhazbi, Jun Han

057 IEEE 17 Multi-agent security Manana Hentea 2004 6 Excluded

[111] service architecture

stage 1

for mobile learning

058 IEEE 18 Achieving privacy A. C. Squicciarini, 2006 50 Excluded

[223] in trust negotiations E. Bertino, E.

stage 2

with an ontology- Ferrari, I. Ray

based approach

059 IEEE 19 Engineering Safety

Donald G.

2007 30 Excluded

[86] and Security Related

Firesmith

stage 2

Requirements

for Software

Intensive Systems

060 IEEE 20 Intelligent agents Harry Chen, Tim 2004 277 Excluded

[43]

meet the semantic Finin, Anupam

stage 1

Web in smart spaces Joshi, Lalana

Kagal, Filip

Perich, Dipanjan

Chakraborty

061 IEEE 21 Environmental

Ju An Wang, 2009 4 Excluded

[249] Metrics for Software Minzhe Guo, Hao

stage 2

Security Based

Wang, Min Xia,

on a Vulnera-

Linfeng Zhou

bility Ontology

062 IEEE 22 The image pro- Bechara Al Bouna, 2011 9 Excluded

[27]

tector - A flexible Richard Chbeir,

stage 1

security rule

Alban Gabillon

specification toolkit

063 IEEE 23 Semantic matching Monia Ben Brahim, 2012 1 Excluded

[20]

of web services

Tarak Chaari,

stage 1

security policies Maher Ben Jemaa,

Mohamed Jmaiel

064 IEEE 24 The design of an Shih-Wei Chen, 2012 0 Excluded

[46]

ontology-based

Yu-Ting Tseng,

stage 1

service-oriented

Tsai-Ya Lai

architecture

framework for

traditional Chinese

medicine healthcare

065 IEEE 25 Soupa: Standard Harry Chen, Filip 2004 634 Excluded

[44] ontology for ubiqui- Perich, Tim Finin,

stage 2

tous and pervasive Anupam Joshi

applications

066 IEEE 26 [4] Ontology of

Galyna Akmayeva, 2010 2 Excluded

e-Learning security Charles Shoniregun

stage 2

067 IEEE 27 The Design and Wei Wei, Ting Yu 2010 1 Excluded

[255]

Enforcement of

stage 1

a Rule-based

Constraint Policy

Language for

Service Composition

068 IEEE 28 Context Ontol- Celine Coma, Nora 2008 17 Excluded

[52]

ogy for Secure Cuppens-Boulahia1,

stage 2

Interoperability Frederic Cuppens,

Ana Rosa Cavalli

069 IEEE 29 Towards knowl-

Rishi Kanth

2015 0 Excluded

[205]

edge level privacy Saripalle, Alberto

stage 1

and security us-

De la Rosa

ing RDF/RDFS Algarin, Timoteus

and RBAC

B. Ziminski

070 IEEE 30 Detecting privacy

Maisonnasse, 2006 4 Excluded

[160]

in attention

J�ero�me, Nicolas

stage 2

aware system

Gourier, Oliver

Brdiczka, Patrick

Reignier, James

L. Crowley

071 IEEE 31 Specifying Dynamic Artem Voro- 2006 17 Excluded

[245] Security Properties biev, Jun Han

stage 1

of Web Service

Based Systems

072 IEEE 32 Semantic Access

Najeeb Elahi, 2008 34 Excluded

[73]

Control in Web

Mohammad

stage 1

Based Communities MR Chowd-

hury, Josef Noll

073 IEEE 33 An Approach for Feng Gao, Jingsha 2010 9 Excluded

[95]

Privacy Protection He, Shufen Peng,

stage 2

Based-On Ontology Xu Wu, Xiu Liu

074 IEEE 34 A Light-Weight Chia-Fen Hsieh, 2011 8 Excluded

[116]

Ranger Intrusion Yung-Fa Huang,

stage 1

Detection System Rung-Ching Chen

on Wireless

Sensor Networks

075 IEEE 35 Knowledge modeling Krishna Chan- 2013 0 Excluded

[39]

for privacy-by-

dramouli,

stage 2

design in smart

Virginia Fer-

surveillance solution nandez Arguedas,

Ebroul Izquierdo

076 IEEE 36 A comparative

Vaishali Singh, 2014 0 Excluded

[209]

study of Cloud

S.K. Pandey

stage 2

Security Ontologies

077 IEEE 37 Privacy-Preserving Jie Bao, Giora 2007 37 Excluded

[18]

Reasoning on the

Slutzki, Vas-

stage 1

Semantic Web

ant Honavar

078 IEEE 38

Ontology of

Chen-Yu Lee, 2015 0 Excluded

[147]

Secure Service Krishna M. Kavi,

stage 2

Level Agreement Paul Raymond,

Gomathisankaran

Mahadevan

079 IEEE 39

Contrology -

Ulrich Koinig,

[140]

An Ontology-

Simon Tjoa,

Based Cloud

Jungwoo Ryoo

Assurance Approach

080 IEEE 40 Secure Enterprise Emmanuel Sardis,

[204]

Interoperability Spyridon V Gogou-

Ontology for Seman- vitis, Thanassis

tic Integration of Bouras, Panagiotis

Business to Business Gouvas, Theodora

Applications

Varvarigou

081 IEEE 41 Towards a base Diego Garcia, M.

[96] ontology for privacy Beatriz F. Toledo,

protection in service- Miriam A. M.

oriented architecture Capretz, David S.

Allison, Gordon S.

Blair, Paul Grace,

Carlos Flores

082 IEEE 42 Information Security Fenz, Stefan,

[82]

Fortification by

Gernot Goluch,

Ontological Mapping Andreas Ekelhart,

of the ISO/IEC Bernhard Riedl,

27001 Standard

Edgar Weippl

083 IEEE 43 [3] CCTB: Context Ahamed, Sheikh

Correlation for Monjur, Mehrab,

Trust Bootstrapping Mohammad

in Pervasive

Saiful Islam

Environment

084 IEEE 44 An interoperable se- Muhammad

[12] curity framework for Asim, Milan

connected healthcare Petkovi/'c, Mike

Qu, Changjie Wang

085 IEEE 45 A framework for Hui Guan, Xuan

[101]

security driven Wang, Hongj Yang

software evolution

086 IEEE 46

Research on

Cuncun Wei,

[254]

Semantic-Based Guanghua Chen,

Security Services

Qianqian Ge

Model of SOA

087 IEEE 47 [3] CCTB: Context Ahamed, Sheikh

Correlation for

I and Monjur,

Trust Bootstrapping Mehrab and Islam,

in Pervasive

Mohammad Saiful

Environment

088 IEEE 48 Enabling Access Mohammad M.

[50] Control and Privacy R. Chowdhury,

through Ontology JosefNoll' and Juan

Miguel Gomez

2015 2015
2009
2007 2008 2011 2014 2009 2008 2007

0 Excluded stage 1
0 Excluded stage 1
1 Excluded stage 2
45 Excluded stage 2
9 Excluded stage 1
2 Excluded stage 1
0 Excluded stage 1
0 Excluded stage 1
9 Duplicated
8 Excluded stage 2

089 IEEE 49

What is com-

Matt Bishop 2003 1916 Excluded

[21]

puter security?

stage 2

090 IEEE 50 Modeling secu-

Paolo Giorgini, 2005 198 Selected

[100]

rity requirements Fabio Massacci,

through owner- John Mylopoulos

ship, permission and Nicola Zannone

and delegation

091 IEEE 51 Privacy Ontology Michael Hecker, 2008 31 Excluded

[110]

Support for

Tharam S.

stage 2

E-Commerce

Dillon, and

Elizabeth Chang

092 IEEE 52 Use of Ontology

Maja Hadzic, 2006 4 Excluded

[105]

Technology for

Dillon Tharam,

stage 2

Standardization of Elizabeth Chang

Medical Records

and Dealing

with Associated

Privacy Issues

093 IEEE 53 Ontology Align- Masakazu Kanbe, 2009 2 Excluded

[131]

ment in RFID

Shuichiro

stage 1

Privacy Protection

Yamamoto

094 IEEE 54 Enhancing Privacy Ignacio Blanquer, 2009 25 Excluded

[25]

and Authorization Hern�andez Vicente,

stage 2

Control Scalability Segrelles Damia�,

in the Grid

Erik Torres

Through Ontologies

095 IEEE 55 Ontology-Based

Antti Evesti, 2010 12 Excluded

[76] Security Adaptation Eila Ovaska

stage 1

at Run-Time

096 IEEE 56 A framework for

Gustavo A.

2004 10 Excluded

[231] multi-agent system Santana Torrellas

stage 2

engineering using

ontology domain

modelling for

security architecture

risk assessment

in e-commerce

security services

097 IEEE 57 A Security Ontology Wentao Kang, 2013 1 Selected

[132] with MDA for Soft-

Liang Ying

ware Development

098 IEEE 58 Security Attack Artem Vorobiev 2006 64 Excluded

[244]

Ontology for

and Jun Han

stage 2

Web Services

099 IEEE 59 Ontology-Based

Pan Yan, Zhao 2008 7 Excluded

[257] Information Content

Yanping,

stage 2

Security Analysis

Sanxing Cao

100 IEEE 60 Security Ontologies: Ekelhart, Andreas,

[68]

Improving Quanti-

Stefan Fenz,

tative Risk Analysis Markus Klemen,

Edgar Weippl

101 IEEE 61 An Ontology for Stefania D'Agostini,

[55]

Run-Time Verifi- Valeria Di Giacomo,

cation of Security Claudia Pandolfo,

Certificates for SOA Domenico Presenza

102 IEEE 62

An adaptable

Stephen S Yau,

[260]

security frame- Yisheng Yao, Zhaoji

work for service- Chen, Luping Zhu

based systems

103 CIT 01 Property attesta- Jonathan Poritz,

[192]

tionscalable and Matthias Schunter,

privacy-friendly

Els Van Her-

security assessment reweghen, and

of peer computers Michael Waidner

104 CIT 02 Formal Ontology Nicola Guarino

[102]

and Informa-

tion Systems

105 CIT 03 Using Security and Amina Souag,

[221] Domain ontologies Camille Salinesi,

for Security Re- Isabelle Wattiau,

quirements Analysis Haris Mouratidis

106 CIT 04 Privacy analysis

Martin Kost,

[141]

using ontologies

Johann-

Christoph Freytag

107 CIT 05 [79] Ontologies: A

Dieter Fensel

Silver Bullet

for Knowledge

Management

and Electronic

108 CIT 06 Privacy Verification Martin Kost,

[142]

using Ontologies

Johann-

Christoph Freytag

109 CIT 07 Modeling Reusable Joaqu�in Lasheras,

[241]

Security Require- Rafael Valencia-

ments Based on an Garc�ia, Jesu-

Ontology Framework aldo Tom�as

Fern�andez-Breis

110 CIT 08 [90] A Security Archi- Ian Foster, Carl

tecture for Com-

Kesselman,

putational Grids

Gene Tsudik,

Steven Tuecke

111 CIT 09 [30] Analyzing regulatory Travis D. Breaux,

rules for privacy

Annie Ant�on

and security

requirements

2007 2012 2005 2004
1998 2013 2012 2000
2011 2009
1998 2008

88 Excluded stage 2
4 Excluded stage 1
13 Excluded stage 1
137 Excluded stage 2
4406 Excluded stage 1
4 Duplicated
9 Duplicated
23 Excluded stage 1
10 Duplicated
30 Selected
1765 Excluded stage 1
251 Excluded stage 2

112 CIT 10 Security Ontology Kim Anya, Jim

[138]

for Annotat-

Luo, Myong Kang

ing Resources

113 CIT 11 SPINS: Security

Adrian Perrig,

[191]

Protocols for

Robert Szewczyk,

Sensor Networks Justin Douglas

Tygar, Victor Wen,

David E Culler

114 CIT 12 [48] Private Informa-

Benny Chor,

tion Retrieval

Kushilevitz Eyal,

Oded Goldreich,

Madhu Sudan

115 CIT 13 Towards a new gen- Amina Souag

[217]

eration of security

requirements defi-

nition methodology

using ontologies

116 CIT 14 [89] The ontological

Luciano Floridi

interpretation of in-

formational privacy

117 CIT 15 [67] Ontological mapping Andreas Ekclhart,

of common criterias Stefan Fenz,

security assurance Gernot Goluch,

requirements

Edgar Weippl

118 CIT 16 Security Attack

Artem Voro-

[244]

Ontology for

biev, Jun Han

Web Services

119 CIT 17

An Ontology

Haralambos

[241]

for Modelling

Mouratidis,

Security: The

Paolo Giorgini,

Tropos Approach Gordon Manson

120 CIT 18 An Ontology for Fabio Massacci,

[164]

Secure Socio-

John Mylopoulos,

Technical Systems Nicola Zannone

2005 2002
1998 2012
2005 2007 2006 2003 2007

121 CIT 19 [41] An Ontology for

Harry Chen,

Context-Aware Per-

Tim Finin,

vasive Computing Anupam Joshi

Environments

122 CIT 20 Achieving Privacy in Anna C. Squiccia-

[223] Trust Negotiations rini, Elisa Bertino,

with an Ontology- Elena Ferrari,

Based Approach

Indrakshi Ray

2003 2006

151 Duplicated
4493 Excluded stage 1

1535 Excluded stage 2
4 Excluded stage 2 - Survey paper
109 Excluded stage 1
21 Excluded stage 2
57 Duplicated
52 Duplicated

45 1023

Excluded stage 2 - better version
Spgr 07 02 Duplicated

50 Duplicated

123 CIT 21 An Information Simon E Parkin,

[189]

Security Ontology Aad van Moorsel,

Incorporating

Robert Coles

Human-Behavioral

Implications

124 CIT 22

An Ontological Artem Vorobiev,

[243] Approach Applied

Bekmame-

to Information

dova Nargiza

Security and Trust

125 CIT 23 Developing a privacy

Ni Zhang,

[264] ontology for privacy Chris Todd

control in context-

aware systems

126 CIT 24 Privacy-preserving Prasenjit Mi-

[175] ontology matching tra, Peng Liu,

Chi-Chun Pan

127 CIT 25 [44] SOUPA: Standard Harry Chen, Filip

Ontology for Ubiqui- Perich, Tim Finin,

tous and Pervasive Anupam Joshi

Applications

128 CIT 26 Privacy by Design Marc Langheinrich

[146]

- Principles of

Privacy-Aware

Ubiquitous Systems

129 CIT 27 [42] The SOUPA

Chen, Harry,

Ontology for Per-

Tim Finin,

vasive Computing Anupam Joshi

130 CIT 28 Privacy support Michael Hecker,

[109]

and evaluation on Dillon Tharam

an ontological basis

131 CIT 29

An ontology

Artem Vorobiev,

[246]

framework for Jun Han, Nargiza

managing security Bekmamedova

attacks and defenses

in component based

software systems

132 CIT 30 [91] Ontology Guided Robin Gandhi,

Risk Analysis:

Seok-Won Lee

From Informal

Specifications to

Formal Metrics

133 CIT 31

Ontologies in a

Anand Ran-

[195] pervasive computing ganathan, Robert

environment

E. McGrath, Roy

H. Campbell, Mick-

unas M. Dennis

2009
2007 2005 2005 2004 2001 2005 2007 2008
2009
2003

33 Excluded stage 1
12 Excluded stage 1
0 Excluded stage 2
10 Excluded stage 1
634 Duplicated
769 Excluded stage 2
179 Duplicated
5 Excluded stage 1
7 Excluded stage 2
1 Duplicated
65 Excluded stage 2

134 CIT 32 [66] Reasoning with

Thomas Eiter,

rules and ontologies Giovambattista

Ianni, Axel Polleres,

Roman Schindlauer,

Hans Tompits

135 CIT 33 Security and Privacy Lin Liu, Eric Yu,

[155]

Requirements

John Mylopoulos

Analysis within

a Social Setting

136 CIT 34 [77] Limiting Privacy Alexandre Ev-

Breaches in

fimievski, Johannes

Privacy Preserving Gehrke, Srikant

Data Mining

Ramakrishnan

137 CIT 35 Use of Ontologies in Robert E Mc-

[171] Pervasive Comput- Grath, Anand

ing Environments Ranganathan,

Roy H Campbell,

Mickunas M Dennis

138 Spgr 01 Security ontology for Kim Anya, Jim

[138] annotating resources Luo, Myong Kang

139 Spgr 02 A comparison of se- Fabian Benjamin,

[78] curity requirements Seda Gurses,

engineering methods Maritta Heisel,

Thomas Santen,

Holger Schmidt

140 Spgr 03 Ontologies for secu- Amina Souag,

[219]

rity requirements: Camille Salinesi,

A literature survey Isabelle Wattiau

and classification

141 Spgr 04

Privacy pre-

Thomas Studer

[226]

serving modules

for ontologies

142 Spgr 05 A framework for Stephen S. Yau,

[258]

specifying and

Chen Zhaoji

managing security

requirements in col-

laborative systems

143 Spgr 06 [5] Model driven se- Muhammad Alam

curity engineering

for the realization

of dynamic security

requirements in col-

laborative systems

144 Spgr 07 An Extended On- Fabio Massacci,

[162] tology for Security John Mylopoulos,

Requirements

Federica Paci,

Thein Thun

Tun, Yijun Yu

2006 2006 2003 2003 2005 2010 2012 2010 2006 2007
2011

75 Excluded stage 1
75 Selected
642 Excluded stage 1
33 Excluded stage 1
151 Excluded stage 2
129 Excluded stage 2 - Survey paper
41 Excluded stage 2 - Survey paper
4 Duplicated
17 Duplicated
14 Duplicated
16 Selected

145 Spgr 08 A Security Ontology Amina Souag, 2015 4 Excluded

[220] for Security Require- Camille Salinesi,

stage 2

ments Elicitation Rau�l Mazo, Isabelle

- Survey

Comyn-Wattiau

paper

146 Spgr 09 Ontologies for Secu- Amina Souag, 2012 29 Duplicated

[219] rity Requirements: Camille Salinesi,

A Literature Survey Isabelle Wattiau

and Classification

147 Spgr 10 Reusable knowl- Amina Souag, Rau�l 2015 1 Excluded

[218]

edge in security

Mazo, Camille

stage 1

requirements engi- Salinesi, Isabelle

neering: a systematic Comyn-Wattiau

mapping study

148 Spgr 11 Security Ontology Kim Anya, Jim 2005 151 Duplicated

[138]

for Annotat-

Luo, Myong Kang

ing Resources

149 Spgr 12 Introducing Pri-

Giuseppe Tro- 2011 1 Excluded

[234]

vacy Awareness

pea, Georgios

stage 1

in Network Moni-

V Lioudakis,

toring Ontologies Nicola Blefari-

Melazzi, Dimitra

I Kaklamani,

Iakovos S Venieris

150 Spgr 13 A Modeling Ontol- Golnaz Elahi, Eric 2009 21 Selected

[71]

ogy for Integrating Yu, Nicola Zannone

Vulnerabilities into

Security Require-

ments Conceptual

Foundation

151 Spgr 14

Security-by-

Bill Tsoumas, 2006 12 Excluded

[236]

Ontology: A

Panagiotis Papa-

stage 2

Knowledge-

giannakopoulos,

Centric Approach Stelios Dritsas,

Dimitris Gritzalis

152 Spgr 15 What are Informa- Bill Sicilia, Miguel- 2015 0 Excluded

[207]

tion Security On- Angel Garc�ia-

stage 1

tologies Useful for? Barriocanal, Elena

Javier Bermejo-

Higuera, Salvador

S�anchez-Alonso

153 Spgr 16 Leveraging Ontolo- Eugenia I Papagian- 2014 4 Excluded

[188] gies upon a Holistic nakopoulou, Maria

stage 1

Privacy-Aware Ac- N Koukovini, Geor-

cess Control Model gios V Lioudakis,

Nikolaos Dellas,

Joaquin Garcia-

Alfaro, Dimitra I

Kaklamani, Iakovos

S Venieris, Nora

Cuppens-Boulahia,

Fr�ed�eric Cuppens

154 Spgr 17 Towards Cross-

York Sure,

2004 5 Excluded

[228]

Domain Security

Jochen Haller

stage 1

Properties Sup-

ported by Ontologies

155 Spgr 18 Ontology-Based Danijel Milicevic, 2010 3 Excluded

[174]

Evaluation of

Matthias Goeken

stage 2

ISO 27001.

156 Spgr 19 An Ontology-Based Dhiah el Diehn, 2006 5 Excluded

[61]

Approach for

Abou-Tair I.

stage 2

Managing and Main- Stefan Berlik

taining Privacy in

Information Systems

157 Spgr 20 Privacy Protection Johann Vincent, 2011 8 Excluded

[242]

for Smartphones: Christine Porquet,

stage 2

An Ontology-

Maroua Borsali,

Based Firewall Harold Leboulanger

158 Spgr 21 Specifying an Access Cecilia Ionita, 2005 9 Excluded

[118]

Control Model Osborn M, Sylvia L

stage 1

for Ontologies for

the Semantic Web

159 Spgr 22 Ontology Guided Robin Gandhi, 2009 1 Excluded

[91]

Risk Analysis:

Lee Seok-Won

stage 2

From Informal

Specifications to

Formal Metrics

160 Spgr 23 HIT Considerations: Miguel Humberto 2012 0 Excluded

[232]

Informatics and Torres-Urquidy,

stage 1

Technology Needs

Valerie J. H.

and Considerations Powell, Franklin M.

Din, Mark Diehl,

Valerie Bertaud-

Gounot, W. Ted

Klein, Sushma

Mishra, Shin-Mey

Rose Yin Geist,

Monica Chaudhari,

Mureen Allen

161 Spgr 24 Towards Combining Allyson M Hoss, 2008 5 Excluded

[115]

Ontologies and

Doris L Carver

stage 1

Model Weaving for

the Evolution of Re-

quirements Models

162 Spgr 25 Ontology Guided Andrei Stoica, 2004 27 Excluded

[225]

XML Secu-

Csilla Farkas

stage 1

rity Engine

163 Spgr 26 Using ontologies

Ping Wang ,

2015 1 Excluded

[250]

to perform threat Kuo-Ming Chao,

stage 1

analysis and develop Chi-Chun Lo,

defensive strategies Yu-Shih Wang

for mobile security

164 Spgr 27

SemanticLIFE Edgar R. Weippl, 2004 13 Excluded

[256]

Collaboration: Alexander Schatten,

stage 1

Security Require- Shuaib Karim,

ments and Solutions A. Min Tjoa

Security Aspects of

Semantic Knowledge

Management

165 Spgr 28 Ontology-Enabled Robin Gandhi, 2009 1 Excluded

[112]

Access Control

Lee Seok-Won

stage 2

and Privacy

Recommendations

166 Spgr 29

Accounting for

Ephraim Nissan 2012 0 Excluded

[182]

Social, Spatial,

stage 1

and Textual

Interconnections

167 Spgr 30

Case Study I:

Maja Hadzic, 2009 0 Excluded

[106]

Ontology-Based Pornpit Wongth-

stage 1

Multi-Agent

ongtham, Tharam

System for Human

Dillon, Eliz-

Disease Studies

abeth Chang

168 Spgr 31

The SOUPA

Harry Chen,

2015 191 Excluded

[42]

Ontology for Per-

Tim Finin,

stage 2

vasive Computing Anupam Joshi

169 Spgr 32

An Ontology

Haralambos

2003 54 Excluded

[180]

for Modelling

Mouratidis,

stage 2

Security: The

Paolo Giorgini,

Tropos Approach Gordon Manson

170 Spgr 33 Evaluating Au-

Peter Spyns

2008 2 Excluded

[222]

tomatically a

stage 1

Text Miner for

Ontologies: A

Catch-22 Situation?

171 Spgr 34 EA Legal Ontology Hugo A. Mitre, 2006 6 Excluded

[177] to Support Privacy

Ana Isabel

stage 2

Preservation

Gonzlez-Tablas,

in Location-

Benjamn Ramos,

Based Services Arturo Ribagorda

172 Spgr 35 Capturing Semantics Mohammad M. 2008 6 Excluded

[49]

for Information

R. Chowdhury,

stage 2

Security and

Javier Chamizo,

Privacy Assurance Josef Noll, Juan

Miguel Go�mez

173 Spgr 36

An Ontology

Teresa Pereira, 2009 10 Excluded

[190] Based Approach to Henrique Santos

stage 2

Information Security

174 Spgr 37 Efficient Projection Julius K�opke, 2013 1 Excluded

[187]

of Ontologies

Johann Eder,

stage 1

Michaela Schicho

175 Spgr 38 Regulatory On- Haojun Yu, Sun 2012 0 Excluded

[58]

tologies: An

Yuqing, Jinyan Hu

stage 2

Intellectual Property

Rights Approach

176 Spgr 39

ICT Tools and

Mikel Sorli,

2009 0 Excluded

[216] Systems Supporting Dragan Stokic

stage 1

Innovation in

Product/Process

Development

177 Spgr 40

A Framework

Theodoros

2006 0 Excluded

[17]

for Exploiting Balopoulos, Lazaros

stage 1

Security Expertise Gymnopoulos,

in Application

Maria Karyda,

Development

Spyros Kokolakis,

Stefanos Gritzalis,

Sokratis Katsikas

178 Spgr 41 Risk Evaluation for Mizuho Iwaihara, 2008 12 Excluded

[120]

Personal Identity Murakami Kohei,

stage 2

Management

Ahn Gail-Joon

Based on Privacy

, Masatoshi

Attribute Ontology

Yoshikawa

179 Spgr 42 [9] A framework

Analyti, Antoniou 2013 3 Excluded

for modular

Anastasia, Grigoris

stage 1

ERDF ontologies

and Dam�asio,

Carlos Viegas,

Ioannis Pachoulakis

180 Spgr 43

An Ontology-

Asm Kayes, Jun 2013 8 Excluded

[134]

Based Approach Han, Alan Colman

stage 1

to Context-Aware

Access Control for

Software Services

181 Spgr 44 Development of

Istva�n Mezga�r, 2007 0 Excluded

[173]

an Ontology-

Zolt�an Kincses

stage 1

Based Smart Card

System Reference

Architecture

182 Spgr 45 Introducing the Vandana Kabilan, 2007 4 Excluded

[124]

Common Non- Paul Johannesson,

stage 1

Functional Ontology Sini Ruohomaa,

Pirjo Moen, Andrea

Herrmann, Rose-

Mharie Ahlfeldt,

Hans Weigand

183 Spgr 46 Ontology-Based Henry Ryan, Peter 2003 7 Excluded

[201]

Platform for

Spyns, Pieter

stage 1

Trusted Regulatory De Leenheer,

Compliance Services Richard Leary

184 Spgr 47

Intrusion Cor-

Gustavo Isaza, 2010 6 Excluded

[119]

relation Using

Andr�es Castillo,

stage 1

Ontologies and

Marcelo L�opez,

Multi-agent Systems Luis Castillo,

Manuel L�opez

185 Spgr 48 [6] Agent Models

Marcel Albers, 2004 27 Excluded

and Different

Catholijn M

stage 1

User Ontologies Jonker, Mehrzad

for an Electronic Karami, Jan Treur,

Market Place

186 Spgr 49 Ontology Views: Rajagopal Rajugan, 2006 11 Excluded

[194]

A Theoretical

Elizabeth Chang,

stage 1

Perspective

Tharam S Dillon,

187 Spgr 50 Modeling Computer Jeffrey Undercoffer, 2003 136 Excluded

[237]

Attacks: An

Anupam Joshi,

stage 1

Ontology for

John Pinkston

Intrusion Detection

188 Spgr 51 Security for DAML Grit Denker, Lalana 2003 183 Excluded

[60]

Web Services: Kagal, Tim Finin,

stage 1

Annotation and Massimo Paolucci,

Matchmaking

Katia Sycara

189 Spgr 52 Ontology-Based

Chi-Lun Liu

2009 6 Excluded

[154]

Requirements

stage 1

Conflicts Analysis in

Activity Diagrams

190 Spgr 53 Ontology-Based Kristian Beckers, 2012 4 Excluded

[19]

Identification of

Stefan Eicker,

stage 1

Research Gaps Stephan Fa�bender,

and Immature

Maritta Heisel,

Research Areas Holger Schmidt,

Widura Schwittek

191 Spgr 54 Managing Identities Paolo Ceravolo

[38]

via Interactions

between Ontologies

192 Spgr 55 Security Ontology: Andreas Ekelhart,

[69]

Simulating Threats

Stefan Fenz,

to Corporate Assets Markus D. Klemen,

Edgar R. Weippl

193 Spgr 56 [1] SIMOnt: A Security Muhammad

Information

Abulaish, Syed

Management Irfan Nabi, Khaled

Ontology Framework Alghathbar,

Azeddine Chikh

194 Spgr 57 Retracted: Shared Junfeng Man,

[161]

Ontology for Per-

Aimin Yang,

vasive Computing Xingming Sun

195 Spgr 58 Ontology-Based

Ioana Ciuciu,

[51] Matching of Security Brecht Claerhout,

Attributes for

Louis Schilders,

Personal Data Robert Meersman

Access in e-Health

196 Spgr 59 Intelligent secu-

Bernd Blobel

[26]

rity and privacy

solutions for en-

abling personalized

telepathology

197 Spgr 60

Eddy, a formal Travis D. Breaux,

[31]

language for

Hibshi Hanan,

specifying and

Rao Ashwini

analyzing data flow

specifications for

conflicting privacy

198 SCH 01 Analyzing regulatory Travis D. Breaux,

[30]

rules for privacy

Annie Ant�on

and security

requirements

199 SCH 02 An Ontology for

Harry Chen,

[41] Context-Aware Per-

Tim Finin,

vasive Computing Anupam Joshi

Environments

200 SCH 03 Using a security Fabio Massacci,

[165]

requirements

Marco Prest,

engineering

Nicola Zannone

methodology

in practice: the

compliance with

the Italian data

protection legislation

2003 2006 2011 2005 2011 2011 2014
2008 2003 2005

4 Excluded stage 1
31 Excluded stage 2
3 Excluded stage 2
3 Excluded stage 1
5 Excluded stage 2
5 Excluded stage 1
16 Excluded stage 2
230 Duplicated
1086 Excluded stage 2
82 Excluded stage 2 - better version
Spgr 07 02

201 SCH 04

Security and

Hassan Takabi, 2010 660 Excluded

[229]

privacy challenges James BD Joshi,

stage 1

in cloud computing Ahn Gail-Joon

environments

202 SCH 05 Gene Ontology: Ashburner M, Ball 2000 15501 Excluded

[11]

tool for the

CA, Blake JA,

stage 1

unification of biology Botstein D, Butler

H, Cherry JM,

Davis AP, Dolinski

K, Dwight SS,

Eppig JT, Harris

MA, Hill DP, Issel-

Tarver L, Kasarskis

A, Lewis S, Matese

JC, Richardson JE,

Ringwald M, Rubin

GM, Sherlock G.

203 SCH 06 A Privacy Pref-

Owen Sacco, 2011 52 Excluded

[202]

erence Ontol- Alexandre Passant

stage 2

ogy (PPO) for

Linked Data

204 SCH 07 Property attesta- Jonathan Poritz, 2004 132 Duplicated

[192]

tionscalable and Matthias Schunter,

privacy-friendly

Els Van Her-

security assessment reweghen, and

of peer computers Michael Waidner

205 SCH 08 Improving privacy Melissa Chase, 2009 375 Duplicated

[40]

and security in

Sherman

multi-authority

S.M. Chow

attribute-based

encryption

206 SCH 09 Data security and Ming Li, Wenjing 2010 297 Excluded

[149] privacy in wireless Lou, Kui Ren

stage 1

body area networks

207 SCH 10 Cryptographic ap- Miyako Ohkubo, 2003 793 Excluded

[183] proach to "privacy- Koutarou Suzuki,

stage 1

friendly" tags Shingo Kinoshita,

and others

208 SCH 11 Soupa: Standard Harry Chen, Filip 2004 634 Duplicated

[44] ontology for ubiqui- Perich, Tim Finin,

tous and pervasive Anupam Joshi

applications

209 SCH 12 Security and privacy Elena Ferrari, Bha- 2004 94 Excluded

[85]

for web databases vani Thuraisingham

stage 1

and services

210 SCH 13 Internet of Things Rolf H Weber 2010 297 Excluded

[252]

New security and

stage 1

privacy challenges

211 SCH 14 Privacy and Security Khalil El-Khatib, 2003 86 Excluded

[70]

in E-Learning Larry Korba, Yuefei

stage 1

Xu, George Yee

212 SCH 15 Security and privacy Elena Ferrari, Bha- 2004 94 Excluded

[85]

for web databases vani Thuraisingham

stage 1

and services

213 SCH 16 Security use cases

Donald G.

2003 353 Excluded

[87]

Firesmith

stage 2

214 SCH 17 Achieving privacy Anna C. Squiccia- 2006 50 Duplicated

[223] in trust negotiations rini, Elisa Bertino,

with an ontology- Elena Ferrari,

based approach

Indrakshi Ray

215 SCH 18 Eliciting security Guttorm Sindre, 2005 830 Selected

[208]

requirements Andreas L. Opdahl

with misuse cases

216 SCH 19

The SOUPA

Chen, Harry, 2005 179 Duplicated

[42]

ontology for

Tim Finin,

pervasive computing Anupam Joshi

217 SCH 20 Analyzing website Annie Ant�on, 2002 105 Excluded

[10] privacy requirements Julia B. Earp,

stage 2

using a privacy

Angela Reese

goal taxonomy

218 SCH 21

Guidelines on

Wayne Jansen, 2011 502 Duplicated

[121]

security and

Timothy Grance,

privacy in public

and others

cloud computing

219 SCH 22 Elaborating security

Axel Van

2004 337 Duplicated

[240]

requirements

Lamsweerde

by construction

of intentional

anti-models

220 SCH 23 Using a security

Wayne Jansen, 2011 502 Excluded

[165]

requirements

Timothy Grance,

stage 1

engineering

and others

methodology

in practice: the

compliance with

the Italian data

protection legislation

221 SCH 24 Addressing privacy Christos Kallo- 2008 76 Selected

[130]

requirements in niatis, Evangelia

system design:

Kavakli, Ste-

the PriS method

fanos Gritzalis

222 SCH 25 Security conscious Barbara Carminati, 2006 93 Excluded

[35]

web service

Elena Ferrari,

stage 1

composition

Patrick CK Hung,

223 SCH 26 Security require-

Charles B.

[107] ments engineering: Haley, Robin

A framework for Laney, Jonathan

representation

D. Moffett,

and analysis

Bashar Nuseibeh

224 SCH 27 A framework for

Qingfeng He,

[108]

modeling privacy Annie I. Ant�on

requirements in

role engineering

225 SCH 28 Secure Tropos: a

Haralambos

[179]

security-oriented

Mouratidis,

extension of the

Paolo Giorgini

Tropos methodology

226 SCH 29 Preserving privacy Abdelmounaam

[197]

in web services

Rezgui, Mourad

Ouzzani, Athman

Bouguettaya,

Brahim Medjahed

227 SCH 30

Semantic web Fabien L Gandon,

[93]

technologies to Norman M Sadeh

reconcile privacy and

context awareness

228 SCH 31 Privacy ontology Michael Tharam S.

[110]

support for

Hecker, Elizabeth

e-commerce

Chang Dillon

229 SCH 32 Toward a secu-

Marc Donner

[62]

rity ontology

230 SCH 33 An approach for Gao Feng, Jingsha

[95]

privacy protection He, Shufen Peng,

based-on ontology Xu Wu, Xiu Liu

231 SCH 34 Security ontology for Kim Anya, Jim

[138] annotating resources Luo, Myong Kang

232 SCH 35 Privacy and security

Ajay Brar,

[29]

in ubiquitous

Judy Kay

personalized

applications

233 SCH 36 [7] HIPAA compliance

Alliance,

and smart cards:

Smart Card

Solutions to privacy

and security

requirements

234 SCH 37 Privacy-preserving Prasenjit Mi-

[175] ontology matching tra, Peng Liu,

Chi-Chun Pan

2008
2003 2007 2002
2004 2008 2003 2010 2005 2004 2003
2005

281 Excluded stage 2
85 Excluded stage 2
193 Selected
102 Duplicated
215 Excluded stage 1
29 Duplicated
56 Excluded stage 2
9 Duplicated
151 Duplicated 38 Excluded
stage 1
17 Excluded stage 2
10 Duplicated

235 SCH 38 Risk evaluation for Mizuho Iwaihara,

[120]

personal identity Murakami Ko-

management

hei, Gail-Joon

based on privacy Ahn, Masatoshi

attribute ontology

Yoshikawa

236 SCH 39 Security and privacy Lalana Kagal,

[126] challenges in open

Tim Finin,

and dynamic

Anupam Joshi,

environments

Sol Greenspan,

237 SCH 40 A comparison of se- Fabian Benjamin,

[78] curity requirements Seda Gurses,

engineering methods Maritta Heisel,

Thomas Santen,

Holger Schmidt

238 SCH 41

A taxonomy

Daniel J Solove

[214]

of privacy

239 SCH 42

A taxonomy

Willis H Ware

[251]

for privacy

240 SCH 43 An information

Geoff Skin-

[212]

privacy taxonomy ner, Song Han,

for collaborative Elizabeth Chang

environments

Added studies from search stage 2

241 Spgr 18 01 An ontology for

M. Karyda, T.

[133] secure e-government Balopoulos,

applications

S. Dritsas, L.

Gymnopoulos,

S. Kokolakis, C.

Lambrinoudakis,

S. Gritzalis

242 Spgr 18 02

Ontology in

Victor Raskin,

[196] information security: Christian F

a useful theoretical Hempelmann, Kat-

foundation and rina E Triezenberg,

methodological tool Sergei Nirenburg

243 Spgr 18 03

Formalizing

Stefan RaskinFenz,

[81]

information

Andreas Ekelhart

security knowledge

244 Spgr 13 01 Risk as depend- Yudistira Asnar,

[15]

ability metrics

Rocco Moretti,

for the evalua- Maurizio Sebastia-

tion of business nis, Nicola Zannone

solutions: a model-

driven approach

2008 2006 2010 2006 1981 2006 2006
2001 2009 2008

12 Duplicated
27 Excluded stage 1
121 Duplicated
967 Selected 5 Excluded stage 1 24 Excluded stage 2
37 Excluded stage 2
133 Excluded stage 2
144 Selected 30 Selected

245 Spgr 13 02 The CORAS Folker den Braber,

[59]

methodology.

Theo Dimitrakos,

model-based risk Bjorn A. Gran,

assessment using

Mass S. Lund,

UML and UP

Ketil Stolen,

Jan O. Aagedal

246 Spgr 13 03 A vulnerability- Golnaz Elahi, Eric

[72] centric requirements Yu, Nicola Zannone

engineering frame-

work. analyzing

security attacks,

countermeasures,

and require-

ments based on

vulnerabilities

247 Spgr 13 04 UMLsec: Extending Ju�rjens, Jan

[123]

UML for secure

systems development

248 Spgr 13 05 Adapting secure

Raimundas

[167] tropos for security Matulevicius,

risk management Nicolas Mayer,

in the early phases

Haralambos

of information

Mouratidis,

systems development Eric Dubois,

Patrick Heymans,

Nicolas Genon,

249 Spgr 13 06 Towards a risk-

Nicolas Mayer,

[170]

based security Andr�e Rifaut, Eric

requirements engi- Dubois, and others

neering framework

2003 2010
2002 2008
2005

250 Spgr 13 07 An extended

[199]

misuse case

notation: Including

vulnerabilities and

the insider threat

251 Spgr 13 08 Revisiting Secu-

[210]

rity Ontologies

252 Spgr 08 01 Model-based

[169]

management

of information

system security risk

Lillian R�stad,
Vaishali Singh, SK Pandey
Nicolas Mayer

2006
2014 2009

66 Selected
73 Selected
583 Selected 60 Selected
52 Excluded stage 2 - better version
Spgr 08 01 46 Selected
2 Excluded stage 2
70 Selected

253 Spgr 08 02 Modelling reusable Joaquin Velasco, 2009

[241]

security require- Lasheras Valencia-

ments based on an Garc�ia, Rafael

ontology framework Fern�andez-Breis,

Tom�as Jesualdo,

Ambrosio Toval,

and others

254 Spgr 08 03 A knowledge-based S. Dritsas, L. 2006

[63] approach to security Gymnopoulos,

requirements for

M. Karyda, T.

e-health applications Balopoulos, S.

Kokolakis, C.

Lambrinoudakis,

S. Katsikas

255 Spgr 07 01 A systematic review Blanco, Carlos and 2008

[24]

and comparison of Lasheras, Joaquin

security ontologies and Valencia-

Garc�ia, Rafael and

Ferna�ndez-Medina,

Eduardo and Toval,

Ambrosio and

Piattini, Mario

256 Spgr 07 02 A requirements

Nicola Zannone 2007

[263]

engineering

methodology for

trust, security,

and privacy

257 Spgr 07 03

Introducing

Luncheng Lin, 2003

[152]

abuse frames for Bashar Nuseibeh,

analysing security

Darrel Ince,

requirements

Michael Jackson,

Jonathan Moffett

258 Spgr 03 01 Basic Concepts and Algirdas Avizienis, 2004

[16]

Taxonomy of De- Jean-Claude Laprie,

pendable and Secure Brian Randell,

Carl Landwehr

259 Spgr 03 02 A taxonomy of Donald G Firesmith 2005

[88]

security-related

requirements

260 Spgr 02 01 From trust to

Yudistira Asnar, 2007

[13]

dependability

Paolo Giorgini,

through risk analysis Fabio Massacci,

Nicola Zannone

261 Spgr 02 02 Risk modelling Yudistira Asnar, 2006

[14]

and reasoning

Paolo Giorgini,

in goal models John Mylopoulos

31
17
79
17 73 3703 44 57 17

Excluded stage 2
Selected
Excluded stage 2 - Survey paper
Selected
Excluded stage 2
Selected
Excluded stage 2 Selected
Selected

262 SCH 24 01 Dealing with

Christos Kallo- 2005 15 Excluded

[129]

privacy issues

niatis, Evangelia

stage 2

during the system

Kavakli, Ste-

design process

fanos Gritzalis,

263 SCH 24 02 Privacy risk mod- Jason I Hong, 2004 218 Selected

[114]

els for designing

Jennifer Ng,

privacy-sensitive Scott D Lederer, ,

ubiquitous com- James A Landay,

puting systems

264 SCH 28 01 STS-Tool Security

Elda Paja,

2014 2 Selected

[186]

Requirements En- Fabiano Dalpiaz,

gineering for Socio- Paolo Giorgini

Technical Systems

265 SCH 43 01 Handbook of GW Van Blarkom, 2003 69 Selected

[239]

privacy and

JJ Borking,

privacy-enhancing

JGE Olk

technologies
