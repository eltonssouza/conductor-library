# Solution Architect's Handbook

> **Category:** 03_design_and_architecture · **Language:** English

---

Solutions Architect's Handbook
Kick-start your solutions architect career by learning architecture design principles and strategies
Saurabh Shrivastava Neelanjali Srivastav
BIRMINGHAM - MUMBAI

Solutions Architect's Handbook
Copyright � 2020 Packt Publishing
All rights reserved. No part of this book may be reproduced, stored in a retrieval system, or transmitted in any form or by any means, without the prior written permission of the publisher, except in the case of brief quotations embedded in critical articles or reviews.
Every effort has been made in the preparation of this book to ensure the accuracy of the information presented. However, the information contained in this book is sold without warranty, either express or implied. Neither the authors, nor Packt Publishing or its dealers and distributors, will be held liable for any damages caused or alleged to have been caused directly or indirectly by this book.
Packt Publishing has endeavored to provide trademark information about all of the companies and products mentioned in this book by the appropriate use of capitals. However, Packt Publishing cannot guarantee the accuracy of this information.
Commissioning Editor: Kunal Chaudhari Acquisition Editor: Karan Gupta Content Development Editor: Ruvika Rao Senior Editor: Afshaan Khan Technical Editor: Gaurav Gala Copy Editor: Safis Editing Project Coordinator: Francy Puthiry Proofreader: Safis Editing Indexer: Manju Arasan Production Designer: Joshua Misquitta
First published: March 2020
Production reference: 1200320
Published by Packt Publishing Ltd. Livery Place 35 Livery Street Birmingham B3 2PB, UK.
ISBN 978-1-83864-564-9
www.packt.com

To our loving daughter Sanvi, who fills our lives with happiness and joy. � Saurabh and Neelanjali

Packt.com
Subscribe to our online digital library for full access to over 7,000 books and videos, as well as industry leading tools to help you plan your personal development and advance your career. For more information, please visit our website.
Why subscribe?
Spend less time learning and more time coding with practical eBooks and Videos from over 4,000 industry professionals
Improve your learning with Skill Plans built especially for you
Get a free eBook or video every month
Fully searchable for easy access to vital information
Copy and paste, print, and bookmark content
Did you know that Packt offers eBook versions of every book published, with PDF and ePub files available? You can upgrade to the eBook version at www.packt.com and as a print book customer, you are entitled to a discount on the eBook copy. Get in touch with us at customercare@packtpub.com for more details.
At www.packt.com, you can also read a collection of free technical articles, sign up for a range of free newsletters, and receive exclusive discounts and offers on Packt books and eBooks.

Foreword
The technology realm has always been fast-moving, and in order to keep growing in their careers, IT professionals need to incrementally acquire new skills over time. However, in the last decade, this trend of fast change has become dominant with cloud computing, becoming the 'new normal.' Now, almost every day, there are some new announcements, features, and service updates from cloud providers, which necessitates a focus on a culture of continuous learning for everyone involved. Along with this, now the typical boundaries between the usual roles of a developer, database administrator, security professional, build/release engineer, and so on have started to blur, and this has also resulted in new roles being created that focus on big-picture and end-to-end ownership. One such role is that of a 'Solutions Architect,' which started to evolve from existing roles in industry like 'Application Architect' and 'IT Architect' and has now become mainstream. There are also variations of this role. However, the most common variant is that of 'Cloud Solutions Architect,' which is a pretty dynamic role in itself.
Oftentimes, IT professionals want to switch roles, but they lack direction on how to be successful on that path. This book focuses on this very aspect around an effective transition from an existing IT role to that of a Solutions Architect and explains in a very logical manner the steps to embark on that journey. It starts off with a simple, very relatable explanation of what this role entails and how it differs from a few of the other similar types of profiles. Post that, it goes into the technical skills and aspects of knowledge that are needed to be a successful Solutions Architect. This begins with basic design pillars and architectural principles (including high availability, reliability, performance, security, and cost optimizations), followed by a deep dive into each one of those. The book also covers some key concepts around cloud-native architectures, DevOps, and the data engineering and machine learning domains, which are the cornerstone of any modern-day architecture.

I have personally been through this journey of being a Solutions Architect from a development team lead, and so has Saurabh, and we always wished for a handbook that could have helped us back then. So, to fill that major gap in the industry, Saurabh has created this very detailed book, which is based on personal experiences and learnings that makes it a very relatable read for anyone from a variety of backgrounds. I highly recommend you read this book and keep it as a handy reference always, as in it you will find very important nuggets of knowledge that will help you be a successful Solutions Architect, and open up a new world of infinite possibilities!
Kamal Arora
Senior Manager, Solutions Architecture, AWS
https:// w ww.amazon.c om/K amal-A rora/e /B 07HLTSNRJ/
AWS Solution Architect Leader and author of two Packt books, Cloud-Native Architectures and Architecting Cloud-Native Applications

Contributors
About the authors
Saurabh Shrivastava is a technology leader, author, inventor, and public speaker with over 16 years of experience in the IT industry. He currently works at Amazon Web Services as a Solutions Architect Leader and enables global consulting partners and enterprise customers on their journey to the cloud. Saurabh has also led global technical partnerships and also holds a patent in the area of cloud platform automation.
Saurabh has written various blogs and white papers in a diverse set of technologies, such as big data, IoT, machine learning, and cloud computing. Prior to AWS, Saurabh worked as an enterprise solution architect and software architect in Fortune 50 enterprises, startups, and global product and consulting organizations.
Neelanjali Srivastav is a technology leader, agile coach, and cloud practitioner with over 14 years of experience in the software industry. She holds B.Sc. and M.Sc. degrees in bioinformatics and information technology from Punjab University, Chandigarh. She currently leads teams of software engineers, solution architects, and systems analysts to modernize IT systems and develop innovative software solutions for large enterprises.
She has worked in different roles in the IT services industry and R&D space. Neelanjali is a result-driven and top-performing leader who excels in project management and Agile Scrum methodologies for large-scale enterprises on a global scale.

About the reviewer
Kamesh Ganesan is a cloud evangelist and seasoned technology professional with nearly 23 years of IT experience in all major cloud technologies, including Azure, AWS, Google Cloud Platform (GCP), and Alibaba Cloud. With over 45 IT certifications, including 5 AWS, 3 Azure, and 3 GCP certifications, he's played many roles, including a certified multicloud architect, cloud-native application architect, lead database administrator, and programmer analyst. He architected, built, automated, and delivered high-quality, missioncritical, and innovative technology solutions to help his enterprise, along with commercial and governmental clients, to be very successful and vastly improve their business value as a result of using multi-cloud strategies.
Packt is searching for authors like you
If you're interested in becoming an author for Packt, please visit authors.packtpub.com and apply today. We have worked with thousands of developers and tech professionals, just like you, to help them share their insight with the global tech community. You can make a general application, apply for a specific hot topic that we are recruiting an author for, or submit your own idea.

Table of Contents

Preface

1

Chapter 1: The Meaning of Solution Architecture

6

What is solution architecture?

7

Evolution of solution architecture

11

Why is solution architecture important?

12

The benefits of solution architecture

13

Addressing the business needs and quality of delivery

14

Selecting the best technology platform

15

Addressing solution constraints and issues

16

Helping in resource and cost management

16

Managing solution delivery and project life cycle

17

Addressing non-functional requirements

17

Solution architecture in the public cloud

19

What is the public cloud?

19

Public clouds, private clouds, and hybrid clouds

20

The public cloud architecture

21

Public cloud providers and cloud service offering

22

Summary

24

Chapter 2: Solution Architects in an Organization

25

Types of solution architect role

26

Enterprise solution architect

29

Solution architect

30

Technical architect

30

Cloud architect

31

Architect evangelist

32

Infrastructure architect

32

Network architect

33

Data architect

34

Security architect

35

DevOps architect

36

Understanding a solution architect's responsibilities

37

Analyzing user requirements

38

Defining non-functional requirements

38

Engaging and working with stakeholders

41

Handling various architecture constraints

41

Making technology selections

44

Developing a proof of concept and a prototype

44

Designing solutions and staying through delivery

45

Table of Contents

Ensuring post-launch operability and maintenance

47

Working as a technology evangelist

47

Solution architects in an agile organization

47

Why Agile methodology?

48

Agile manifesto

49

Agile process and terminology

50

Sprint ceremonies

51

Agile tools and terms

52

Agile versus waterfall

53

Agile architecture

54

Summary

55

Chapter 3: Attributes of the Solution Architecture

56

Scalability and elasticity

57

The capacity dilemma in scaling

58

Scaling your architecture

59

Static content scaling

60

Server fleet elasticity

61

Database scaling

61

High availability and resiliency

62

Fault-tolerance and redundancy

64

Disaster recovery and business continuity

65

Extensibility and reusability

67

Usability and accessibility

69

Portability and interoperability

70

Operational excellence and maintainability

72

Security and compliance

73

Authentication and authorization

74

Web security

74

Network security

74

Infrastructure security

75

Data security

75

Cost optimization and budget

76

Summary

77

Chapter 4: Principles of Solution Architecture Design

78

Scaling workload

79

Predictive scaling

79

Reactive scaling

82

Building resilient architecture

83

Design for performance

85

Using replaceable resources

86

Creating immutable infrastructure

87

Canary testing

87

Think loose coupling

88

[ ii ]

Table of Contents

Think service not server

90

Using the right storage for the right need

92

Think data-driven design

94

Overcoming constraints

95

Adding security everywhere

97

Automating everything

98

Summary

99

Chapter 5: Cloud Migration and Hybrid Cloud Architecture Design

101

Benefits of cloud-native architecture

102

Creating a cloud migration strategy

104

Lift and Shift migration

106

Rehost

106

Replatform

107

Relocate

107

Cloud-native approach

108

Refactor

109

Repurchase

109

Retain or retire

110

Retain

110

Retire

111

Steps for cloud migration

112

Discovering your workload

113

Analyzing the information

115

Creating migration plan

117

Designing the application

121

Performing application migration to the cloud

124

Data migration

124

Server migration

126

Integration, validation, and cutover

127

Live migration cutover

128

Operating cloud application

130

Application optimization in the cloud

131

Creating a hybrid cloud architecture

133

Designing a cloud-native architecture

135

Popular public cloud choices

137

Summary

138

Further reading

139

Chapter 6: Solution Architecture Design Patterns

140

Building an n-tier layered architecture

141

The web layer

142

The application layer

143

The database layer

143

Creating multi-tenant SaaS-based architecture

144

Building stateless and stateful architecture designs

146

[ iii ]

Table of Contents

Understanding SOA

148

SOAP web service architecture

149

RESTful web service architecture

152

Building an SOA-based e-commerce website architecture

153

Building serverless architecture

154

Creating microservice architecture

156

Real-time voting application reference architecture

158

Building queue-based architecture

159

Queuing chain pattern

160

Job observer pattern

162

Creating event-driven architecture

163

Publisher/subscriber model

163

Event stream model

165

Building cache-based architecture

166

Cache distribution pattern in a three-tier web architecture

169

Rename distribution pattern

170

Cache proxy pattern

171

Rewrite proxy pattern

173

App caching pattern

174

Memcached versus Redis

175

Understanding the circuit breaker pattern

176

Implementing the bulkheads pattern

176

Creating a floating IP pattern

178

Deploying an application with a container

179

The benefit of containers

180

Container deployment

182

Database handling in application architecture

184

High-availability database pattern

186

Avoiding anti-patterns in solution architecture

187

Summary

189

Chapter 7: Performance Considerations

191

Design principles for architecture performance

192

Reducing latency

192

Improving throughput

194

Handling concurrency

196

Apply caching

197

Technology selection for performance optimization

199

Making a computational choice

199

Selecting the server instance

200

Working with containers

203

Docker

203

Kubernetes

204

Going serverless

205

Choosing a storage

207

Working with block storage and storage area network (SAN)

207

[ iv ]

Table of Contents

Working with file storage and network area storage (NAS)

208

Working with object storage and the cloud data storage

208

Choosing the database

210

Online transactional processing (OLTP)

211

Nonrelational databases (NoSQL)

212

Online analytical processing (OLAP)

212

Building a data search

213

Making the networking choice

214

Defining a DNS routing strategy

215

Implementing a load balancer

216

Applying autoscaling

217

Managing performance monitoring

219

Summary

221

Chapter 8: Security Considerations

222

Designing principles for architectural security

223

Implementing authentication and authorization control

223

Applying security everywhere

224

Reducing blast radius

224

Monitoring and auditing everything all the time

225

Automating everything

225

Protecting data

226

Preparing a response

226

Selecting technology for architectural security

227

User identity and access management

227

FIM and SSO

229

Kerberos

229

AD

231

Amazon Web Services (AWS) Directory Service

232

Security Assertion Markup Language (SAML)

232

OAuth and OpenID Connect (OIDC)

234

Handling web security

236

Web app security vulnerabilities

236

Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks

236

SQLi attacks

238

XSS attacks

238

Cross-Site Request Forgery (CSRF) attacks

238

Buffer overflow and memory corruption attacks

239

Web security mitigation

239

Web Application Firewall (WAF)

239

DDoS mitigation

240

Securing an application and its infrastructure

242

Application and operating system hardening

242

Software vulnerabilities and secure code

243

Network, firewall, and trusted boundary

243

IDS/IPS

246

Host-based IDS

247

Network-based IDS

247

Data security

248

[v]

Table of Contents

Data classification

248

Data encryption

249

Encryption key management

250

Envelope encryption

250

AWS Key Management Service (KMS)

251

Hardware security module (HSM)

252

Data encryption at rest and in transit

252

Security and compliance certifications

253

The cloud's shared security responsibility model

254

Summary

257

Chapter 9: Architectural Reliability Considerations

258

Design principles for architectural reliability

259

Making systems self-healing

259

Applying automation

260

Creating a distributed system

260

Monitoring capacity

261

Performing recovery validation

262

Technology selection for architecture reliability

262

Planning the RTO and RPO

263

Replicating data

264

Synchronous versus asynchronous replication

264

Replication methods

265

Planning disaster recovery

266

Backup and restore

268

Pilot light

269

Warm standby

272

Multi-site

274

Applying best practices for disaster recovery

275

Improving reliability with the cloud

276

Summary

278

Chapter 10: Operational Excellence Considerations

279

Designing principles for operational excellence

280

Automating the operation

280

Making incremental and reversible changes

281

Predicting failures and responding

282

Learning from the mistake and refining

282

Keeping operation's runbook updated

282

Selecting technologies for operational excellence

283

Planning for operational excellence

283

IT Asset Management (ITAM)

284

Configuration management

286

The functioning of operational excellence

288

Monitoring system health

289

Infrastructure monitoring

289

Application monitoring

290

Platform monitoring

291

[ vi ]

Table of Contents

Log monitoring

292

Security monitoring

295

Handling alerts and incident response

295

Improving operational excellence

298

ITOA

299

RCA

300

Auditing and reporting

301

Achieving operational excellence in the public cloud

302

Summary

303

Chapter 11: Cost Considerations

305

Design principles for cost optimization

306

Calculating the total cost of ownership

306

Planning the budget and forecast

308

Managing demand and service catalogs

309

Keeping track of expenditure

310

Continuous cost optimization

311

Techniques for cost optimization

312

Reducing architectural complexity

312

Increasing IT efficiency

314

Applying standardization and governance

316

Monitoring cost usage and report

318

Cost optimization in the public cloud

323

Summary

325

Chapter 12: DevOps and Solution Architecture Framework

326

Introducing DevOps

327

Understanding the benefits of DevOps

328

Understanding the components of DevOps

329

CI/CD

330

Continuous monitoring and improvement

332

IaC

333

Configuration management (CM)

334

Introducing DevSecOps

335

Combining DevSecOps and CI/CD

336

Implementing a CD strategy

337

In-place deployment

338

Rolling deployment

338

Blue-green deployment

338

Red-black deployment

340

Immutable deployment

340

Implementing continuous testing in the CI/CD pipeline

341

A/B testing

343

Using DevOps tools for CI/CD

344

Code editor

344

Source code management

345

[ vii ]

Table of Contents

CI server

345

Code deployment

347

Code pipeline

349

Implementing DevOps best practices

351

Summary

352

Chapter 13: Data Engineering and Machine Learning

354

What is big data architecture?

355

Designing big data processing pipelines

357

Data ingestion

359

Technology choices for data ingestion

360

Ingesting data to the cloud

362

Storing data

364

Technology choices for data storage

366

Structured data stores

366

Relational databases

367

Data warehousing

367

NoSQL databases

368

SQL versus NoSQL databases

369

Types of NoSQL data store

370

Search data stores

370

Unstructured data stores

371

Data lakes

371

Processing data and performing analytics

373

Technology choices for data processing and analysis

375

Visualizing data

378

Technology choices for data visualization

378

Understanding IoT

380

What is ML?

382

Working with data science and ML

383

Evaluating ML models � overfitting versus underfitting

385

Understanding supervised and unsupervised ML

386

Summary

388

Chapter 14: Architecting Legacy Systems

389

Learning the challenges of legacy systems

390

Difficulty in keeping up with user demand

391

Higher cost of maintenance and update

391

Shortage of skills and documentation

392

Vulnerable to corporate security issues

393

Incompatibility with other systems

394

Defining a strategy for system modernization

395

Benefits of system modernization

395

Assessment of a legacy application

397

Defining the modernization approach

398

Documentation and support

399

[ viii ]

Table of Contents

Looking at legacy system modernization techniques

400

Encapsulation, rehosting, and re-platforming

400

Refactoring and rearchitecting

401

Redesigning and replacing

401

Defining a cloud migration strategy for legacy systems

403

Summary

405

Chapter 15: Solution Architecture Document

406

Purpose of the SAD

407

Views of the SAD

408

Structure of the SAD

411

Solution overview

412

Business context

413

Conceptual solution overview

415

Solution architecture

416

Solution delivery

420

Solution management

421

Appendix section of SAD

422

IT procurement documentation for a solution architecture

422

Summary

424

Chapter 16: Learning Soft Skills to Become a Better Solution Architect 425

Acquiring pre-sales skills

426

Presenting to C-level executives

427

Taking ownership and accountability

429

Defining strategy execution and OKRs

430

Thinking big

431

Being flexible and adaptable

432

Design thinking

433

Being a builder by engaging in coding hands-on

436

Becoming better with continuous learning

436

Being a mentor to others

439

Becoming a technology evangelist and thought leader

439

Summary

440

Other Books You May Enjoy

441

Index

444

[ ix ]

Preface
This book guides readers to create a robust, scaled, highly available, and fault-tolerant solution by learning a different aspect of solution architecture and next-generation architecture design in a cloud environment. This book will start by providing an understanding of solution architecture and how it fits into an agile enterprise environment. It will take the reader through the journey of solution architecture design by providing detailed knowledge of design pillars, advanced design patterns, anti-patterns, and the cloud-native aspects of modern software design.
The reader will dive deep into performance optimization, security, compliance, reliability, cost optimization, and operational excellence in solution design. This book provides an indepth understanding of the automation of security, infrastructure, DevOps, disaster recovery, and the documentation of solution architecture. In addition, readers will learn various architecture designs in cloud platform like Amazon Web Services (AWS) and how to best utilize cloud platform for your solution design, modernization and migration need.
This book also provides a good understanding of future-proof architecture design with data engineering, machine learning, and the Internet of Things (IoT). As a bonus, this book will also offer a soft skill aspect to enhance your solution architecture skills and continuous learning techniques. This book will you to start your career journey and improve your skills in the solution architect role. By end of this book, you will have gained the required skills to advance your career as a solution architect.
Who this book is for
This book is for software developers, system engineers, DevOps engineers, architects, and team leaders working in the IT industry, who aspire to become solution architects and are keen on designing secure, reliable, high-performance, and cost-effective architectures.
What this book covers
Chapter 1, The Meaning of Solution Architecture, is used as a base to define what solution architecture is and explain its importance. It explains various benefits of having a solution architecture in place and talks about architecting on the public cloud.

Preface
Chapter 2, Solution Architects in an Organization, talks about the different types of solution architect roles and how they fit into the organizational structure. It explores the various responsibilities of the solution architect in detail. It further explains the solution architect's role fit in an agile organization along with agile processes.
Chapter 3, Attributes of the Solution Architecture, throws light on various attributes of solution architecture, such as scalability, resiliency, disaster recovery, accessibility, usability, security, and cost. It explains the coexistence and utilization of these architectural attributes to create an efficient solution design.
Chapter 4, Principles of Solution Architecture Design, talks about architectural principles for creating scalable, resilient, and high-performance architecture. It explains efficient architecture design by applying security, overcoming constraints, and applying changes, along with test and automation approaches. It explores architecture principals to use design thinking effectively by exploring service-oriented architecture and taking a data-driven approach.
Chapter 5, Cloud Migration and Hybrid Cloud Architecture Design, explains the benefits of the cloud and approaches to design cloud-native architecture. It gives an understanding of different cloud migration strategies and migration steps. It talks about hybrid cloud design and explores popular public cloud providers.
Chapter 6, Solution Architecture Design Patterns, explores various architecture design patterns, such as layered, microservice, event-driven, queue-based, serverless, cache-based, and service-oriented with examples. It demonstrates the applicability of solution architecture attributes and principles to design the best architecture as per business requirements. It explains about the various reference architectures in AWS cloud platform.
Chapter 7, Performance Considerations, provides an understanding of essential attributes of application performance improvement such as latency, throughput, and concurrency. It explains various technology choices to improve performance at multiple layers of architecture, including compute, storage, database, and networking, along with performance monitoring.
Chapter 8, Security Considerations, talks about the various design principles applicable to securing your workload. Security needs to apply at every layer and to every component of the architecture, and this chapter helps you to get an understanding of the right selection of technology to ensure your architecture is secure at every layer. It explores the industry compliance guidelines applicable to architecture design and explains security in the cloud with a shared responsibility model.
[2]

Preface
Chapter 9, Architectural Reliability Considerations, talks about design principles to make your architecture reliable. It explores various disaster recovery techniques to ensure high availability of your application, and data replication methods for business process continuations. It explains best practices and the role of the cloud in the application to achieve reliability.
Chapter 10, Operational Excellence Considerations, talks about various processes and methods for achieving operational excellence in applications. It explains best practices and technology selections that apply throughout the phases of application design, implementation, and post-production to improve application operability. It also explores operational excellence for cloud workloads.
Chapter 11, Cost Considerations, talks about the various techniques for optimizing cost without risking business agility. It explains multiple methods used to monitor cost and apply governance for cost control. It helps you to understand cost optimization using the cloud.
Chapter 12, DevOps and the Solution Architecture Framework, explains the importance of DevOps in application deployment, testing, and security. It explores DevSecOps and its role in the application's continuous deployment and delivery pipeline. It talks about DevOps best practices and the tools and techniques to implement them.
Chapter 13, Data Engineering and Machine Learning, talks about how to design big data and analytics architectures. It outlines the steps to create a big data pipeline, including data ingestion, storage, processing, and visualization. It helps you to understand the concepts and technology involved in IoT. It explores details about machine learning, model evaluation techniques, and gives an overview of various machine learning algorithms.
Chapter 14, Architecting Legacy Systems, talks about the various challenges and modernization drivers for legacy systems. It explains strategies and techniques to modernize legacy systems. Use of the public cloud is becoming a go-to strategy for many organizations, so this chapter also explores the cloud migration of legacy systems.
Chapter 15, Solution Architecture Document, talks about the solution architecture document along with its structure and the various details required to accommodate the documentation. It explores a variety of IT procurement documentation, where the solution architect participates in providing feedback.
Chapter 16, Learning Soft Skills to Become a Better Solution Architect, talks about various soft skills required for a solution architect to be successful in the role. It helps you to understand methods to acquire strategic skills such as pre-sales and executive communication, develop design thinking, and personal leadership skills such as thinking big and ownership. It explores techniques to establish yourself as a leader and continue improving your skillset.
[3]

Preface
To get the most out of this book
Prior experience of software architecture design will help you to follow along with this book. However, no specific prerequisites are required to understand this book. All the examples and relevant instructions are provided throughout the various chapters. This book takes you into the deep concepts underlying solution architecture design and does not require knowledge of any particular programming language, framework, or tool.
Download the color images
We also provide a PDF file that has color images of the screenshots/diagrams used in this book. You can download it here: https://s tatic.packt-cdn.c om/downloads/ 9781838645649_ColorImages.p df.
Conventions used
There are a number of text conventions used throughout this book. CodeInText: Indicates code words in text, database table names, folder names, filenames, file extensions, pathnames, dummy URLs, user input, and Twitter handles. Here is an example: "You can apply data encryption in transit and at rest. When you push into a code repository (git push), it encrypts the data and then stores it. When you pull from a code repository (git pull), it decrypts the data and then sends the data back to the caller." Bold: Indicates a new term, an important word, or words that you see onscreen. For example, words in menus or dialog boxes appear in the text like this. Here is an example: "The Jenkin Master offload builds to the slave node instance in case of overload."
Warnings or important notes appear like this.
Tips and tricks appear like this.
[4]

Preface
Get in touch
Feedback from our readers is always welcome. General feedback: If you have questions about any aspect of this book, mention the book title in the subject of your message and email us at customercare@packtpub.com. Errata: Although we have taken every care to ensure the accuracy of our content, mistakes do happen. If you have found a mistake in this book, we would be grateful if you would report this to us. Please visit www.packtpub.com/support/errata, selecting your book, clicking on the Errata Submission Form link, and entering the details. Piracy: If you come across any illegal copies of our works in any form on the Internet, we would be grateful if you would provide us with the location address or website name. Please contact us at copyright@packt.com with a link to the material. If you are interested in becoming an author: If there is a topic that you have expertise in and you are interested in either writing or contributing to a book, please visit authors.packtpub.com.
Reviews
Please leave a review. Once you have read and used this book, why not leave a review on the site that you purchased it from? Potential readers can then see and use your unbiased opinion to make purchase decisions, we at Packt can understand what you think about our products, and our authors can see your feedback on their book. Thank you! For more information about Packt, please visit packt.com.
[5]

1
The Meaning of Solution
Architecture
This book is your first step in the solution architecture world. Throughout this book, you will learn all about solution architecture, and how to become a solution architect. In this first chapter, let's understand the meaning of solution architecture. Solution architecture is the building blocks of solution development in the organization. It helps to create a successful solution in a complex organization, where product development has dependencies on multiple groups.
For the success of application development, defining solution architecture should be the first step, which then lays out the foundations and the robust building block of implementation. Solution architecture not only considers the requirements of the business, but also handles critical, non-functional requirements such as scalability, high availability, maintainability, performance, security, and so on.
A solution architect is a person who is responsible for designing solution architecture by collaborating across stakeholders. The solution architect analyzes the functional requirement and defines a non-functional requirement in order to cover all aspects of the solution and avoid any surprises. Each solution has multiple constraints such as cost, budget, timeline, regulatory, and so on, and the solution architect considers them, while also creating the design and making technology selection.
The solution architect develops a proof of concept and prototype in order to evaluate various technology platforms, and then chooses the best strategy for solution implementation. They mentor the team throughout solution development and provide post-launch guidance to maintain and scale the final product.

The Meaning of Solution Architecture
In this chapter, you will learn about the following topics:
What is solution architecture? Evolution for solution architecture Understanding the importance of solution architecture The benefits of solution architecture The workings of solution architecture in the public cloud

Chapter 1

What is solution architecture?
If you ask around, there may be 10 different answers for the definition of solution architecture, and they may all be correct, as per their organization's structure. Each organization may see solution architecture from a different perspective, based on their business needs, organizational hierarchy, and solution complexity.
In a nutshell, solution architecture defines and foresees multiple aspects of a business solution, at both the strategic and tactical perspectives. Solution architecture is not just about a software solution. It covers all aspects of a system, which will be included but not limited to, system infrastructure, networking, security, compliance requirement, system operation, cost, and reliability. As you can see, the following diagram provides a different aspect that a solution architect can address:

Circle of solution architecture
[7]

The Meaning of Solution Architecture

Chapter 1

As shown in the preceding diagram, a good solution architect addresses the most common aspects of the solution in an organization:
Globally distributed teams: In this age of globalization, almost every product has users distributed across the globe, and stakeholder's groups to take care of customer needs. Often, the software development team has an onshore�offshore model, where a team works across different time zones to increase productivity and optimize project cost. Solution design needs to consider a globally distributed team structure.
Global compliance requirement: When you are deploying your solution globally, each country and region has its laws and compliance regime, which your solution needs to adhere. Some examples are as follows:
The Federal Risk and Authorization Management Program (FedRAMP) and Department of Defense Cloud Computing Security Requirements Guide (DoD SRG) for the USA The General Data Protection Regulation (GDPR) for Europe The Information Security Registered Assessors Program (IRAP) for Australia
The Center for Financial Industry Information Systems (FISC) for Japan
The Multi-Tier Cloud Security (MTCS) standard for Singapore The G-Cloud for the UK The IT-Grundschutz for Germany The Multi-Level Protection Scheme (MLPS) Level 3 for China
Also, compliance requirements are different from industry to the industry, for example, the International Organization for Standardization (ISO) 9001 (which is primarily for healthcare, life sciences, medical devices, and the automotive and aerospace industries), the Payment Card Industry Data Security Standard (PCI-DSS) for finance, the Health Insurance Portability and Accountability Act (HIPPA) for healthcare, and so on. Solution architecture needs to consider that compliance in the design phase. You will learn more about compliance in Chapter 8, Security Considerations.

[8]

The Meaning of Solution Architecture

Chapter 1

Cost and budget: Solution architecture gives a good estimation of the overall cost of the project, which helps to define a budget. This includes capital expenditure (CapEx), which is the upfront cost and, operational expenditure (OpEx), which is an ongoing cost. It helps management to create an overall budget for human resources, infrastructure resources, and other licensing-related costs.
Solution implementation component: Solution architecture provides a highlevel overview of different implementation components of the product beforehand, which helps to plan execution.
Business requirements: Solution architecture considers all business requirements, which includes both functional and non-functional requirements. It makes sure that business requirements are compatible, therefore allowing them to be converted into the technical implementation stage and strike a balance between stakeholders.
IT infrastructure requirements: Solution architecture determines what kind of IT infrastructure is required to execute the project, which includes computing, storage, network, and so on. This helps to plan the IT resources more effectively.
Technology selection: During solution design, a solution architect creates a proof of concept and prototype, which considers the corporate requirements, and then recommends the right technology and tools for implementation. Solution architecture aims to build in-house versus third-party tool sourcing and define software standards across the organization.
End user requirements: Solution architecture pays special attention to the requirements of the end user, who will be the actual consumer of the product. It helps to discover the hidden requirements that a product owner may not be able to capture, due to a lack of technicality. During implementation and launch, solution architect provides a standard document and typical language structure in order to make sure that all of the requirements have been met to satisfy the user's needs.
Solution maintenance: Solution architecture is not just about solution design and implementation, but it also takes care of post-launch activities, such as solution scalability, disaster recovery, operational excellence, and so on.
Project timeline: Solution architecture designs the layout details of each component with their complexity, which further helps to define the project milestones and timeline by providing resource estimation and associated risks.

[9]

The Meaning of Solution Architecture

Chapter 1

An industry-standard and well-defined solution architecture address all business requirements in a technical solution, and they make sure to deliver the desired result in order to satisfy the stakeholders, as per their expectations in terms of the quality, availability, maintainability, and scalability of the solution.
The initial design of a solution architecture may be conceived at a very early stage during the pre-sales cycle, such as the request for proposal (RFP) or the request for information (RFI) and is followed by the creation of a prototype or proof of concept, in order to discover any solution risk. Solution architect also identifies whether to build a solution or to source it. It helps to identify technology selection, while also keeping an organization's critical security and compliance requirements in mind.
There could be two primary situations for creating a solution architecture:
First, enhancing technology for an existing application, which may include hardware refresh or software re-architecting Second, to create a new solution from scratch, where you get more flexibility to choose the best fit of technology to address a business requirement
However, while re-architecting the existing solution, you need to consider the minimal impact and create a solution that can best fit the current environment. Solution architects may decide to re-build if re-architecting the existing solution is not worth it, and a better solution can be provided by a re-build approach.
In a more simplified language, solution architecture is about looking at all the aspects of the system in order to generate a technical vision, which provides steps to implement the business requirements. Solution architecture can define an implementation for a project or a group of projects in a complex environment, by putting together all of the different pieces that are related to data, infrastructure, networking, and software application. A good solution architecture not only satisfies the functional and non-functional requirements, but also addresses system scalabilities and maintenance in the long run.
We have just learned about an overview of solution architecture and its different aspects. In the next section, we will look at the evolution of solution architecture.

[ 10 ]

The Meaning of Solution Architecture

Chapter 1

Evolution of solution architecture
Solution architecture has evolved with technological modernization. Today, solution architecture design has changed drastically compared to a couple of decades ago, due to the increasing use of the internet, the availability of high-bandwidth network, the low cost of storage, and computer availability.
Back in the days before the era of the internet, most solution designs focused on providing a thick desktop client, which was capable of operating with low bandwidth and working offline when a system could not connect to the internet.
This technology started evolving in the last decade. Service-oriented architecture (SOA) started taking shape for distributed design, and applications started moving from monolithic to modern n-tier architecture, where the frontend server, application server, and database were live in their computer and the storage layer. These SOAs are mostly achieved by an XML-based messaging protocol, called Simple Object Access Protocol (SOAP). This majorly follows a client�server model in order to create services.
In this age of digitization, you will see microservice-based solution design becoming increasingly popular, which is based on JavaScript Object Notation (JSON)-based messaging and the Representational State Transfer (REST) service. These are Web APIs, which do not require XML-based web service protocols (SOAPs) to support their interfaces. They rely on web-based HTTP protocols such as POST, GET, UPDATE, DELETE, and so on. You will learn more about different architecture patterns in great detail in Chapter 6, Solution Architecture Design Patterns.
The microservice architecture addresses the need for changing requirements in an agile environment, where any solution changes need to be accommodated and deployed rapidly. Organizations have to be agile to stay ahead of the competition. This forces solution architecture to be flexible, compared to the waterfall model, where you have a long cycle of project release.
The web-based microservice architecture is fueled by an almost unlimited resource capability, which is available from cloud providers and which can scale in minutes or seconds. It's becoming easier to innovate, experiment, and change as solution architects and developers can risk failing without harming anything.

[ 11 ]

The Meaning of Solution Architecture

Chapter 1

Why is solution architecture important?
Solution architecture is the building block for an overall enterprise software solution that addresses specific problems and requirements. As the project size increases, the team becomes distributed globally. It is required to have a solution architecture in place for longterm sustainability and a solid foundation.
Solution architecture addresses various solution needs, keeping the business context intact. It specifies and documents technology platforms, application components, data requirements, resource requirements, and many important non-functional requirements such as scalability, reliability, performance, throughput, availability, security, and maintainability.
Solution architecture is vital for any industry and its solution. In the absence of solution architecture, there is a chance that software development could fail; projects can get delayed, get over budget, and not deliver enough functionalities. This scenario can be drastically improved by creating a solution architecture and applying experience and knowledge; all of which are provided by a solution architect. It helps to keep stakeholders from all areas � from non-technical business functions to technical development � on the same page, which avoids confusion, keeps the project on track within schedule and time, and helps to derive maximum return on investment(ROI).
Often, the solution architect requires customer collaboration in order to understand specifications. In a solution architect's role, the architect needs multiple skillsets from technical leaders and experts, to business analysts and project management. We will learn more about the solution architect's role in Chapter 2, Solution Architects in an Organization.
A good solution architecture puts specifications in place with a well-defined solution, which helps us to deliver and accomplish the final product, along with smooth product operability after launch. A single problem can have multiple solutions, and each solution has its constraints. Solution architecture considers all the solutions, and finds the best way, by creating a hands-on proof of concept that accommodates all of the business and technical limitations.

[ 12 ]

The Meaning of Solution Architecture

Chapter 1

The benefits of solution architecture
The previous section sheds light on the importance of solution architecture. This section will further explore and provide more details on the benefits of solution architecture in various aspects of an organization, as shown in the following solution architecture benefits diagram:

A solution architecture's beneficial attributes
The preceding diagram highlights the following attributes of a good solution architecture:
Technology value and requirement: Solution architecture determines the return on investment, which solution can be obtained by a particular technology selection, and the market trend. The solution architect evaluates which technology an organization or project should adopt in order to achieve long-term sustainability, maintainability, and team comfort. Business goal: The primary responsibility of a solution architecture design is to accommodate the needs of the stakeholders and adapt change in their requirements. Solution architecture converts business goals into a technical vision by analyzing market trends and implementing the best practice. Solution architecture needs to be flexible enough to meet new, challenging, demanding, and rapidly changing business requirements.
[ 13 ]

The Meaning of Solution Architecture

Chapter 1

Target date: A solution architect continuously works with all stakeholders, including the business team, customer, and development team. A solution architect defines the process standard and provides guidelines for solution development. He/she makes sure that the overall solution is in alignment with the business objective and launch timeline, to ensure minimal chances of target date slippage.
Increased Return on Investment (ROI): Solution architecture determines the ROI and help to measure the success of the project. Solution architecture forces businesses to think about how to reduce costs and remove waste in the process, in order to improve the overall ROI.
Market opportunity: Solution architecture involves the process of analyzing and continuously evaluating the latest trends in the market. It also helps with backing up and promoting new products.
Budget and resourcing: For a better budget, it is always recommended to invest well in estimation. A well-defined solution architecture helps to understand the number of resources that are required for project completion. This helps with a better budget forecast and resource planning.
Project timeline: Defining an accurate project timeline is very critical for solution implementation. A solution architect determines the resources and effort that are required during the design phase, which should help define the schedule.
Now, you have had a high-level overview of solution architecture and its benefits. Let's dive deep into the everyday aspects of solution architecture.

Addressing the business needs and quality of
delivery
In the life cycle of product development, the most challenging phase is to establish the nature of the requirements, especially when all the elements need to be addressed as high priority, and they keep changing rapidly. This challenge is even worse when there are different views of the same requirement from various stakeholders. For example, a business user analyzes the page design from a user point of view, while a developer is looking at it from implementation feasibility and load latency perspectives. This can cause conflicts and misunderstandings of requirements between functional and technical members. In such cases, solution architecture helps to bridge the gap, and define a standard that all members can understand.

[ 14 ]

The Meaning of Solution Architecture

Chapter 1

Solution architecture defines standard documentation, which can explain the technical aspects to non-technical stakeholders and update them regularly. As a solution architecture's design spans across the organization and different teams, it can help to discover hidden requirements. The solution architect makes sure that the development team knows about the requirements, and also maintains the cycle of progress.
A good solution architecture defines not only the solution design, but also the success criteria in the form of qualitative and quantitative output, in order to ensure the quality of delivery. The qualitative output can be collected from user feedback, such as their sentiment analysis, while quantitative output may include latency, performance, load time at the technical side, and sales numbers at the business side. Taking continuous feedback and adapting to it is the key to high-quality delivery, which should adhere to all the phases of solution design and development.

Selecting the best technology platform
In a rapid and competitive market, the biggest challenge is maintaining the use of the best technologies. Today, when you have multiple resources all around the world, then you have to choose a technology very carefully. The solution architecture design process can effectively tackle this problem.
The selection of the technology stack plays a significant role in efficient solution implementation by the team. In solution architecture, we should use different strategies to adopt various platforms, technologies, and tools. A solution architect should validate all of the needs carefully, and then evaluate and investigate the result with multiple parameters in order to find the best-fit solution for the product development, by creating a working model of the product as a prototype.
A good solution architecture addresses the depth of different tools and technologies by investigating all possible architectural strategies, based on the mixed-use case, techniques, tools, and code reuse, which comes from years of experience. The best platform simplifies the implementation process; however, the right technology selection is very critical. This can be achieved by building a prototype according to the business requirement assessment, and the agility, speed, and security of the application.

[ 15 ]

The Meaning of Solution Architecture

Chapter 1

Addressing solution constraints and issues
Any solution can be limited by various constraints and may encounter issues due to complexities or unforeseen risks. Solution architecture needs to balance multiple constraints, such as resources, technologies, cost, quality, time to market, frequently changing requirements, and so on.
Each project has its own specific goal, requirement, budget, and timeline. Solution architecture evaluates all of the possible critical paths and shares best practices to achieve a project goal in a given timeframe and budget. This is a systematic approach, where all tasks are interdependent of its prior task, and in order to achieve success in the project, all tasks need to execute in sequence. A delay in one task can impact the project timeline and can result in the organization losing the market window to launch the product.
If there is an issue in the project development process, the probability of a project getting delayed is higher. Sometimes, you encounter problems that are limitations of technology or of the solution environment. If you have a well-thought-out solution architecture, the most common issues are related to the non-functional requirements; resources and budgeting can mitigate for the product development life cycle.
A solution architect helps to drive the project by diving deep into each component of the project. They think of an out-of-the-box idea to save the project from the issues, and they will prepare a backup plan in the event that things do not work out as in the main plan. They evaluate the best possible way to execute the project by choosing the best practice and balancing constraints.

Helping in resource and cost management
There are always risks and uncertainties involved during solution implementation. It's very tedious to understand how much time a developer will spend on fixing a bug. A good solution architecture controls the cost and budget and reduces uncertainty by providing developers with the required guidance in terms of priority, different communication services, and details of each component.
Solution architecture also creates documentation for keeping the system up to date, a deployment diagram, software patches, version; and enforces the runbook to solve frequent issues and business continuation processes. It also addresses the indirect impacts of the cost of building a solution by considering extensibility, scalability, and other external factors that matter to the development environment.

[ 16 ]

The Meaning of Solution Architecture

Chapter 1

Managing solution delivery and project life cycle
Lots of planning is involved in the inception stage of solution architecture. Solution architecture starts with a strategic view and provides more technical implementation input as you move forward with the solution implementation.
Solution architecture ensures an end-to-end solution delivery and impacts the overall project life cycle. It defines a process standard for different phases of the project life cycle and makes sure that it is applied across the organization so that other dependencies can be addressed as the implementation moves forward.
Solution architecture considers a holistic view of the project. It keeps syncing other dependent groups such as security, compliance, infrastructure, project management, and support, in order to keep them engaged in different phases of the project life cycle as required.

Addressing non-functional requirements
Often, you have to deal with the non-functional requirements (NFRs) in your application. For project success, it is highly essential to address them, as they have a broader impact on the overall project and solution. These NFRs can make or break your user base, and address very critical aspects of a solution such as security, availability, latency concerns, maintenance, logging, masking confidential information, performance concerns, reliability, maintainability, scalability, usability, and so on. If these are not considered on time, it can impact your project delivery.
The following diagram shows some of the most common NFRs:

[ 17 ]

The Meaning of Solution Architecture

Chapter 1

Non-functional attributes of solution architecture
As shown, NFRs include the following attributes of solution architecture. However, there can be more NFRs, depending upon the project:
Disaster recovery: To make sure the solution is up and running in case of any unforeseen events. Security and compliance: Put a safety net in place for a solution to save it from an external attack, such as a virus, malware, and so on. Also make sure that the solution complies with local and industry laws, by meeting compliance requirements. High availability: To make sure the solution is always up and running.
[ 18 ]

The Meaning of Solution Architecture

Chapter 1

Scalability: To make sure the solution can handle the additional load in case of increasing demands. Application performance: To make sure the application is loading as per user expectation, and without much delay. Network request and response latency: Any activity performing on the application should be completed within the appropriate time and should not time out.
You will learn more details about the preceding attributes in Chapter 3, Attributes of the Solution Architecture. Solution architecture defines an initial framework for product development and the building blocks of the solution. While establishing a solution, architecture, quality, and customer satisfaction are always the main focus. Solution architecture needs to build continuously by working on a proof of concept and keep exploring and testing until the desired quality is reached.

Solution architecture in the public cloud
Solution architecture in the cloud has become increasingly important these days, and it is the future of application solutions. The great thing about cloud computing architecture is that you have an end-to-end view of all architecture components, which include the frontend platforms, the application development platform, servers, storage, database, automation, delivery, and the networks that are required to manage the entire solution landscape.
Before jumping into solution architecture in the cloud, let's understand more about the public cloud, and how it is becoming a more essential and driving technology platform.
What is the public cloud?
A public cloud is a base on the standard computing model in which a service provider makes resources such as virtual machines, applications, storage, and so on, available to their customers over the internet. Public cloud services offer a pay-as-you-go model.
In the cloud computing model, a public cloud vendor provides on-demand availability of IT resources such as the server, database, network, storage, and so on, which organizations can use with secure web-based interfaces, or through application programs over the internet. In most of the cases, the customer only pays for the services that they are applying for the duration of utilization, which saves costs for them by optimizing IT resources to reduce idle time.
[ 19 ]

The Meaning of Solution Architecture

Chapter 1

You can annotate the public cloud with an electric power supply model, where you switch on the light and pay only for the amount of electricity you use in units. As soon as you switch off, you are not paying for it. It abstracts you from the complexity of power generation using turbines, resources to maintain the facility, a large infrastructure setup, and you use the entire service in a simplified way.

Public clouds, private clouds, and hybrid clouds
Here, you will learn about a high-level overview of the different types of cloud computing deployment models. You will learn more details in Chapter 5, Cloud Migration and Hybrid Cloud Architecture Design.
A private cloud, or on-premises, is registered to a single organization that owns and accesses it. Private clouds act as a replicate or extension of the company's existing data center. Often, a public cloud has shared tenancy, which means virtual servers from multiple customers share the same physical server; however, they offer dedicated physical servers to customers if the customer wants it for a license or compliance need. A public cloud such as Amazon Web Services (AWS), Microsoft Azure, or Google Cloud Platform (GCP) creates a massive IT infrastructure, which can be utilized over the internet with a pay-as-you-go model.
A third model is a hybrid cloud, used by large enterprises who are moving their workload from on-premises to a cloud, where they still have a legacy application that cannot move to the cloud directly, or maybe they have a licensed application that needs to stay onpremises, or sometimes due to compliance reasons, they need to secure data on-premises. In such a situation, the hybrid model helps, where the enterprise has to maintain a partial environment on-premises and move other applications to the public cloud. Sometimes an organization moves to test and develop the environment to the public cloud and keep production environments on-premises. A hybrid model can vary depending upon the organization's cloud strategy.

[ 20 ]

The Meaning of Solution Architecture

Chapter 1

The public cloud architecture
In a typical definition, the public cloud is a fully virtualized environment, which is accessible both over the internet or private network lines. However, in recent times, public cloud vendors also started offering an on-premises physical infrastructure for better hybrid cloud adoption. The public cloud provides a multi-tenancy model, where IT infrastructure such as storage and compute are shared between multiple customers; however, they are isolated at the software and logical network levels, and do not interfere with each other's workload. In the public cloud, by creating network-level isolation, organizations can have their virtual private cloud, which is equivalent to the logical data center.
Public cloud storage achieves high durability and availability, by creating a redundancy model using multiple data centers, and robust data replication. This makes them achieve architecture resiliency and easy scalability.
There are three major types of cloud computing model, as shown here:

Type of cloud computing model
[ 21 ]

The Meaning of Solution Architecture

Chapter 1

As shown in the diagram, you can see a comparison between customer responsibilities in the on-premises environment with the cloud computing service model. In on-premises, the customer has to manage everything, while in the cloud computing model, customers can offload responsibilities to the vendor and focus on their business needs. The following points are high-level details of services that are provided under different cloud computing models:
Infrastructure as a Service (IaaS): In the IaaS model, a vendor provides infrastructure resources such as a compute server, networking components, and data storage space as managed services. It helps customers to use IT resources without worrying about handling data center overheads such as heating and cooling, racking and stacking, physical security, and so on.
Platform as a Service (PaaS): The PaaS model adds a layer of service, where the vendor takes care of the resources that are required for your development platform, such as the operating system, software maintenance, patching, and so on, along with infrastructure resources. The PaaS model facilitates your team's focus on writing business logic and handle data, by taking care of all of the platform maintenance burdens for you.
Software as a Service (SaaS): The SaaS model adds one more layer of abstraction on top of the PaaS and IaaS models, where the vendor provides ready-to-use software, and you pay for the service. For example, you use email services such as Gmail, Yahoo! Mail, AOL, and so on, where you get your own space of email as a service, and you don't have to worry about underlying applications or infrastructures.
The fourth emerging model is the Function as a Service (FaaS) model, which is becoming popular in the building of serverless architecture using services including AWS Lambda. You will learn more details about serverless architecture in Chapter 6, Solution Architecture Design Patterns.

Public cloud providers and cloud service offering
There are several public cloud providers in the IT industries; among them, key players are AWS, GCP, Microsoft Azure, and Alibaba Cloud. These providers offer an array of services, from computing, storage, networking, databases, and application development, to big data analytics and AI/ML, and so on.

[ 22 ]

The Meaning of Solution Architecture

Chapter 1

In the following screenshot from the AWS console, you can see 100+ services that are offered in multiple areas. The highlighted EC2 service, known as Amazon Elastic Cloud Compute, allows you to spin-up the virtual machine in minutes in the AWS cloud:

AWS console and service offerings
Public cloud vendors not only provide infrastructure, but also facilitate an array of services in various areas such as analytics, big data, artificial intelligence, application development, email, security, monitoring, alert, and so on. With the public cloud, different technical capabilities become more accessible to the development team, which helps to drive innovation and reduce the time to market for the product launch.
[ 23 ]

The Meaning of Solution Architecture

Chapter 1

Summary
In this chapter, you learned about the definition of solution architecture from both the industry standards and in a more simplified way. You learned the importance of solution architecture, and how it can help the organization to achieve a more significant result and maximize the return on its investments. This chapter helped you to understand the benefits of having a solution architecture, and how it helps in different aspects of solution design and implementation.
In summary, solution architecture is a building block in a complex organization and is used to address all stakeholder's needs and establish a standard in order to fill the gap between business requirements and technical solutions. A good solution architecture not only addresses functional requirements but also puts long-term thought into, and takes care of, non-functional requirements such as scalability, performance, resiliency, high availability, disaster recovery, and so on. Solution architecture finds an optimal solution to accommodate the constraints of cost, resources, timelines, security, and compliance.
Later in the chapter, you learned about the basics of cloud computing, solution architecture in the cloud environment, and about significant public cloud providers and their service offerings. This also helped you to gain a high-level overview of different cloud computing models, such as IaaS, PaaS, SaaS, and the cloud computing deployment models in the public cloud, private cloud, and hybrid cloud. Finally, this chapter sheld some light on the evolution of solution architecture design.
In the next chapter, you will learn all about the solution architecture role � the different types of solution architect, the role's responsibilities as regards solution architecture, and how they fit into an organizational structure and an agile environment.

[ 24 ]

2
Solution Architects in an
Organization
A solution architect understands the needs and goals of an organization. Often, solution architects work for the organization as part of a team. All stakeholders, processes, teams, and organization management affect solution architect roles and their work. In this chapter, you will learn and understand the solution architect role and how solution architects fit within the organization. Following that, you will learn about the various types of solution architect and how they coexist in an organization. You may need a generalist solution architect and other specialist solution architects, depending on your project's complexity.
This chapter will provide details on the solution architect's responsibility and how it can impact an organization's success. A solution architect wears multiple hats and business executives heavily depend on their experience and decision-making to understand their technical vision.
The solution-and-software development methodology has evolved over the last few decades, from waterfall to agile environment, which a solution architect needs to adopt. This chapter will provide details about the Agile methodology and the iterative approach that a solution architect should take for the continuous improvement of solution delivery. Overall, agile thinking is very important for a solution architect.

Solution Architects in an Organization

Chapter 2

In addition to solution design, solution architects need to handle various constraints to evaluate risk and plan risk mitigation. Also, quality management plays a significant role, which shouldn't be overlooked. The solution architect plays an essential role throughout the solution's life cycle (from requirement collection, solution design, and solution implementation to testing and launch).
A solution architect needs to engage regularly post-launch to ensure the scalability, high availability, and maintainability of the solution. For broader consumer products, the solution architect also needs to work with the sales team as a technology evangelist of the product through content publishing and public speaking in various forums.
In this chapter, you will learn about the following topics:
Types of solution architect role Solution architect responsibilities Solution architects in an agile organization

Types of solution architect role
In the previous chapter, you learned about solution architecture and how various stakeholders impact solution strategies. Now, let's understand the solution architect's role. The software solution can develop without a solution architect, depending on the project's size, but for a large project, it is a requirement to have a dedicated solution architect. The success and failure of the plan depends on the solution architect.
There is always a need for someone who can make architectural decisions for the team and drive team collaboration with stakeholders. Sometimes, it is required to have multiple solution architects in the team, depending on the size of the project.
The different types of solution architects are depicted in the following diagram, showing how they have different self-differentiating responsibilities in the organization:

[ 26 ]

Solution Architects in an Organization

Chapter 2

Types of solution architect
As shown in the preceding diagram, an organization can have multiple types of solution architects. Solution architect can be categorized as generalists or specialists. Generalist solution architects have the breadth that comes from multiple technical domains. Specialist solution architects have very in-depth knowledge in their area of expertise, such as big data, security, and networking. A generalist solution architect needs to collaborate with a specialist solution architect, to align with project's requirements and complexity.
[ 27 ]

Solution Architects in an Organization

Chapter 2

The role of a solution architect varies from organization to organization and you may encounter a variety of job titles related to solution architect, the most common being generalist solution architect roles. Their focuses are as follows:
Enterprise solution architect: Organization strategy Business architecture
Solution architect: Solution design Solution integration
Technical architect: Software design Software development
Cloud architect: Cloud strategy Cloud migration
Architect evangelist: Platform adoption Technical content

There may be other titles (such as application architect and software architect); however, this depends on the organization's structure.
Specialist solution architect roles are as follows:
Infrastructure architect: IT infrastructure design Software standardization and patching
Network architect: Network design IT network strategy and latency
Data architect: Data engineering and analysis Data science and data intelligence

[ 28 ]

Solution Architects in an Organization

Chapter 2

Security architect: Cyber security IT compliance
DevOps architect: IT automation Continuous integration and continuous deployment (CI/CD)

There may be other types of specialist solution architect, such as migration architect and storage architect. This, again, depends on the organization's structure. As per the project and organizational complexity, a solution architect can take on multiple roles or different solution architects can have overlapping responsibilities. You will learn more about each architect role in subsequent sections.

Enterprise solution architect
Do you ever think about how products launch in the information technology industry? This is where the enterprise solution role comes into the picture � they define best practices, culture, and suitable technologies. An enterprise architect works closely with stakeholders, subject matter experts, and management to identify organizational strategies for information technology and make sure that their knowledge aligns with company business rules.
Enterprise architects handle solution design across the organization; they create long-term plans and solutions with stockholders and leadership. One of the most important aspects is to finalize which technologies should be used by the company and making sure the company is using these technologies with consistency and integrity.
Another important aspect of the enterprise architect is defining the business architecture. In some organizations, you may see a business architect as the job title. Business architecture fills the gap between organizational strategy and its successful execution. It helps convert a map strategy into executable action items and takes this to a tactical level for implementation.
Overall, enterprise architects are more aligned with company visions and responsibilities when it comes to defining organization-wide standards for the successful implementation of the business' vision.

[ 29 ]

Solution Architects in an Organization

Chapter 2

Solution architect
In general, this book explores the role of a solution architect in a more generic way. Still, you often see solution architects with different titles, as per the organization's structure, for example, enterprise solution architect, software architect, or technical architect. In this section, you will find some distinct attributes related to the various titles. However, the responsibilities of the solution architect overlap, depending on an organization's structure.
If you wish to know how a solution should be organized and delivered, then a solution architect plays an essential role in this context. A solution architect designs the overall system and how different systems integrate across different groups. A solution architect defines the expected outcome by working with business stakeholders and providing a clear understanding of the delivery objective on the part of the technical team.
The solution architect connects the dots across the organization and ensures consistency within different teams to avoid any last-minute surprises. The solution architect engages throughout the project life cycle and also defines monitoring and alerting mechanisms to ensure smooth operations after a product's launch. The solution architect also plays an essential role in project management by providing advice regarding resource, cost, and timeline estimation.
Overall, the solution architect gets to engage on a more tactical level compared to the enterprise architect. Sometimes, the solution architect takes on the role of an enterprise architect if a more strategic involvement is required.

Technical architect
A technical architect can also be called application architect or software architect. A technical architect is responsible for software design and development. The technical architect works with the organization in terms of engineering and is more focused on defining technical details for software development by a team. They also work across the organization to understand how integration will work alongside other parts of the software module, which may be managed by other groups.
A technical architect can manage the details of API design and define API performance and scaling aspects. They make sure that the software is being developed consistently with the organization's standards and that they can easily integrate with another component.

[ 30 ]

Solution Architects in an Organization

Chapter 2

The technical architect is a point of contact for any technical question related to the engineering team and will have the ability to troubleshoot the system as required. For a small software development project, you may not see a technical architect role, as a senior engineer may take up that role and work on software architecture design.
The technical architect mentors and supports the software engineering team by working closely with them and resolving any hindrance that arises from cross-team integration or business requirements.

Cloud architect
The cloud architect role may not have been in existence within the last decade, but as cloud adoption is increasing among enterprises this is one role that is in high demand in the current scenario. The cloud architect plans and designs the cloud environment and is responsible for deploying and managing the company's cloud computing strategies. Cloud architects provide breadth and depth for cloud services and can define the cloud-native design.
As you learned in the Solution architecture in the public cloud section in Chapter 1, The Meaning of Solution Architecture, using the cloud is now the current trend and it has become the norm for organizations to move onto a public cloud. Major cloud providers such as Amazon Web Service, Microsoft Azure, and Google Cloud Platform are helping customers to adopt cloud platforms at exponential speed with Software as a Service (SaaS), Platform as a Service (PaaS), and Infrastructure as a Service (IaaS) offerings. You will learn more about cloud architectures in Chapter 5, Cloud Migration and Hybrid Cloud Architecture Design.
There are a large number of enterprises that have an existing workload that they want to migrate into the cloud to utilize scalability, ease of business, and price benefits. A cloud architect can prepare a cloud migration strategy and develop a hybrid cloud architecture. A cloud architect can advise how on-premise applications will connect to the cloud and how different traditional offerings fit into a cloud environment.
For startup businesses and enterprises starting in the cloud, a cloud architect can help to design a cloud-native architecture, which is more optimized for the cloud and uses the full capabilities it provides. The cloud-native architecture tends to be built on pay-as-you-go models to optimize cost and leverage automation available in the cloud.
Cloud is now an essential part of enterprise strategy, and a cloud architect is a must-have role of companies want to succeed in the modern era by increasing the pace of innovation and automation.
[ 31 ]

Solution Architects in an Organization

Chapter 2

Architect evangelist
An architect evangelist is also known as a technology evangelist, and this is a comparatively new role. This is a new paradigm in marketing, especially when you want to increase the adoption of complex solution platforms. People will always want to hear from an expert who has in-depth knowledge and the ability to answer their queries so that they can make an informed decision. Here, architect evangelists come into the picture as they work as a subject matter expert in a competitive environment.
An architect evangelist can design the architecture based on customer requirements, which resolves the customer's pain points, and results in the customer wins. The evangelist can be a trusted advisor for customers and partners. The architect evangelist has a deep understanding of architectural issues, concepts, and market trends to help secure platform adoption and show revenue growth through market capture.
To increase platform adoption for the overall target audience, the architect evangelist writes public content such as blogs, whitepapers, and articles. They speak on public platforms such as industry summits, technical talks, and conferences. They conduct technical workshops and publish tutorials to spread the word about the platform. This makes it very important for a solution architect to have excellent written and verbal communication skills, as you will often see solution architects taking technology evangelism as an additional responsibility.

Infrastructure architect
An infrastructure architect is a specialist architect role heavily focused on enterprise IT infrastructure design, security, and data center operation. They work closely with solution architects to make sure that the organization's infrastructure strategy is aligned with its overall business requirements, and they plan an appropriate resource capacity to fulfill this need by analyzing system requirements and the existing environment. They help reduce capital expenditure that could be utilized for operational spending to increase organizational efficiency and ROI.
The infrastructure architect is the backbone of the organization since they define and plan overall IT resources, from storage servers to individual workspaces. The infrastructure architect creates detailed plans for procuring and setting up IT infrastructures. They define software standards, software patching, and software update plan systems across an organization. The infrastructure architect handles infrastructure security and makes sure all environments are protected from unwanted virus attacks. They also plan for disaster recovery and system backups to make sure business operations are always running.

[ 32 ]

Solution Architects in an Organization

Chapter 2

In most e-commerce businesses, infrastructure architect jobs become challenging as they need to plan for the peak season such as Thanksgiving in USA, Boxing Day in Canada and UK, Diwali in India and so on, when most consumers start shopping. They need to prepare enough server and storage capacity to accommodate the peak season, whose workload may be 10 times higher than normal, thus increasing the cost. A system will be sitting idle for most of the year, outside of the peak season. They need to plan for cost optimization and better user experience at the same time, which is another reason they may use the cloud to fulfill additional capacity and scale on-demand to reduce the cost. They need to ensure that systems are occupied while supporting the growth of the new expertise.
Overall, an infrastructure architect needs to have a good understanding of data center operation and the components involved, such as heating, cooling, security, racking and stacking, server, storage, backup, software installation and patching, load balancers, and virtualization.

Network architect
Have you ever wondered how giant enterprises with multiple locations for offices or stores are connected? Here, the network architect comes into the picture, as they orchestrate an organization's network communication strategy and establish communication between IT resources, giving life to the IT infrastructure.
A network architect is responsible for designing the computer network, Local Area Network (LAN), Wide Area Network (WAN), internet, intranet, and other communication systems. They manage organizational information and network systems. They ensure low network latency and high network performance is available for users to increase their productivity. They establish secure connectivity between user workspaces and the internal network using Virtual Private Network (VPN) connectivity.
The network architect works closely with the infrastructure architect and sometimes you see this as an overlapping role to ensure all IT infrastructures are connected. They work with the security team and design the organization's firewall to protect against unethical attacks. They are responsible for monitoring and protecting the network via packet monitoring, port scanning, and putting Intrusion Detection System (IDS) and Intrusion Prevention System (IPS) into place. You will learn more about IDS/IPS systems in Chapter 8, Security Considerations.
Overall, a network architect needs to have a good understanding of network strategies, network operations, secure connections using VPN, firewall configuration, network topology, load balance configuration, DNS routing, IT infrastructure connectivity, and so on.
[ 33 ]

Solution Architects in an Organization

Chapter 2

Data architect
Any solution design revolves around data, and it is mostly about storing, updating, and accessing it regardless of whether it is about customers or products. As the adoption of the internet is increasing, so are data and the need for data architects. In the last decade, data growth has risen exponentially � not long ago, gigabytes of data were considered to be big data, but now even 100 terabytes of data are deemed to be normal. You can even get a 1terabyte computer hard disk.
Traditionally, data used to be stored in a structured relational way. Now, most data are in an unstructured format generated from resources such as social media, Internet of Things (IoT), and application logs. There is a need to store, process, and analyze data to get useful insights, where the data architect role comes into the picture.
The data architect defines a set of rules, policies, standards, and models that govern the type of data that's used and collected in the organization database. They design, create, and manage the data architecture in an organization. A data architect develops data models and data lake designs to capture business's key performance indicators (KPIs) and enable data transformation. They ensure consistent data performance and data quality across the organization.
The primary customers for a data architect are as follows:
Business executives using Business Intelligence (BI) tools for data visualization Business analysts using a data warehouse to get more data insight Data engineers performing data wrangling using Extract, Transform, and Load (ETL) jobs Data scientists for machine learning Development teams for application data management
To fulfill organizational needs, the data architect is responsible for the following:
Selection of database technology A relational database schema for application development Data warehousing for data analysis and BI tools Data lake as the centralized datastore Datamart design Machine learning tools Data security and encryption Data compliance

[ 34 ]

Solution Architects in an Organization

Chapter 2

You will learn more about data architectures in Chapter 13, Data Engineering and Machine Learning. Overall, the data architect needs to be aware of different database technologies, BI tools, data security, and encryption to make the right selection.

Security architect
Security should be the top priority for any organization. There are multiple instances when large and well-established organizations went out of business due to a security breach. Organizations not only lose customer trust but also experience legal complications due to security incidents. There are various industry compliance certifications, such as Organizational Security (SOC2), Finance Data (PCI), and HealthCare data (HIPPA), that are in place to ensure organization and customer data security, which a company needs to adhere to as per the nature of their application.
Looking at the critical nature of security, organizations need to research and design the most robust security architecture for their projects, and that's where a security architect is necessary. A security architect works closely with all groups and solution architects to make sure security is a high priority. A security architect's responsibilities include the following:
Designing and deploying the implementation of the network and computer security in the organization. Understanding the company's technology, and information systems, and safeguarding the security of the computers in the organization. Working with a variety of settings, such as securing company networks and websites. Planning vulnerability testing, risk analysis, and security audits. Reviewing and approving the installation of a firewall, VPN, and router, and scanning the server. Testing final security processes and making sure they work as expected. Providing technical guidance to the security teams. Making sure applications comply with industry standards as required. Making sure data is secure with the required accessibility and encryption.
Security architects are expected to understand, design, and guide all aspects of security related to data, network, infrastructure, and applications with a variety of tools and techniques. You will learn more about security and compliance in Chapter 8, Security Considerations.

[ 35 ]

Solution Architects in an Organization

Chapter 2

DevOps architect
As a system gets complex, there are more chances of human error, which can lead to additional effort being needed, increased cost, and reduced quality. Automation is the best way to avoid failure and improve overall system efficiency. Now automation is not an optional choice--if you want to be agile and move faster, automation is a must.
Automation can be applied anywhere, whether it is testing and deploying applications, spinning up infrastructure, and even ensuring security. Automation plays a critical role, and a DevOps architect automates everything everywhere. DevOps is a combination of practices and tools that assist in delivering an application at a faster pace.
It allows the organization to serve its customers better and stay ahead of the competition. In DevOps, model- development team and operational teamwork together in sync. For a software application, a DevOps architect defines continuous integration and continuous delivery (CI/CD). In CI, automated builds and test runs happen before the development team merges its code changes into a central repository. CD expands upon continuous integration by deploying all code changes to a production environment after the build and test stage.
The DevOps architect automates infrastructure deployment, known as Infrastructure as a code, which is highly prevalent in the cloud environment. DevOps can utilize tools such as Chef and Puppet for instructed automation or use cloud-native tools if the workload is in a cloud environment. Infrastructure automation provides excellent flexibility for the development team for experimentation and enables the operations team to create replica environments.
For smooth operation, a DevOps architect plans monitoring and alerting with automated communication in the event of issues or any significant changes. Any security incidents, deployment failures, or infrastructure failures can be monitored automatically, and alerts can be sent via mobile or email to the respective team when required.
The DevOps architect also plans for disaster recovery different deployment methods. Organizational Recovery Point Objective (RPO) is the volume of data loss that an organization can tolerate. Recovery Time Object (RTO) suggests how much time the application can take to recover and start functioning again. You will learn more about DevOps in Chapter 12, DevOps and Solution Architecture Framework.

[ 36 ]

Solution Architects in an Organization

Chapter 2

Understanding a solution architect's
responsibilities
In the previous section, you learned about the role of a solution architect, the different types of architect in an organization, and how they coexist. In this section, you will learn more details about the responsibilities of a solution architect. A solution architect is a technical leader, and a customer-facing role, which comes with many responsibilities. The primary responsibility of a solution architect is to convert organization business visions into a technical solution and work as a liaison between businesses and technical stakeholders. A solution architect uses broad technology expertise and business experience to ensure the success of the solution's delivery.
A solution architect's responsibilities may differ slightly based on the nature of the organization. Often, in a consulting organization, a solution architect may be dedicated to a particular project and customer, while in a product-based organization, a solution architect may be working with multiple customers to educate them on a product and review their solution design. Overall, a solution architect holds the following primary responsibilities:

Solution architect's responsibility model
[ 37 ]

Solution Architects in an Organization

Chapter 2

As shown in the preceding diagram, there are various significant responsibilities for a solution architect. In upcoming sections, you will learn about the various aspects of the solution architect's responsibilities.

Analyzing user requirements
Business requirements are at the center of any solution design and they are defined in raw terms when a project starts. It is necessary to engage a diverse set of groups from the beginning, which includes the technical capability to identify requirements. The business stakeholder defines requirements, and it warrants multiple adjustments when it comes to technological evolution. To save effort, it is necessary to engage solution architects while defining the user requirement document.
The solution architect designs the application, which may impact the overall business outcome. This makes requirement analysis a critical skill that a solution architect should possess. A good solution architect needs to have the skills of a business analyst and the ability to work with a diverse set of stakeholders.
Solution architect bring a broad range of business experience with them. They are not only technical experts but also have a good knowledge of the business domain. They work closely with the product manager and other business stakeholders to understand all the aspects of requirements. A good solution architect helps the product team uncover hidden requirements, which a non-technical stakeholder may not have thought about from an overall solution perspective.

Defining non-functional requirements
Non-functional requirements (NFR) may not be visible to users and customers directly, but their absence may impact the overall user experience in a negative way and hamper the business. NFR includes critical aspects of the system, such as performance, latency, scalability, high availability, and disaster recovery. The most common non-functional requirements are shown in the following diagram:

[ 38 ]

Solution Architects in an Organization

Chapter 2

NFRs in a solution design
The preceding diagram shows the following NFRs for consideration: Performance: What will be the application load time for users? How can we handle network latency?
Security and compliance: How can we secure an application from unauthorized access? How can we protect an application from malicious attacks? How can we meet local laws and audit requirements?
Recoverability: How can we recover an application from an outage? How can we minimize recovery time in the event of an outage? How can we recover data loss?
[ 39 ]

Solution Architects in an Organization

Chapter 2

Maintainability: How can we ensure application monitoring and alerts?
How can we ensure application support?

Reliability: How can we make sure the application performs consistently?
How can we inspect and correct glitches?

Availability: How can we ensure the high availability of an application?
How can we make an application fault-tolerant?

Scalability: How can we meet the increasing demand for resources?
How can we achieve a good scale for a sudden spike in utilization?

Usability:

How can we simplify an application's use? How can we achieve a seamless user experience?

However, depending on the nature of the project, there may be an NFR that is suitable for that project only (for example, voice clarity for a call center solution). You will learn more about these attributes in Chapter 3, Attributes of the Solution Architecture.
The solution architect becomes engaged in a project from a very early stage, which means they need to design a solution by gauging requirements across groups in an organization. The solution architect needs to ensure consistency in solution design across system components and requirements. The solution architect is responsible for defining NFR across groups and different components since they make sure that the desired usability of a solution is achieved across the board.
NFRs are an integral and essential aspect of solution design, which tends to slip when teams are too focused on business requirements, and this can impact the user experience. A good solution architect has the primary responsibility of conveying the importance of NFR and making sure they are implemented as part of solution delivery.

[ 40 ]

Solution Architects in an Organization

Chapter 2

Engaging and working with stakeholders
Stakeholders could be anyone who has a direct or indirect interest in the project. As well as the customer and user, it may also be the development team, sales, marketing, infrastructure, network, support team, or the project funding group.
Stakeholders could be internal or external to the project. Internal stakeholders include the project team, sponsors, employees, and senior management. External stakeholders include customers, suppliers, vendors, partners, shareholders, auditors, and the government.
Often, stakeholders have a different understanding of the same business problem as per their context; for example, a developer may look at a business requirement from a coding perspective, while an auditor may look at it from a compliance and security perspective. A solution architect needs to work with all technical and non-technical stakeholders.
They possess excellent communication skills and negotiation techniques which help to find out the optimal path for a solution while keeping everyone on board. A solution architect works as a liaison between technical and non-technical resources and fills the communication gap. Often, those communication gaps between a businessperson and the technical team become a reason for failure. The businessperson tries to look at things from more of a feature and functionality perspective, while the development team strives to build a more technically compatible solution, which may sometimes lean toward the nonfunctional side of the project.
The solution architect needs to make sure both teams are on the same page and that the suggested features are also technically compatible. They mentor and guide the technical team as required and put their perspective into a simple language that everyone can understand.

Handling various architecture constraints
Architecture constraints are one of the most challenging attributes of solution design. A solution architect needs to manage architectural constraints carefully and be able to negotiate between them to find an optimal solution. Often, these constraints depend on each other, and emphasizing on one limitation can inflate others.

[ 41 ]

Solution Architects in an Organization The most common constraints are as following:

Chapter 2

Architectural constraints in a solution design

As shown in the preceding diagram, solution design helps us understand the following attributes of an application:

Cost:

How much funding is available for solution implementation? Expected Return on Investment (ROI)?

Quality:

How closely should outcomes match functional and non-functional requirements?
How can we ensure and track the quality of the solution?

Time:

When should the output be delivered? Is there any flexibility regarding time?

[ 42 ]

Solution Architects in an Organization

Chapter 2

Scope:

What is the exact expectation?
How does the requirement gap need to be handled and accommodated?

Technology: What technology can be utilized?
What flexibility does using legacy versus new technologies provide?
Should we build in-house or source from a vendor?

Risk: Resource:

What can go wrong and how can we mitigate that? What is the risk tolerance of stakeholders?
What is required to complete solution delivery? Who will work on the solution's implementation?

Compliance: What are the local law requirements that can impact the solution?
What are the audit and certification requirements?

There could be more specific constraints related to a project, such as storing data in a country due to government regulation and opting for in-house development due to security concerns. Handling constraints could be very tricky. Saving costs by reducing resources may impact the delivery timeline.
Achieving a schedule with limited resources may affect quality, which in turn increases cost due to unwanted bug fixes. So, finding the balance between cost, quality, time, and scope is significant. Scope creep is one of the most challenging situations as it can negatively impact all other constraints and increase risks of solution delivery.
It is essential for a solution architect to understand all the aspects of every constraint and to be able to identify any resulting risk. They must put risk mitigation plans into place and find a balance between them. Handling any scope creep can help a lot in delivering the project on time.

[ 43 ]

Solution Architects in an Organization

Chapter 2

Making technology selections
Technology selection is the key aspect and complexity of the solution architect's role. There is a broad range of technologies available, and a solution architect is required to identify the right ones for the solution. The solution architect needs to have a breadth and depth of technologies to make the right decision since the chosen technology stack can impact the overall delivery of the product.
Each problem can have multiple solutions and an available range of technologies. To make the right selection, a solution architect needs to keep functional requirements and NFRs in mind and define selection criteria while creating a technology decision. The selected technology needs to consider different perspectives, whether the goal is the ability to integrate with other frameworks and APIs or to meeting performance requirements and security needs.
A solution architect should be able to choose the technology that not only satisfies current requirements but also scaling for future needs.

Developing a proof of concept and a prototype
Creating a prototype is probably the most fun part of being a solution architect. To choose a proven technology, a solution architect needs to develop a proof of concept (POC) in various technology stacks to analyze their fit for functional and non-functional requirements for the solution.
The idea of developing POC is to evaluate technology with a subset of critical functional implementations, which can help us to decide on technology stack based on their capabilities. It has a short life cycle and is limited to being reviewed by experts within a team or organization. The solution design POC is when a solution architect is trying to figure out the building blocks of the solution.
After evaluating multiple platforms using POC, the solution architect may proceed with prototyping to a technology stack. A prototype is developed for demonstration purposes and given to the customer so that it can be used to secure funding. POCs and prototyping are by no means production-ready; solution architect builds have limited functionality, which can prove a challenging aspect of solution development.

[ 44 ]

Solution Architects in an Organization

Chapter 2

Designing solutions and staying through delivery
Solution architects work on solution design after understanding different aspects of functional requirements, NFRs, solution constraints, and technology selection. In an agile environment, this is an iterative approach where the requirements may change over time and need to accommodate the solution design.
The solution architect needs to design a future-proof solution, which should have strong building blocks and be flexible enough to adjust to changes. However, the solution architect needs to be careful about drastic changes to the requirements and apply a risk mitigation plan.
For future-proof design, you can take the example of a loosely coupled microservice architecture based on RESTful APIs. These architectures can be extendable to new requirements and have the ability to integrate easily. You will learn more about different architecture designs in Chapter 6, Solution Architecture Design Patterns.
The following flow-chart shows the solution delivery life cycle. The solution architect is involved in all the phases of solution design and delivery:

Solution delivery life cycle
As shown in the preceding diagram, the solution delivery life cycle includes the following: Business Requirement and Visions: A solution architect works with business stakeholders to understand their vision. Requirement Analysis and Technical Vision: A solution architect analyzes the requirements and defines a technical vision in order to execute the business strategy.
[ 45 ]

Solution Architects in an Organization

Chapter 2

Prototyping and Recommendation: A solution architect makes a technology selection by developing POC and showcase prototypes. Solution Design: A solution architect develops solution designs in line with an organization's standards and in collaboration with other impacted groups. Development: A solution architect works with the development team on solution development and works as a bridge between the business and technical team. Integration and Testing: A solution architect makes sure that the final solution is working as expected with all functional and non-functional requirements. Implementation: A solution architect works with the development and deployment team for smooth implementation and guides them through any hindrances. Operation and Maintenance: A solution architect makes sure logging and monitoring are in place and guides the team on scaling and disaster recovery as required.
However, the overall life cycle is an iterative process. Once the application goes into production and customers start using it, you may discover more requirements from customer feedback, which will drive the product vision for future enhancements.
The solution architect has major ownership during solution design in which they do the following:
Document solution standards Define high-level design Define cross-system integration Define different solution phases Define an implementation approach Define a monitoring and alert approach Document the pros and cons of design choices Document audit and compliance requirement
Solution architects are not only responsible for solution design. They also help project managers with resource and cost estimation, defining the project's timeline and milestones, the project's release, and its support plan. The solution architect works through different phases of the solution life cycle, from design to delivery and launch. The solution architect helps the development team overcome obstacles and hurdles by providing expertise and a broad understanding.

[ 46 ]

Solution Architects in an Organization

Chapter 2

Ensuring post-launch operability and maintenance
The solution architect plays an integral role after the solution's launch in respect of product operability. To handle the increasing user base and product utilization, a solution architect should know how to scale the product to meet demands and ensure high availability without impacting the user experience.
In unforeseen events such as outages, a solution architecture guides you to execute a disaster recovery plan for business process continuation. The solution architect satisfies organization Recovery Point Objectives (RPO) and Recovery Point Objectives (RTO). RPO is how much data loss an organization can tolerate in terms of the volume of data which is lost during the outage interval-- for example, a loss of 15 minutes of data. RTO is how much time the system takes to get back up and running again. You will learn more about RTO and RPO in Chapter 12, DevOps and Solution Architecture Framework.
In the event of performance issues due to an increase in demand, the solution architect helps scale the system horizontally to mitigate application bottlenecks or vertically to alleviate database bottlenecks. You will learn more about different scaling mechanisms and self-healing in Chapter 9, Architectural Reliability Considerations.
The solution architect plans to accommodate any new requirements in an existing product that arise from usage patterns, or due to any other reason. They can make changes to nonfunctional requirements based on monitoring user behavior; for example, users bounce off the page if it takes more than 3 seconds to load. The solution architect works through this and guides the team in handling issues that may occur post-release.

Working as a technology evangelist
An evangelist is the most exciting part of the solution architect role where they work as a technology evangelist. The solution architect increases product and platform adoption by spreading the word through public forums. They write blogs about solution implementation and conduct workshops to showcase potential benefits and the use of technology platforms.
They build mass support for technologies and help establish a standard. A solution architect should be passionate about technology. They should be an excellent public speaker and possess excellent writing skills to perform the technology evangelist role.

[ 47 ]

Solution Architects in an Organization

Chapter 2

Solution architects in an agile organization
In the last half decade, you may have seen the rapid adoption of the Agile methodology. In this competitive market, an organization needs to be proactive toward rapid changes and bring output to the customer a very fast. Fast innovation and release can only be possible if organizations are adapting quickly and respond to change faster, which means there must be flexibility built into every part of the organization and solution architecture.
To be successful in an agile environment, a solution architect needs an agile mindset and must adopt the rapid delivery method by continuously working with stakeholders to fulfill their needs. First, let's understand a little bit more about the Agile methodology. This is a vast topic, and in this section, we will take a high-level overview of it.

Why Agile methodology?
Agile can create and respond to changes to make a profit in a fast-moving business environment. Its agility comes from balancing flexibility and stability. In today's competitive environment, where technology is moving fast (which results in a high probability of changes and customer demand), agile is the answer to coping with the situation and gaining a competitive edge.
Nowadays, all successful organizations are customer driven. They take frequent feedback from end users on their products and use that feedback to expand their user base. Agile helps gather results from the development team to continuously adapt feedback into software releases, and most of the time everything has a high priority. To deal with this situation, you need agile.
Executive management provides funding and looks for transparency. They demand productive output to increase ROI, and you want to win their confidence by showing incremental development of the product. To create transparency for a project and keep track of its budget and delivery timeline, you need agile.
When you continuously want to engage your stakeholders by showing them a demonstration of the product, and when development and testing are part of the same cycle, you need Agile methodology.
In the preceding scenarios, you looked at various situations where the Agile methodology is required to keep the organization ahead with robust delivery and customer feedback.

[ 48 ]

Solution Architects in an Organization

Chapter 2

Agile is able to quickly move in a time box manner, which means you time box activities in a short cycle and take an iterative approach for product development instead of working on the entire product to develop and deliver it at once. The agile method advocates seeking continuous feedback by keeping customers and stakeholders engaged closely, involving them in every phase of product development, adapting feedback into requirements, evaluating market trends, and working with them to prioritize the stakeholders. Then, the development team take up the prioritized requirements, conduct technical analyses, design, develop, test, and deliver.
Everyone works as one team toward one goal and breaks the silo mindset. Agile thinking helps the technical team understand the requirements from the customer's perspective and respond to changes quickly and efficiently. This is the reason why most companies want to go agile. The Agile methodology is fast and easy to adopt using many tools that are available on the market, such as JIRA, VersionOne, and Rally. You may face some initial challenges while developing agile thinking, but the benefits are very high compared to the challenges that every organization faces when moving toward adopting the Agile methodology.

Agile manifesto
Applying any agile method requires a clear understanding of the four values stated in the Agile manifesto. Let's understand these manifestos:
Individuals and interactions over processes and tools: Processes and tools always help complete the project. Project stakeholders, who are a part of the project, know how to implement the plan and how to deliver the successful result with the help of tools for project delivery. But the primary responsibility for project delivery is the people and their collaboration. Working software over comprehensive documentation: Documentation is always an essential process for any product's development. In the past, many teams only worked to collect and create a repository for documents such as highlevel design, low-level design, and design change, which later help achieve qualitative and quantitative descriptions of the product.
With the Agile methodology, you focus on the deliverable. Therefore, according to this manifesto, you need documentation. However, you need to define how much documentation is vital to the continuous delivery of the product. Primarily, the team should focus on delivering software incrementally throughout the product's life cycle.

[ 49 ]

Solution Architects in an Organization

Chapter 2

Customer collaboration over contract negotiation: Earlier, when organizations worked on a fixed bid or time & material projects, the customer always came in the first and the last stages of the software life cycle. They were outsiders who were not involved in product development; by the time they finally got a chance to see the product after launch, the market trends had changed, and they lost the market.
Agile believes that customers share equal responsibility for the product's launch and that they should be involved in every step of development. They are part of demonstrating giving feedback based on new market trends or consumer demand. Since the business is now part of the development cycle, these changes can be attainable by being agile and having continuous customer collaboration.
Responding to change when following a plan: In the current fast-paced market in which customers demand change with new market trends, businesses keep on changing. It is vital to make sure there's a balance between frequently changing the requirements and agilely welcoming the changes since sprint cycles vary from 1 to 3 weeks. Responding to change means that if, anything changes in the specification, the development team will accept the change and show the deliverable in sprint demonstrations to keep winning the confidence of the customers. This manifesto helps the team understand the value of welcoming changes.
The Agile Manifesto is a tool that's used to establish basic guidelines for adopting an agile methodology. These manifestos are the core of all agile techniques. Let's understand the agile process in more detail.

Agile process and terminology
Let's get familiar with the most common agile terminologies and how they bind together. Here, you will learn about the agile scrum process, which is widely adopted. The agile scrum process has a small sprint cycle of 1 to 3 weeks, depending on the project's stability, but the most common is a 2-week sprint cycle, which you can call a development cycle.
These sprints are development cycles where the team will analyze, develop, test, and deliver a working feature. The team takes an iterative approach and creates a working building block of the product as the project progresses with each sprint. Each requirement is written as a user story that keeps a customer persona in mind, and makes the requirement clearly visible.

[ 50 ]

Solution Architects in an Organization

Chapter 2

The agile scrum team has varied roles. Let's understand the most common roles and how the solution architect collaborates with them:
Scrum Team: This consists of the Product Owner, Scrum Master, and development team. Analysts, technical architects, software engineers, software testers, and deployment engineers are part of the development team.
Scrum Master: This facilitates all scrum ceremonies (which you will learn in next section), keeps the team motivated, and removes impediments for the team. The Scrum Master works with the solution architect to remove any technical blockers and get technical clarification for business requirements.
Product owner: This is a businessperson who is a customer advocate. The product owner understands market trends and can define priorities within the business. The solution architect works with the product owner to understand the business' vision and keep it aligned with the technical view.
Development team: They do product implementation and are responsible for the project's delivery. They are a cross-functional team that is committed to continuous and incremental delivery. The solution architect needs to work closely with the development team for smooth product implementation and delivery.

Sprint ceremonies
The sprint cycle includes multiple activities that are performed to manage development, which are often called scrum ceremonies. Those scrum ceremonies are as follows:
Backlog grooming: Grooming is a time-box meeting in which the product owner, solution architect, and business connect to discuss backlog stories, prioritize them, and create a consensus for sprint deliverables. Sprint planning: In sprint planning, the Scrum Master facilitates groomed stories being assigned to the scrum team based on the team's capacity. Sprint Daily Standup: Daily Standup is a very efficient way of collaboration, where all team members meet in one place, and all discuss their last day workload, what plans they have for today, and whether they are facing any problems. This meeting is meant to be short and straightforward and around 15 minutes in length. Standup is the platform that the solution architect uses to collaborate with the development team.

[ 51 ]

Solution Architects in an Organization

Chapter 2

Sprint demonstration: During demonstrations, all stakeholders gather and review the team's work of what they had done in a sprint. Based on this, the stakeholder accepts and rejects the stories. The solution architect makes sure that the functional and non-functional requirements have been met. During this meeting, teams collect feedback from the product owners and solution architect and look at what changes were made.
Sprint retrospect: Retrospect is conducted at the end of each sprint cycle and is where the team inspects and adopts best practices. The team identifies things that went well and what they should continue to practice, as well as things that they can do better in the next sprint. Sprint Retrospect helps the organization apply continuous improvement while working on their delivery.

Agile tools and terms
Let's learn about some agile tools that help drive team metrics and project progress:
Planning poker: Planning poker is one of the most popular estimation techniques in agile methodology, where the Scrum Master plays poker games to estimate user stories when a sprint starts. During this activity, each user story will be evaluated based on its complexity. Team members use comparative analysis to give story points for each user story, which helps the team understand how much effort is required to complete the user stories.
Burndown chart: A burndown chart is used to monitor sprint progress and help the team understand how much work is pending. The Scrum Master and the team always follow the burndown chart to make sure there is no risk in the sprint and reuse that information to improve the estimation next time.
Product backlog: The product backlog contains a collection of requirements in the form of user stories and epics. The product owner continuously updates the backlog and prioritizes requirements during sprint grooming. Epic is a high-level requirement, and product owners write a user story to refine them. The development team breaks down these user stories into a task, which is an executable action item.
Sprint board: The sprint board contains a collection of user stories listed for the active sprint. The sprint board provides transparency as anyone can look at the project's progress for that particular sprint cycle. The team refers to the board on a daily standup to determine overall work progress and remove any obstructions.

[ 52 ]

Solution Architects in an Organization

Chapter 2

Definition of Done: This means all user stories should pass the Done criteria that have been set up by the solution architect and product owner in collaboration with stakeholders. Some of these criteria are as follows:
The code must be peer reviewed
The code should be unit tested
Enough documentation
Code quality
Code writing standard

Agile versus waterfall
Waterfall is one of the oldest and most traditional software development methodologies that organizations used to follow. In this section, you will learn about the difference between waterfall and agile and why organizations need to move over to agile. We are not going to look at the details of the waterfall process; instead, we will point out the key differences:
Agile methodologies help change the mindset from the traditional method to an agile mindset. The motivation for this is to move from a waterfall method to agile methods in order to achieve maximum business values and win customer confidence. This makes agile an advocate for customer collaboration at each step and provides transparency. The waterfall method tends to be more project-and document-centric, where customers were involved at the end phase.
The waterfall method is more helpful for the project where all requirements are unambiguous, and the sequence of their deliverables also known, which helps remove any unpredictability as requirements are very straightforward. The Agile methodology is helpful for companies that want to keep up with the market trend and have increased pressure from the customer. They need early releases for their products and have to be adaptive to changes in the requirements.
Agile projects are delivered in a small iterative manner with the highest quality and to achieve business value. Many agile teams work in parallel across the sprint to provide a shippable solution for the product at every end of the sprint cycle. As every sprint has a small deliverable and keeps building on top of that, the customer continuously gets to see the working model of the product. Waterfall has a long cycle and stakeholders get to see the final product at the end, which means there isn't much scope left to accommodate changes.

[ 53 ]

Solution Architects in an Organization

Chapter 2

The agile process makes sure the team is progressing toward the goal and that the project will be completed on time by putting checkpoints at every sprint cycle. In traditional waterfall methods, there is no frequent checkpoint that can ensure that the team is on the right path and verify whether the project will be completed on time, which may cause ambiguity.
In the Agile methodology, the customer always collaborates with the product owner and the team. This collaboration makes sure they observe and review the small, shippable product. Agile also ensures that work is being done and shows progress to the stakeholder. However, in the waterfall method, there is no such customer interaction until the project ends.
Agile is the most adaptive methodology since fast-moving technologies and businesses are becoming so unpredictable and need high velocity. Agile supports inspecting and adapting cycles, which creates a balance between demand and control.

Agile architecture
What comes into your mind when you think about the solution architect in an agile model? there are many myths , such as thinking that the solution architecture is a very complex activity, and with agile you will be asked to submit your design right away or in the next sprint cycle. Another myth is that the agile architecture will not be robust to such architecture design and development, that testing cannot be possible, and so on.
Agile architecture is about designing decoupled and extendable interfaces. A solution architect in an agile environment needs to follow an iterative re-architect concept by inspecting and adapting the approach. It's about choosing the right solution for enterprises, communicating well, taking continuous feedback, and modeling in an agile way. The development team needs a solid foundation and the ability to adapt to a changing requirement; they need guidance and mentoring from a solution architecture.
The foundation of the agile architecture should be reducing the cost of changes, reducing unnecessary requirements by challenging them, and creating a framework to reverse incorrect requirements rapidly. The Agile architect builds prototypes to minimize risk and plans for change by understanding them. They design the prototype while balancing the needs of all stakeholders and creating a loosely coupled architecture that can easily integrate with other modules. You will learn more about various loosely coupled architecture patterns in Chapter 6, Solution Architecture Design Patterns.

[ 54 ]

Solution Architects in an Organization

Chapter 2

Summary
In this chapter, you learned how the solution architect fits into the organization and how different kinds of solution architect roles coexist. There is generalist solution architect role such as enterprise solution architect, solution architect, technical architect, cloud architect, and architect evangelist.
The generalist solution architect has a broad knowledge of technology and may develop indepth expertise in a particular area. The specialist solution architect dives deep in other required areas of the project. The specialist solution architect possesses in-depth knowledge of their area of expertise, with some of the most common specialist solution architect roles being network architect, data architect, security architect, infrastructure architect, and DevOps architect.
You learned about solution architect responsibilities in great detail. Solution architects wear multiple hats; they work with stakeholders across the organization and analyze functional requirements and define non-functional requirements. The solution architect ensures consistency and standards across the organization, and they provide technology recommendations and solution prototypes. The solution architect handles various project constraints such as cost, quality, scope, and resources, and finds a balance between them.
The solution architect helps the project manager estimate cost and resources, and define a timeline, and stays throughout the project from design to launch. During the project's implementation, the solution architect makes sure that the stakeholder's expectations have been met and works as a liaison between the technical and business teams. The solution architect engages in post-launch application monitoring, alerts, security, disaster recovery, and scaling.
At the end of this chapter, you learned about the benefits of an agile process. We took a brief overview of the Agile methodology, roles, tools, terminology, and how agile differ from the traditional waterfall method. You learned about the traits of the agile architecture and how solution architects should make their architecture more flexible and agile.
In the next chapter, you will learn about the different attributes of the solution architecture that you should consider while designing a solution. These attributes include architecture security, scalability, availability, reliability, fault tolerance, extensibility, portability, interoperability, operational excellence, performance efficiency, cost optimization, and selfhealing.

[ 55 ]

3
Attributes of the Solution
Architecture
The solution architecture needs to consider multiple attributes and design applications. Solution design may have a broad impact across numerous projects in an organization and that demands a careful evaluation of the various properties of the architecture and striking a balance between them.
This chapter will provide an overall understanding of each attribute and how they are related to each other and coexist in solution design.
There may be more attributes, depending on the solution's complexity, but in this chapter, you will learn about the common characteristics that can be applied to most aspects of solution design. You can also view them as NFRs (which fulfills an essential aspect of design). It is the responsibility of a solution architect to look at all the attributes and make sure they satisfy the desired requirements and fulfill customer expectations.
In this chapter, we will cover the following topics:
Scalability and elasticity High availability and resiliency Fault tolerance and redundancy Disaster recovery and business continuity Extensibility and reusability Usability and accessibility Portability and interoperability Operational excellence and maintainability Security and compliance Cost optimization and budgets

Attributes of the Solution Architecture

Chapter 3

Scalability and elasticity
Scalability has always been a primary factor while designing a solution. If you ask any enterprise about their existing and new solutions, most of the time they like to plan ahead for scalability. Scalability means giving your system the ability to handle growing workloads, and it can apply to multiple layers, such as the application server, web app, and database.
As most applications nowadays are web-based, let's talk about elasticity. This is not only about growing out your system by adding more capabilities but also shrinking it to save cost. Especially with the adoption of the public cloud, it becomes easy to grow and shrink your workload quickly, and elasticity is replacing the term scalability.
Traditionally, there are two modes of scaling:
Horizontal scaling: It is becoming increasingly popular as compute commodity has become exponentially cheaper in the last decade. In horizontal scaling, the team adds more instances to handle increasing workloads:

Horizontal scaling
For example, as shown in the preceding diagram, let's say your application is capable of handling a thousand requests per second with two instances. As your user base grows, the application starts receiving 2,000 requests per second, which means you may want to double your application instance to four to handle the increased load.
Vertical scaling: This has been around for a long time. It's where the team adds additional compute storage and memory power to the same instance to handle increasing workloads. As shown in the following diagram, during vertical scaling, you will get a larger instance rather than adding more new instances to handle increased workload:
[ 57 ]

Attributes of the Solution Architecture

Chapter 3

Vertical scaling
The vertical scaling model may not be cost-effective. When you purchase hardware with more compute and memory capacity, the cost increases exponentially. You want to avoid vertical scaling after a certain threshold unless it is essential. Vertical scaling is most commonly used to scale relational database servers. However, you need to think about database sharding here. If your server hits the limits of vertical scaling, a single server cannot grow beyond certain memory and compute capacity.
The capacity dilemma in scaling
Most businesses have a peak season when the user is most active, and the application has to handle an additional load to meet demands. Take the classic example of an e-commerce website, selling all kinds of products such as cloth, groceries, electronic items, merchandise, and many more. These e-commerce sites have regular traffic throughout the year but get 10 times more traffic in the shopping season, for example, Black Friday and Cyber Monday in the US, or Boxing Day in the UK. This pattern creates an interesting problem for capacity planning, where your workload is going to increase drastically for just 1 month in the entire year.
In the traditional on-premise data center, ordering additional hardware can take between 4 to 6 months before it becomes application-ready, which means a solution architect has to plan for capacity. Excess capacity planning means your IT infrastructure resources will be sitting idle for most of the year, and less capacity means you are going to compromise user experience during significant sales events, thus impacting the overall business significantly. This means a solution architect needs to plan elastic workloads, which can grow and shrink on demand. The public cloud made this very easy.
[ 58 ]

Attributes of the Solution Architecture

Chapter 3

Scaling your architecture
Let's continue with the e-commerce website example by considering a modern three-tier architecture. Let's see how we can achieve elasticity at a different layer of the application. Here, we are only targeting the elasticity and scalability aspects of architecture design. You will learn more about this in Chapter 6, Solution Architecture Design Patterns.
The following diagram shows a three-tier architecture diagram of the AWS Cloud tech stack:

Scaling three-tier architecture
In the preceding architecture diagram, you can see a lot of components, such as the following:
Virtual server (Amazon EC2) Database (Amazon RDS) Load balancer (Amazon Elastic Load Balancer) DNS Server (Amazon Route53) CDN Service (Amazon CloudFront) Network boundary (VPC) and Object Store (Amazon S3)
[ 59 ]

Attributes of the Solution Architecture

Chapter 3

As shown in the preceding diagram, there is a fleet of web servers and application servers behind the load balancer. In this architecture, the user sends an application request to the load balancer, which routes traffic to the web server. As user traffic increases, auto scaling adds more servers in the web and application fleet. When there is low demand, it removes additional servers gracefully. Here, auto scaling can add or remove servers based on the chosen matrix-like CPU utilization and memory utilization; for example, you can configure whether CPU utilization goes beyond 60% and add three new servers; if this goes below 30%, you can then remove two existing servers.
We will dive deep into each component throughout this book. In the next section, you will learn about static content scaling.

Static content scaling
The web layer of the architecture is mostly concerned about displaying and collecting data and passing it to the application layer for further processing. In the case of an e-commerce website, each product will have multiple images and maybe videos to show a product's texture and demos, which means the website will have lots of static content with readheavy workload since, most of the time, users will be browsing products.
Storing static content in the web server means consuming lots of storage space, and as product listings grow you have to worry about scalability. The other problem is that static content (such as high-resolution images and videos) is heavy in size, which may cause significant load latency on the user's end. The web tier needs to utilize the Content Distribution Network (CDN) to solve this issue.
CDN providers (such as Akamai, Amazon CloudFront, Microsoft Azure CDN, and Google CDN) provide edge locations across the globe where static content can be cached from the web server to available videos and images near the user's location and reduce latency.
To scale the origin storage, it's recommended to use object storage such as Amazon S3 or an on-premise custom origin, which can grow independent of memory and compute capabilities. These storage solutions can hold static HTML pages to reduce the load of web servers and enhance user experience by reducing latency through the CDN network.

[ 60 ]

Attributes of the Solution Architecture

Chapter 3

Server fleet elasticity
The application tier collects user requests from the web tier and performs the heavy lifting of calculating business logic and talking to the database. When user requests increase, the application tier needs to scale to handle them and shrink back as demands decrease. In such scenarios, users are tied to the session, where they may be browsing from their mobile and purchasing from their desktop. Performing horizontal scaling without handling user sessions may cause a bad user experience as it will reset their shopping progress.
Here, the first step is to take care of user sessions by decoupling them from the application server instance, which means you should consider maintaining the user session in an independent layer such as a NoSQL database. NoSQL databases are key-value pair stores, where you can store semi-structured data.
Once you start storing your user session in NoSQL databases such as Amazon DynamoDB or MongoDB, your instance can scale horizontally without impacting the user experience. You can add a load balancer in front of a fleet of application servers, which can distribute the load among instances; with the help of auto scaling, you can automate adding or removing instances on demand.

Database scaling
Most applications use relational databases to store their transactional data. The main problem with relational databases is that they can scale horizontally until you plan for other techniques such as sharding and modifying your application accordingly. This sounds like a lot of work.
When it comes to databases, it is better to take preventive care and reduce their load. Using a mix of storage, such as storing user sessions in separate NoSQL databases and storing static content in an object store, helps to offload the master database. It's better to keep the master database node only for writing and updating data and use an additional read replica for all read requests.
Amazon RDS engine provides up to six read replicas for relational databases, and Oracle plugins can live-sync data between two nodes. Read replicas may have milliseconds of delay while syncing with the master node, and you need to plan for that while designing your application. It is recommended to use a caching engine such as Memcached or Redis to cache frequent queries and thus reduce the load to the master node.

[ 61 ]

Attributes of the Solution Architecture

Chapter 3

If your database starts growing beyond capacity, then you need to redesign and divide the database in the shard by applying partitions. Here, each shard can grow independently, and the application needs to be determined based on a partition key that the shard request will go to.
So, as you can see, scalability is a significant factor while designing a solution architecture, and it can impact the overall project budget and user experience significantly if it's not planned properly. A solution architect always needs to think in terms of elasticity while designing applications and optimizing workloads for the best performance and cost.
Statistical Analysis System (SAS) need to evaluate different options such as CDNs for static content scaling, load balancing, and autoscaling options for server scaling and various data storage options for caching, object stores, NoSQL stores, read replicas, and sharding.
In this section, you learned about various methods of scaling and how to inject elasticity into the different layers of your architecture. Scalability is an essential factor to ensure you have high application availability and make your application resilient. We'll learn more about high availability and resiliency in the next section.

High availability and resiliency
The one thing an organization doesn't want to see is downtime. Application downtime can cause a loss of business and user trust, which makes high availability one of the primary factors while designing the solution architecture. The requirement of application uptime varies from application to application.
If you have an external-facing application with a large user base such as an e-commerce website or social media, then 100% uptime becomes critical. In the case of an internal application (accessed by an employee such as an HR system or internal company), a blog can tolerate some downtime. Achieving high availability is directly associated with cost, so a solution architect always needs to plan for high availability, as per the application requirements, to avoid over-architecting.
To achieve a high availability (HA) architecture, it's better to plan workloads in the isolated physical location of the data center so that if an outage happens in one place, then your application replica can operate from another location.
As shown in the following architecture diagram, you have a web and application server fleet available in two separate availability zones (which is the different physical location of the data center). The load balancer helps distribute the workload between two availability zones in case Availability Zone 1 goes down due to power or network outage. Availability Zone 2 can handle user traffic, and your application will be up and running.
[ 62 ]

Attributes of the Solution Architecture

Chapter 3

In the case of the database, you have a standby instance in Availability Zone 2, which will failover and become the primary instance in the event of an issue in Availability Zone 1. Both the master and standby instances continuously sync data:

High availability and resilience architecture
The other factor is the architecture's resiliency. When your application is in trouble and you are facing an intermittent issue then apply the principle of self-healing, this means your application should be able to recover itself without human intervention. For your architecture, resiliency can be achieved by monitoring the workload and taking proactive action. As shown in the preceding architecture, the load balancer will be monitoring the health of instances. If any instance stops receiving the request, the load balancer can take out the bad instances from the server fleet and tell autoscaling to spin up a new server as a replacement. The other proactive approach to monitor the health of all instances (such as CPU and memory utilization and spinning up new instances as soon as a working instance starts to reach a threshold limit) such as CPU utilization is higher than 70% or that memory utilization is more than 80%.
[ 63 ]

Attributes of the Solution Architecture

Chapter 3

The attributes of high availability and resiliency can help in terms of cost by achieving elasticity, for example, if server utilization is low, you can take out some servers and save costs. The HA architecture goes hand in hand with self-healing, where you can make sure that your application is up and running, but; you also need to have a quick recovery to maintain the desired user experience.

Fault-tolerance and redundancy
In the previous section, you learned that fault tolerance and high availability have a close relationship with each other. High availability means your application is available for the user, but maybe with degraded performance. Suppose you need four servers to handle a user's traffic. For this, you put two servers in two different physically isolated data centers. If there is an outage in one data center, then user traffic can be served from another data center. But now, you have only two servers, which means you're left with 50% of the original capacity, and users may experience performance issue. In this scenario, your application has 100% high availability but is only 50% fault tolerant.
Fault tolerance is about handling workload capacity if an outage occurs without compromising system performance. A full fault-tolerant architecture involves high costs due to increased redundancy. It depends on your application's criticality as whether your user base can live with degraded performance for a period of application recovery:

Fault-tolerance architecture
[ 64 ]

Attributes of the Solution Architecture

Chapter 3

As shown in the preceding diagram, your application needs four servers to handle the full workload by distributing them into two different zones. In both scenarios, you are maintaining 100% high availability.
To achieve 100% fault tolerance, you need full redundancy and have to maintain the double count of the server so that the user doesn't encounter any performance issues during the outage of one zone. By keeping the same number of servers, we will achieve only 50% fault tolerance.
While designing the application architecture, a solution architect needs to determine the nature of the application's user base, only design for 100% fault tolerance (as required) and offset any redundancy costs involved.

Disaster recovery and business continuity
In the previous section, you learned about using high availability and fault tolerance to handle application uptime. There may be a situation when the entire region where your data center is located goes down due to massive power grid outages, earthquakes, or floods, but your global business should continue running. In such situations, you must have a disaster recovery plan where you will plan your business continuity by preparing sufficient IT resources in an entirely different region, maybe in different continents or countries.
When planning disaster recovery, a solution architect must understand an organization's Recovery Time Objective (RTO) and Recovery Point Objective (RPO). RTO means how much downtime a business can sustain without any significant impact. RPO indicates how much data loss a business can resist. A reduced RTO and RPO means more cost, so it is essential to understand whether the business is mission-critical and needs minimal RTO and RPO.
The following architecture diagram shows a multi-site disaster recovery architecture where the primary data center location is in Ireland, Europe, and the disaster recovery site is in Virginia, USA, hosted on AWS public cloud. In this case, your business will continue operating, even if something happens to the entire European region or to the public cloud. The fact that the disaster recovery plan is multi-site to achieve minimal RTO and RPO means minimal to no outage and no data loss:

[ 65 ]

Attributes of the Solution Architecture

Chapter 3

Hybrid multi-site disaster recovery architecture
The following are the most common disaster recovery plans, all of which you will learn about in Chapter 12, DevOps and Solution Architecture Framework:
Backup and Store: This plan is the least costly and has maximum RTO and RPO. In this plan, all the server's machine images, and database snapshots should be stored in the disaster recovery site. In the event of a disaster, the team will try to restore the disaster site from a backup. Pilot Lite: In this plan, all the server's machine images are stored as a backup, and a small database server is maintained in the disaster recovery site with continual data sync from the main site. Other critical services, such as Active Directory, may be running in small instances. In the event of a disaster, the team will try to bring up the server from the machine image and scale up a database. Pilot Lite is a bit more costly than the backup and recovery option but has less RTO and RPO than Backup and Store.
[ 66 ]

Attributes of the Solution Architecture

Chapter 3

Warm Standby: In this plan, all the application servers and the database server (running on lower capacity) instances in the disaster recovery site and continue to sync up with the leading site. In the event of a disaster, the team will try to scale up all the servers and databases. Warm Standby is costlier than the Pilot Lite option but has less RTO and RPO.
Multi-site: This plan is the most expensive and has a near-zero RTO and RPO. In this plan, a replica of the leading site maintains in a disaster recovery site with equal capacity and actively serves user traffic. In the event of a disaster, all traffic will be routed to an alternate location.
Often, organizations choose a less costly option for disaster recovery, but it is essential to do regular testing and make sure the failover is working. The team should put a routine checkpoint in operational excellence to make sure there's business continuity in the event of disaster recovery.

Extensibility and reusability
Businesses evolve as they grow, where applications not only scale to handle an increased user base but also keep adding more features to stay ahead and get a competitive edge. A solution design needs to be extendable and flexible enough to modify an existing feature or add new functionality. To modularize their application, often organizations want to build a platform with a group of features and launch them as separate applications. This is only possible with reusable design.
To achieve solution extensibility, a solution architect needs to use a loosely coupled architecture wherever possible. At a high level, creating a RESTful- or queue-based architecture can help develop loosely coupled communication between different modules or across applications. You will learn more about the other kinds of architecture in Chapter 6, Solution Architecture Design Patterns. In this section, we will take a simple example to explain the concept of architecture flexibility.
The following architecture diagram shows an API-based architecture in an e-commerce application. Here, you have independent services such as product catalog, order, payment, and shipping being utilized by an end user application in a pick-and-choose manner. Mobile and browser applications are used by the customer to place an online order. These applications need a product catalog service to browse the product on the web, an order service to place an order, and a payment service to make a payment.

[ 67 ]

Attributes of the Solution Architecture

Chapter 3

The product catalog and order service, in turn, communicate with the shipping service to send ordered items to the customer's doorstep. On the other hand, brick-and-mortar stores use Point of Sales systems, where a customer representative scans barcodes, places orders on behalf of the customer, and takes payment. Here, no shipping service is required as the customer picks the item up in-store:

Extensible API-based architecture
In the preceding diagram, you can see the Reward API, which is used for third-party API integration. This architecture allows you to extend the current design to integrate the Reward API for customer retention and to attract new customers by providing benefits when they purchase an item. Here, you can see how payment services are reutilized by both online and store ordering. Another service can reuse this if the organization wants to take payments for gift card service, food services, and so on. Extensibility and reusability are not limited to the service design level. It goes deep into the actual API framework level, where software architects should use object-oriented analysis and design (OOAD) concepts such as inheritance and containership to create an API framework. This can be extended and reutilized to add more features to the same service.
[ 68 ]

Attributes of the Solution Architecture

Chapter 3

Usability and accessibility
You want your users to have a seamless experience when browsing through the application. It should be so smooth that even the users don't notice that they can find things without any difficulties. You can do this by making your application highly usable. User research and testing are an essential aspect when it comes to defining usability that can satisfy user experience.
Usability is how quickly the user can learn navigation logic when using your application for the first time. It's about how quickly they can bounce back if they make a mistake and are able to perform the task efficiently. Complex and feature-rich applications have no meaning if they can't be used effectively.
Often, when you are designing your application, you want to target a global audience or significant geographic region. Your user base should be diverse in terms of technical amenities and physical abilities. You want your application to be accessible to everyone, regardless of whether a user has a slow internet-connection or old devices, or they have physical limitations.
Accessibility is about inclusion and making your application usable by everyone. While designing an application, a solution architect needs to make sure it can be accessed over a slow internet and is compatible with a diverse set of devices. Sometimes, they may have to create a different version of the application altogether to achieve that.
Accessibility design should include design components such as voice recognition and voice-based navigation, screen magnifiers, and reading content aloud. Localization helps the application become available in a language that's specific to a region, for example, Spanish, Mandarin, German, Hindi, or Japanese.
As shown in the following diagram, customer satisfaction is a component in both usability and accessibility:

[ 69 ]

Attributes of the Solution Architecture

Chapter 3

Customer satisfaction with usability and accessibility
You must know your users to achieve usability and accessibility, where accessibility is a component of usability, and they both go hand in hand. Before starting the solution design process, a solution architect should work alongside a product owner to research users by conducting interviews, and surveys, and gathering feedback on the mock frontend design. You need to understand the user's limitations and empower them with supporting features during application development.
When the product is launched, the team should plan for A/B testing by routing a small portion of user traffic to new features and understanding user reactions. After launch, the application must have a mechanism to collect continuous feedback (by providing a feedback form or by launching customer support) to make the design better.
Portability and interoperability
Interoperability is about the ability of one application to work with others through a standard format or protocol. Often, an application needs to communicate with the various upstream systems to consume data and downstream systems to supply data, so it is essential to establish that communication seamlessly.
[ 70 ]

Attributes of the Solution Architecture

Chapter 3

For example, an e-commerce application needs to work with other applications in the supply chain management ecosystem. This includes enterprise resource planning applications to keep a record of all transactions, transportation life cycle management, shipping companies, order management, warehouse management, and labor management, and so on.
All applications should be able to exchange data seamlessly to achieve an end-to-end feature from customer order to delivery. You will encounter similar use cases everywhere, whether it is a healthcare application, manufacturing application, or telecom application.
A solution architect needs to consider application interoperability during design by identifying and working with various system dependencies. An interoperable application saves lots of costs as it depends on systems that can communicate in the same format without any data messaging effort. Each industry has its standard size for data exchange that it needs to understand and adhere to.
In general, for software design, the architect may choose a popular format such as JSON or XML between different applications so that they can communicate with each other. In modern RESTful API design and microservice architecture, both formats are supported out of the box.
System portability allows your application to work across different environments without the need for any changes or with minimal changes. Any software application must work across various operating systems and hardware to achieve higher usability. Since technology changes rapidly, you will often see that a new version of a software language, development platform, or operating system is released. Today, mobile applications are an integral part of any system design, and your mobile apps need to be compatible with major mobile operating systems platforms such as iOS, Android, and Windows.
During design, the solution architect needs to choose a technology that can achieve the desired portability of the application; for example, if you are aiming to deploy your application across different operating systems. Programming languages such as Java may be the better choice as it is often supported by all operating systems, and your application will work on a different platform without needing to be ported across. For mobile applications, an architect may choose a JavaScript-based language such as React Native, which can provide cross-platform mobile app development.
Interoperability enriches system extensibility, and portability increases the usability of an application. Both are critical attributes of an architecture design and may add additional exponential costs if they're not addressed during solution design. A solution architect needs to carefully consider both aspects as per industry requirements and system dependencies.

[ 71 ]

Attributes of the Solution Architecture

Chapter 3

Operational excellence and maintainability
Operational excellence can be a great differentiator for your application by providing an on-par service to customers with minimal outage and high quality. It also helps the support and engineering team to increase productivity by applying proactive operational excellence. Maintainability goes hand in hand with operational excellence. Easily maintainable applications help reduce costs, avoid errors, and let you gain a competitive edge.
A solution architect needs to design for operation, which means the design should include how the workload will be deployed, updated, and operated in the long run. It is essential to plan for logging, monitoring, and alerting to capture all incident and take quick actions for the best user experience. Apply automation wherever possible, whether deploying infrastructures or changing the application code to avoid human error.
Including deployment methods and automation strategy in your design is very important as this can accelerate the time to market for any new changes without impacting existing operations. Operation excellence planning should consider security and compliance elements as regulatory requirements may change over time and your application has to adhere to them to operate.
Maintenance can be proactive or reactive. For example, once a new version of an operating system becomes available in the market, you can modernize your application to switch platforms immediately or monitor system health and wait until the end of the life of the software before making any changes. In any case, changes should be in small increments with a rollback strategy. To apply these changes, you can automate the entire process by setting up the continuous integration and continuous deployment (CI/CD) pipeline. For the launch, you can plan for A/B deployment or blue-green deployment.
For operational readiness, architecture design should include appropriate documents and knowledge-sharing mechanisms-- for example, creating and maintaining a runbook to document routine activity and creating a playbook that can guide your system process through issues. This allows you to act quickly in the event of an incident. You should use root cause analysis for post incidence to determine why the issue occurred and make sure it doesn't happen again.
Operational excellence and maintenance are an ongoing effort; every operational event and failure is an opportunity to learn and help you improve your operation by learning from previous mistakes. You must analyze the operation's activities and failures, do more experimenting, and make improvements. You will learn more about performing excellent consideration in solution design in Chapter 10, Operational Excellence Considerations.

[ 72 ]

Attributes of the Solution Architecture

Chapter 3

Security and compliance
Security is one of the most essential attributes of solution design. Many organizations fail due to security breaches, which results in a loss in customer trust and an unrecoverable business loss. Industry-standard regulations such as PCI for finance, HIPPA for health care, GDPR for European Union, and SOC compliance enforce security to protect consumer data and provide standard guidance to the organization. Depending on your industry and region, you must comply with local legislation by adhering to compliance needs. Primarily, application security needs to be applied in the following aspects of solution design:
Authentication and Authorization Web security Network security Infrastructure security Data security
These can be seen in the following diagram:

Security aspects in solution design
Let's take a look at the different security aspects. You will dive deep into each component in Chapter 8, Security Considerations.
[ 73 ]

Attributes of the Solution Architecture

Chapter 3

Authentication and authorization
Authentication means specifying who can access the system and authorization is applied to activities that a user can perform after getting inside the system or application. Solution architects must consider the appropriate authentication and authorization system while creating a solution design. Always start with the least privileged and provide further access as required by the user role.
If your application is for corporate internal use, you may want to allow access through a federated organizational system such as Active Directory, SAML 2.0, or LDAP. If your application is targeting mass user bases such as social media websites or gaming apps, you can allow them to authenticate through OAuth 2.0 and OpenID access, where users can utilize their other IDs such as Facebook, Google, Amazon, and Twitter.
It is important to identify any unauthorized access and take immediate action to mitigate security threats, which warrants continuously monitoring and auditing the access management system. You will learn about application security in Chapter 8, Security Considerations.

Web security
A web application is often exposed to the internet and is more vulnerable to external attacks. Solution design must consider preventing attacks such as cross-site scripting (XSS) and SQL injection. These days, the Distributed Denial of Service (DDoS) attack is causing trouble for organizations. To prevent this, the appropriate tools are required, and an incident response plan needs to be put in place.
Solution architects should plan to use a Web Application Firewall (WAF) to block malware and SQL injection attacks. WAF can be used to prevent traffic from a country where you don't have a user base or to block malicious IP addresses. WAF, in combination with a Content Distribution Network (CDN), can help to prevent and handle DDoS attacks.

Network security
Network security helps prevent overall IT resources inside an organization and application being open to external users. Solution design must plan to secure the network, which can help prevent unauthorized system access, host vulnerabilities, and port scanning.

[ 74 ]

Attributes of the Solution Architecture

Chapter 3

Solution architects should plan for minimal system exposure by keeping everything behind a corporate firewall and avoiding internet access wherever possible. For example, the web server shouldn't be exposed to the internet instead; only the load balancer should be able to talk to the internet. For network security, plan to utilize an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS) and put them in front of network traffic.

Infrastructure security
If you are maintaining your own data center, then the physical security of the infrastructure is very important if you wish to block physical access to your server on the part of any unauthorized user. However, if you are leasing the data center or using a private cloud, then this can be handled by a third-party vendor. Logical access to the server must be secured by network security, which is done by configuring the appropriate firewall.

Data security
This is one of the most critical components that need to be secured. After all, you are putting layers of security at the access, web, application, and network layers to secure your data. Data can be exchanged between two systems, so it need to be secure in transit, or it may be sitting in a database or some storage where data needs to be secure at rest.
Solution design needs to plan data-in-transit security with Secure Socket Layer/Transport Layer Security (SSL/TLS) and security certification. Data at rest should be secured using various encryption mechanisms, which may be symmetric or asymmetric. The design should also plan to secure the encryption key with the right key management approach, as per application requirements. Key management can be achieved using a hardware security module or services provided by cloud vendors.
While ensuring security, it is essential to have a mechanism to identify any security breach as soon as it occurs and respond to it. Adding automation to every layer to monitor, and get an immediate alert for, any violation must be part of the solution design. DevSecOps is becoming a trend in most organizations since it applies best practices to automating security needs and security responses during the software development life cycle. You will learn more about DevSecOps in Chapter 12, DevOps and Solution Architecture Framework.

[ 75 ]

Attributes of the Solution Architecture

Chapter 3

To adhere to compliance with the local legislation, solution design needs to include an audit mechanism. For finance, regulatory compliance such as Payment Card Industry Data Security Standard (PCI DSS) is strictly required to gain the log trails of every transaction in the system, which means all activity needs to be logged and sent to the auditor when required. Any Personal Identifiable Information (PII) data, such as customer email IDs, phone numbers, and credit card numbers needs to be secured by applying encryption and limited access for any application storing PII data.
In on-premise environments, it is the customer's responsibility to secure the infrastructure and application and also to get certification for compliance. However, in the public cloud, environments such as AWS ease this burden since infrastructure security and compliance are taken care by a cloud vendor. The customer shares responsibility for the security of the application and make sure it's compliant by completing the required audit.

Cost optimization and budget
Every solution is limited by budget and investors look for maximal ROI. The solution architect needs to consider cost-saving during architecture design. Cost should be optimized from pilot creation to solution implementation and launch. Cost optimization is a continuous effort and should be continuous process. Like any other constraint, costsaving comes with a trade-off; it should make a point of determining whether other components such as the speed of delivery and performance are more critical.
Often, cost increases due to over-provision resources and overlooks the cost of procurement. The solution architect needs to plan optimal resources to avoid excessive underutilization. At the organization level, there should be an automated mechanism to detect ghost resources, which team members may create dev and test environments, and it may no longer be in use after completion of the implementation task. Often, those ghost resources go unnoticed and cause costs to overrun. Organizations need to keep a record of their inventory by applying automated discovery.
During technology selection, it's essential to evaluate build versus source cost. Sometimes, it's better to use a third-party tool when your organization doesn't have the expertise and the cost of the build will be high, for example, by sourcing log analysis and business intelligence tools. Also, we need to determine the ease of learning and the complexity of implementation when selecting a technology for solution implementation. From an IT infrastructure perspective, we need to evaluate capital expenditure versus operation expenditures as maintaining a data center requires high capital investment upfront to meet unforeseen scaling demands. Since multiple choices are available, solution architects can select options from the following-- public cloud, private cloud, and multi-cloud. Alternatively they can take a hybrid approach.
[ 76 ]

Attributes of the Solution Architecture

Chapter 3

Like all components, cost needs to be automated and alerts need to be set up against budget consumption. Cost needs to be planned and divided between the organizational unit and the workload so that responsibilities can be shared with all groups. The team needs to continuously look at cost optimization by optimizing operation support and workload as more historical data is collected.

Summary
In this chapter, you learned about various solution architecture attributes that need to be considered while creating a solution design. You learned about two modes of scalability, vertical and horizontal, and how to scale various layers of the architecture, including the web layer, application servers, and databases.
You also learned how to apply elasticity in your workload using autoscaling so that it can grow and shrink on demand. This chapter provided insights into designing a resilient architecture and the methods to achieve high availability. Furthermore, this helped you understand fault tolerance and redundancy so that you can make your application performant, as per your user's expectations, and plan for disaster recovery for the continuation of your business in the case of any unforeseen events.
Then, you learned about the importance of making your architecture extendable and accessible and how architecture portability and interoperability help reduce costs and increase the adoption of your application. This chapter ended with how to apply operational excellence, security, and cost to every layer of your architecture and how those attributes should be considered right from the beginning of the solution design process. You will look at each component in more detail later in this book.
In the next chapter, you will learn about the principle of solution architecture design, which will focus on how to design the solution architecture while bearing in mind various attributes that were explained in this chapter.

[ 77 ]

4
Principles of Solution
Architecture Design
In the previous chapter, you learned about the attributes of solution architecture. Those attributes are essential properties, which a solution architect needs to keep in mind while creating a solution design. In this chapter, you will learn about the principles of solution architecture design, which incorporate various attributes during solution design.
This chapter throws light on the most important and common design principles. However, there could be more design aspects based on the nature of the product complexity and industry domain. As you move forward to your learning path of becoming a solution architect in this book, these design principles and attributes will be further applied in order to create various design patterns in Chapter 6, Solution Architecture Design Patterns.
You will learn about the following topics in this chapter:
Scaling workload Building resilient architecture Design for performance Using replaceable resources Think loose coupling Think service not server Using the right storage for the right need Think data-driven design Overcoming constraints Adding security everywhere Automating everything

Principles of Solution Architecture Design

Chapter 4

In this chapter, you will not only learn about designing scalable, resilient, and performance architecture, but you will also learn how to take care of your architecture by applying security, overcoming constraints, and applying changes along with the test and automation approach. These principles will help you to apply thinking in the right way, by using service-oriented architecture (SOA) and a data-driven approach.

Scaling workload
In the Scalability and elasticity section of Chapter 3, Attributes of the Solution Architecture, you learned about different modes of scaling and how to scale static content, a server fleet, and a database at a high level. Now, let's look at various types of scaling that can be used to handle workload spikes.
Scaling could be predictive if you are aware of your workload, which is often the case; or it could be reactive if you get a sudden spike or if you have never handled that kind of load before. Regardless of scaling being reactive or predictive, you need to monitor the application and collect the data in order to plan your scaling needs accordingly. Let's dive deep into these patterns with examples.
Predictive scaling
Predictive scaling is the best-case approach that any organization wants to take. Often, you can collect historical data of application workload, for example, an e-commerce website such as Amazon may have a sudden traffic spike, and you need predictive scaling to avoid any latency issues. Traffic patterns may include the following:
Weekends have three times more traffic than a weekday. Daytime has five times more traffic than at night. Shopping seasons, such as Thanksgiving or Boxing Day, have 20 times more traffic than regular days. Overall, the holiday season in November and December has 8 to 10 times more traffic than during other months.
You may have collected the previous data based on monitoring tools that are in place to intercept the user's traffic, and based on this, you can make a prediction for scaling. Scaling may include planning to add more servers when workload increases, or to add additional caching. This example of an e-commerce workload is one that tends toward higher complexity and provides lots of data points to help us to understand overall design issues. For such complex workloads, predictive scaling becomes more relevant.
[ 79 ]

Principles of Solution Architecture Design

Chapter 4

Predictive auto-scaling is becoming very popular, where historical data and trends can be fed to prediction algorithms, and you can predict in advance how much workload is expected at a given time. Using this expected data, you can set up the configuration to scale your application.
To better understand predictive auto-scaling, look at the following metrics dashboard from the AWS predictive auto-scaling feature. This graph has captured historical CPU utilization data of the server, and based on that, has provided the forecasted CPU utilization:

Predictive scaling forecast
[ 80 ]

Principles of Solution Architecture Design

Chapter 4

In the following screenshot, an algorithm is suggesting how much minimum capacity you should plan in order to handle the traffic, based on the forecast:

Predictive scaling capacity plan
You can see that there is a variation in the minimum capacity at different times of the day. Predictive scaling helps you to best optimize your workload based on predictions. Predictive auto-scaling helps to reduce latency and avoid an outage, as adding new resources may take some time. If there is a delay in adding additional resources to handle website traffic spikes, it may cause a request flood and false high traffic, as users tend to send a repeated request when they encounter slowness or outages.
In this section, you learned about predictive auto-scaling, but sometimes, due to a sudden spike in the workload, you need reactive scaling. We will learn about this in the next section.
[ 81 ]

Principles of Solution Architecture Design

Chapter 4

Reactive scaling
With the use of a machine learning algorithm, predictive scaling is getting more accurate, but you have to deal with sudden traffic spikes, and depend upon reactive scaling. This unexpected traffic that may come could be even 10 times the regular traffic; this usually happens due to a sudden demand or, for example, due to a first attempt to run sales events, where we're not sure about the amount of incoming traffic.
Let's take an example where you are launching a flash deal on your e-commerce website. You will have a large amount of traffic on your home page, and from there, the user will go to the flash deal product-specific page. Some users may want to buy the product; therefore, they will go to the add to cart page.
In this scenario, each page will have a different traffic pattern, and you will need to understand your existing architecture and traffic patterns, along with an estimate of the desired traffic. You also need to understand the navigation path of the website. For example, the user has to log in to buy a product, which can lead to more traffic on the login page.
In order to plan for the scaling of your server resources for traffic handling, you need to determine the following patterns:
Determine web pages, which are read-only and can be cached. Which user queries need just to read that data, rather than write or update anything in the database? Does a user query frequently, requesting the same or repeated data, such as their own user profile?
Once you understand these patterns, you can plan to offload your architecture in order to handle excessive traffic. To offload your web-layer traffic, you can move static content, such as images and videos, to content distribution networks from your web server. You will learn more about the Cache Distribution pattern in Chapter 6, Solution Architecture Design Patterns.
At the server fleet level, you need to use a load balancer in order to distribute traffic, and you need to use auto-scaling to increase or shrink several servers in order to apply horizontal scaling. To reduce the database load, use the right database for the right need--a NoSQL database to store user sessions and review comments, a relational database for the transaction, and apply caching to store frequent queries.

[ 82 ]

Principles of Solution Architecture Design

Chapter 4

In this section, you learned about the scaling patterns and methods that are used to handle the scaling needs of your application in the form of predictive scaling and reactive scaling. In Chapter 6, Solution Architecture Design Patterns, you will learn about the details of the different types of design patterns, and how to apply them in order to be able to scale your architecture.

Building resilient architecture
Design for failure, and nothing will fail. Having a resilient architecture means that your application should be available for customers while also recovering from failure. Making your architecture resilient includes applying best practices in every aspect, in order to make your application recoverable. Resiliency needs to be used in all layers of architecture, including infrastructure, application, database, security, and networking.
From the security perspective, the Distributed Denial of Service (DDoS) attack has the potential to impact the availability of services and applications. The DDoS attack usually puts fake traffic in your server and makes it busy, therefore, legitimate users are unable to access your application. This can happen at the network layer or the application layer. You will learn more about DDoS attack and mitigation in Chapter 8, Security Considerations.
It's essential to take a proactive approach to prevent DDoS attacks. The first rule is to keep as much as application workload possible in the private networks and not expose your application endpoints to the internet wherever possible. To take early action, it is essential to know your regular traffic and have a mechanism in place to determine substantial suspicious traffic at the application and network packet levels.
Exposing your application through the content distribution network (CDN) will provide the inbuilt capability and adding the Web Application Firewall (WAF) rule can help to prevent unwanted traffic. Scaling should be your last resort but be ready with an autoscaling mechanism to enable you to scale your server in the case of such an event.
To achieve resiliency at the application level, the first thing that comes to mind is redundancy, which leads to making your application highly available by spreading the workload across the geographic location. To achieve redundancy, you can have a duplicate server fleet at a different rack in the same data center and in a different region. If servers are spread across different physical locations, the first level of traffic routing can be handled using the Domain Name System (DNS) before it reaches the load balancer:

[ 83 ]

Principles of Solution Architecture Design

Chapter 4

Application architecture resiliency
As you can see in the preceding architecture, resiliency needs to be applied in all the critical layers that affect the application's availability to implement the design of failure. To achieve resiliency, the following best practices need to be applied in order to create a redundant environment:
Use the DNS server to route traffic between different physical locations so that your application will still be able to run in the case of entire region failure.
Use the CDN to distribute and cache static content such as videos, images, and static web pages near the user location, so that your application will still be available in case of a DDoS attack or local point of presence (PoP) location failure. Once traffic reaches a region, use a load balancer to route traffic to a fleet of servers so that your application should still be able to run even if one location fails within your region. Use auto-scaling to add or remove servers based on user demand. As a result, your application should not get impacted by individual server failure. Create a standby database to endure the high availability of the database, meaning that your application should be available in the instance of a database failure.
[ 84 ]

Principles of Solution Architecture Design

Chapter 4

In the preceding architecture, if any components fail, you should have a backup to recover it and achieve architecture resiliency. The load balancer and routers at the DNS server perform a health check to make sure that the traffic is routed to only healthy application instances. You can configure this to perform a shallow health check, which monitors local host failures; or deep health checks, which can also take care of dependency failure. However, a deep health check takes more time and is more resource-intensive than to the shallow health check.
At the application level, it is essential to avoid cascading failure, where the failure of one component can bring down the entire system. There are different mechanisms available to handle cascading, such as applying timeout, traffic rejection, implementing the idempotent operation, and using circuit-breaking patterns. You will learn more about these patterns in Chapter 6, Solution Architecture Design Patterns.

Design for performance
With the availability of fast internet, customers are seeking high-performant applications with minimal load time. Organizations have noticed that a direct revenue impact is proportional to application performance, and slowness in application load time can significantly impact customer engagement. Modern-era companies are setting a high expectation when it comes to performance, which results in high-performant applications becoming a necessity in order to stay in the market.
Like resiliency, the solution architect needs to consider performance at every layer of architecture design. The team needs to put monitoring in place to continue to perform effectively, and work to improve upon it continuously. Better performance means more user engagements and increases in return on investment--high-performance applications are designed to handle application slowness due to external factors such as a slow internet connection. For example, you may have designed your blog web page to load within 500 milliseconds where there is good internet availability. However, in cases of a slow internet, you can load text and engage the user while images and videos are still loading.
In an ideal environment, as your application workload increases, automated scaling mechanisms start handling additional requests without impacting upon application performance. But in the real world, your application latency goes down for duration when scaling takes effect. In a real-world situation, it's better to test your application for performance by increasing the load and understand if you can achieve the desired concurrency and user experience.

[ 85 ]

Principles of Solution Architecture Design

Chapter 4

At the server level, you need to choose the right kind of server depending upon your workload. For example, choose the right amount of memory and compute to handle the workload, as memory congestion can slow down application performance, and eventually, the server may crash. For storage, it is important to choose the right input/output operations per second (IOPS). For write-intensive applications, you need high IOPS to reduce latency and to increase disk write speed.
To achieve great performance, apply caching at every layer of your architecture design. Caching makes your data locally available to the users or keeps data in-memory in order to serve an ultra-fast response. The following are the considerations that are required to add caching to various layers of your application design:
Use browser cache on the user's system to load frequently requested web pages. Use the DNS cache for quick website lookup. Use the CDN cache for high-resolution images and videos that are near to the user's location. At the server level, maximize the memory cache to serve user requests. Use cache engines such as Redis and Memcached to serve frequent queries from the caching engine. Use the database cache to serve frequent queries from memory. Take care of cache expiration and cache eviction at every layer.
As you can see, keeping your application performant is one of the essential design aspects and is directly related to organization profitability. The solution architect needs to think about performance when creating solution design and should work relentlessly to keep improving the performance of the application.
You will learn more about different caching patterns in Chapter 6, Solution Architecture Design Patterns. Performance is a critical factor, and in Chapter 7, Performance Considerations, you will dive deep further to learn techniques to optimize your application for better performance.

Using replaceable resources
Organizations make a significant capital investment in hardware, and they develop the practice of updating them with a new version of the application and configuration. Over time, this leads to different servers running in varied configurations, and troubleshooting them becomes a very tedious task. Sometimes, you have to keep running unnecessary resources when they are not needed, as you are not sure which server to shut down.

[ 86 ]

Principles of Solution Architecture Design

Chapter 4

The inability to replace servers makes it challenging to roll out and test any new updates in your server fleet. These problems can be solved by treating your server as a replaceable resource, which enables you to move more quickly to accommodate changes such as upgrading applications and underlying software.
That is why, while designing your application, always think of immutable infrastructure.

Creating immutable infrastructure
Immutable means, during application upgrades, you will not only replace software, but hardware too. Organizations make a significant capital investment in hardware and develop the practice of updating them with a new version of the application and configuration.
To create replaceable servers, you need to make your application stateless and avoid the hardcoding of any server IP or database DNS name. Basically, you need to apply the idea of treating your infrastructure as software instead of hardware, and not apply updates to the live system. You should always spin up new server instances from the golden machine image, which has all necessary security and software in place.
Creating immutable infrastructure becomes comfortable with the use of a virtual machine, where you can create a golden image of your virtual machine and deploy it with the new version, rather than trying to update an existing version. This deployment strategy is also beneficial for troubleshooting, where you can dispose the server that has an issue and spin up a new server from a golden image. You should take a backup of logs for root cause analysis before disposing the server with issues. This approach also ensures consistency across the environment, as you are using the same baseline server image to create all of your environment.
Canary testing
Canary testing is one of the popular methods that is used to apply rolling deployment with immutable infrastructure. It helps you to ensure that old-version production servers are replaced safely with new servers, without impacting the end users. In canary testing, you deploy your software update in a new server and route a small amount of traffic to it.
If everything goes well, you will keep increasing traffic by adding more new servers, while disposing the old servers. Canary deployment gives you a safe option to push your changes in the live production environment. If something goes wrong, only small numbers of users are impacted, and you have the option of immediate recovery by routing traffic back to old servers.
[ 87 ]

Principles of Solution Architecture Design

Chapter 4

The solution architect needs to think ahead to use replaceable resources for deployment. They need to plan session management and avoid server dependency on hardcoded resources ahead of time. Always treat resources as replaceable and design your applications to support changes in hardware.
The solution architect needs to set a standard to use various rolling deployment strategies, such as A/B testing or Blue/Green deployment. Treat your server like cattle, not like a pet; when this principle is applied to the replacement of problematic IT resources, quick recovery is ensured, and troubleshooting time reduced.

Think loose coupling
A traditional application builds a tightly integrated server, where each server has a specific responsibility. Applications depend upon other servers for completeness of functionality. As shown in the following diagram, in a tightly coupled application, the web server fleet has a direct dependency on all application servers, and vice versa:

Tightly coupled architecture
In the preceding architecture diagram, if one application server goes down, then all web servers will start receiving errors, as the request will route to an unhealthy application server, which may cause a complete system failure. In this case, if you want to scale by adding and removing servers, it requires lots of work, as all connections need to be set up appropriately.
[ 88 ]

Principles of Solution Architecture Design

Chapter 4

With loose coupling, you can add an intermediate layer such as a load balancer or a queue, which automatically handles failures or scaling for you. In the following architecture diagram, there is a load balancer between the web server and the application server fleet, which makes sure to always serve user requests from a healthy application server:

Load balancer-based loosely coupled architecture
If one of the application servers goes down, the load balancer will automatically start directing all the traffic to the other three healthy servers. Loosely coupled architecture also helps you to scale your servers independently and replace unhealthy instances gracefully. It makes your application more fault tolerant as an error radius is limited to a single instance only.
For queue-based loosely coupled architecture, take an example of an image-processing website, where you need to store an image, and then process it for encoding, thumbnail, and copyright. The following architecture diagram has a queue-based decoupling. You can achieve loose coupling of systems by using queues between systems and exchanging messages that transfer jobs:
[ 89 ]

Principles of Solution Architecture Design

Chapter 4

Queue-based loosely coupled architecture
Queue-based decoupling enables asynchronous linking of systems, where one server is not waiting for a response from another server and it is working independently. This method lets you increase the number of virtual servers that receive and process the messages in parallel. If there is no image to process, you can configure auto-scaling in order to terminate the excess servers.
In a complex system, a loosely coupled architecture is achieved by creating a serviceoriented architecture (SOA), where independent services contain a complete set of functionalities and communicate with each other over a standard protocol. In modern design, microservice architecture is becoming highly popular, which facilitates the decoupling of an application component. The loosely coupled design has many benefits, from providing scalability and high availability, to ease of integration.
In the next section, you will learn more about SOA, and you will also dive deep into the details of this topic in Chapter 6, Solution Architecture Design Pattern.
Think service not server
In the previous section, you learned about loose coupling and how important it is for our architecture to be loosely coupled for scalability and fault-tolerance. Developing serviceoriented thinking will help to achieve a loosely coupled architecture (as opposed to a server-oriented design, which can lead to hardware dependency and a tightly coupled architecture). SOA helps us to achieve ease of deployment and maintenance for your solution design.
[ 90 ]

Principles of Solution Architecture Design

Chapter 4

When it comes to service-oriented thinking, solution architects always gear towards SOA. The two most popular SOAs are based on Simple Object Access Protocol (SOAP) services and RESTful services. In SOAP-based architecture, you format your message in XML and send it over the internet using the SOAP protocol, which builds on top of the HTTP.
In RESTful architecture, you can format a message in XML, JSON, or plain text, and send it over a simple HTTP. However, RESTful architecture is comparatively more popular, as it is very lightweight and much more straightforward than SOAP.
When talking about SOA nowadays, microservice architecture is increasingly popular. Microservices are independently scalable, which makes it easier to expand or shrink one component of your application without impacting others. As you can see in the following diagram, in a monolithic architecture, all components are built in a single server and tied up with a single database, which creates a hard dependency, whereas, in a microservice architecture, each component is independent with their framework and database, which allows them to be scaled independently:

Monolithic to the microservice architecture
In the preceding diagram, you can see an example of an e-commerce website, where customers can log in and place an order, assuming the items they want are available, by adding items to the cart. To convert a monolithic architecture to a microservice-based architecture, you can create applications that are made of small independent components, which constitute smaller parts to iterate.
[ 91 ]

Principles of Solution Architecture Design

Chapter 4

Taking the modularization approach means that the cost, size, and risk of change reduces. In the preceding case, each component is created as a service. Here, the Login Service can independently scale to handle more traffic, as the customer may log in frequently to explore the product catalog and order status, while the Order Service and the Cart Service may have less traffic, as a customer may not place the order very often.
Solution architects need to think of SOA while designing a solution. The clear advantage of services is that you have a smaller surface area of code to maintain and services are selfcontained. You can build them with no external dependencies. All prerequisites are included in the service, which enables loose coupling, scaling, and reduces the blast radius in case of failure.

Using the right storage for the right need
For decades, organizations have been using a traditional relational database and trying to fit everything there, whether it is key/value-based user session data, unstructured log data, or analytics data for a data warehouse. However, the truth is, the relational database is meant for transaction data, and it doesn't work very well for other data types--it's like using a Swiss Army knife, which has multiple tools that work but to a limited capacity; if you want to build a house, then the screwdriver will not be able to perform a heavy lift. Similarly, for specific data needs, you should choose the right tool that can do the heavy lifting, and scale without compromising performance.
Solution architects need to consider multiple factors while choosing the data storage to match the right technology. Here are the important ones:
Durability requirement: How should data be stored to prevent data corruption? Data availability: Which data storage system should be available to deliver data? Latency requirement: How fast should the data be available? Data throughput: What is the data read and write need? Data size: What is the data storage requirement? Data load: How many concurrent users need to be supported? Data integrity: How to maintain the accuracy and consistency of data? Data queries: What will be the nature of queries?

[ 92 ]

Principles of Solution Architecture Design

Chapter 4

In the following table, you can see different types of data with examples and appropriate storage types to use. Technology decisions need to be made based on storage type, as shown here:

Data Type Transactional, structured schema
Key-value pair, semi-structured, unstructured
Analytics
In-memory Object Block Streaming Archive Web storage Search Data catalog Monitoring

Data Example User order data, financial transaction

Storage Type Relational database

User session data, application log, review, comments

NoSQL

Sales data, Supply chain intelligence, Business flow

Data warehouse

User home page data, common dashboard Cache

Image, video

File-based

Installable software

Block-based

IoT sensor data, clickstream data

Temporary storage for streaming data

Any kind of data

Archive storage

Static web contents such as images, videos, HTML pages
Product search, content search

CDN
Search index store and query

Table metadata, data about data

Meta-data store

System log, network log, audit log

Monitor dashboard and alert

Storage Example
Amazon RDS, Oracle, MySQL, PostgreSQL, MariaDB Microsoft SQL Server
Amazon DynamoDB, MongoDB, Apache HBase, Apache Cassandra, Azure Tables,
IBM Netezza, Amazon Redshift, Teradata, Greenplum, Google BigQuery
Redis cache, Amazon ElastiCache, Memcached
SAN, Amazon S3, Azure Blob Storage, Google Storage
NAS, Amazon EBS, Amazon EFS, Azure Disk Storage
Apache Kafka, Amazon Kinesis, Spark Streaming, Apache Flink
Amazon Glacier, magnetic tape storage, virtual tape library storage
Amazon CloudFront, Akamai CDN, Azure CDN, Google CDN, Cloudflare
Amazon Elastic Search, Apache Solr, Apache Lucene
AWS Glue, Hive metastore, Informatica data catalog, Collibra data catalog
Splunk, Amazon CloudWatch, SumoLogic, Loggly

As you can see in the preceding table, there are various properties of data, such as structured, semi-structured, unstructured, key-value pair, streaming, and so on. Choosing the right storage helps to improve not only the performance of the application, but also its scalability. For example, you can store user session data in the NoSQL database, which will allow application servers to scale horizontally and maintain user sessions at the same time.

While choosing storage options, you need to consider the temperature of the data, which could be hot, warm, or cold:

For hot data, you are looking for sub-millisecond latency and required cache data storage. Some examples of hot data are stock trading and making product recommendations in runtime.
For warm data, such as financial statement preparation or product performance reporting, you can live with the right amount of latency, from seconds to minutes, and you should use a data warehouse or a relational database.
For cold data, such as storing 3 years of financial records for audit purposes, you can plan latency in hours, and store it in archive storage.

[ 93 ]

Principles of Solution Architecture Design

Chapter 4

Choosing the appropriate storage, as per the data temperature also saves costs in addition to achieving performance SLA. As any solution design revolves around handling the data, so a solution architect always needs to understand their data thoroughly and then choose the right technology.
In this section, we have covered a high-level view of data in order to get the idea of using the proper storage, as per data nature. You will learn more about data engineering in Chapter 13, Data Engineering and Machine Learning. Using the right tool for the right job helps to save costs and improve performance, so it's essential to choose the right data storage for the right need.

Think data-driven design
Any software solution revolves around the collection and management of data. Take the example of an e-commerce website; the software application is built to showcase product data on the website and encourage the customers to buy them. It starts by collecting customer data when they create a login, adding a payment method, store order transactions, and maintaining inventory data as the product gets sold. Another example is a banking application, which is about storing customer financial information and handling all financial transaction data with integrity and consistency. For any application, the most important thing is to handle, store, and secure data appropriately.
In the previous section, you have learned about different kinds of data types, along with the storage needs, which should help you to apply data thinking in your design. Solution design is heavily influenced by data and enables you to apply the right designdriven solution by keeping data in mind. While designing a solution, if your application needs ultra-low latency, then you need to use cache storage such as Redis and Memcached. If your website needs to improve its page load time with an attractive high-quality image, then you need to use a content distribution network such as Amazon CloudFront or Akamai to store data near the user location. Similarly, to improve your application performance, you need to understand if your database will be read-heavy (such as a blog website) or write-heavy (such as survey collection) and plan your design accordingly.
It's not just application design, but operational maintenance and business decisions all revolves around data. You need to add monitoring capabilities to make sure that your application, and in turn, your business, is running without any issues. For application monitoring, you collect log data from the server and create a dashboard to visualize the metrics.

[ 94 ]

Principles of Solution Architecture Design

Chapter 4

Continuous data monitoring and sending alerts in the case of issues helps you to recover quickly from failure, by triggering the auto-healing mechanism. From a business perspective, collecting sales data helps you to run a marketing campaign to increase the overall business revenue. Analyzing review sentiments data helps to improve the customer experience and retain more customers, which is critical for any business. Collecting overall order data and feeding to the machine learning algorithm helps you to forecast future growth and maintains the desired inventory.
As a solution architect, you are not only thinking about application design, but also about overall business value proposition. It's about other factors around the application, which can help to increase customer satisfaction and maximize the return on your investment. Data is gold and getting insights into data can make a tremendous difference to an organization's profitability.

Overcoming constraints
Earlier, in Chapter 2, Solution Architect in an Organization, you learned about the various constraints that a solution architecture needs to handle and balance. The major limitations are cost, time, budget, scope, schedule, and resources. Overcoming with these constraints is one of the significant factors that needs to be considered while designing a solution. You should look at the limitations as challenges that can be overcome rather than obstacles, as challenges always push you to the limit for innovation in a positive way.
For a successful solution, always put the customer first, while also taking care of architectural constraints. Think backward from the customers' needs, determine what is critical for them, and plan to put your solution delivery in an agile way. One popular method of prioritized requirement is MoSCoW, where you divide customer requirements into the following categories:
Mo (Must have): Requirements that are very critical for your customers, without which the product cannot launch. S (Should have): Requirements that are the most desirable to the customer, once they start utilizing the application. Co (Could have): Requirements that are nice to have, but their absence will not impact upon the desired functionality of the application. W (Won't have): Requirements that customers may not notice if it is not there.

[ 95 ]

Principles of Solution Architecture Design

Chapter 4

You need to plan a minimum viable product (MVP) for your customer with must-have (Mo) requirements and go for the next iteration of delivery with should-have (S) requirements. With this phased delivery approach, you can thoroughly utilize your resources and overcome the challenges of time, budget, scope, and resources. The MVP approach helps you to determine customer needs. You are not trying to build everything without knowing if the features you've built have added value for the customer. This customer-focused approach helps to utilize resources wisely and reduces the waste of resources.
In the following diagram, you can see the evaluation for a truck manufacturing delivery, where the customer wants a delivery truck that gets delivered initially, and you evolve the process based on the customer's requirements:

MVP approach to building the solution
Here, once a customer gets a first delivery truck, which is a full functioning, they can determine if they need a more significant load to handle, and based on that, the manufacturer can build a six-wheel, a 10-wheel, and finally an 18-wheel truck trailer. This stepwise approach provides working products with essential features that the customers can use, and the team can build upon it, as per the customer requirement.
Technology constraints become evident in a large organization, as bringing changes across hundreds of systems will be challenging. When designing applications, you need to use the most common technique that is used across the organization, which will help to remove the everyday challenges. You also need to make sure that the application is upgradable in order to adopt new technology, and able to plug in components that are built in a different platform.
A RESTful service model is pretty popular when teams are free to use any technology for their development, the only thing they need to provide is a URL with which their services can be accessed. Even legacy systems such as mainframes can be integrated into the new system using an API wrapper around it and overcome technology challenges.
You can see how the MVP approach helps to utilize limited resources in an efficient way, which helps to buy more time and clarify the scope. In terms of the other factors, when you put the working product in the customer's hands early, it gives you an idea of where to invest. As your application has already started generating revenue, you can present use cases to ask for more resources, as required.
[ 96 ]

Principles of Solution Architecture Design

Chapter 4

Taking an agile approach helps you to overcome various constraints and build a customercentric product. In design principles, take everything as a challenge and not an obstacle. Consider any constraint as a challenge and find a solution to solve it.

Adding security everywhere
Security is one of the essential aspects of solution design; any gap in security can have a devastating effect on business and the organization's future. The security aspect can have a significant impact on solution design, so you need to understand your security needs even before starting the application design. Security needs to include in platform readiness at the hardware level and in application development at the software level. The following are the security aspects that need to be considered during the design phase:
Physical security of data center: All IT resources in data centers should be secure from unauthorized access. Network security: The network should be secure to prevent any unauthorized server access. Identity and Access Management (IAM): Only authenticated users should have access to the application, and they can do the activity as per their authorization. Data security in-transit: Data should be secure while traveling over the network or the internet. Data security at rest: Data should be secure while stored in the database or any other storage. Security monitoring: Any security incident should be captured, and the team alerted to act.
Application design needs to balance security requirements such as encryption, and other factors such as performance and latency. Data encryption always has a performance impact as it adds a layer of additional processing because data needs to be decrypted in order to be utilized. Your application needs to accommodate the overhead of additional encryption processing without impacting overall performance. So, while designing your application, think of use cases where encryption is really required. For example, if the data is not confidential, you don't need to encrypt it.
The other aspect of application design to consider is regulatory compliance for adherence to local law. Compliance is essential if your application belongs to a regulated industry such as health care, finance, or federal government. Each compliance has its requirement, which commonly includes the protection of data and the recording of each activity for audit purposes. Your application design should build comprehensive logging, and ensure through monitoring, which will fulfill the audit requirement.
[ 97 ]

Principles of Solution Architecture Design

Chapter 4

In this section, you have learned to apply security thinking while designing and keeping any regulatory needs in mind. Security automation is another factor, which you should always implement along with your design, in order to reduce and mitigate any security incidence. However, you have a high-level overview here. You will learn more details in Chapter 8, Security Considerations.

Automating everything
Most accidents happen due to human error, which can be avoided by automation. Automation not only handles jobs efficiently, but also increases productivity and saves costs. Anything identified as a repeatable task should be automated to free up valuable human resources so that team members can spend their time on more exciting work and focus on solving a real problem. It also helps to increase team morale.
When designing a solution, think about what can be automated. Consider the following components to be automated in your solution:
Application testing: You need to test your application every time you make any changes to make sure that nothing breaks. Also, manual testing is very time consuming and requires lots of resources. It's better to think about automating repeatable test cases to speed up deployment and product launch. Automate your testing at production scale and use rolling deployment techniques, such as canary testing and A/B testing, to release changes. IT infrastructure: You can automate your infrastructure by using infrastructure as code scripting, for example, Ansible, Terraform, and Amazon CloudFormation. Automation of infrastructure allows environments to be created in minutes compared to days. Automation of infrastructure as code helps to avoid configuration errors and creates a replica of the environment. Logging, monitoring, and alerting: Monitoring is a critical component, and you want to monitor everything every time. Also, based on monitoring, you may want to take automated action such as scaling up your system or alerting your team to act. You can monitor the vast system only by using automation. You need to automate all activity monitoring and logs in order to make sure that your application is running smoothly, and that it is functioning as desired.

[ 98 ]

Principles of Solution Architecture Design

Chapter 4

Deployment automation: Deployment is a repeatable task that is very time consuming and delays the last-minute launch in many real-time scenarios. Automating your deployment pipeline by applying continuous integration and continuous deployment helps you to be agile and iterate quickly on product features with a frequent launch. Continuous deployment and continuous integration help you to make small incremental changes to your application.
Security automation: While automating everything, don't forget to add automation for security. If someone is trying to hack your application, you want to know immediately and act quickly. You want to take preventive action by automating any incoming or outgoing traffic in your system boundary and alert any suspicious activity.
Automation provides peace of mind by making sure the product is functioning without a glitch. While designing an application, always makes sure to think from an automation perspective and consider that as a critical component. You will learn more details about automation throughout the book in the coming chapters.

Summary
In this chapter, you learned about the various principles of solution architecture design which you need to apply when creating a solution design. These principles help you to take a multi-dimensional look into architecture and consider the important aspects for the success of the application.
We started the chapter with predictive and reactive patterns of scaling, along with the methodology and benefits. We also learned about building a resilient architecture that can withstand failure and recover quickly without impacting the customer experience.
Designing flexible architecture is the core of any design principle, and we learned about how to achieve a loosely coupled design in your architecture. SOA helps to build an architecture that can be easily scaled and integrated. We also covered microservice architecture, and how it is different from the traditional monolithic architecture, and its benefits.

[ 99 ]

Principles of Solution Architecture Design

Chapter 4

We then learned about the principle of data-focused design, as pretty much all applications revolve around data. You learned about different data types, with the example of storage and associated technology. Finally, you learned the design principle of security and automation, which applies everywhere and in all components.
As cloud-based services and architecture are becoming standard, in the next chapter, you will learn about cloud-native architecture and develop a cloud-oriented design. You will learn about different cloud migration strategies and how to create an effective hybrid cloud. You will also learn about the popular public cloud providers, with which you can explore cloud technologies further.

[ 100 ]

5
Cloud Migration and Hybrid
Cloud Architecture Design
So far, you have learned about various aspects of solution architecture, architecture attributes, and architecting principals. Since the cloud is a developing trend, you will see different examples from popular cloud technologies. The public cloud is becoming one of the primary destinations to host applications, so it's important not to undervalue the preposition and migration method in the cloud. In this chapter, you will learn about the various aspects of the cloud and develop cloud thinking, which will also help you understand the upcoming chapters better.
As you learned in Chapter 1, The Meaning of Solution Architecture, cloud computing refers to the on-demand delivery of IT resources over the web, and you pay as you utilize resources. The public cloud helps you acquire technologies such as compute, storage, network, and databases on an as-needed basis, instead of buying and maintaining your own data centers.
With cloud computing, the cloud vendor manages and maintains the technology infrastructure in a secure environment and organizations access these resources over the web to develop and run their applications. An IT resource's capacity can go up or down instantly and organizations only pay for what they use.
Now, the cloud is becoming essential for every enterprise strategy. Almost every organization increases its spending in IT, and on top of saving cost, they convert upfront capital expenditures into operational expenditures. A lot of startups born in the last decade started in the cloud and were fueled by cloud infrastructure for rapid growth.
As an enterprise moving to the cloud, they are focusing on cloud migration strategy and hybrid cloud first before becoming cloud-native.

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

In this chapter, you will learn about the various strategies of cloud migrations and hybrid cloud by covering the following topics:
Benefits of cloud-native architecture Creating a cloud migration strategy Steps for cloud migration Creating a hybrid cloud architecture Designing a cloud-native architecture Popular public cloud choices
By the end of this chapter, you will learn about the benefits of the cloud and be able to design cloud-native architecture. You will understand different cloud migration strategies and steps. You will also learn about hybrid cloud design and popular public cloud providers.

Benefits of cloud-native architecture
In recent years, technology has been changing rapidly and new companies have been born in the cloud world, disrupting old and long-standing organizations. Rapid growth is possible because of no upfront cost involved when organizations are using the cloud, and there is less risk in experimentation due to the pay-as-you-go model of the cloud.
The cloud agile approach helps employees in an organization develop innovative thinking and implement their ideas without waiting for the long cycle of infrastructure. With the cloud, customers don't need to plan excess capacity in advance to handle their peak season, such as holiday shopping season for retailers; they have the elasticity to provision resources per demand instantly. This significantly helps reduce costs and improve the customer's experience. For any organization to stay in the competition, they have to move fast and innovatively.
With the cloud, enterprises are not only able to get their infrastructure quickly across the globe but can also access a wide variety of technologies that were never available before. These include access to cutting edge technologies such as the following:
Big data Analytics Machine learning

[ 102 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Artificial intelligence Robotics IoT (Internet of Things) Blockchain
Also, to achieve scalability and elasticity, these are some of the reasons that can trigger the initiative for cloud migration and hybrid cloud strategy:
The data center needs a technology refresh The data center's lease is ending The data center has run out of storage and compute capacity Modernization of an application Leverage cutting-edge technologies Need to optimize IT resources to save cost Disaster recovery planning Utilizing a content distribution network for the website
Every organization has a different strategy, and one size does not fit all when it comes to cloud adoption. The frequent use cases are putting development and testing environments in the cloud to add agility for developers so that they can move faster. As hosting web applications is becoming more economical and more comfortable with the cloud, organizations are using the cloud for digital transformation by hosting their websites and digital properties in the cloud.
For application accessibility, it is essential to not only build an application for the web browser but to ensure it is accessible through smart mobiles and tablets. The cloud is helping with such transformations. Data processing and analytics is another area where enterprises are utilizing the cloud since it is less expensive to collect, store, analyze, and share data with the cloud.
Building a solution architecture for the cloud is slightly different than it is for regular enterprise architecting. While moving to the cloud, you have to develop cloud thinking and understand how to leverage the in-built capabilities of the cloud. For cloud thinking, you follow the pay-as-you-go model. You need to make sure that you optimize your workload properly and run your servers when it's required.
You need to think about how to optimize costs by bringing up your workload (when needed) and choosing the right strategy for the workload, which always needs to be running. In the cloud, the solution architect needs to have a holistic view of each component regarding performance, scaling, high availability, disaster recovery, fault tolerance, security, and automation.

[ 103 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

The other areas of optimization are cloud-native monitoring and alerting mechanisms. You may not need to bring your existing third-party tool from on-premise to the cloud as you can utilize native cloud monitoring better and get rid of costly third-party licensing software. Also, now, you get to have deployment capabilities to any parts of the world in minutes, so don't restrict yourself to a particular region and utilize the global deployment model to build better high availability and disaster recovery mechanisms.
The cloud provides excellent deals for automation; you can pretty much automate everything. Automation not only reduces errors and speeds up process time to market; it also saves lots of cost by utilizing human resources efficiently and freeing them up from performing tedious and repetitive tasks. The cloud works on a shared responsibility model where cloud vendors are responsible for securing physical infrastructure. However, the security of an application and its data is entirely the customer's responsibility. Therefore, it's important to lock down your environment and keep a tab on security by utilizing cloud-native tools for monitoring, alerts, and automation.
Throughout this book, you will learn about the cloud perspective of solution architecture and get an in-depth understanding of cloud architecture. In the next section, you will learn about various strategies for cloud migration.

Creating a cloud migration strategy
As we mentioned in the previous section, there could be various reasons for migrating to the cloud, and those reasons play an essential role in your cloud migration journey. They will help you determine a migration strategy and prioritize applications. In addition to primary business drivers for cloud migration, you could have more reasons related to the data center, business, application, team, and workload for cloud migration.
Often, migration projects adopt multiple strategies and utilize different tools accordingly. The migration strategy will influence the time it takes to migrate and how the applications are grouped for the migration process. The following diagram shows some of the commonly used strategies for migrating existing applications to the cloud:

[ 104 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Cloud migration strategy
As shown in the preceding diagram, an organization can take a mix of migration strategies; for example, if an application-hosted operating system is at its end of life, then you need to upgrade the OS. You can take this opportunity to migrate to the cloud for better flexibility. In this case, most likely, you will choose the Replatform method to recompile your code into a new version of the OS and validate all its features. After you've finished testing, you can migrate the application to the OS hosted in the infrastructure provided by the cloud.
You can do a Lift and Shift of the server or application from the source environment to the cloud. Migrating a resource only needs minimal changes for it to work in the cloud. To take a more cloud-native approach, you can refactor your application to fully utilize the cloudnative feature, for example, converting monolithic into microservice. If your application is a legacy application and cannot be moved, or it is not cloud compatible, you may want to retire it and replace it with a cloud-native SaaS product or third-party solution.
[ 105 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Your business objectives will drive your decision to migrate applications and their priority and strategy for migration. For example, when cost efficiency is the main driver, the migration strategy typically involves mass migration with a heavy focus on the Lift and Shift approach. However, if the main goal is to enable agility and innovation, the cloudnative approach (such as rearchitecting and refactoring) plays a key role in the cloud migration strategy. We'll learn more about each strategy in the following subsections.

Lift and Shift migration
Lift and Shift are the fastest modes of migration, as you need minimal work to move your application. However, it does not take advantage of the cloud-native feature. Let's look at the most common migration strategies, that is, rehost, replatform, and relocate, which are often utilized to do Lift and Shift with minimal changes needing to be made to the application.

Rehost
Rehost is fast, predictable, repeatable, and economical, which makes it the most preferred method for migrating to the cloud. Rehost is one of the quickest cloud migration strategies, where the server or application is lifted and shifted from the source on-premises environment to the cloud. Minimal changes may be made to the resources during the migration process.
Customers often use rehost to migrate their applications to the cloud quickly and then focus on optimization when the resources are running in the cloud. This technique allows them to realize the cost benefits of using the cloud.
Customers typically use the rehost technique for the following reasons:
The temporary development and testing environment For when servers are running packaged software, such as SAP and Microsoft SharePoint An application doesn't have an active roadmap
While rehost is an application for packaged software and helps us move quickly into the cloud, you may need to upgrade underlying application platforms such as operating systems. In such a situation, you can use the replatform approach of cloud migration.

[ 106 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Replatform
When the operating system, server, or database version goes to its end of life from providers, then it can trigger the cloud migration project, for example, upgrading the operating system of your web server from Microsoft Windows 2003 to Microsoft Windows 2008/2012/2016 or upgrading your Oracle database engine, and so on. Replatform involves upgrading the platform as a part of the cloud migration project. You can decide to update your operating system or application to a newer release as part of the migration.
When using the replatform migration strategy, you may need to reinstall your application on the target environment, which triggers application changes. This requires thorough testing on your application after replatform to ensure and validate its post-migration operational efficiency.
The following common reasons warrant the use of the replatform technique:
Changing the operating system from 32-bit to 64-bit OS Changing the database engine Updating the latest release of the application Upgrading an operating system from Windows 2008 to Windows 2012 or 2016 Upgrading the Oracle database engine from Oracle 8 to Oracle 11 To get the benefits of managed services that are available from cloud vendors such as managed storage, databases, application deployment, and monitoring tools
Replatform helps you advance your application's underlying platform while migrating to the cloud. You can simply relocate your application to the cloud if it was deployed in containers or VMware. Now, let's learn more about the Relocate strategy.

Relocate
You may deploy your application using containers or VMware appliances in your onpremise data center. You can move such workloads to the cloud using the accelerate migrations strategy known as relocate. Relocate helps you move hundreds of applications in days. You can quickly relocate applications based on VMware and container technologies to the cloud with minimal effort and complexity.

[ 107 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

The relocation strategy does not require much upfront developer investment or an expensive test schedule since it provides the agility and automation you expect from the cloud. You need to determine existing configurations and use VMotion or Docker to relocate your servers to the cloud. VMotion is known for live migration. It's a VMware technology that enables a virtual instance to be moved from one physical host server to another without any interruption in the service.
Customers typically use the relocating technique for the following reasons:
Workloads have been deployed in the container Applications have been deployed in VMware appliances
VMware Cloud (VMC) on AWS not only migrates applications, but it migrates thousands of virtual machines, live from individual application to your entire data centers. While migrating your application to the cloud, you may want to take the opportunity to rebuild and rearchitect your entire application to make it more cloud-native. The cloud-native approach allows you to use the full capability of the cloud. Let's learn more about the cloud-native approach.

Cloud-native approach
When your team decides to move cloud-native for the short term, it seems like more upfront work and slower migration to the cloud. This is a bit costly, but it pays off in the long term when you start using all the cloud benefits with the agile team to innovate.
You will see a drastic decrease in cost over time with the cloud-native approach as you can optimize your workload for the right price while keeping performance intact with the pay as you go model. Cloud-native includes containerizing your application by rearchitecting as a microservice or opting for a purely serverless approach.
For your business needs, you may want to replace the entire product with a ready-touse SaaS offering, for example, replacing on-premise Sales and HR solutions with Salesforce and Workday SaaS offerings. Let's learn more about the refactor and repurchase methods for the cloud-native migration approach.

[ 108 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Refactor
Refactor involves rearchitecting and rewriting an application before migrating it to the cloud to make it a cloud-native application. Cloud-native applications are applications that have been designed, architected, and built to perform efficiently in a cloud environment. The benefits of these cloud-inherent capabilities include scalability, security, agility, and costefficiency.
Refactoring requires more time and resources to recode the application and re-architecture it before it can be migrated. This approach is commonly used by organizations that have extensive cloud experience or a highly skilled workforce. An alternative option for refactoring is to migrate your application to the cloud and then optimize it.
Common examples of refactoring include the following:
Changing platforms such as AIX to UNIX Database transition from traditional to the cloud build Replacing middleware products Rearchitecting the application from monolithic to microservice Rebuilding application architecture such as containerizing or serverless Recoding application components
Sometimes, you may find a large effort being made to rebuild an application. As an architect, you should evaluate if purchasing the Software-As-A-Service (SaaS) product helps you get a better return on investment (ROI). Let's explore the repurchase strategy in more detail.

Repurchase
When your IT resources and projects are migrated to the cloud, you may need servers or applications, which requires you to purchase a cloud-compatible license or release. For example, the current on-premises license for your application might not be valid when you run the application in the cloud.
There are multiple ways to address such scenarios of licensing. You can purchase a new license and continue to use your application in the cloud, or you can drop the existing application and replace it with another one in the cloud. This replacement could be a SaaS offering of the same application.

[ 109 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Common examples of repurchase include the following:
Replacing the application with a SaaS such as Salesforce CRM or Workday HR Purchasing a cloud-compatible license
The cloud may not be the answer for all of your problems and sometimes, you will find a legacy application that may not benefit from cloud migration or discover rarely used applications that can be retired. Let's learn about the retain or retire strategy in more detail.

Retain or retire
When you are planning a cloud migration, it may not be necessary to move all the applications. You may need to retain some applications due to technology constraints; for instance, they may be legacy applications coupled with an on-premise server and cannot move. On the other hand, you may want to retire some applications and use cloud-native capabilities, for example, third-party application monitoring and alerting system. Let's learn more about the retain or retire decision.
Retain
You might encounter a few applications in your on-premises environment that are essential for your business but are not suitable for migration because of technical reasons, such as the OS/application not being supported on a cloud platform. In such situations, your application cannot be migrated to the cloud, but you can continue running it in your onpremises environment.
For such servers and applications, you may need to perform only the initial analysis to determine their suitability for cloud migration. However, the server or application may still have dependencies with applications that are migrated. Therefore, you may have to maintain the connectivity of these on-premises servers to your cloud environment. You will learn more about on-premises to cloud connectivity in the Creating a hybrid cloud architecture section of this chapter.
Some typical workload examples for retentions are as follows:
The legacy application where the customer doesn't see the benefit of moving to the cloud. The operating system or application support is not available in the cloud such as AS400 and mainframe application.

[ 110 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

You may want to retain complex legacy systems to on-premise and prioritize them so that they can be moved a later point; however, during discovery, often, organizations find applications that are not in use anymore but still sitting around and consuming infrastructure space. You can choose to retire such applications. Let's explore more about the retiring strategy.

Retire
While migrating to the cloud, you may discover the following:
Rarely used applications Applications consuming an excessive amount of server capacity Applications that may not be required due to cloud incompatibility
In such a situation, you may want to retire the existing workload and take a fresh approach, which is more cloud-native.
A retirement strategy can be applied to hosts and applications that are soon going to be decommissioned. This can also be applied to unnecessary and redundant hosts and applications. Depending on your business needs, such applications can be decommissioned on-premises without even migrating to the cloud. Hosts and applications that are commonly suited for retirement include the following:
On-premise servers and storage for disaster recovery purposes Server consolidation to resolve redundancies Duplicate resources due to mergers and acquisitions Alternative hosts in a typical high-availability setup Third-party licensed tools such as workload monitoring and automation, which is available as in-built capabilities in the cloud
Most migration projects employ multiple strategies, and there are different tools available for each strategy. The migration strategy will influence the time it takes to migrate and how the applications are grouped for the migration process.

[ 111 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Cloud migration is a good time to examine your overall inventory and get rid of the ghost server running under the developer desk and going unaccounted for. Often, the customer sees the typically unseen advantage of optimizing the workload and tightening security while running application discovery to prepare for migration. There are multiple phases involved in cloud migration. In the next section, you will learn about the steps for cloud migration.

Steps for cloud migration
In the previous section, you learned about different migration strategies and grouped your application in order to apply the appropriate migration technique. Since you may need to perform and manage multiple applications in the cloud, it's better to set up a cloud Center of Excellence (CoE) and standardize this process with a cloud migration factory.
The cloud CoE includes experienced people from various IT and business teams across the organization that act as a dedicated cloud team focused on accelerating the building of cloud expertise in the organization. The cloud migration factory defines migration processes and tools, as well as the steps that need to be taken, as shown in the following diagram:

Cloud migration steps
[ 112 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

As shown in the previous diagram, the cloud migration steps include the following:
Discover: Discovery of cloud migration portfolios and on-premise workloads Analyze: Analyze discovered data and workloads Plan: Plan migration to the cloud and define the migration strategy Design: Design the application as per the migration strategy Migrate: Execute the migration strategy Integrate: Integrate with dependencies Validate: Validate functionality after migration Operate: Plan to operate in the cloud Optimize: Optimize your workload for the cloud
One of the initial steps of a cloud migration project is to assess and prioritize the applications for migration. To accomplish this, you need to get a complete inventory of the IT assets in your environment to determine which servers, applications, and business units are suitable for migrating to the cloud, prioritize the migration plan, and determine a migration strategy for these applications. Let's drill down each step and learn more about them.

Discovering your workload
In the discovery phase of your migration project, you discover and capture detailed data about your cloud migration portfolio, for example, the scope of your migration project. You identify servers and applications in your portfolio, as well as their interdependencies and current baseline performance metrics. Then, you analyze the gathered information to determine application connectivity and capacity requirements, which can guide you in designing and architecting the target cloud environment and identifying the cost.
A detailed discovery can also help in identifying any issues in the current state of the application that might need mitigation before you migrate to the cloud. While analyzing the discovery data, you will also determine an appropriate migration method for your application. Portfolio discovery is the process of identifying all the IT assets that are involved in your cloud migration project, including servers and applications, their dependencies, and performance metrics.

[ 113 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

You will also need to gather business details about your resources, such as the Net Present Value (NPV) of the resource, the refresh cycle of the application, the roadmap of the application, and the business criticality of the server or application. These details will help you determine your migration strategy and create a migration plan. In most organizations, these details are maintained across multiple business units and teams. Therefore, during the process of discovery, you may have to interact with various teams, such as business, development, data center, network, and finance.
It is essential to understand that your discovery landscape will depend on various factors:
What has already been migrated to the cloud? What application dependencies are there, along with resources and assets? What are the business drivers for cloud migration? What is the estimated duration for the entire migration project? How many phases is the migration process going to happen in?
One of the top challenges of a migration project is determining interdependencies among applications, particularly since they pertain to Input/Output (I/O) operations and communications. Cloud migration becomes even more challenging as organizations expand due to mergers, acquisitions, and growth. Organizations often do not have complete information about the following:
The inventory of the number of servers Server specifications such as the type and version of OS, RAM, CPU, and disk Server utilization and performance metrics Server dependencies Overall networking details
Performing a thorough portfolio discovery helps in answering questions such as the following:
Which applications, business units, and data centers are good candidates for migration? How suitable are the applications for migrating to the cloud? What known or unknown risks are associated with migrating an application to the cloud? How should the applications be prioritized for migration?

[ 114 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Which other IT assets is the application dependent on? What is the best migration strategy for the application? Is it better to have some downtime for the application than to perform a live migration due to its dependencies and risks?
Several tools are available in the market that can help automate the discovery process and provide more detailed information in a variety of formats. These tools can be classified based on various characteristics, such as deployment type, operation, support, and type of data discovered and reported.
Most of the available solutions can be broadly classified into two categories:
Agent-based solutions: They require their software client to be installed on a server to gather the necessary details. Agentless solutions: They may be able to capture this information without any additional installations.
Some solutions perform port scanning to probe a server or host for open ports, while others perform packet scanning, which often involves capturing and analyzing network packets to decode the information. The tools also vary based on the granularity of the data that's discovered, the storage types, and the reporting options. For example, some tools can provide a higher stack of intelligence beyond the network and can also determine the type of applications running.
The complexity of the discovery process depends on the organization's workload and if they already have a well-maintained inventory in place. Discovery processes are typically run for at least a couple of weeks to gather more holistic information about your environment. Once you discover all the necessary information, you need to analyze it. Let's look at the analysis step in more detail.

Analyzing the information
To identify server and application dependencies, you need to analyze the network connectivity data, port connections, system, and process information on the hosts. Depending on your tool, you can visualize all the contacts from a server to identify its dependencies, or you can run queries to list all the servers running a specific process, using a particular port, or talking to a specific host.

[ 115 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

To group your servers and applications for migration scheduling, you need to identify patterns in your host configurations. Often, some prefixes are embedded in the server hostnames to signify their association with a particular workload, business unit, application, or requirement. Some environments might also use tags and other metadata to associate such details with the host.
To right-size your target environment, you can analyze the performance metrics for your servers and applications:
If a server is over-provisioned, you can revise your right-size mapping information. You can also optimize this process by leveraging the utilization data for the server/application instead of the server specifications. If a server is under-provisioned, you might assign a higher priority to the server to migrate to the cloud.
Depending on the environment, the type of data that's captured during the discovery process might vary. The data analyzed for migration planning is to determine target network details such as firewall configuration and workload distribution and also the phase, in which the application will be migrated.
You can combine this insight with the availability of your resources and business requirements to prioritize your cloud migration workload. This insight can help you in determining the number of servers to be included as part of each cloud migration sprint.
Based on the discovery and analysis of your cloud migration portfolio, you can determine an appropriate cloud migration strategy for your applications. For instance, servers and applications that are less complex and running on a supported OS might be suitable candidates for a Lift and Shift strategy. Servers or applications that run on unsupported OS might need further analysis to determine an appropriate strategy.
In a cloud migration project, discovery, analysis, and planning are tightly integrated. You are performing a full discovery of your cloud migration portfolio and analyzing the data to create a migration plan. By the end of the analysis phase, based on your analysis and the details you've gathered from business owners, you should be able to do the following for each server/application that is part of your cloud migration portfolio:
Choose a migration strategy for the server/application, depending on your organization's cloud adoption strategy. You may be limited to specific choices within retaining, retire, repurchase, rehost, replatform, and refactor. Assign a priority for migrating the resource to the cloud. Eventually, all the resources that are part of the cloud migration portfolio may migrate to the cloud, but this priority will determine the urgency of that migration. A higher priority resource might move earlier in the migration schedule.

[ 116 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Document the business driver for migrating the resource to the cloud, which will drive the need and priority for migrating the resource to the cloud.
Let's look at migration planning in more detail.

Creating migration plan
The next phase in your migration project is planning cloud migration. You will use the information you gathered during the portfolio discovery phase to create an efficient migration plan. By the end of this phase in your migration project, you should be able to create an ordered backlog of applications that can migrate to the cloud.
The main goals of the migration planning phase include the following:
Choosing a migration strategy Defining the success criteria for the migration Determining the right-sizing of the resources in the cloud Determining a priority for applications to migrate to the cloud Identifying migration patterns Creating a detailed migration plan, checklist, and schedule Creating migration sprint teams Identifying tools for migration
In preparation for the migration planning phase, you must perform a detailed discovery of all the IT assets that are part of your cloud migration portfolio. The target destination environment in the cloud is also architected before the planning phase. Migration planning includes determining the cloud account structure and creating a network structure for your application. It is also essential to understand hybrid connectivity with the target cloud environment. Hybrid connectivity will help you plan for applications that might have dependencies with resources that are still running on-premise.

[ 117 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

The order of application migration can be determined through three high-level steps:
1. Evaluate each application across several business and technical dimensions associated with a potential migration to accurately quantify the environment.
2. Identify the dependencies for each application with qualifications such as locked, tightly coupled, and loosely coupled to identify any dependency-based ordering requirements.
3. Determine the desired prioritization strategy of the organization to determine the appropriate relative weighting of the various dimensions.
The initiation of an application or server migration depends on two factors:
First, the prioritization strategy of your organization and the application priority. Your organization might place varying emphasis on a few dimensions, such as maximizing ROI, minimizing risk, ease of migration, or another custom dimension. Second, the insight gained through the portfolio discovery and analysis phase can help you identify application patterns that match its strategy.
For example, if the organizational strategy is to minimize the risk, then business criticality will have more weight in identifying the applications. If ease of migration is the strategy, applications that can be migrated using rehost will have higher priority. The outcome of planning should be an ordered list of applications that can be used to schedule the cloud migration.
The following are the planning aspects of migration:
Gather baseline performance metrics for your applications before migration. Performance metrics will help you design or optimize your application architecture in the cloud quantitatively. You might have captured most of these performance details during the discovery phase. Create test plans and user acceptance plans for your applications. These plans will help in determining the outcome (success or failure) of the migration process. You also need to have cutover strategies and rollback plans that define how and where the applications will continue to run based on the outcome of the migration. Operations and management plans will be useful for determining the ownership of roles during migration and post-migration. You can leverage RACI matrix spreadsheets to define these roles and responsibilities for your application that span the entire cloud migration journey.

[ 118 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Identify points of contact within the application team that can provide timely support in case of escalations. Close collaboration across the teams will ensure the successful completion of the migration per schedule (sprint).
If your organization has some of these processes already documented for your existing onpremises environment, for example, change control process, test plans, and run books for operations and management, you might be able to leverage them.
You need to compare performance and cost before, during, and after migration, which can be an indication that they are not currently capturing enough of the right Key Performance Indicators (KPIs) to enable this insight. The customer needs to identify and begin achieving useful KPIs so that there is a baseline to compare against during and after migration. The KPI approach in migration has a twofold goal. First, it needs to define the capabilities of your existing application and then compare them with the cloud infrastructure.
When the new products are added to the catalog or a new service is launched, it increases your company revenue, and that's a count against company KPI. Generally, IT metrics include the quality of the product and the number of bugs that are reported for an application. Service-Level Agreement (SLA) defined for fixing a critical bug, system downtime, and performance metrics include system resource utilization values such as memory utilization, CPU utilization, disk utilization, and network utilization.
You can use a continuous delivery methodology such as Scrum to efficiently migrate applications to the cloud. With the help of the Scrum methodology, you can create multiple sprints and add your applications to the sprint backlogs based on prioritization. You can sometimes combine many applications that follow a similar migration strategy and are possibly related to each other. Typically, you would maintain a constant duration across sprints and vary the application based on factors such as sprint team size and the complexity of the application.
If you have small teams that have in-depth knowledge about the applications that need to be migrated, then you can use weekly sprints, where each sprint consists of the discover/analyze, plan/design, and migrate phases, with a final cutover on the last day of the sprint. However, as the team iterates through the sprints, the workload in each sprint can increase because the teams have now gained experience in the migration process and can incorporate the feedback from previous sprints to make the current sprint more efficient with continuous learning and adaptation.
If you are migrating a complex application, you could also use the entire week for just the plan/design phase and perform the other phases in separate sprints. Tasks that you perform within the sprint and their deliverables can vary, depending on factors such as complexity and team size. The key is to get some values from the sprint.

[ 119 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

You can create multiple teams to assist in the migration process, depending on various factors such as your product backlog, migration strategy, and organizational structure. Some customers create groups focused on each migration strategy such as a Rehost team, a Refactor team, and a Replatform team. You could also have a team specialized in optimizing your application architecture in the cloud. The multi-team strategy is the preferred model for organizations that have a large number of applications to be migrated to the cloud.
The team can be divided into the following segments:
First, the team can validate the essential components to ensure your environment (dev, test, or prod) is working, adequately maintained, and monitored. The integration team will determine the application configuration and also find the dependencies, which will help reduce the waste that's made by another team. The Lift and Shift migration sprint team migrates large applications that don't require refactoring or replatforming. The team will use automation tools to deliver small incremental value after every sprint. The replatform migration sprint team focuses on application architecture changes in order to migrate applications to the cloud, for example, modernizing application design for microservices or updating the operating system to the latest version. The refactor migration sprint team is responsible for managing various migration environments such as production, testing, and development. They make sure all the environments are scalable and functioning as required by monitoring them closely. The innovation migration sprint teamworks collaboratively with groups such as the foundation and transition team to develop a package solution that can be used by other groups.
It's recommended that you run a pilot migration project while planning and continuously building a product backlog so that these adaptations and lessons learned can be incorporated into the new plan. The successful results of the pilot project and sprint can also be used to help secure stakeholders buy-in for the cloud transformation program.

[ 120 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Designing the application
During the design phase, your focus should be on successfully migrating applications and making sure your application design to meet the required success criteria is up to date after it has been migrated to the cloud. For example, if you are maintaining user sessions in the on-premise application server (so that it can scale horizontally), make sure that a similar architecture is implemented in the cloud after the migration, which defines the success criteria.
It is essential to understand that the primary goal of this phase is to ensure that your application has been designed to meet the migration success criteria. You need to identify opportunities that enhance your application, and these can be accomplished and achieved during the optimization phase.
For migration, first, you need to have a complete understanding of your organization's foundational architecture on-premises and in the cloud, which includes the following:
User account Network configuration Network connectivity Security Governance Monitoring
Knowledge of these components will help you to create and maintain a new architect for your application. For example, if your application handles sensitive information such as Personally Identifiable Information (PII) and has control access, this means your architecture needs a specific network setting.
During the design phase, you will identify the architecture gap and enhance your architecture as per your application requirements. When you have multiple accounts, each account may have some level of relationship or dependency; for example, you can have a security account to ensure that all your resources are compliant with company-wide security guidelines.
When thinking about your application's network design, you need to consider the following:
Network packet flows entering the boundaries of your application External and internal traffic routing Firewall rules for network protection Application isolation from the internet and other internal applications
[ 121 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Overall network compliance and governance Network log and flow audit Separation of application risk levels, as per their exposure to data and users DDoS attack protection and prevention Network requirements for production and non-production environments SaaS-based multi-tenancy application access requirements Network boundaries at the business unit level in an organization Billing and implementation of the shared services model across the business unit
You can consider hybrid connectivity options with an on-premise system, depending on your connectivity needs. To build and maintain a secure, reliable, performant, and costoptimized architecture in the cloud, you need to apply best practices. Review your cloud foundational architecture against the cloud best practices before migrating to the cloud.
Chapter 4, Principles of Solution Architecture Design, highlights common architectural design patterns that you can consider when migrating your application to the cloud. It is important to emphasize here that the primary goal of the design phase in the migration process is to design your application architecture so that it meets the migration success criteria identified in the planning phase. Your application can be further optimized during the optimization phase of the migration project.
In the process of migrating to the cloud, you can design your application architecture so that it benefits from the global cloud infrastructure and increases proximity to your end users, mitigates risk, improves security, and addresses data residency constraints. Systems that are expected to grow over time should be built on top of a scalable architecture that can support growth in users, traffic, or data with no drop in performance.
For applications that need to maintain some state information, you could make specific components of the architecture stateless. If there are any layers in the architecture that need to be stateful, you could leverage techniques such as session affinity to be still able to scale such components. Leverage a distributed processing approach for applications that process vast amounts of data.
Another approach to reducing the operational complexity of running applications is using serverless architectures. These architectures can also reduce cost because you are neither paying for underutilized servers nor provisioning redundant infrastructure to implement high availability. You will learn more about the serverless architecture in Chapter 6, Solution Architecture Design Patterns.

[ 122 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

The following diagram shows a migration design from on-premise to AWS Cloud:

On-premise to AWS Cloud architecture
In the preceding diagram, as part of the cloud migration strategy, it was determined to rehost the web servers and introduce autoscaling to provide the elasticity that can help meet the spikes in demand. Elastic load balancers are also added to distribute the incoming traffic to the web server instances. The application servers were migrated using refactor, and the platform for the database tier changed from the traditional database to a cloudnative Amazon RDS. The entire architecture is distributed across multiple availability zones to provide high availability, and the database replicates to a standby instance in the second availability zone.
As an output of your design phase, you should create a detailed design document for the architecture of your application in the cloud. The design document should include details such as the user account that the application must migrate to, network configuration, and a list of users, groups, and applications that need access to the data held by this application. The design document should clearly articulate application hosting details and applicationspecific requirements for backup, licensing, monitoring, security, compliance, patching, and maintenance. Ensure that you create a design document for each application. You will need it during the migration validation phase to perform a basic cloud functionality check and an application functionality check.
[ 123 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Performing application migration to the cloud
Before executing on migration, ensure that you have a migration plan and that you have identified the sprint teams and schedules, created a prioritized backlog, and notified all the application stakeholders about the migration schedule, timelines, and their roles and responsibilities. You must also ensure that the target environment in the cloud has already been set up with the foundational architecture and core services. You might have some application-specific pre-steps, such as performing a backup or sync before migration, shutting down the servers, or unmounting disks and devices from the server.
Make sure you have good network connectivity with the cloud environment during the migration process. A good estimate of the amount of data that needs to be migrated also helps you properly estimate the time it will take to migrate your data to the cloud, given other factors such as bandwidth and network connectivity. You also need to understand the tools that are available to perform the migration. Given the number of devices that are available in the market, you might have to narrow down the selection criteria based on your requirements and other constraints.
As you know, rehost is often the fastest way to migrate your application to the cloud. When the application is running in the cloud, you can further optimize it to leverage all the benefits that the cloud has to offer. By quickly migrating your applications to the cloud, you may start realizing the cost and agility benefits sooner.
Depending on the migration strategy, you typically migrate the entire server, including the application and the infrastructure that the application is running on, or just the data that belongs to an application. Let's look at how to migrate data and servers.

Data migration
Cloud data migration refers to the process of moving existing data to a new cloud storage location. Most applications will require data storage throughout their progression into the cloud. Storage migration typically aligns with one of two approaches, but organizations may perform both at the same time:
First, a single lift-and-shift move. This may be required before new applications can be started up in the cloud. Second, a hybrid model weighted toward the cloud, which results in newly architected cloud-native projects with some legacy on-premises data. The legacy data stores may shift toward the cloud over time.

[ 124 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

However, your approach to migrating data will vary. It depends on factors such as the amount of data, network and bandwidth constraints, the data classification tier such as backup data, mission-critical data, data warehouses, or archive data, and the amount of time you can allocate for the migration process.
If you have extensive archives of data or data lakes in a situation where bandwidth and data volumes are unrealistic, you might want to Lift and Shift the data from its current location straight into a cloud provider's data centers. You can do this either by using dedicated network connections to accelerate network transfers or by physically transferring the data.
If your data stores can gradually migrate over time, or when new data is aggregating from many non-cloud sources, consider methods that provide a friendly interface to cloud storage service. These migration services can leverage or complement existing installations such as backup and recovery software or a Storage Area Network (SAN).
For a small-scale database, one-step migration is the best option, which requires you to shut down the application for 2 to 4 days. During the downtime, all information from the database is extracted and migrated to the destination database in the cloud. Once the database has been migrated, it needs to be validated with the source database for no data loss. After that, a final cutover can be completed.
In the other case, if a system requires minimal downtime, a two-step migration process is more commonly used for databases of any size:
In the first step, information is extracted from the source database. In the next step, data is migrated while the database is still up and running.
In the entire process, there is no downtime. After the migration task has been completed, you can perform functionality and performance tests for connectivity to external applications or any other criteria as needed.

During this time, because the source database is still up and running, changes will need to be propagated or replicated before the final cutover. At this point, you would schedule downtime for the database, usually a few hours, and synchronize the source and destination databases. After all the change data has been transferred to the target database, you should perform data validation to ensure a successful migration and finally route application traffic to a new cloud database.

[ 125 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

You might have mission-critical databases that cannot have any downtime. Performing such zero-downtime migrations requires detailed planning and the appropriate data replication tools. You will need to use continuous data replication tools for such scenarios. It is important to note here that source database latency can be impacted in the case of synchronous replication as it waits for data to be replicated everywhere before responding to the application while the replication is happening.
You can use asynchronous replication if your database downtime is only for a few minutes. With the zero-downtime migration, you have more flexibility regarding when to perform the cutover since the source and target databases are always in sync.

Server migration
There are several methods you can use to migrate a server to the cloud:
The host or OS cloning technique involves installing an agent on the source system that will clone the OS image of the system. A snapshot is created on the source system and then sent to the target system. This type of cloning is used for a one-time migration. With the OS Copy method, all operating system files are copied from the source machine and hosted on a cloud instance. For the OS Copy method to be effective, the people and/or tool that executes the migration must understand the underlying OS environment.
The Disaster Recovery (DR) replication technique deploys an agent on the source system that's used to replicate data to the target. However, the data is replicated at the filesystem or block level. A few solutions continuously replicate the data to target volumes, offering a continuous data replication solution. With the Disk Copy method, the disk volume is copied in its entirety. Once the disk volume has been captured, it can be loaded into the cloud as volumes, which can then be attached to a cloud instance.
For virtual machines, you could use agentless techniques to export/import your virtual machine into the cloud. With the VM Copy method, the on-premise virtual machine image is copied. If the on-premise servers are running as virtual machines, such as VMware or OpenStack, then you can copy the VM image and import it into the cloud as a machine image. One main benefit of this technique is that you can have server backup images that can be launched over and over again.

[ 126 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

With the User Data Copy method, only the application's user data is copied. Once the data has been exported from the original server, you can choose one of three migration strategies--repurchase, replatform, or refactor. The User Data Copy method is only viable for those who know the application's internals. However, because it only extracts user data, the User Data Copy method is an OS-agnostic technique.
You can containerize your application and then redeploy it in the cloud. With the containerization method, both the application binary and user data are copied. Once the application binary and user data have been copied, it can be run on a container runtime that is hosted on the cloud. Because the underlying platform is different, this is an example of the replatform migration strategy.
Several migration tools in the market can help you migrate your data and/or server to the cloud. Some tools take a DR strategy for migration, and some DR tools also support continuous replication to facilitate live migrations. There are some that specialize in forklifting your servers, performing database migrations across platforms, or database schema conversion. The tool must be able to support business processes that you are comfortable with, and you must have the operational staff to manage it.

Integration, validation, and cutover
Migration, integration, and validation go hand in hand as you want to do continuous validation while performing various integration with your application in the cloud.
The team starts by performing the necessary cloud functionality checks to ensure that the application is running with proper network configuration (in the desired geolocation) with some designated traffic flow. Instances can start or stop as desired when the basic cloud functionality check is complete. You need to validate that the server configuration (such as RAM, CPU, and hard disk) is the same as intended.
Some knowledge of the application and its functionality is required to perform these checks. When the primary check is complete, then you can perform integration tests for the application. These integration tests include checking integration with external dependencies and applications; for example, to make sure the application can connect to the Active Directory, Customer Relationship Management (CRM), patch or configuration management servers, and shared services. When integration validation is successful, the application is ready for cutover.

[ 127 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

During the integration phase, you integrate the application and migrate it to the cloud with external dependencies to validate its functionality. For example, your application might have to communicate with an Active Directory server, a configuration management server, or shared services resources that are all external to the application. Your application may also need to be integrated with external applications that belong to your clients or vendors, such as a supplier receiving a feed from your APIs after a purchase order placement.
When the integration process is complete, you need to validate the integration by performing unit tests, smoke tests, and user acceptance test (UAT). The results from these tests help you get approval from the application and business owners. The final step of the integration and validation phase includes a sign-off process from the application and business owner of the application, which will allow you to cut over the application from on-premises to the cloud.
The final phase of the cloud migration factory is the cutover process. In this phase, you take the necessary steps to redirect your application traffic from the source on-premise environment to the target cloud environment. Depending on the type of data or server migration (one-step, two-step, or zero-downtime migration), the steps in your cutover process may vary. Some factors to consider when determining a cutover strategy include the following:
Acceptable downtime for the application The frequency of the data update Data access patterns such as read-only or static data Application-specific requirements such as database syncs, backups, and DNS name resolutions Business constraints, such as the day or time during which the cutover can happen and the criticality of the data Changing management guidelines and approvals
Live migration is most popular for business-critical workload migration, let's learn more about it.

Live migration cutover
The following diagram illustrates a cutover strategy for live zero-downtime migration. In this method, the data is continuously replicated to the destination, and you perform most of the functional validation and integration testing at the destination while the application is still up and running:

[ 128 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Live migration cutover using blue-green deployment
In the replication process, the source on-premise database and target cloud database are always in sync. When all the integration and validation tests are completed successfully and the application is ready for cutover, you can take a blue-green approach to do the cutover. You will learn more about blue-green deployments in Chapter 12, DevOps and Solution Architecture Framework.
Initially, the application continues to run both on-premises and in the cloud, resulting in traffic being distributed between the two sides. You can increase traffic to cloud applications gradually until all the traffic is directed to the new application, thus resulting in a cutover with no downtime.
The other most commonly used cutover strategies involve some downtime. You schedule downtime for the application, pause the traffic, take the application offline, and perform a final sync. After the final sync, it might be a good idea to perform a quick smoke test on the destination side. At this point, you can redirect the traffic from the source to the application running in cloud, thus completing the cutover.
[ 129 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Operating cloud application
The operation phase of the migration process helps you to allow, run, use, and operate applications in the cloud to the level agreed upon with the business stakeholders. Most organizations typically already have guidelines defined for their on-premises environments. This operational excellence procedure will help you identify the process changes and training that will allow operations to support the goals of cloud adoption.
Let's discuss the differences between deploying complex computing systems in a data center versus deploying them in the cloud. In a data center environment, the burden of building out the physical infrastructure for a project falls on the company's IT department. This means you need to make sure that you have the appropriate physical environmental safeguards for your servers, such as power and cooling, that you can physically safeguard these assets, and that you have maintained multiple redundant facilities at various locations to reduce the chances of a disaster.
The downside of the data center approach is that it requires significant investment; it can be challenging to secure the resources that are necessary if you wish to experiment with new systems and solutions.
In a cloud computing environment, this changes dramatically. Instead of your company owning the physical data center, the physical data center is managed by the cloud provider. When you want to provision a new server, you ask your cloud provider for a new server with a certain amount of memory, disk space, data I/O throughput rate, processor capability, and so on. In other words, computing resources becomes a service that you can provision, and de-provision as needed.
The following are the IT operations that you would want to address in the cloud:
Server patching Service and application logging Cloud monitoring Event management Cloud security operations Configuration management Cloud asset management Change management Business continuity with disaster recovery and high availability

[ 130 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

IT organizations typically follow standards such as Information Technology Infrastructure Library (ITIL) and Information Technology Service Management (ITSM) for most of these operations. ITSM organizes and describes the activities and processes involved in planning, creating, managing, and supporting IT services, while ITIL applies best practices to implement ITSM. You need to modernize your ITSM practices so that it can take advantage of the agility, security, and cost benefits provided by the cloud.
In traditional environments, the development team and the IT operations teamwork in their silos. The development team gathers the requirements from business owners and develops the builds. System administrators are solely responsible for operations and for meeting uptime requirements. These teams generally do not have any direct communications during the development life cycle, and each team rarely understands the processes and requirements of the other team. Each team has its own set of tools, processes, and approaches, which often leads to redundant and sometimes conflicting efforts.
In a DevOps approach, both the development team and the operations teamwork collaboratively during the build and deployment phases of the software development life cycle to share responsibilities and provide continuous feedback. The software builds are tested frequently throughout the build phase on production-like environments, which allows for the early detection of defects or bugs.
DevOps is a methodology that promotes collaboration and coordination between developers and operational teams to deliver products or services continuously. This approach is beneficial in organizations where the teams rely on multiple applications, tools, technologies, platforms, databases, devices, and so on in the process of developing or delivering a product or service. You will learn more about DevOps in Chapter 12, DevOps and Solution Architecture Framework.

Application optimization in the cloud
Optimization is a very important aspect of operating in the cloud, and this is a continuous process of improvement. In this section, you will learn about the various optimization areas. There are chapters dedicated to each optimization consideration in this book. The following are the major optimization areas:
Cost: Optimize the cost efficiency of an application or a group of applications, while considering fluctuating resource needs. You will learn more about architecture cost considerations in Chapter 11, Cost Considerations.

[ 131 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Security: Continuously review and improve security policies and processes for the organization to protect data and assets in the AWS cloud. You will learn more about architecture security considerations in Chapter 8, Security Considerations. Reliability: Optimize applications for reliability to achieve high availability and defined downtime thresholds for applications, which will aid in recovering from failures, handling increased demand, and mitigating disruptions over time. You will learn more about architecture reliability consideration in Chapter 9, Architectural Reliability Considerations. Operational excellence: Optimize operational efficiency and the ability to run and monitor systems to deliver business value and to improve supporting processes and procedures continually. You will learn more about architecture operational considerations in Chapter 10, Operational Excellence Considerations.
Performance: Optimize for performance to ensure that a system is architected to deliver efficient performance for a set of resources, such as instances, storage, databases, and space/time. You will learn more about architecture performance considerations in Chapter 7, Performance Considerations.
To optimize costs, you need to understand what is currently being deployed in your cloud environment and the price of each of those resources. By using detailed billing reports and enabling billing alerts, you can proactively monitor your costs in the cloud.
Remember that, in the public cloud, you pay for what you use. Therefore, you might be able to reduce costs by turning off instances when they are not needed. By automating your instance deployment, you can also tear down and build up the instance entirely as required.
As you offload more, you need to maintain, scale, and pay for less infrastructure. Another way to optimize costs is by designing your architecture for elasticity. Make sure you rightsize your resources, use auto-scaling, and adjust your utilization based on price and need. For example, it might be more cost-efficient for an application to use more small instances than fewer large instances.
Several application architectural modifications can help you improve the performance of your application. One way to improve the performance of your web servers is to offload your web page through caching. You can write an application that lets you cache images, JavaScript, or even full pages to provide a better experience to your users.

[ 132 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

You can design n-tier and service-oriented architectures to scale each layer and module independently, which will help optimize performance. You will learn more about this architecture pattern in Chapter 6, Solution Architecture Design Patterns.

Creating a hybrid cloud architecture
The value of the cloud is growing, and many large enterprises are moving their workload to the cloud. However, often, it's not possible to move entirely to the cloud in one day, and for most customers, this is a journey. Those customers seek a hybrid cloud model where they maintain a part of the application in an on-premise environment that needs to communicate with the cloud module.
In a hybrid deployment, you need to establish connectivity between the resources running in the on-premises environment and the cloud environment. The most common method of hybrid deployment is between the cloud and existing on-premises infrastructure to extend and grow an organization's infrastructure into the cloud while connecting cloud resources to the internal system. The common causes of setting up a hybrid cloud may include the following:
You want to have operating legacy applications in an on-premise environment while you refactor and deploy in the cloud with a blue-green deployment model. A legacy application such as a mainframe may not have a compatible cloud option and has to continue running on-premise. Need to keep part of the application on-premise due to compliance requirements. To speed up migration, keep the database on-premise and move the application server to the cloud. The customer wants to have more granular control of part of the application. Data ingestion in the cloud from on-premise for the cloud's Extract, Transform, Load (ETL) pipeline.
Cloud providers provide a mechanism for integrations between a customer's existing infrastructure and the cloud so that customers can easily use the cloud as a seamless extension to their current infrastructure investments. These hybrid architecture functionalities allow customers to do everything from integrating networking, security, and access control to powering automated workload migrations and controlling the cloud from their on-premises infrastructure management tools.

[ 133 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Taking the example of AWS Cloud, you can establish a secure connection to AWS Cloud using a VPN. Since a VPN connection is set up over the internet, there may be latency issues due to multiple router hops from third-party internet providers. You can have your fiber optics private line go to AWS Cloud for better latency using AWS Direct Connect.
As shown in the following diagram, with AWS Direct Connect, you can establish highspeed connectivity between your data center and AWS Cloud to achieve a low latency hybrid deployment:

Hybrid cloud architecture (on-premise to cloud connectivity)
As shown in the preceding diagram, AWS Direct Connect Location establishes the connectivity between the on-premises data center to AWS Cloud. This helps you achieve the customer need of having dedicated fiber-optic lines to an AWS Direct Connect location; the customer can opt for this fiber optic line from a third-party vendor such as AT&T, Verizon, or Comcast in the USA. AWS has a directly connected partner in each region of the world.
[ 134 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

At the AWS Direct Connect location, the customer fiber optic line is connected to AWS private network, which provides dedicated end-to-end connectivity from the data center to AWS Cloud. These optic lines can provide speeds of up to 10 GB/s. To secure traffic over direct connect, you can set up a VPN, which will apply IPSec encryption to the traffic flow.

Designing a cloud-native architecture
You learned about the cloud-native approach earlier in this chapter from a migration point of view, where the focus was on refactoring and rearchitecting applications when migrating to the cloud. Each organization may have a different opinion on cloud-native architecture but, at the center of it, cloud-native is all about utilizing all the cloud capabilities in the best way possible. True cloud-native architecture is about designing your application so that it can be built in the cloud from its foundations.
Cloud-native doesn't mean hosting your application in the cloud platform; it's about leveraging services and features provided by the cloud. This may include the following:
Containerizing your monolithic architecture in a microservice and creating a CI/CD pipeline for automated deployment. Building a serverless application with technology such as AWS Lambda Function as a Service (FaaS) and Amazon DynamoDB (a managed NoSQL database in the cloud). Creating a serverless data lake using Amazon S3 (managed Object Storage Service), AWS Glue (managed Spark Cluster for ETL), and Amazon Athena (managed Presto cluster for ad hoc queries). Using a cloud-native monitoring and logging service, for example, Amazon Cloud Watch. Using a cloud-native auditing service, for example, AWS CloudTrail.

[ 135 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

The following architecture is an example of a cloud-native serverless architecture for a micro-blogging application:

Cloud-native micro-blogging application architecture
The preceding diagram is utilizing cloud-native serverless services in AWS Cloud. Here, Amazon Route53, which manages the DNS service, is routing user requests. Lambda manages function as a service to handle the code for User Validation, User Profile, and Blog Page. All the blog assets are stored in Amazon S3, which manages object storage services and all user profile data stored in Amazon DynamoDB, which is managed by the NoSQL store.
As users send requests, AWS lambda validates the user and looks at their profile to ensure they have a subscription in Amazon DynamoDB; after that, it picks blog assets such as pictures, videos, and a static HTML writeup from Amazon S3 and displays them to the user. This architecture can be scaled in an unlimited manner as all services are cloud-native managed services, and you are not handling any infrastructure. Crucial factors such as high availability, disaster recovery, and scalability are taken care of by these cloud-native services so that you can focus on your feature development. In terms of cost, you will only pay if a request goes to a blogging application. If no one is browsing for the blog at night, you are not paying anything for hosting your code; you are only paying nominal cost for storage.
[ 136 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

The benefit of the cloud-native architecture is that it enables fast-paced innovation and agility in the team. It simplifies building out a complex application and infrastructure. As system administrators and developers, you focus strictly on designing and building your networks, servers, file storage, and other computing resources, and leave the physical implementation to your cloud computing provider. The cloud-native architecture provides several benefits:
Fast scale-out, on-demand: You can request the resources you need when you need them. You only pay for what you use. Replicate quickly: Infrastructure-as-a-code means you can build once and replicate more. Instead of building your infrastructure by hand, you can structure it as a series of scripts or applications. Building your infrastructure programmatically gives you the ability to build and rebuild it on demand, when needed for development or testing. Tear up and tear down easily: In the cloud, services are provided on-demand, so it's easy to build up a large experimental system. Your system may include a cluster of scalable web and application servers, multiple databases, terabytes of capacity, workflow applications, and monitoring. You can tear it all down as soon as the experiment is completed and save costs.
There are many more examples in the area of storage, networking, and automation for building the cloud-native architecture. You will learn more about this architecture in Chapter 6, Solution Architecture Design Patterns.

Popular public cloud choices
Since the cloud is becoming the norm, there are many cloud providers in the market that provide cutting-edge technology platforms that are competing to get market share. The following are the major cloud providers (at the time of writing):
Amazon Web Services (AWS): AWS is one of the oldest and largest cloud providers. AWS provides IT resources such as compute power, storage, databases, and other services on need basis over the internet with a pay as you go model. AWS not only offers IaaS; it has a broad range of offerings in PaaS and SaaS. AWS provides multiple offerings in cutting-edge technologies in the area of machine learning, artificial intelligence, blockchain, internet of things (IoT), and a comprehensive set of significant data capabilities. You can almost host any workload in AWS and combined services to design an optimal solution.

[ 137 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Microsoft Azure: Also known as Azure and like any cloud provider, it provides IT resources such as compute, network, storage, and database over the internet to their customers. Like AWS, Azure also provides IaaS, PaaS, and SaaS offerings in the cloud, which include a range of services from the computer, mobile, storage, data management, content distribution network, container, big data, machine learning, and IoT. Also, Microsoft has wrapped its popular offerings in the cloud through Microsoft Office, Microsoft Active Directory, Microsoft SharePoint, MS SQL Database, and so on.
Google Cloud Platform (GCP): GCP provides cloud offerings in the area of computing, storage, networking, and machine learning. Like AWS and Azure, they have a global network of data centers available as infrastructure as a service for their customers to consume IT resources over the internet. In compute, GCP offers Google Cloud functions for the serverless environment, which you can compare with AWS Lambda functions in AWS and Azure Cloud functions in Azure. Similarly, GCP offers multiple programming languages for application development with containers so that you can deploy application workloads.
There are many other cloud vendors available, such as Alibaba Cloud, Oracle Cloud, and IBM Cloud, but the major markets are captured by the aforementioned cloud providers. The choice of which cloud provider to use is up to the customer, which can be impacted by the availability of the functionality they are looking for or based on their existing relationship with providers. Sometimes, large enterprises choose a multi-cloud strategy to utilize the best providers.

Summary
In this chapter, you learned how the cloud is becoming the most popular mainstream application hosting and development environment for enterprises. At the beginning of this chapter, you learned about cloud thinking and how it's related to solution architecture design. Since more organizations are looking to move into the cloud, this chapter focused on various cloud migration strategies, techniques, and steps.
You learned about various cloud strategies, as per the nature of workload and migration priorities. Migration strategies include the ability to rehost and replatform your application for Lift and Shift and takes the cloud-native approach by refactoring and rearchitecting your application to take advantage of cloud-native capabilities. You may find some unused inventory during application discovery and retire it. If you choose to not migrate a certain workload then retain the application as is on-premises.

[ 138 ]

Cloud Migration and Hybrid Cloud Architecture Design

Chapter 5

Then, you learned about the steps involved in cloud migration, which help you discover your on-premise workload, analyze collected data, and create a plan to decide on which migration strategy to take. During the design phase, you create a detailed implementation plan and executed that during the migration steps, where you learned to set up connectivity with the cloud and move your application from on-premise to the cloud.
After that, you learned about how to integrate, validate, and operate your workload into the cloud after migration and apply continuous optimization for cost, security, reliability, performance, and operational excellence. The hybrid cloud architecture is an integral part of the migration process, so you learned about how to establish connectivity between onpremise and the cloud by looking at an architecture example of AWS Cloud. At the end of this chapter, you learned about significant cloud providers and their offerings.
In the next chapter, you will dive deep and learn more about various architecture design patterns, along with the reference architecture. You will learn about different architecture patterns such as multi-tier, service-oriented, serverless, and microservices.

Further reading
To learn more about the major public cloud providers, please refer to the following links:
Amazon Web Services (AWS): https://a ws.amazon.c om Google Cloud Platform (GCP): https:// c loud.google.c om Microsoft Azure: https:// azure.m icrosoft.com
Almost every cloud provider extends their learning credentials to new users, which means you can sign up with your email and try their offerings out before you choose which one to go with.

[ 139 ]

6
Solution Architecture Design
Patterns
There are multiple ways to design a solution. A solution architect needs to take the right approach based on user requirements along with the architecture constraint of cost, performance, scalability, and availability. In this chapter, you will learn about various solution architecture patterns along with reference architectures and how to apply them in real-world scenarios.
In the previous chapters, you learned about the attributes and principles of solution architecture design. This chapter is both exciting and essential as you will be able to apply your learning to various architecture design patterns. In this chapter, you will gain an understanding of some of the significant solution architecture patterns, such as layered, event-driven, microservice, loosely coupled, service-oriented, and RESTful architectures.
You will learn the advantages of various architectural designs and examples that demonstrate when to utilize them. You will also gain an understanding of architecture design anti-patterns in addition to the following architecture design patterns:
Building an n-tier layered architecture Creating multi-tenant SaaS-based architecture Building stateless and stateful architecture designs Understanding service-oriented architecture (SOA) Building serverless architecture Creating microservice architecture Building queue-based architecture Creating event-driven architecture

Solution Architecture Design Patterns

Chapter 6

Building cache-based architecture Understanding the circuit breaker pattern Implementing the bulkheads pattern Creating a floating IP pattern Deploying an application with a container Database handling in application architecture Avoiding anti-patterns in solution architecture
By the end of the chapter, you will know how to optimize your solution architecture design and apply best practices, making this chapter the center point and core of your learning.

Building an n-tier layered architecture
In n-tier architecture (also known as multitier architecture), you need to apply the principle of loosely coupled design (refer to Chapter 4, Principles of Solution Architecture Design) and attributes of scalability and elasticity (refer to Chapter 3, Attributes of the Solution Architecture). In multilayer architecture, you divide your product functions into multiple layers, such as presentation, business, database, and services, so that each layer can be implemented and scaled independently.
With multitier architecture, it is easy to adopt new technologies and make development more efficient. This layered architecture provides flexibility to add new features in each layer without disturbing features of other layers. In terms of security, you can keep each layer secure and isolated from others, so if one layer gets compromised, the other layers won't be impacted. Application troubleshooting and management also become manageable as you can quickly pinpoint where the issue is coming from and which part of the application needs to troubleshoot.
The most famous architecture in multilayer design is three-tier architecture, so let's learn more about it. The following diagram shows the most common architecture, where you interact with a web application from the browser and perform the required functions, for example, ordering your favorite T-shirt or reading a blog and leaving a comment:

[ 141 ]

Solution Architecture Design Patterns

Chapter 6

Three-tier website architecture
In the preceding architecture, you have the following three layers:
Web Layer: The web layer is the user-facing part of the application. End users interact with the web layer to collect or provide information. Application Layer: The application layer mostly contains business logic and acts upon information received from the web layer. Database Layer: All kinds of user data and application data are stored in the database layer.
Let's take a look at these layers in more detail.
The web layer
The web layer is also known as the presentation tier. The web layer provides a user interface that helps the end user to interact with the application. The web layer is your user interface (in this case, the website page), where the user enters information or browses for it. Web developers may build a presentation tier user interface in technologies such as HTML, CSS, AngularJS, Java Server Page (JSP), and Active Server Page (ASP). This tier collects the information from the user and passes it to the application layer.
[ 142 ]

Solution Architecture Design Patterns

Chapter 6

The application layer
The application layer is also known as a logic tier, as this is the core of the product where all the business logic resides. The presentation tier collects the information from the user and passes it to the logic tier to process and get a result. For example, on an e-commerce website such as Amazon.com, users can enter a date range on the order page of the website to find their order summary. In return, the web layer passes the data range information to the application layer. The application layer processes the user input to perform business logic such as the count of orders, the sum of amounts, and the number of items purchased. This returns information to the web layer to render it for the user.
Generally, in three-tier architecture, all algorithms and complex logic live in the logic tier, which includes creating a recommendation engine or showing personalized pages to the user as per their browsing history. Developers may choose to implement this layer in a server-side programming language, for example, C++, Java, .NET, or Node.js. The application layer performs logic on the data, which is stored in the database layer.

The database layer
The database layer, which is also known as the data tier, stores all the information related to user profiles and transactions. Essentially, it contains any data that needs to persist in being stored in the data tier. This information is sent back to the application layer for logic processing and then, eventually, it renders to the user in the web layer. For example, if the user is logged in to a website with their user ID and password, then the application layer verifies the user credentials with information stored in the database. If the credentials match the stored information, the user is allowed to log in and access the authorized area of the website.
The architect may choose to build a data tier in relational databases, for example, PostgreSQL, MariaDB, Oracle Database, MySQL, Microsoft SQL Server, Amazon Aurora, or Amazon RDS. The architect may also add a NoSQL database such as Amazon DynamoDB, MongoDB, or Apache Cassandra. The data tier is not only used to store transaction information but also to hold user-session information and application configuration.

[ 143 ]

Solution Architecture Design Patterns

Chapter 6

In the n-tier layered architecture diagram, you will notice that each layer has its own Auto Scaling configuration, which means it can be scaled independently. Also, each layer has a network boundary, which means having access to one layer doesn't allow access to other layers. You will learn more about security considerations in Chapter 8, Security Considerations.
When designing multitier architecture, you need to take careful consideration of how many layers should be added to your design. Each layer requires its own fleet of servers and network configurations. So, adding more layers means increasing the cost and management overhead, whereas keeping fewer layers means creating a tightly coupled architecture. The architect needs to decide the number of tiers based on application complexity and user requirement.

Creating multi-tenant SaaS-based
architecture
In the previous section, you learned about multitier architecture; however, the same architecture that is built for a single organization is also called a single tenancy. Multitenant architecture is becoming more popular as organizations adopt the digital revolution while keeping the overall application cost low. The Software-as-a-Service (SaaS) model is built on a multi-tenant architecture, where a single instance of the software and supporting infrastructure serve multiple customers. In this design, each customer shares the application and database, with each tenant isolated by their unique configuration, identity, and data. They remain invisible to each other while sharing the same product.
As multi-tenant SaaS providers own everything from the hardware to the software, SaaSbased products offload an organization's responsibilities to the maintenance and updates of the application, as this is taken care by the SaaS provider. Each customer (tenant) can customize their user interface using a configuration without any code changes. As multiple customers share a common infrastructure, they get the benefit of scale, which lowers the cost further. Some of the most popular SaaS providers are Salesforce CRM, the JIRA bug tracking tool, and Amazon QuickSight.

[ 144 ]

Solution Architecture Design Patterns

Chapter 6

As shown in the following architecture diagram, there are two organizations (tenants) using the same software and infrastructure. The SaaS vendor provides access to the application layer by allocating a unique tenant ID to each organization. Each tenant can customize their user interface as per their business needs using a simple configuration:

Multi-tenant SaaS architecture
As shown in the preceding architecture design, the presentation layer provides a user interface and the application layer holds the business logic. At the data access layer, each tenant will have data level isolation with one of the following methods:
Database Level Isolation: In this model, each tenant has its database associated with its tenant ID. When each tenant queries data from the user interface, they are redirected to their database. This model is required if the customer doesn't want a single shared database for compliance and security reasons. Table Level Isolation: This isolation level can be achieved by providing a separate table for each tenant. In this model, tables need to be uniquely assigned to each tenant, for example, with the tenant ID prefix. When each tenant queries data from the user interface, they are redirected to their tables as per their unique identifier. Row Level Isolation: In this isolation level, all tenants share the same table in a database. There is an additional column in a table where a unique tenant ID is stored against each row. When an individual tenant wants to access their data from the user interface, the data access layer of the application formulates a query based on the tenant ID to the shared table. Each tenant gets a row that belongs to their users only.
[ 145 ]

Solution Architecture Design Patterns

Chapter 6

For enterprise customers, a careful assessment of whether a SaaS solution is the right fit for them based on their unique feature's requirements. This is because, often, a SaaS model has limited customization capabilities. Additionally, we need to find the cost value proposition if a vast number of users need to subscribe. The cost comparison should be calculated based on the total cost of ownership when taking a build versus buy decision. This is because building software is not the primary business of most organizations, so the SaaS model is becoming highly popular as organizations can focus on their business and let the experts handle the IT side of it.

Building stateless and stateful architecture
designs
While designing a complex application such as an e-commerce website, you need to handle the user state to maintain activity flow, where users may be performing a chain of activities such as adding to the cart, placing an order, selecting a shipping method, and making a payment. Currently, users can use various channels to access an application, so there is a high possibility that they will be switching between devices; for example, adding items in the cart from their mobile and then completing checkout and payment from a laptop. In this situation, you would want to persist user activity across the devices and maintain their state until the transaction is complete. Therefore, your architecture design and application implementation need to plan for user session management in order to fulfill this requirement.
To persist user states and make applications stateless, user-session information needs to be stored in persistent database layers such as the NoSQL database. This state can share between multiple web servers or microservices. Traditionally, a monolithic application uses stateful architecture, where user-session information is stored in the server itself rather than via any external persistence database storage.
The session storage mechanism is the main difference between stateless and stateful application designs. Since session information in a stateful application is local to the server, it cannot be shared between other servers and also doesn't support modern microservice architecture. You will learn more about microservice-based architecture in the Creating microservice architecture section.

[ 146 ]

Solution Architecture Design Patterns

Chapter 6

Often, a stateful application doesn't support horizontal scaling very well, as the application state persists in the server which cannot be replaced. The stateful application worked well early on when the user base was not very huge. However, as the internet becomes more popular, it is reasonable to assume that you will have millions of users active on a web application. Therefore, efficient horizontal scaling is important to handle such a large user base and achieve low application latency.
In a stateful application, state information is handled by the server, so once users establish a connection with a particular server, they have to stick with it until the transaction completes. You can put a load balancer in front of the stateful application, but to do that, you have to enable sticky sessions in a load balancer. The load balancer has to route user requests to one server, where session information has been established. Enabling sticky sessions violates the load balancer's default round-robin request for the distribution method. Other issues may include lots of open connections to the server as you need to implement a session timeout for the client.
Your design approach should focus more on the shared session state using the stateless method, as it allows horizontal scaling. The following diagram shows an architecture that depicts a stateless application for a web application:

A stateless application architecture
[ 147 ]

Solution Architecture Design Patterns

Chapter 6

The preceding architecture diagram is a three-tier architecture with a web, application, and database layer. To make applications loosely coupled and scalable, all user sessions are stored persistently in the NoSQL database, for example, Amazon DynamoDB. You should use client-side storage, such as cookies, for the session ID. This architecture lets you use the scale-out pattern without having to worry about a loss of user state information. A stateless architecture removes the overhead to create and maintain user sessions and allows consistency across the application's modules. A stateless application has performance benefits too, as it reduces memory usage from the server-side end and eliminates the session timeout issue.
Adopting a stateless pattern can complicate tasks; however, with the right approach, you can achieve a rewarding experience for your user base. You can develop applications using the microservice approach with REST design patterns and deploy them in containers. For this, use authentication and authorization to connect users to the server.
You will learn more about the REST design pattern and microservices in the next section. As access to state information from multiple web servers focuses on a single location, you must use caution to prevent the performance of the data store from becoming a bottleneck.

Understanding SOA
In SOA patterns, different application components interact with each other using a communication protocol over the network. Each service provides end-to-end functionality, for example, fetching an order history. SOA is widely adopted by large systems to integrate business processes, for example, taking your payment service from the main application and putting it as a separate solution.
In a general sense, SOAs take monolithic applications and spread some of those operations out into individual services that operate independently to each other. The goal of using an SOA is to loosen the coupling of your application's services.
Sometimes, an SOA includes not just splitting services apart from one another but splitting resources into separate instances of that service. For instance, while some choose to store all of their company's data in a single database split by tables, an SOA would consider modularizing the application by function into separate databases altogether. This allows you to scale and manage throughput based on the individual needs of tables for each database.

[ 148 ]

Solution Architecture Design Patterns

Chapter 6

SOA has multiple benefits, for example, the parallelization of development, deployment, and operation. It decouples the service so that you can optimize and scale each service individually. However, it also requires more robust governance to ensure work performed by each service's team meets the same standard. With SOA, the solution could become complex enough to increase the overhead to balance that, so you need to make the right choice of tools and automation of service monitoring, deployment, and scaling.
There are multiple ways in which to implement SOA architecture. Here, you will learn about the Simple Object Access Protocol (SOAP) web service architecture and Representational State Transfer (REST) web service architecture.
Originally, SOAP was the most popular messaging protocol, but it is a bit heavyweight as it entirely relies on XML for data interchange. Now, REST architecture is becoming more popular as developers need to build more lightweight mobile and web applications. Let's learn about both architectures and their differences in more detail.

SOAP web service architecture
SOAP is a messaging protocol that is used to exchange data in a distributed environment in XML format. SOAP is a standard XML where data is transported in an envelope format called SOAP Envelope, as shown in the following diagram:

SOAP Envelope for web service data exchange
[ 149 ]

Solution Architecture Design Patterns

Chapter 6

As shown in the preceding diagram, SOAP Envelope contains two parts: SOAP Header: The SOAP header provides information on how a recipient of a SOAP message should process it. It contains authorization information to deliver the message to the right recipient and for data encoding. Message Body: The message body contains the actual message in Web Services Description Language (WSDL) specification. WSDL is an XML format file that describes the Application Programming Interface (API) contract with the message structure, API operations, and server Unique Resource Locator (URL) address. Using a WSDL service, a client application can determine where a service is being hosted and what functionality it can perform.
The following code shows an example of a SOAP envelope XML. Here, you can see both the header and message wrap up under the SOAP envelope:
<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
<env:Header>
<n:orderinfo xmlns:n="http://exampleorder.org/orderinfo">
<n:priority>1</n:priority>
<n:expires>2019-06-30T16:00:00-09:00</n:expires>
</n:orderinfo>
</env:Header>
<env:Body>
<m:order xmlns:m="http://exampleorder.org/orderinfo">
<m:getorderinfo>
<m:orderno>12345</m:oderno>
</m:getorderinfo>
</m:order>
</env:Body>
SOAP commonly uses HTTP, but other protocols such as SMTP can be used.

[ 150 ]

Solution Architecture Design Patterns

Chapter 6

The following diagram shows details about a message exchange in a web service using SOAP. Here, the web service client sends the request to the service provider who hosts the web service, and receives the response with the desired result:

SOAP-based web service
In the preceding diagram, the client is an e-commerce website user interface. The user wants their order information and hence sends the SOAP message in the XML-format to the application server with the order number. The application server hosts the order service, which then responds with the customer's order details.
In a SOAP-based web service, the service provider creates an API contract in the form of WSDL. WSDL lists all of the operations that web services can perform, such as providing order information, updating orders, deleting orders, and more. The service provider shares WSDL with web service client team, using which the client generates an acceptable message format, sends data to the service provider, and gets the desired response. The web service client fills the values in the generated XML message and sends it across to the service provider with authentication details for processing.
The implementation of a SOAP-based web service has a higher complexity and requires more bandwidth, which can impact web application performance, such as page loading time, and any major changes in the server logic require all clients to update their code. REST was created to address SOAP-based web service problems and provide a more flexible architecture. Let's learn more about RESTful architecture and why it is becoming widely popular.
[ 151 ]

Solution Architecture Design Patterns

Chapter 6

RESTful web service architecture
A RESTful web service offers better performance due to its lightweight architecture. It allows different messaging formats such as JSON, plaintext, HTML, and XML, compared to SOAP, which only allows XML. REST is an architecture style that defines the standard for loosely coupled application design using the HTTP protocol for data transmission.

JavaScript Object Notation (JSON) is a more accessible format for data exchange in REST architecture. JSON is lightweight and language independent. JSON contains a simple keyvalue pair that makes it compatible with data structures defined in most programming languages.

REST focuses on the design principle for creating a stateless service. The web service client doesn't need to generate a complex client skeleton, but it can access the web server resources using the unique Uniform Resource Identifier (URI). The client can access RESTful resources with the HTTP protocol and perform standard operations such as GET, PUT, DELETE, and POST on the resources.

Your choice of architecture design between REST and SOAP depends upon your organization's needs. The REST service offers an effective way to integrate with lightweight clients such as smartphones, while SOAP provides high security and is suitable for complex transactions. Let's take a look at the differences between REST and SOAP:

Attributes

REST

SOAP

Design

Architectural style with an informal Predefined rules with a standard

guideline

protocol

Message

Format

JSON, YAML, plaintext, and

XML, CSV

HTML,

XML

Protocol

HTTP

HTTP, SMTP, and UPD

Session State Default stateless

Default stateful

Security

HTTPS and SSL

Web Services Security and ACID compliance

Cache

Cached API calls

Cannot cache API calls

Performance Fast with fewer resources

Needs more bandwidth and compute power

Now, let's learn about a reference architecture based on service-oriented design.

[ 152 ]

Solution Architecture Design Patterns

Chapter 6

Building an SOA-based e-commerce website architecture
An e-commerce website such as Amazon.com has users from all parts of the world and a huge catalog with millions of products. Each product has multiple images, reviews, and videos. Maintaining such a big catalog for a global user base is a very challenging task.
This reference architecture follows SOA principles. Each service is operating as independently as possible from each other. This architecture can be implemented using either SOAP-based or RESTful-based web architecture:

E-commerce website SOA architecture
As shown in the preceding architecture diagram, we can take note of the following: When a user types a website address into the browser, the user request reaches out to the DNS server to load the website. The DNS requests for the website are routed by Amazon Route 53 to the server where the web applications are being hosted.
[ 153 ]

Solution Architecture Design Patterns

Chapter 6

The user base is global, and users continue browsing for products to purchase as the website has a large product catalog with static images and videos. A content distribution network such as Amazon CloudFront caches and delivers static assets to users.
The catalog contents, such as static product images and videos, along with other application data, such as log files, are stored in Amazon S3.
Users will browse the website from multiple devices, for example, they will add items in a cart from their mobile and then make a payment on a desktop. To handle user sessions, a persistent session store is required such as DynamoDB. In fact, DynamoDB is a NoSQL database where you don't need to provide a fixed schema, so it is a great storage option for product catalogs and attributes.
To provide high performance and reduce latency, Amazon ElastiCache is used as a caching layer for the product to reduce read and write operations on the database.
A convenient search feature is key for product sales and business success. Amazon Cloud Search helps to build scalable search capability by loading the product catalog from DynamoDB.
A recommendation can encourage a user to buy additional products based on their browsing history and past purchases. A separate recommendation service can consume the log data stored on Amazon S3 and provide potential product recommendations to the user.
The e-commerce application can also have multiple layers and components that require frequent deployment. AWS Elastic Beanstalk handles the autoprovisioning of the infrastructure, deploys the application, handles the load by applying Auto Scaling, and monitors the application.
In this section, you learned about SOA along with an architecture overview. Let's learn more about the critical aspect of modern architecture design with a serverless architecture.

Building serverless architecture
In a traditional scenario, if you want to develop an application, you need to have a server where your desired operating system and required software can be installed. While you are writing your code, you need to make sure that your server is up and running. During deployment, you need to add more servers to keep up with user demand and add scaling mechanisms such as Auto Scaling to manage the desired number of servers to fulfill users' requests. In this entire situation, a lot of effort goes into infrastructure management and maintenance, which has nothing to do with your business problem.

[ 154 ]

Solution Architecture Design Patterns

Chapter 6

Going serverless gives you the ability to focus on your application and write code for feature implementation without worrying about underlying infrastructure maintenance. Serverless means there is no server to run your code, which frees you up from Auto Scaling and decoupling overheads while providing a low-cost model.
A public cloud, such as AWS, provides several serverless services in the area of computer and data storage, which makes it easier to develop an end-to-end serverless application. When you talk about serverless, the first thing that comes to mind is AWS Lambda functions, which is a Function as a Service (FaaS) and is provided by AWS cloud. To make your application service-oriented, Amazon API Gateway offers you the ability to put RESTful endpoints in front of your AWS Lambda functions and helps you to expose them as microservices. Amazon DynamoDB provides a highly scalable NoSQL database, which is an entirely serverless NoSQL data store, and Amazon Simple Storage Service (S3) provides serverless object data storage.
Let's take a look at an example of a reference serverless architecture in the following architecture diagram for the delivery of a secure survey:

Serverless architecture for a secure survey delivery
In this example, a serverless architecture serves, delivers, and processes secure surveys, all on managed services:
1. First, a customer requests the website over HTTPS. The web page is served directly from Amazon S3.
[ 155 ]

Solution Architecture Design Patterns

Chapter 6

2. The customer's survey is submitted via an AJAX call to Amazon API Gateway. 3. Amazon API Gateway logs this to Amazon CloudTrail. If a survey's results are
lost, or if one of the AJAX calls includes malicious activity of some sort, these logs may be helpful in identifying and fixing the problem. 4. Amazon API Gateway then turns the AJAX call into an event trigger for an AWS Lambda function, which pulls the survey data and processes it. 5. The results of the survey are sent by the AWS Lambda function to an Amazon S3 bucket, where they are secured with server-side encryption. 6. Metadata from the survey, which does not include any personally identifiable information, is then written and stored in a DynamoDB table. This could be used for later queries and analysis.
Due to the increasing popularity of serverless architecture, you will see more reference architectures using serverless services as we move forward with this book. The concept of microservices is also becoming popular with the adoption of RESTful-style architectures. Let's learn more about REST architectures and microservices in the next sections.

Creating microservice architecture
Microservices are architected in REST-style web services and are independently scalable. This makes it easier to expand or shrink the relevant components of your system while leaving the rest untouched. A system that employs microservices can more easily withstand incidents where application availability can degrade gracefully to avoid any cascading failures. Your system becomes fault-tolerant, that is, built with failure in mind.
The clear advantage of microservices is that you have to maintain a smaller surface area of code. Microservices should always be independent. You can build each service with no external dependencies where all prerequisites are included, which reduces the interdependency between application modules and enables loose coupling.
The other overarching concept of microservices is bounded contexts, which are the blocks that combine together to make a single business domain. A business domain could be something like car manufacturing, bookselling, or social network interactions that involve a complete business process. An individual microservice defines boundaries in which all the details are encapsulated.

[ 156 ]

Solution Architecture Design Patterns

Chapter 6

Scaling each service is essential while dealing with the large-scale access of applications, where different workloads have different scaling demands. Let's learn about some best practices for designing microservice architecture:
Create a separate data store: Adopting a separate data store for each microservice allows the individual team to choose a database that works best for their service. For example, the team that handles website traffic can use a very scalable NoSQL database to store semi-structured data. The team handling order services can use a relational database to ensure data integrity and the consistency of transactions. This also helps to achieve loose coupling where changes in one database do not impact other services.
Keep servers stateless: As you learned in the previous section, Building stateless and stateful architecture designs, keeping your server stateless helps in scaling. Servers should be able to go down and be replaced easily, with minimal or no need for storing state on the servers.
Create a separate build: Creating a separate build for each microservice makes it easier for the development team to introduce new changes and improve the agility of the new feature release. This helps to make sure that the development team is only building code that is required for a particular microservice and not impacting other services.
Deploy in a container: Deploying in a container gives you the tool to deploy everything in the same standard way. You can choose to deploy all microservices in the same way regardless of their nature using containers. You will learn more about container deployment in the, Deploying an application with a container section.
Blue-green deployment: The better approach is to create a copy of the production environment. Deploy the new feature and route a small percentage of the user traffic to make sure the new feature is working as per expectation in a new environment. After that, increase the traffic in the new environment until the entire user base is able to see the new feature. You will learn more about blue-green deployment in Chapter 12, DevOps and Solution Architecture Framework.
Monitor your environment: Good monitoring is the difference between reacting to an outage and proactively preventing an outage with proper rerouting, scaling, and managed degradation. To prevent any application downtime, you want services to offer and push their health status to the monitoring layer, because who knows better about status than the service itself! Monitoring can be done in many ways, such as plugins, or by writing to a monitoring API.
As you learned about the various advantages of microservice in this section, let's take a look at a microservice-based reference architecture for a real-time voting application.

[ 157 ]

Solution Architecture Design Patterns

Chapter 6

Real-time voting application reference
architecture
A microservice-based architecture is illustrated in the following diagram, representing a real-time voting application, where small microservices process and consolidate user votes. The voting application collects individual user votes from each mobile device and stores all the votes in a NoSQL-based Amazon DynamoDB database. Finally, there is application logic in the AWS Lambda function, which aggregates all of the voting data cast by users to their favorite actor and returns the final results:

Microservice based real-time voting application architecture
[ 158 ]

Solution Architecture Design Patterns

Chapter 6

In the preceding architecture, the following things are happening:
1. Users text a vote to a phone number or shortcode provided by a third party such as Twilio.
2. The third party is configured to send the content of the message to an endpoint created by Amazon API Gateway, which then forwards the response to a function built in AWS Lambda.
3. This function extracts the vote from the message content and writes the result and any metadata into a table in Amazon DynamoDB.
4. This table has DynamoDB Streams enabled, which allows you to track changes to your tables on a rolling basis.
5. After the update, DynamoDB Streams notifies a second AWS Lambda function, which has the application logic to aggregate the votes (to every second) and writes them back to another DynamoDB table. The second table only stores the sum of the votes for each category.
6. A dashboard to display a summary of votes is created using HTML and JavaScript and hosted as a static website in Amazon S3. This page uses the AWS JavaScript SDK to query the aggregate Amazon DynamoDB table and display the voting results in real time.
7. Finally, Amazon Route 53 is used as a DNS provider to create a hosted zone pointing a custom domain name to the Amazon S3 bucket.
This architecture is not only microservice-based but also serverless. Using microservices, you can create applications made of small independent components, which constitute smaller parts to iterate. Microservice-based architecture means that the cost, size, and risk of change reduces, increasing the rate of change.
Message queues play a vital role to achieve accurate loose coupling and help to avoid application throttling. A queue allows secure and reliable communication between components. Let's learn more about queue-based architecture in the next section.

Building queue-based architecture
In the previous section, you learned about microservice design using RESTful architecture. The RESTful architecture helps your microservice to be easily discoverable, but what happens if your service goes down? This is a contemporary architecture, where your client service waits for a response from the host service, which means that the HTTP request blocks the API. Sometimes, your information may be lost due to the unavailability of a downstream service. In such cases, you must implement some retry logic in order to retain your information.
[ 159 ]

Solution Architecture Design Patterns

Chapter 6

A queue-based architecture provides a solution to this problem by adding message queues between services, which holds information on behalf of services. The queue-based architecture provides fully asynchronous communication and a loosely coupled architecture. In a queue-based architecture, your information is still available in the message. If a service crashes, the message can get the process as soon as the service becomes available. Let's learn some terminology of a queue-based architecture:
Message: A message can have two parts--the header and the body. The header contains metadata about the message, while the body contains the actual message. Queue: The queue holds the messages that can be used when required. Producer: A service that produces a message and publishes it to the queue. Consumer: A service that consumes and utilizes the message. Message broker: Helps to gather, route, and distribute messages between the producer and consumer.
Let's learn about some typical queue-based architecture patterns to get an idea of how they work.

Queuing chain pattern
A queuing chain pattern is applied when sequential processing needs to run on multiple systems that are linked together. Let's understand the queuing chain pattern using the example of an image-processing application. In an image-processing pipeline, sequential operations of capturing the image and storing it on a server, running a job to create different-resolution copies of the image, watermarking the image, and thumbnail generation are tightly linked to each other. A failure in one part can cause the entire operation to be disrupted.
You can use queues between various systems and jobs to remove a single point of failure and design true loosely coupled systems. The queuing chain pattern helps you to link different systems together and increase the number of servers that can process the messages in parallel. If there is no image to process, you can configure Auto Scaling to terminate the excess servers.

[ 160 ]

Solution Architecture Design Patterns

Chapter 6

The following diagram shows a queuing chain pattern architecture. Here, the queue provided by AWS is called Amazon Simple Queue Service (SQS):

Queuing chain pattern architecture
The preceding architecture has the following steps:
1. As soon as the raw image is uploaded to the server, the application needs to watermark all of the images with the company's logo. Here, a fleet of Amazon EC2 servers is running batch jobs to watermark all the images and push the processed image into the Amazon SQS queue.
2. The second fleet of Amazon EC2 servers pulls the watermarked images from the Amazon SQS queue.
3. The second fleet of EC2 workers has a job to process the image and create multiple variations with different resolutions.
4. After encoding the images, the EC2 workers push the message into another Amazon SQS queue.
5. As the image is processed, the job deletes the message from the previous queue to make up space.
6. The final fleet of EC2 servers gets encoded messages from the queue and creates thumbnails along with the copyright.
[ 161 ]

Solution Architecture Design Patterns

Chapter 6

The benefits of this architecture are as follows:
You can use loosely coupled asynchronous processing to return responses quickly without waiting for another service acknowledgment. You can structure the system through the loose coupling of Amazon EC2 instances using Amazon SQS. Even if the Amazon EC2 instance fails, a message remains in the queue service. This enables processing to be continued upon recovery of the server and creates a system that is robust to failure.
You may get fluctuations in application demand that can cause unexpected message loads. Automating your workload as per the queue message load will help you to handle any fluctuations. Let's learn more about the job observer pattern to handle such automation next.

Job observer pattern
In the job observer pattern, you can create an Auto Scaling group, based upon number of messages in the queue to process. The job observer pattern helps you to maintain performance through increasing or decreasing the number of server instances used in job processing.
The following diagram depicts the job observer pattern:

Job observer pattern architecture
[ 162 ]

Solution Architecture Design Patterns

Chapter 6

In the preceding architecture, the first fleet of Amazon EC2 servers is on the left-hand side, running batch jobs and putting messages in the queue, for example, image metadata. The second fleet of EC2 servers on the right-hand side is consuming and processing those messages, for example, image encoding. As the message reaches a certain threshold, Amazon CloudWatch triggers Auto Scaling to add the additional server in the consumer fleet to speed up the job processing. Auto Scaling also removes additional servers when the queue depth goes below the threshold.
The job observer pattern computes scale with job size, providing efficiency and cost savings. The job observer pattern architecture allows the job to be completed in a shorter time frame. The process is resilient, which means job processing doesn't stop if a server fails.
While queue-based architecture provides loose coupling, it works mostly on the Asynchronous Pull method, where the consumer can pull the message from the queue as per their availability. Often, you need to drive communication between various architecture components where one event should trigger other events. Let's learn more about eventdriven architecture in the next section.

Creating event-driven architecture
Event-driven architecture helps you to chain a series of events together to complete a feature flow. For example, when you are making a payment to buy something on a website, you are expecting to get your order invoice generated and to get an email as soon as the payment is complete. Event-driven architecture helps to rope in all of these events so that making a payment can trigger another task to complete the order flow. Often, you will see message queues, which you learned about in the previous section, as the central point while talking about event-driven architecture. Event-driven architecture can also be based on the publisher/subscriber model or the event stream model.
Publisher/subscriber model
In the pub/sub model, when an event is published, a notification is sent to all subscribers, and each subscriber can take the necessary action as per their requirements of data processing. Let's take an example of a photo studio application, which enriches a photo with different filters and sends a notification to the user. The following architecture depicts a pub/sub model:

[ 163 ]

Solution Architecture Design Patterns

Chapter 6

Photo studio application pub/sub-event-driven architecture
In the preceding diagram, you will notice the following things: 1. The user first uploads the picture to an Amazon S3 bucket using a web/mobile application. 2. The Amazon S3 bucket then sends a notification to Amazon Simple Notification Service (SNS). Amazon SNS is a message topic with the following subscribers: 1. Here, the first subscriber is using the email service, and as soon as the photo upload is complete, an email is sent to the user. 2. The second subscriber is using Amazon SQS queue, which gets the message from the Amazon SNS topic and applies various filters in code written in AWS Lambda to improve the image quality. 3. The third subscriber is using the direct AWS Lambda function, which creates the image thumbnail.
In this architecture, Amazon S3 publishes the message to the SNS topic as a producer which is consumed by multiple subscribers. Additionally, as soon as the message comes to SQS, it triggers an event for the Lambda function to process images.
[ 164 ]

Solution Architecture Design Patterns

Chapter 6

Event stream model
In the event stream model, the consumer can read from the continuous flow of events coming from the producer. For example, you can use the event stream to capture the continuous flow of a clickstream log and also send an alert if there are any anomalies detected, as shown in the following architecture diagram:

Clickstream analysis event stream architecture
Amazon Kinesis is a service that is used to ingest, process, and store continuous streaming data. In the preceding diagram, various customers clicking on e-commerce applications from web and mobile applications produce a stream of click events. These clickstreams are sent to analytics applications using Amazon API Gateway for real-time analytics. In this analytics application, Kinesis Data Analytics calculates Conversion Rates over a certain period of time, for example, the number of people that ended up making a purchase in the last five minutes. After aggregating data in real time, Amazon Kinesis Data Analytics sends the results to Amazon Kinesis Data Firehose, which stores all the data files in Amazon S3 storage for further processing as needed.
[ 165 ]

Solution Architecture Design Patterns

Chapter 6

A Lambda function reads from the event stream and starts examining the data for Anomalies. As anomalies in the conversion rates are detected, the AWS Lambda function sends a notification on email for the campaign team to be notified. In this architecture, the event stream is occurring continuously, and AWS Lambda is reading from the stream for a specific event.
You should use event-driven architecture to decouple the producer and consumer and keep the architecture extendable so that a new consumer can be integrated at any time. This provides a highly scalable and distributed system with each subsystem having an independent view of events. However, you need to apply a mechanism to avoid duplicate processing and error message handling.
To achieve good application performance, caching is an important factor and it can be applied at every architecture layer and in pretty much any architecture component. Let's learn more about cache-based architecture in the next section.

Building cache-based architecture
Caching is the process of temporarily storing data or files in an intermediary location between the requester and the permanent storage, for the purpose of making future requests faster and reducing network throughput. Caching increases the application speed and lowers the cost. It allows you to reuse previously retrieved data. To increase application performance, caching can be applied at various layers of the architecture such as the web layer, application layer, data layer, and network layer.
Normally, the server's random access memory (RAM) and in-memory cache engines are utilized to support application caching. However, if caching is coupled to a local server, then the cache will not be persisting data, in case of a server crash. Now, most of the applications are in a distributed environment, so it's better to have a dedicated caching layer that should be independent of the application life cycle. When you applied horizontal scaling to your application, all servers should be able to access the centralized caching layer to achieve the best performance.

[ 166 ]

Solution Architecture Design Patterns

Chapter 6

The following diagram depicts the mechanism of caching in various layers of solution architecture:

Caching at the architecture layers
[ 167 ]

Solution Architecture Design Patterns

Chapter 6

As shown in the preceding diagram, the following are the caching mechanisms at each layer of architecture:
Client side: Client-side caching is applied to user devices such as mobile and desktop. This caches the previously visited web content to respond faster to a subsequent request. Each browser has its own caching mechanism. HTTP caching makes the application faster by caching content at the local browser. The cache-control HTTP header defines browser caching policies for both client request and server response. These policies define where the content should be cached and how long it will persist, which is known as Time to Live (TTL). Cookies are another method used to store information at the client machine in order to respond to the browser faster.
DNS cache: When a user types the website address over the internet, the public Domain Name System (DNS) server looks up the IP address. Caching this DNS resolution information will reduce the website's load time. DNS can be cached to a local server or browser after the first request and any further request to that website will be faster.
Web caching: Much of the request involves retrieving web content such as images, video, and HTML pages. Caching these assets near to the user location can provide a much faster response for a page load. This also eliminates disk read and server load time. A content distribution network (CDN) provides a network of edge locations where static content such as high-resolution images and videos can be cached. It's very useful for reading heavy applications such as games, blogs, e-commerce product catalog pages, and more. The user session contains lots of information regarding user preference and their state. It provides a great user experience to store the user's session in its own key-value store and applies to cache for quick user response.
Application caching: At the application layer, caching can be applied to store the result of a complex repeated request to avoid business logic calculations and database hits. Overall, it improves application performance and reduces the load on the database and infrastructure.
Database caching: Application performance highly depends upon speed and throughput provided by the database. Database caching allows you to increase database throughput significantly and lower data retrieval latency. A database cache can be applied in front of any kind of relational or non-relational database. Some database providers integrate caching, while applications handle local caching.

[ 168 ]

Solution Architecture Design Patterns

Chapter 6

Redis and Memcached are the most popular caching engines. While Memcached is faster (it is good for low-structure data and stores data in a key-value format), Redis is a more persistent caching engine and is capable of handling complex data structures required for an application such as a gaming leader board. Let's learn about a few more caching design patterns.

Cache distribution pattern in a three-tier web
architecture
Traditional web hosting architecture implements a standard three-tier web application model that separates the architecture into the presentation, application, and persistence layers. As shown in the following architecture diagram, caching is applied at the presentation, persistence, and application layers:

Cache distribution pattern architecture
[ 169 ]

Solution Architecture Design Patterns

Chapter 6

One of the ways you can offload your web page is through caching. In caching patterns, your goal is to try to hit the backend as little as possible. You can write an application where you can cache images, JavaScript, or even full pages to provide a better experience for your users. As shown in the preceding diagram, caching is applied to the various layers of architecture:
Amazon Route 53 provides DNS services to simplify domain management and to help cache DNS-to-IP mapping. Amazon S3 stores all static content such as high-resolution images and videos. Amazon CloudFront provides edge caching for high-volume content. It also uses these cache-control headers to determine how frequently it needs to check the origin for an updated version of that file. Amazon DynamoDB is used for session stores in which web applications cache to handle user sessions. Elastic Load Balancing spreads traffic to web server Auto Scaling groups in this diagram. Amazon ElastiCache provides caching services for the app, which removes the load from the database tier.
In general, you only cache static content; however, dynamic or unique content affects the performance of your application. Depending on the demand, you might still get some performance gain by caching the dynamic or unique content. Let's take a look at a more specific pattern.

Rename distribution pattern
When using a content distribution network (CDN) such as Amazon CloudFront, you store frequently used data in an edge location near to the user for fast performance. Often, you set up TTL in CDN for your data, which means the edge location will not query back to the server for updated data until TTL expires. You may have situations where you need to update CDN cached content immediately, for example, if you need to correct the wrong product description.

[ 170 ]

Solution Architecture Design Patterns

Chapter 6

In such a situation, you can't wait for the file's TTL to expire. The rename distribution pattern helps you to update the cache as soon as new changes are published so that the user can get updated information immediately. The following diagram shows the rename distribution pattern:

Rename distribution pattern architecture
As shown in the preceding diagram, using the rename distribution pattern with the cache distribution pattern helps to solve the update issue. With this pattern, instead of overwriting the file in the origin server and waiting for the TTL in CloudFront to expire, the server uploads the updated file with a new filename and then updates the web page with the new URL. When the user requests original content, CloudFront has to fetch it from the origin and can't serve the obsolete file that's already cached.
You may not always want to use a CDN; instead, you can use the proxy cache server. Let's learn more about it in the next section.
Cache proxy pattern
You can increase your application performance significantly by adding a cache layer. In a cache proxy pattern, static content or dynamic content is cached upstream of the web app server. As shown in the following architectural diagram, you have a caching layer in front of the web application cluster:
[ 171 ]

Solution Architecture Design Patterns

Chapter 6

Cache proxy pattern architecture
In the preceding diagram, for high-performance delivery, cache content is delivered by the cache server. A few benefits of cache proxy patterns are as follows:
Cache proxy patterns help you to deliver content using the cache, which means no modification is needed at the web server or application server level. They reduce the load of content generation for dynamic content in particular. You have the flexibility to set up a cache at the browser level such as in HTTP headers, URLs, cookies, and more. Alternatively, you can cache information in the cache layer if you don't want to store it at the browser level. In the cache proxy pattern, you need to make sure that you maintain multiple copies of the cache to avoid the single point of failure. Sometimes, you may want to serve your static content from both the server and CDN, each of which requires a different approach. Let's deep dive into this hybrid situation in the next section.
[ 172 ]

Solution Architecture Design Patterns

Chapter 6

Rewrite proxy pattern
Sometimes, you want to change the access destinations of static website content such as images and videos, but don't want to make changes to the existing systems. You can achieve this by providing a proxy server using rewrite proxy patterns. To change the destination of static content to other storage such as content service or internet storage, you can use a proxy server in front of the web server fleet. As shown in the following architecture diagram, you have a proxy server in front of your application layer, which helps to change the content delivery destination without modifying the actual application:

Rewrite proxy pattern architecture
As shown in the preceding diagram, to accomplish a rewrite proxy pattern, place the proxy server in front of the currently running system. You can construct a proxy server using software such as Apache NGINX. The following are the steps to build a rewrite proxy pattern:
1. Put a running proxy server on an EC2 instance, which is able to overwrite the content between the Load balancer and the storage service such as Amazon S3, which stores the static content.
2. Add to the proxy server rules for overwriting URLs within the content. These rules will help Elastic Load Balancing (ELB) to point to a new location, as shown in the preceding diagram, which redirects the proxy server rule from https://cdn/test.jpg to /test.jpg.
[ 173 ]

Solution Architecture Design Patterns

Chapter 6

3. As required, apply Auto Scaling to the proxy servers by configuring a number of minimum and maximum proxy servers needed as per application load.
In this section, you learned about various ways to handle caching for static content distribution over the network. However, caching at the application layer is very important for improving application performance for overall user experience. Let's learn more about the app caching pattern to handle dynamic user data delivery performance.

App caching pattern
When it comes to applying caching to applications, you want to add a cache engine layer between your application servers and the database. The app caching pattern allows you to reduce the load on the database as the most frequent query is served from the caching layer. The app caching pattern improves overall application and database performance. As shown in the following diagram, you can see the caching layer applied between the application layer and the database layer:

Application caching pattern architecture
[ 174 ]

Solution Architecture Design Patterns

Chapter 6

As shown in the preceding diagram, based on your data access pattern, you can use either lazy caching or write-through. In lazy caching, the cache engine checks whether the data is in the cache and, if not, gets it from the database and keeps it in the cache to serve future requests. Lazy caching is also called the cache aside pattern.
In the write-through method, data is written in the cache and in the data store at the same time. If the data gets lost from the cache, then it can get it again from the database. Writethrough is used mainly in application-to-application situations where users are writing a product review (which always needs to load on the product page). Let's learn more about the popular caching engines Redis and Memcached.

Memcached versus Redis
Redis and Memcached are two popular caching engines used in application design. Often, the Redis cache engine is required for more complex application caching needs such as creating a leader board for a game. However, Memcached is more high-performing and is helpful for handling heavy application loads. Each caching engine has its own pros and cons. Let's take a look at the major differences between them, which will help you to make a decision of which to use:

Memcached

Redis

Offers multithreading

Single-threaded

Able to use more CPU core for faster processing

Unable to utilize multi-core processor, which results in comparatively slow performance

Supports key-value style data

Supports complex and advance data structures

Lacks data persistence; loses the data stored in cache memory in the event of a crash

Data can persist using built-in read replicas with failover

Easy maintenance

More complexity involved owing to the need to maintain the cluster

Good to cache flat strings such as flat HTML pages, serialized JSON, and more Good to create a cache for a gaming leader board, a live voting app, and more

Overall, if you need to decide which engine to use, base it on a use case that can justify using Redis or Memcached. Memcached is simple and has lower maintenance, and it is typically preferred when your cache doesn't need the advanced features that Redis offers. However, if you need the advantage of data persistence, advanced data types, or any of the other features listed, then Redis is the best solution.

When implementing caching, it's essential to understand the validity of data that needs to be cached. If the cache hit rate is high, that means the data is available in the cache when required. For a higher cache hit ratio, offload the database by reducing direct queries; this also improves the overall application performance. A cache miss occurs when data is not present in the cache and this increases the load in the database. The cache is not a large data store, so you need to set the TTL and evict the cache as per your application need.

[ 175 ]

Solution Architecture Design Patterns

Chapter 6

As you have seen in this section, there are multiple benefits of applying caches, including application performance improvement, the ability to provide predictable performance, and the reduction in database cost. Let's learn about some more application-based architecture that demonstrates the principle of loose coupling and constraint handling.

Understanding the circuit breaker pattern
It's common for a distributed system to make a call to other downstream services, and the call could fail or hang without response. You will often see code that retries the failed call several times. The problem with a remote service is that it could take minutes or even hours to correct, and an immediate retry might end up in another failure. As a result, end users wait longer to get an error response while your code retries several times. This retry function would consume the threads, and it could potentially induce a cascading failure.
The circuit breaker pattern is about understanding the health of downstream dependencies. It detects when those dependencies are unhealthy and implements logic to gracefully fail requests until it detects that they are healthy again. The circuit breaker can be implemented using a persistence layer to monitor healthy and unhealthy requests over the past request interval.
If a defined percentage of requests observe an unhealthy behavior over the past interval or over a total count of exceptions, regardless of percentage, the circuit marks as open. In such a situation, all requests throw exceptions rather than integrate with the dependency for a defined timeout period. Once the timeout period has subsided, a small percentage of requests try to integrate with the downstream dependency, to detect when health has returned. Once a sufficient percentage of requests are healthy again over an interval, or no errors are observed, the circuit closes again, and all the requests are allowed to integrate as they usually would thoroughly.
The implementation decisions involve the state machine to track/share the healthy/unhealthy request counts. The states of services can be maintained in DynamoDB, Redis/Memcached, or another low-latency persistence store.

Implementing the bulkheads pattern
Bulkheads are used in ships to create separate watertight compartments that serve to limit the effect of failure, ideally preventing the ship from sinking. If water breaks through the hull in one compartment, the bulkheads prevent it from flowing into other compartments, limiting the scope of the failure.
[ 176 ]

Solution Architecture Design Patterns

Chapter 6

The same concept is useful to limit the scope of failure in the architecture of large systems, where you want to partition your system to decouple dependencies between services. The idea is that one failure should not cause the entire system to fail, as shown in the following diagram:

Bulkhead pattern
In the bulkhead pattern, it's better to isolate the element of the application into the pool for service, which has a high dependency; so, if one fails, others continue to serve upstream services. In the preceding diagram, Service 3 is partitioned into two pools from a single service. Here, if Service 3 fails, then the impact of either Service 1 or Service 2 depends on their dependency on the pool, but the entire system does not go down. The following are the major points to consider when introducing the bulkhead pattern in your design, especially for the shared service model:
Save part of the ship, which means your application should not shut down due to the failure of one service. Decide whether less-efficient use of resources is okay. Performance issues in one partition should not impact the overall application. Pick a useful granularity. Don't make the service pools too small; make sure they are able to handle application load. Monitor each service partition performance and adhere to the SLA. Make sure all of the moving parts are working together and test the overall application when one service pool is down.
You should define a service partition for each business or technical requirement. You should use this pattern to prevent the application from cascading failure and isolating critical consumers from the standard consumer.
Often, legacy application servers have a configuration with hardcoded Internet Protocol (IP) addresses or Domain Name Server (DNS) names. Making any server change for modernization and upgrade requires making changes in application and revalidating it. In these cases, you don't want to change the server address. Let's learn how to handle such a situation with a floating IP in the next section.
[ 177 ]

Solution Architecture Design Patterns

Chapter 6

Creating a floating IP pattern
It's common that monolithic applications have lots of dependencies on the server where they are deployed. Often, application configuration and code have hardcoded parameters based on server DNS name and IP address. Hardcoded IP configuration creates challenges if you want to bring up a new server in case of an issue with the original server. Additionally, you don't want to bring down the entire application for the upgrade, which may cause significant downtime.
To handle such a situation, you need to create a new server keeping the same server IP address and DNS name. It can be achieved by moving the network interface from a problematic instance to the new server. The network interface is generally a Network Interface Card (NIC), which facilitates communication between servers over a network. It can be in the form of hardware or software. Moving network interface means that now your new server assumes the identity of the old server. With that, your application can live with the same DNS and IP address. It also allows easy rollback by moving the network interface to the original instance.
The public cloud (for example, AWS) made it easy by providing Elastic IP (EIP) and Elastic Network Interface (ENI). If your instance fails and you need to push traffic to another instance with the same public IP address, then you can move the elastic IP address from one server to another, as shown in the following architecture diagram:

Floating IP and interface pattern
[ 178 ]

Solution Architecture Design Patterns

Chapter 6

Since you are moving EIP, the DNS may not need to update. EIP can move your server's public IP across instances. If you need to move both public and private IP addresses, then use a more flexible approach such as ENI, as shown on the right of the preceding diagram. ENI can move across instances, and you can use the same public and private address for traffic routing or application upgrades.
So far, you have learned multiple architecture patterns where applications are deployed in the virtual machine. However, in many cases, you may not be able to utilize the virtual machine fully. To optimize your utilization further, you can choose to deploy your application in containers. Containers are most suitable for microservice deployment. Let's learn more about a container-based deployment in the next section.

Deploying an application with a container
As many programming languages are invented and technologies evolve, this creates new challenges. There are different application stacks that require different hardware and software deployment environments. Often, there is a need to run applications across different platforms and migrate from one to another platform. Solutions require something that can run anything everywhere and is consistent, lightweight, and portable.
Just as shipping containers standardized the transport of freight goods, software containers standardize the transport of applications. Docker creates a container that contains everything a software application would need to be able to run all of its files, such as filesystem structure, daemons, libraries, and application dependencies. Containers isolate software from its surrounding development and staging environments. This helps to reduce conflicts between teams running different software on the same infrastructure.
VMs isolate at the operating system level, and containers isolate at the kernel level. This isolation allows several applications to run on a single-host operating system, and yet still have their filesystem, storage, RAM, libraries, and, mostly, their own view of the system:

[ 179 ]

Solution Architecture Design Patterns

Chapter 6

Virtual machines and containers for application deployment
As shown in the preceding diagram, multiple applications are deployed in a single virtual machine using containers. Each application has its runtime environment, so you can run many individual applications while keeping the same number of servers. Containers share a machine's operating system kernel. They start instantly and use less computing time and RAM. Container images are constructed from the filesystem layers and share standard files. Shared resourcing minimizes disk usage, and container image downloads are much faster. Let's take a look at why containers are becoming more popular along with their benefits.
The benefit of containers
Customers often ask these questions when it comes to containers: Why do we need containers when we have instances? Don't instances already provide us with a level of isolation from the underlying hardware?
While the preceding questions are valid, several benefits accrue from using a system such as Docker. One of the key benefits of Docker is that it allows you to fully utilize your virtual machine resources by hosting multiple applications (on distinct ports) in the same instance.
[ 180 ]

Solution Architecture Design Patterns

Chapter 6

Docker uses certain features of the Linux kernel, namely kernel namespaces and groups, to achieve complete isolation between each Docker process, as indicated in the following architecture diagram:

Container layer in application infrastructure
As shown in the preceding diagram, it's possible to run two or more applications that require different versions of the Java runtime on the same machine, as each Docker container has its version of Java and the associated libraries installed. In turn, the container layer in the application infrastructure makes it easier to decompose your applications into microservices that can run side by side on the same instance. Containers have the following benefits:
Portable runtime application environment: Containers provide platformindependent capabilities, where you build your application once and deploy it anywhere regardless of the underlying operating system. Faster development and deployment cycles: Modify the application and run it anywhere with quick boot time, typically within seconds. Package dependencies and application in a single artifact: Package the code, library, and dependencies together to run the application in any operating system.
[ 181 ]

Solution Architecture Design Patterns

Chapter 6

Run different application versions: Applications with different dependencies run simultaneously in a single server. Everything can be automated: Container management and deployment is done through scripting, which helps to save cost and human error. Better resource utilization: Containers provides efficient scaling and high availability with multiple copies of the same microservice container can be deployed across servers for your application. Easy to manage the security aspect: Containers are platform-specific rather than application-specific.
Container deployment is becoming very popular due to its benefits. There are multiple ways to orchestrate containers. Let's look at container deployment in more detail next.

Container deployment
Complex applications with multiple microservices can be quickly deployed using container deployment. The container makes it easier to build and deploy the application more quickly as the environment is the same. Build the container in development mode, push to test, and then release to production. For hybrid cloud environments, container deployment is very useful. Containers make it easier to keep environments consistent across microservices. As microservices aren't always very resource-consuming, they can be placed together in a single instance to reduce cost.
Sometimes, customers have short workflows that require a temporary environment setup. Those environments may be queue systems or continuous integration jobs, which don't always utilize server resources efficiently. Container orchestration services such as Docker and Kubernetes can be a workaround, allowing them to push and pop containers onto the instance.
Docker's Lightweight container virtualization platform provides tools to manage your applications. Its stand-alone application can be installed on any computer to run containers. Kubernetes is a container orchestration service that works with Docker and another container platform. Kubernetes allows automated container provisioning and handles security, networking, and scaling aspects diligently.

[ 182 ]

Solution Architecture Design Patterns

Chapter 6

Containers help the enterprise to create more cloud-native workloads, and public cloud providers such as AWS extend services to manage Docker containers and Kubernetes. The following diagram shows Docker's container management using Amazon Elastic Containers Service (ECS), providing a fully managed elastic service to automate the scaling and orchestration of Docker containers:

Container deployment architecture
In the preceding diagram, multiple containers are deployed in a single Amazon EC2 virtual machine, which is managed through Amazon ECS and facilitates Agent Communication Service and cluster management. All user requests are distributed using a load balancer among the containers. Similarly, AWS provides Amazon Elastic Kubernetes Service (EKS) to manage containers using Kubernetes.
Containers are a broad topic, and, as a solution architect, you need to be familiar with all of the available options. This section provides an overview of containers. However, you will need to deep dive further if you choose to utilize containers for your microservice deployment.
[ 183 ]

Solution Architecture Design Patterns

Chapter 6

As of now, you have learned about various architecture patterns focusing on application development. Everyone has to agree that data is an integral part of any architecture design, and most of the architecture revolves around collecting, storing, and processing the visualization of data. Let's learn more about handling data in application architecture in the next section.

Database handling in application
architecture
Data is always at the center of any application development, and scaling data has always been challenging. Handling data efficiently improves application latency and performance. In the previous section, Building cache-based architecture, you learned how to handle frequently queried data by putting a cache in front of your database under the app caching pattern. You can put either a Memcached or Redis cache in front of your database, which reduces the many hits on the database and results in improving database latency.
In application deployment, as the user base of your application grows, you need to handle more data by your relational database. You need to add more storage or vertically scale the database server by adding more memory and CPU power. Often, horizontal scaling is not very straightforward when it comes to scaling relational databases. If your application is read-heavy, you can achieve horizontal scaling by creating a read replica. Route all read requests to database read replicas, while keeping the master database node to serve write and update requests. As read replica has asynchronous replication, it can add some lag time. You should choose to read the replica option if your application can tolerate some milliseconds of latency. You can use read replica to offload reporting.

[ 184 ]

Solution Architecture Design Patterns

Chapter 6

You can use database sharding to create a multi-master for your relational database and inject the concept of horizontal scaling. The sharding technique is used to improve writing performance with multiple database servers. Essentially, databases are prepared and divided with identical structures using appropriate table columns as keys to distribute the writing processes. As demonstrated in the following architecture diagram, the customer database can be divided into multiple shards:

Relational database sharding
As shown in the preceding diagram, without shards, all data resides in one partition; for example, the user's first name starts with A to Z in one database. With sharding, data is split into large chunks called shards. For example, user first name A to I is in one database, J to R in another database, and S to Z in a third database. In many circumstances, sharding gives you higher performance and better operating efficiency.
You can use Amazon RDS in sharding backend databases. Install sharding software such as MySQL server combined with a Spider Storage Engine on an Amazon EC2 instance. Then, first, prepare multiple RDS databases and use them as the sharding backend databases.
However, what if your master database instance goes down? In that case, you need to maintain high availability for your database. Let's take a closer look at database failover.
[ 185 ]

Solution Architecture Design Patterns

Chapter 6

High-availability database pattern
For the high availability of your application, it is critical to keep your database up and running all of the time. As horizontal scaling is not a straightforward option in the relational database, it creates additional challenges. To achieve high database availability, you can have a standby replica of the master database instance, as shown in the following diagram:

High-availability database pattern
As shown in the preceding diagram, if the master instance goes down, your application server switches over to standby instance. Read replica takes the load off of master to handle latency. Master and standby are located in different availability zones, so your application will still be up even when an entire availability zone is down. This architecture also helps to achieve zero downtime which may cause during the database maintenance window. When a master instance is down for maintenance, the application can failover to secondary standby instance and continue serving user request.
For the purpose of disaster recovery, you will want to define the database backup and archival strategy, depending on your application's Recovery point object (RPO) of how frequently you want to take backups. If your RPO is 30 minutes, it means your organization can only tolerate data loss worth of 30 minutes. In that case, you should take a backup every half an hour. While storing the backup, you need to determine how long the data can be stored for customer query purposes. You may want to store data for six months as an active backup and then in an archival store as per the compliance requirement.
Consider how quickly you might need to access your backup and determine the type of network connection needed to meet your backup and recovery requirements as per the company recovery time objective (RTO). For example, if your company's RTO is 60 minutes, it means you should have enough network bandwidth to retrieve and restore your backup within an hour. Also, define whether you are backing up snapshots of complete systems or volumes attached to systems.
[ 186 ]

Solution Architecture Design Patterns

Chapter 6

You may also need to classify your data, for example, if it has customer-sensitive information such as email, addresses, personally identifiable information, and more. You need to define the data encryption strategy accordingly. You will learn more about data security in Chapter 8, Security Considerations.
You can also consider migrating from an RDBMS to a NoSQL database depending upon your application's growth and complexity. NoSQL can provide you with greater scalability, management, performance, and reliability than most relational databases. However, the process of migrating to NoSQL from an RDBMS can be time-consuming and laborintensive.
There is lots of data to process in any application, for example, clickstream data, application log data, rating and review data, social media data, and more. Analyzing these datasets and getting insight can help you to grow your organization exponentially. You will learn more about these use cases and patterns in Chapter 13, Data Engineering and Machine Learning. As of now, you have learned about the best practices to design a solution architecture. Let's learn about some anti-patterns, which should be avoided, in the next section.

Avoiding anti-patterns in solution
architecture
In this chapter, you have learned about a different way of designing solution architecture with various design patterns. Often, the teams can drift away from best practices due to timeline pressure or the unavailability of resources. You always need to give special attention to the following architecture design anti-patterns:
In an anti-pattern (an example of a poorly designed system), scaling is done reactively and manually. When application servers reach their full capacity with no more room, users are prevented from accessing the application. On user complaints, the admin finds out that the servers are at their full capacity and starts launching a new instance to take some of the load off. Unfortunately, there is always a few minutes' lag between the instance launch and its availability. During this period, users are not able to access the application.
With anti-patterns, automation is missing. When application servers crash, the admin manually launches and configures the new server and notifies the users manually. Detecting unhealthy resources and launching replacement resources can be automated, and you can even notify when resources are changed.

[ 187 ]

Solution Architecture Design Patterns

Chapter 6

With anti-patterns, the server is kept for a long time with hardcoded IP addresses, which prevent flexibility. Over time, different servers end up in different configurations and resources are running when they are not needed. You should keep all of the servers identical and should have the ability to switch to a new IP address. You should automatically terminate any unused resources.
With anti-patterns, an application is built in a monolithic way, where all layers of architecture including web, application, and data layers are tightly coupled and server dependent. If one server crashes, it brings down the entire application. You should keep the application and web layer independent by adding a load balancer in between. If one of the app servers goes down, the load balancer automatically starts directing all of the traffic to the other healthy servers.
With anti-patterns, the application is server bound, and the server communicates directly with each other. User authentication and sessions are stored in the server locally and all static files are served from the local server. You should choose to create an SOA, where the services talk to each other using a standard protocol such as HTTP. User authentication and sessions should be stored in low latencydistributed storage so that the application can be scaled horizontally. The static asset should be stored in centralized object storage that is decoupled from the server.
With anti-patterns, a single type of database is used for all kinds of needs. You are using a relational database for all needs, which introduces performance and latency issues. You should use the right storage for the right need, such as the following:
NoSQL to store user session
Cache data store for low latency data availability
Data warehouse for reporting needs
Relation database for transactional data
With anti-patterns, you will find a single point of failure by having a single database instance to serve the application. Wherever possible, eliminate single points of failure from your architectures. Create a secondary server (standby) and replicate the data. If the primary database server goes offline, the secondary server can pick up the load.
With anti-patterns, static content such as high-resolution images and videos are served directly from the server without any caching. You should consider using a CDN to cache heavy content near the user location, which helps to improve page latency and reduce page load time.

[ 188 ]

Solution Architecture Design Patterns

Chapter 6

With anti-patterns, you can find security loopholes that open server access without a fine-grained security policy. You should always apply the principle of least privilege, which means starting with no access and only giving access to the required user group.
The preceding points provide some of the most common anti-patterns. Throughout this book, you will learn the best practices of how to adopt them in solution design.

Summary
In this chapter, you learned about various design patterns by applying the techniques from Chapter 3, Attributes of the Solution Architecture, and Chapter 4, Principles of Solution Architecture Design. First, you built the architecture design foundation from a multilayer architecture with a reference architecture from three-tier web application architecture. You learned how to design a multi-tenant architecture on top of a three-tier architecture, which can provide a SaaS kind of offering. You learned how to isolate multi-tenant architecture at the database label, schema level, and table level as per customer and organization need.
User state management is very critical for complex applications such as finance, ecommerce, travel booking, and more. You learned about the difference between stateful and stateless applications and their benefits. You also learned how to create a stateless application with a persistent layer of the database for session management. You learned about the two most popular SOA patterns, SOAP-based and RESTful-based patterns, along with their benefits. You looked at a reference architecture of an e-commerce website based on SOA and learned how to apply the principle of loose coupling and scaling.
You learned about serverless architecture and how to design a secure survey delivery architecture that is entirely serverless. You also learned about microservice architecture using the example of a serverless real-time voting application, which builds on the microservice pattern. For more loose coupling designs, you learned about queuing chain and job observer patterns, which provide loosely coupled pipelines to process messages in parallel. You learned about the pub/sub and event stream models to design event-driven architecture.

[ 189 ]

Solution Architecture Design Patterns

Chapter 6

It's not possible to achieve your desired performance without applying caching. You learned about various cache patterns to apply to caches at the client side, content distribution, web layer, application layer, and database layer. You learned architecture patterns to handle failure such as a circuit breaker to handle the downstream service failure scenario and bulkhead pattern to handle complete service failure. You learned about floating IP patterns to change servers without changing their address in failure situations to minimize downtime.
You learned about the various technique of handing data in an application and how to make sure your database is highly available to serve your application. Finally, you learned about various architecture anti-patterns and how to replace them using best practices.
While, in this chapter, you learned about various architecture patterns, in the next chapter, you will learn about architecture design principles for performance optimization. Additionally, you will deep dive into technology selection in the area of computing, storage, databases, and networking, which can help to improve your application's performance.

[ 190 ]

7
Performance Considerations
In this era of fast internet, users expect very high-performance applications. There have been experiments that show that every second of application loads delay, cause a significant loss in the revenue of an organization. Therefore, the performance of the application is one of the most critical attributes of solution design that can impact your product adoption growth.
In the previous chapter, you learned about various solution architecture design patterns that can be used to solve a complex business problem. In this chapter, you will gain an understanding of the best practices to optimize your application for optimal performance. You will learn various design principles that you can use to optimize the solution architecture's performance. Here, performance needs to be optimized at every layer and in every component of the architecture. You will gain an understanding of how to choose the right technology at various layers of your architecture for the continuous improvement of your application's performance. You will learn how to follow the best practices of performance optimization in this chapter. We will focus on the following topics in particular:
Design principles for architecture performance Technology selection for performance optimization Performance monitoring
By the end of the chapter, you will have an understanding of important attributes of performance improvement, such as latency, throughput, and concurrency. You will be able to make better decisions regarding your choice of technology, which can help you to improve performance at the various layers of architecture, such as compute, storage, database, and networking.

Performance Considerations

Chapter 7

Design principles for architecture
performance
Architectural performance efficiency focuses on efficiently using application infrastructure and resources to meet increasing demand and technology evaluation. Technology vendors and open source communities continuously work to improve the performance of applications. Often, large enterprises continue to work on legacy programming languages and technologies because of fear of changing and taking risks. As technology evolves, it often addresses critical performance issues, and the advancement of technology in your application helps to improve application performance.
Many large public cloud providers, such as Amazon Web Service (AWS), Microsoft Azure, and Google Cloud Platform (GCP), offer technology as a service. This makes it easier to adopt enterprise jobs and complex technologies more efficiently and with minimal effort--for example, you might use storage as a service to manage a massive amount of data or a NoSQL database as a managed service to provide high-performance scalability to your application.
Now organizations can utilize a content distribution network (CDN) to store heavy image and video data near user locations to reduce network latency and improve performance. With infrastructure as a service (IaaS), it becomes easier to deploy workloads closer to your user base, which helps to optimize application performance by reducing latency over the network.
As servers virtualize, you can be more agile and experiment with your application, and you can apply a high degree of automation. Agility helps you to experiment and find out what technology and method are best suited for your application workload--for example, my server deployment should go for virtual machines or containers, or it can even go completely serverless with the use of AWS Lambda, which is a Function as a Service (FaaS). Let's look at some vital design principles to consider for your workload performance optimization.

Reducing latency
Latency can be a major factor in your product adoption, as users are looking for faster applications. It doesn't matter where your users are located, you need to provide a reliable service for your product to grow. You may not be able to achieve zero latency, but the goal should be to reduce response time within the user tolerance limit.

[ 192 ]

Performance Considerations

Chapter 7

Latency is the time delay between the user sending a request and receiving the desired response. As shown in the following diagram, it takes 600 ms for a client to send a request to the server and 900 ms for the server to respond, which introduces a total latency of 1.5 seconds (1500 ms):

Request response latency in a client-server model
Most of the application needs to access the internet in order to have a diverse set of global users. These users are expecting consistency in performance, regardless of their geographical location. This is sometimes challenging, as it takes time to move data over the network from one part of the world to another.
Network latency can be caused by various factors, such as the network transmission medium, router hops, and network propagation. Oftentimes, a request that is sent over the internet hops over multiple routers, which adds latency. Enterprises commonly use their fiber optics line to set up connectivity between their corporate network or cloud, which helps to avoid inconsistency.
In addition to the problems caused by the network, latency can also be caused by various components of the architecture. At the infrastructure level, your compute server can have latency issues due to memory and processor problems, where the data transfer between the CPU and RAM is slow. The disk can have latency due to slow read and write. Latency in a hard disk drive (HDD) is dependent on the time it takes to select a disk memory sector to come around and position itself under the head for reading and writing.
The disk memory sector is the physical location of data in the memory disk. In an HDD, data is distributed in memory sectors during write operations, as the disk is continuously rotating, so data can be written randomly. During the read operation, the head needs to wait for the rotation to bring it to the disk memory sector.
[ 193 ]

Performance Considerations

Chapter 7

At the database level, latency can be caused by slow data reads and writes from the database due to hardware bottlenecks or slow query processing. Taking the database load off by distributing the data with partitioning and sharding can help to reduce latency. At the application level, there could be an issue with transaction processing from code that needs to be handled using garbage collection and multithreading. Achieving low latency means higher throughput, as latency and throughput are directly related, so let's learn more about throughput.

Improving throughput
Throughput is the quantity of data that is sent and received at a given time, while latency is defined as the time between when the user initiates a request in the application and receives the response from the application. When it comes to networks, bandwidth plays an important role.
Bandwidth determines the maximum number of data that can get transferred over the network.

Throughput and latency have a direct relationship as they work together. Lower latency means high throughput as more data can transfer in less time. To understand this better, let's take the analogy of a country's transportation infrastructure.
Let's say that highways with lanes are network pipelines and cars are data packets. Suppose a given highway has 16 lanes between 2 cities, but that not all vehicles can reach the destination at the desired time; they may get delayed because of traffic congestion, lanes closing, or accidents. Here, latency determines how fast a car can travel from one city to another, while throughput tells us how many cars can reach their destinations. For a network, using full bandwidth is challenging because of error and traffic congestion.
Network throughput transfers a significant amount of data over the network in bits per second (bps). Network bandwidth is the maximum size of the network pipeline, which it can process. The following diagram illustrates the amount of data transferred between client and server:

[ 194 ]

Performance Considerations

Chapter 7

Throughput in a network
In addition to the network, the throughput is applicable at the disk level. Disk throughput is determined by a factor of input/output per second (IOPS) and the amount of data requested (I/O size). Disk throughput is determined in megabytes per second using the following formula:
Average IO size x IOPS = Throughput in MB/s
So, if your disk IOPS is 20,000 IOPS and the I/O size is 4 KB (4096 bytes), then the throughput will be 81.9 MB/s (20,000 x 4096 and converted from bytes to megabytes).
Input/output (I/O) requests and disk latency have a direct relationship. I/O means write and read respectively, while disk latency is the time taken by each I/O request to receiving the response from the disk. Latency is measured in milliseconds and should be minimal. This is impacted by disk revolution per minute (RPM). The IOPS is the number of operations that the disk can serve per second.
The throughput, also applicable at CPU and memory level, is determined by the amount of data transfer between the CPU and RAM per second. At the database level, throughput is determined by the number of transactions a database can process per second. At the application level, your code needs to handle transactions that can be processed every second by managing the application memory with the help of garbage collection handling and efficient use of the memory cache.
As you learned when you looked at latency, throughput, and bandwidth, there is another factor called concurrency, which is applicable to the various components of architecture and helps to improve application performance. Let's learn more about concurrency.
[ 195 ]

Performance Considerations

Chapter 7

Handling concurrency
Concurrency is a critical factor for solution design as you want your application to process multiple tasks simultaneously--for example, your application needs to handle multiple users simultaneously and process their requests in the background. Another example is when your web user interface needs to collect and process web cookie data to understand user interaction with the product while showing users to their profile information and product catalog. Concurrency is about doing multiple tasks at the same time.
People often get confused between parallelism and concurrency by thinking that they are both the same thing; however, concurrency is different from parallelism. In parallelism, your application divides an enormous task into smaller subtasks, which it can process in parallel with a dedicated resource for each subtask. In concurrency, however, an application processes multiple tasks at the same time by utilizing shared resources among the threads. The application can switch from one task to another during processing, which means that the critical section of code needs to be managed using techniques such as locks and semaphores.
As illustrated in the following diagram, concurrency is like a traffic light signal where traffic flow switches between all four lanes to keep traffic going. As there is a single thread along which you should pass all traffic, processing in other lanes has to stop while traffic in one lane is in the clearing process. In the case of parallelism, there is a parallel lane available, and all cars can run in parallel without interrupting each other, as shown in the following diagram:

Concurrency versus parallelism
[ 196 ]

Performance Considerations

Chapter 7

In addition to transaction processing at the application level, concurrency needs to apply at the network level where multiple servers share the same network resources. For a web server, there is a need to handle many network connections when users try to connect to it over the network. It needs to process the active request and close the connection for the completed or timeout request. At the server level, you will see multiple CPUs assigned or a multicore processor. These help in handling concurrency as the server can handle more threads to complete various tasks simultaneously.
At the memory level, the shared memory concurrency model helps to achieve concurrency. In this model, the concurrent modules interact with each other using shared memory. It could be two programs running in the same server and sharing filesystems where they can read and write. Also, there could be two processors or processor cores sharing the same memory. The disk in your server can encounter concurrency situations where two programs try to write to the same memory block. Concurrent I/O helps to improve disk concurrency by allowing the disk to read and write a file simultaneously.
The database is always a central point of architecture design. Concurrency plays an essential role in data handling as the database should have the ability to respond to multiple requests simultaneously. Database concurrency is more complicated as one user might be trying to read a record while another user is updating it at the same time. The database should only allow data viewing when it gets fully saved. Make sure that the data is completely committed before another user tries to update it. Caching can help to improve performance significantly; let's learn about some different cache types in architecture.

Apply caching
In Chapter 6, Solution Architecture Design Patterns, you learned how to apply caching at various levels of architecture in the Cache-based architecture section. Caching helps to improve application performance significantly. Although you learned the different design patterns to apply to the cache by adding an external caching engine and technology, such as a content distribution network (CDN), it's essential to understand that almost every application component and infrastructure have their cache mechanism. Utilizing the buildcaching mechanism at each layer can help to reduce latency and improve the performance of the application.

[ 197 ]

Performance Considerations

Chapter 7

At the server level, the CPU has its hardware cache, which reduces the latency when accessing data from the main memory. The CPU cache includes the instruction and data cache, where the data cache store copies frequently used data. The cache is also applied at the disk level, but it is managed by operating system software (known as the page cache); however, the CPU cache is entirely managed by hardware. The disk cache is originating from secondary storage, such as the hard disk drive (HDD) or solid-state drive (SSD). Frequently used data is stored in an unused portion of the main memory (that is, the RAM as page cache, which results in quicker access of content).
Oftentimes, the database has a cache mechanism that saves the results from the database to respond faster. The database has an internal cache that gets data ready in the cache based on the pattern of your use. They also have a query cache that saves data in the main server memory (RAM) if you make a query more than once. The query cache gets cleared in case of any changes in data inside the table. In the case that the server runs out of memory, the oldest query result gets deleted to make space.
At the network level, you have a DNS cache, which stores the web domain name and corresponding IP address local to the server. DNS caching allows a quick DNS lookup if you revisit the same website domain name. The DNS cache is managed by the operating system and contains a record of all recent visits to websites. You learned about client-side cache mechanisms such as the browser cache and various caching engines like Memcached and Redis in Chapter 6, Solution Architecture Design Patterns.
In this section, you learned about the original design factors, such as latency, throughput, concurrent, and caching, which need to be addressed for architecture performance optimization. Each component of the architecture (whether it is a network at the server level or an application at the database level) has a certain degree of latency and a concurrency issue that needs to be handled.
You should design your application for the desired performance, as improving performance comes with a cost. The specifics of performance optimization may differ from application to application. Solution architecture needs to direct the effort accordingly--for example, a stock-trading application cannot tolerate sub-millisecond latency, while an ecommerce website can live with a couple of seconds latency. Let's learn about selecting technology for various architecture levels to overcome performance challenges.

[ 198 ]

Performance Considerations

Chapter 7

Technology selection for performance
optimization
In Chapter 6, Solution Architecture Design Patterns, you learned about various design patterns, including microservice, event-driven, cached-based, and stateless. An organization may choose a combination of these design patterns depending on their solution's design needs. You can have multiple approaches to architecture design depending on your workload. Once you finalize your strategy and start solution implementation, the next step is to optimize your application. To optimize your application, you need to collect data by performing load testing and defining benchmarking as per your application's performance requirements.
Performance optimization is a continuous improvement process, one in which you need to take cognizance of optimal resource utilization from the beginning of solution design to after the application's launch. You need to choose the right resources as per the workload or tweak the application and infrastructure configuration--for example, you may want to select a NoSQL database to store the session state for your application and store transactions in the relational database.
For analytics and reporting purposes, you can offload your production database by loading data from the application database to data warehousing solutions and create reports from there. In the case of servers, you may want to choose a virtual machine or containers. You can take an entirely serverless approach to build and deploy your application code. Regardless of your approach and application workload, you need to choose the primary resource type, which includes computing, storage, database, and network. Let's look at more details on how to select these resources type for performance optimization.

Making a computational choice
In this section, you will see the use of the term compute instead of the server, as nowadays software deployments are not limited to servers. A public cloud provider such as AWS has serverless offerings, where you don't need a server to run your application. One of the most popular FaaS offerings is AWS Lambda. Similar to AWS Lambda, other popular public cloud providers extend their offerings in FaaS space--for example, Microsoft Azure has Azure Functions and Google Cloud Platform (GCP) offers Google Cloud functions.

[ 199 ]

Performance Considerations

Chapter 7

However, organizations still make the default choice to go for servers with virtual machines. Now, containers are also becoming popular as the need for automation and resource utilization is increased. Containers are becoming the preferred choice, especially in the area of microservice application deployment. The optimal choice of computing--whether you want to choose server instances, containers, or go for serverless--depends upon application use cases. Let's look at the various compute choices available.

Selecting the server instance
Nowadays, the term instance is getting more popular as virtual servers become norms. These virtual servers provide you flexibility and better use of resources. Particularly for cloud offerings, all cloud providers offer you virtual servers, which can be provisioned with a mere click on a web console or API call. The server instance helps in automation and provides the concept of infrastructure as a code, where everything can be automated everywhere.
As your workload varies, there is a different kind of processing unit choice available. Let's look at some of the most popular options of processing power:
Central processing unit (CPU): The CPU is one of the most popular computing processing choices. CPUs are easy to program, they enable multitasking, and, most importantly, are versatile enough to fit anywhere, which makes them a preferred choice for the general-purpose application. The CPU function is measured in GHz (giga hertz), which indicates that the clock rate of the CPU speed is in billions of cycles per second. CPUs are available at a low cost; however, they are not able to perform well for parallel processing as CPUs have the primary capabilities of sequential processing.
Graphical processing unit (GPU): As the name suggests, the GPU was designed initially to process graphics applications, and is able to provide massive processing power. As the volume of data grows, it needs to process data by utilizing massive parallel processing (MPP). For large data processing use cases, such as machine learning, GPUs have become the obvious choice, and are used in a wide range of compute-intensive applications. You may have heard of the tera floating point operation (TFLOP) as a unit of computation power for GPUs. A teraflop refers to the processor capability to calculate one trillion floating-point operations per second.

[ 200 ]

Performance Considerations

Chapter 7

GPUs consist of thousands of smaller cores compared to CPUs, which have very few lager cores. GPUs have a mechanism to create thousands of threads using CUDA programming, and each thread can process data in parallel, which makes processing super fast. GPUs are a bit costlier than CPUs. When it comes to processing capabilities, you will find that GPUs are in the sweet spot of cost and performance for an application that requires image analysis, video processing, and signal processing; however, they consume lots of power and may not work with a specific type of algorithm where more customized processors are required.
Field-programmable gate array (FPGA): FPGAs are very different to CPUs or GPUs. They are programmable hardware with a flexible collection of logic elements that can be reconfigured for the specific application, which can be changed after installation. FPGAs consume much less power than GPUs but are also less flexible. They can accommodate massive parallel processing and also provide a feature to configure them as CPUs.
Overall, the FPGA cost is higher, as they need to be customized for each individual application and require a longer development cycle. FPGAs may perform poorly for sequential operations and are not very good for flops (float point operations).
Application-specific integrated circuit (ASIC): ASICs are purpose built, and custom integrate circuit optimization for a specific application--for example, specific to the deep learning TensorFlow package, which Google provides as a tensor processing unit (TPU). They can be custom designed for the applications to achieve an optimum combination of power consumption and performance. ASICs incur high costs because of the most extended development cycle, and you have to perform a hardware-level redesign for any changes.

[ 201 ]

Performance Considerations

Chapter 7

The following diagram shows a comparison between the types of processing mentioned in the preceding list. Here, the ASIC is most efficient, but takes a longer development cycle to implement. ASICs provide the most optimal performance but have the least flexibility to reutilize, while CPUs are very flexible and can fit major use cases:

Comparison between CPUs, GPUs, FPGAs, and ASICs
As shown in the preceding diagram, judging by the prospective cost, CPUs are the cheapest and ASICs are the costliest. Today, the CPU has become a commodity and is used everywhere for general-purpose devices to keep costs lower. The GPU has become famous for compute-intensive applications and The FPGA has become the first choice where more customized performance is required. You will see these processing choices available over public cloud providers, such as AWS. In addition to CPUs, their Amazon Elastic Cloud Compute (EC2) offering provides a P-series instance that has a heavy use of the GPU and Fseries instance provides FPGAs for custom hardware acceleration.
In this section, you learned about the most popular compute choice. You may hear about other types of processor, such as the accelerated processing unit (APU). The APU is a combination of the CPU, GPU, and digital signal processor (DSP), which is optimized to analyze analog signals and then requires high-speed processing of data in real time. Let's learn more about other popular compute type containers that are gaining popularity rapidly because of the optimization of the use of resources within the virtual machine.
[ 202 ]

Performance Considerations

Chapter 7

Working with containers
In Chapter 6, Solution Architecture Design Patterns, you learned about container deployment and their benefits under the section titled Deploying an application with a container. The use of containers is becoming the norm to deploy complex microservice applications because of the ease of automation and the efficiency of resource utilization. There are various platforms available for container deployment. Let's learn about some of the most popular choices in the area of the container, their differences, and how they work together.

Docker
Docker is among one of the most in-demand technologies. It allows you to package an application and its related dependencies together as a container and deploy it to any operating system platform. As Docker provides platform-independent capabilities to a software application, this makes the overall software development, testing, and deployment process simplified and more accessible.
Docker container images are portable from one system to another over a local network or across the internet using Docker Hub. You can manage and distribute your container using a Docker Hub container repository in case you make any changes in the Docker image that cause issues in your environment. It's easy to revert to the working version of the container image, which makes overall troubleshooting easier.
Docker containers help you to build a more complex multilayer application--for example, if you need to run the application server, database, and message queue together. You can run them side by side using a different Docker image and then establish communication between them. Each of these layers may have a modified version of libraries, and Docker allows them to run on the same compute machine without conflict.
Public cloud providers, such as AWS, provide containers management platforms, such as Amazon Elastic Container Service (ECS). Container management helps to manage Docker containers on top of the cloud virtual machine, Amazon EC2. AWS also provides the serverless option of container deployment using Amazon Fargate, where you can deploy containers without provisioning virtual machines. Instead of Docker Hub, you can use Amazon Elastic Container Repository (ECR) to manage your Docker imager in the cloud.
Complex enterprise applications are built based on microservices that may span across multiple containers. Managing various Docker containers as a part of one application can be pretty complicated. Kubernetes helps to solve the challenges of the multicontainer environment; let's learn more about Kubernetes.

[ 203 ]

Performance Considerations

Chapter 7

Kubernetes
Kubernetes can manage and control multiple containers in production environments compared to Docker, where you can only work with a few containers. You can consider Kubernetes as a container orchestration system. You can host a Docker container in bare metal, or a virtual machine node called a Docker host, and Kubernetes can co-ordinate across a cluster of these nodes.
Kubernetes makes your application self-healing by replacing unresponsive containers. It also provides horizontal scaling capabilities and a blue�green deployment ability to avoid any downtime. Kubernetes distributes incoming user traffic load between the container and manages the storage shared by various containers.
As shown in the following diagram, Kubernetes and Docker work well together to orchestrate your software application. Kubernetes handles network communication between Docker nodes and Docker containers:

Docker and Kubernetes
[ 204 ]

Performance Considerations

Chapter 7

Docker works as an individual piece of the application and Kubernetes takes care of the orchestration to make sure all these pieces work together as designed. It's easier to automate overall application deployment and scaling with Kubernetes. In Docker, containers are hosted in nodes and each Docker container in a single node shares the same IP space. In Docker, you need to manage the connections between containers by taking care of any IP conflict. Kubernetes solves this problem by having a master instance that keeps track of all nodes hosting containers.
Kubernetes's master node is responsible for assigning an IP address and hosting a key�value store for container configuration along with Kubelet to manage the containers. Docker containers are groups in the pod, where they share the same IP address. This entire setup is called the Kubernetes cluster.
While Kubernetes is quickly becoming popular, there are other options available, such as Docker Swarm, which is built by Docker itself; however, Swarm doesn't have a webbased interface like Kubernetes, and also does not provide autoscaling and external load balancing.
Kubernetes is more complex to learn. A public cloud provider, such as AWS, provides Amazon Elastic Kubernetes Service (EKS) to simplify the management of the Kubernetes cluster. OpenShift is another Kubernetes distribution managed by Red Hat and is offered as a platform as a service (PaaS).
Overall, containers add a layer of virtualization to the whole application infrastructure. While they are useful in resource utilization, you may want to choose a bare metal physical machine for your application deployment if it requires ultra-low latency.

Going serverless
In recent years, serverless computing has become possible because of the popularity of public cloud offerings by cloud providers such as Amazon, Google, and Microsoft. Serverless computing allows the developers to focus on their code and application development without worrying about underlying infrastructure provisioning, configuration, and scaling. This abstracts server management and infrastructure decisions from the developer and lets them focus on their area of expertise and the business problem they are trying to solve. Serverless computing brings a relatively new concept of FaaS.

[ 205 ]

Performance Considerations

Chapter 7

The FaaS offering is available using services such as AWS Lambda, Microsoft Azure Function, and Google Cloud Function. You can write your code in the cloud editor and AWS Lambda handles the computing infrastructure underneath to run and scale your function. You can design event-based architecture or RESTful microservices by adding an API endpoint using Amazon API Gateway and AWS Lambda functions. Amazon API Gateway is a managed cloud service that adds RESTful APIs and WebSocket APIs as frontends for the Lambda functions and enables real-time communication between applications. You can further break your microservice into small tasks that can be scaled automatically and independently.
In addition to focusing on your code, you never have to pay for idle resources in the FaaS model. Rather than scaling your entire service, you can scale the required functions independently with built-in availability and fault tolerance; however, it could be a pretty daunting task if you have thousands of features to orchestrate, and predicting the autoscaling cost can be tricky. These are especially good for scheduling jobs, processing web requests, or queuing messages.
In this section, you learned about the various computing choices, looking at server instances, serverless options, and containers. You need to select these compute services based on your application's requirement. There is no rule that forces you to choose a particular type of computing; it is all about your choice of organization's technology, the pace of innovation, and the nature of the software application.
However, in general, for the monolithic application, you can stick to a virtual or bare-metal machine, and for complex microservices, you can choose containers. For simple task scheduling or events-based applications, you can go for function as an obvious choice. Many organizations have built complex applications that are entirely serverless, which helped them to save costs and achieve high availability without managing any infrastructure.
Let's learn about another important aspect of your infrastructure and how it can help you to optimize performance.

[ 206 ]

Performance Considerations

Chapter 7

Choosing a storage
Storage is one of the critical factors for your application's performance. Any software application needs to interact with storage for installation, logging, and accessing files. The optimal solution for your storage will differ based on the following factors:

Access methods

Block, file, or object

Access patterns Access frequency Update frequency Access availability Access durability
Access throughput

Sequential or random Online (hot), offline (warm), or archival (cold) Write once read many (WORM) or dynamic Availability of storage when required Reliability of data store to minimize any data loss
Input/output per second (IOPS) and data read/write per second in MBs.

These depend upon your data format and scalability needs. You first need to decide whether your data will be stored in block, file, or object storage. These are the storage formats that store and present data in a different way. Let's look at this in more detail.

Working with block storage and storage area network
(SAN)
Block storage divides data into blocks and stores them as chunks of data. Each block has a unique ID that allows the system to place data wherever it is accessible faster. As blocks don't store any metadata about files, so a server-based operating system manages and uses these blocks in the hard drive. Whenever the system requests data, the storage system collects the blocks and gives the result back to the user. Block storage deployed in a storage area network (SAN) stores data efficiently and reliably. It works well where a large amount of data needs to be stored and accessed frequently--for example, database deployment, email servers, application deployment, and virtual machines.

[ 207 ]

Performance Considerations

Chapter 7

SAN storage is sophisticated and supports complex, mission-critical applications. They are a high-performance storage system that communicates block-level data between the server and storage; however, SAN is significantly costly and should be used for largescale, enterprise applications where low latency is required.

To configure your block-based storage, you have to choose between a solid-state drive (SSD) and a hard-disk drive (HDD). HDDs are the legacy data storage for servers and enterprise storage arrays. HDDs are cheaper, but they are slower and need more power and cooling. SSDs use semiconductor chips and are faster than HDDs. They are much more costly; however, as technology evolves, SSDs will become more affordable and gain popularity because of their efficiency and lower power and cooling requirements.

Working with file storage and network area storage
(NAS)
File storage has been around for a long time and is widely used. In file storage, data is stored as a single piece of information and is organized inside folders. When you need to access the data, you provide the file path and get the data files; however, a file path can grow complicated as files become nested under multiple folder hierarchies. Each record has limited metadata, including the filename, time of creation, and updated timestamps. You can take the analogy of a book library where you store books in drawers and keep a note of the location where each book is stored.
An NAS is a file storage system that is attached to the network and displays to the user where they can store and access their files. NAS storage also manage user privilege, file locking, and other security mechanisms that protect the data. NAS storage works well as file-sharing systems and local archives. When it comes to storing billions of files, NAS might not be the right solution, given that it has limited metadata information and a complex folder hierarchy. To store billions of files, you need to use object storage. Let's learn more about object storage and its benefits over file storage.

Working with object storage and the cloud data storage
Object storage bundles the data itself with a unique identifier and metadata that is customizable. Object storage uses a flat address space compared to the hierarchical addresses in file storage or addresses distributed over a chunk of blocks in block storage. Flat address space makes it easier to locate data and retrieve it faster regardless of the data storage's location. Object storage also helps the user to achieve an unlimited scalability of storage.
[ 208 ]

Performance Considerations

Chapter 7

Object storage metadata can have lots of details, and users can customize it to add more details compared to the addition of tagging in file storage. Data can be accessed by a simple API call and is very cost-effective to store. Object storage performs best for high-volume, unstructured data; however, objects cannot be modified but only replaced, which makes it not a good use case for a database.
Cloud data storage, such as Amazon Simple Storage Service (S3), provides an unlimited scalable object data store with high availability and durability. You can access data with a unique global identifier and metadata file prefix. The following diagram shows all three storage systems in a nutshell:

Data storage systems
As shown in the preceding diagram, block storage stores data in blocks. You should use block storage when your application needs very low latency and data storage access by a single instance. File storage stores data in a hierarchical folder structure and has little latency overhead. You should use the file storage system when a separate room needs to access multiple instances. Object storage stores data in buckets with a unique identifier for the object. It provides access over the web to reduce latency and increase throughput. You should use object storage to store and access static content, such as images and videos. You can store a high volume of data in the object store and perform big data processing and analysis.
Direct-attached storage (DAS) is another kind of data storage where the storage is directly attached to the host server; however, it has a very limited scalability and storage capacity. The magnetic tape drive is another popular storage system for backing up and archiving. Because of its low cost and high availability, magnetic tape drives are used for archival purposes, but have high latency, which makes them unsuitable for use in direct applications.
[ 209 ]

Performance Considerations

Chapter 7

Oftentimes, you will need to increase throughput and data protection for a mission-critical application, such as a transactional database, where data is stored in SAN storage; however, an individual SAN storage may have limited volume and throughput. You can overcome this situation using a redundant array of independent disks (RAID) configuration. A RAID is a way of storing data on multiple disks. It protects data loss from a drive failure and increases disk throughput by striping various disks together.
RAID uses the technique of disk mirroring or disk striping, but for the operating system, RAID is a single logical disk. RAID has a different level to distinguish the configuration type--for example, RAID 0 uses disk striping and provides the best performance, but has no fault tolerance, whereas RAID 1 is known as disk mirroring. It duplicates the data storage and provides no performance improvement for write operations but doubles the read performance. You can combine both RAID 0 and RAID 1 to form RAID 10 and achieve the best of both with high throughput and fault tolerance.
Select the storage solution that matches your access pattern to maximize performance. There are various options available with a cloud offering to choose for your block, file, and object storage method--for example, the public cloud AWS provides Amazon Elastic Block Store (EBS) as a SAN type of storage in the cloud and Amazon Elastic File Storage (EFS) as an NAS type of storage in the cloud. Amazon S3 is very popular for object storage. Different storage solutions provide you the flexibility to choose your storage methods based on the access pattern, whether you are working in an on-premise environment or wanting to go cloud native.
Now that you have learned about the compute and storage choices that are necessary to achieve optimal performance, let's look at the next critical component of the application development, which is the database. Choosing the right database for the right need will help you to maximize your application performance and lower overall application latency. There are different types of database available, and choosing the correct database is critical.

Choosing the database
Oftentimes, you will want to standardize a common platform and use a database for ease of management; however, you should consider using a different type of database solution as per your data requirement. Selecting the incorrect database solution can impact system latency and performance. The choice of database can vary based on your application's requirements for availability, scalability, data structure, throughput, and durability. There are multiple factors to consider when choosing to use a database--for example, the access pattern can significantly impact the selection of database technology. You should optimize your database based on the access pattern.

[ 210 ]

Performance Considerations

Chapter 7

Databases generally have a configuration option for workload optimization. You should consider the configuration for memory, cache, storage optimization, and so on. You should also explore the operational aspect of database technologies in terms of scalability, backup, recovery, and maintenance. Let's look at the different database technologies that can be used to fulfill the database requirements of applications.

Online transactional processing (OLTP)
Most of the traditional relational databases are considered OLTP. The transactional database is the oldest and most popular method of storing and handling application data. Some examples of relational OLTP databases are Oracle, Microsoft SQL Server, MySQL, PostgreSQL, Amazon RDS, as well as others. The data access pattern for OLTP involves fetching a small dataset by looking up their ID. A database transaction means that either all related updates of the database table completed, or none of them did.
The relational model allows the processing of complex business transactions in an application, such as banking, trading, and e-commerce. It will enable you to aggregate data and create complex queries using multiple joins across tables. While optimizing your relational database, you need to consider including the following optimizations:
Database server that includes computing, memory, storage, and network Operating system-level settings, such as a RAID configuration of the storage volume, volume management, and block size Database engine configuration and partition as required Database-related options, such as schema, index, and view
Scaling can be tricky for the relational database as it can scale vertically and hit the upper limit of system capacity. For horizontal scaling, you have to read the replica for read scaling and partition for write scaling. In the previous chapter, you learned how to scale a relational database in the section titled Database handling in the application architecture.
OLTP databases are suitable for large and complex transactional applications; however, they don't scale well where a massive amount of data needs to aggregate and be queried. Also, with the internet boom, there is a lot of unstructured data that is coming from everywhere, and relational databases are not able to handle unstructured data efficiently out of the box. In this case, the NoSQL database comes to the rescue. Let's learn more about how to handle a nonrelational database.

[ 211 ]

Performance Considerations

Chapter 7

Nonrelational databases (NoSQL)
There is a lot of unstructured and semistructured data produced by application such as social media programs, the IoT (internet of things), and logs, where you have a very dynamic schema. These data types may have different schemas from each set of records. Storing this data in a relational database could be a very tedious task. Everything has to be filed into fixed schema, which can either cause lots of null values or data loss. The nonrelational or NoSQL database provides you with the flexibility to store such data without worrying about fixed schema. Each record can have a variable number of columns and can be stored in the same table.
NoSQL databases can store a large amount of data and provide low-access latency. They are easy to scale by adding more nodes when required and can support horizontal scaling out of the box. They can be an excellent choice to store user session data and can make your application stateless to achieve horizontal scaling without compromising user experience. You can develop a distributed application on top of the NoSQL database, which provides good latency and scaling, but query joining has to be handled at the application layer. NoSQL databases don't support complex queries such as joining tables and entities.
There are various choices available for the NoSQL database--for example, Cassandra, HBase, and MongoDB, which you can install in a cluster of virtual machines; however, the public cloud-like AWS provides a managed NoSQL database called Amazon Dynamo DB, which provides high throughput and sub-millisecond latency with unlimited scaling.
You can use OLTP for a relational database, but it has limited storage capacity. It doesn't respond well to queries for large amounts of data, and those that perform aggregations as required for data warehouses. Data warehousing needs are more analytical than transactional. The OLAP database satisfies the gap of the OLTP database to query a large dataset. Let's learn more about the OLAP database.

Online analytical processing (OLAP)
OLTP and NoSQL databases are useful for application deployment but have limited capabilities for large-scale analysis. A query for a large volume of structured data for analytics purposes is better served by a data warehouse platform designed for faster access to structured data. Modern data warehouse technologies adopt the columnar format and use massive parallel processing (MPP), which helps to fetch and analyze data faster.

[ 212 ]

Performance Considerations

Chapter 7

The columnar format avoids the need to scan the entire table when you need to aggregate only one column for data--for example, if you want to determine the sales of your inventory in a given month. There may be hundreds of columns in the order table, but you need to aggregate data from the purchase column only. With a columnar format, you will only scan the purchase column, which reduces the amount of data scanned compared to the row format, and thereby increases the query performance.
With massive parallel processing, you store data in a distributed manner between child nodes and submit a query to the leader nodes. Based on your partition key, the leader node will distribute queries to the child nodes, where each node picks up part of a query to perform parallel processing. The leader node then collects the subquery result from each child node and returns your aggregated result. This parallel processing helps you to execute the query faster and process a large amount of data quicker.
You can use this kind of processing by installing software such as IBM Netezza or Microsoft SQL server on a virtual machine, or you can go for a more cloud-native solution, such as Snowflake. A public cloud, such as Amazon Web Service, provides the petabytescale data warehousing solution Amazon Redshift, which uses the columnar format and massively parallel processing. You will learn more about data processing and analytics in Chapter 13, Data Engineering and Machine Learning.
You need to store and search a large amount of data, especially when you want to find a specific error in your logs or build a document search engine. For this kind of capability, your application needs to create a data search. Let's learn more about the data search.

Building a data search
Oftentimes, you will need to search a large volume of data to solve issues quickly or get business insights. The ability to search your application data will help you to access detailed information and analyze it from different views. To search for data with low latency and high throughput, you need to have search engines as your technology choice.
Elasticsearch is one of the most popular search engine platforms and is built on top of the Apache Lucene library. Apache Lucene is a free and open source software library that is the foundation of many popular search engines. The ELK (short for Elasticsearch, LogStash, and Kibaba) stack is easy to use for the automatic discovery of large-scale data and to index it for searching. Because of its property, there are multiple tools that have been developed around Elasticsearch for visualization and analysis--for example, LogStash works with Elasticsearch to collect, transform, and analyze a large amount of an application's log data. Kibana has an in-built connector with Elasticsearch that provides a simple solution for creating dashboards and analysis on indexed data.

[ 213 ]

Performance Considerations

Chapter 7

Elasticsearch can be deployed in virtual machines and scale horizontally to increase capacity by adding new nodes to the cluster. The public cloud AWS provides the managed service Amazon Elasticsearch Service (Amazon ES), which makes it cost effective and simple to scale and manage the Elasticsearch cluster in the cloud.
In this section, you learned about the various database technologies and what they are used for. Your applications can use a combination of all database technologies in order for their different components to achieve optimal performance. For complex transactions, you need to use a relation OLTP database, and to store and process unstructured or semistructured data, you need to use a nonrelational NoSQL database. You should use the NoSQL database where very low latency is required over multiple geographical regions and where you need to handle complex queries at the application layer, such as in a gaming application. If you need to perform any large-scale analytics on structured data, use a data warehouse OLAP database.
Let's look at another critical component of your architecture, which is networking. Networking is the backbone of the entire application and establishes communication between the servers and the outside world. Let's learn about networking as regards application performance.

Making the networking choice
In this era of fast internet availability in almost every corner of the world, it is expected that applications will have a global user reach. Any delay in the system's response time depends upon the request load and the distance of the end user from the server. If the system is not able to respond to user requests in a timely manner, it can have a ripple effect by continuing to engage all system resources and pile up a huge request backlog, which will degrade overall system performance.
To reduce latency, you should simulate the user's location and environment to identify any gap. As per your findings, you should design the server's physical location and caching mechanism to reduce network latency; however, the network solution choice for an application depends upon the networking speed, throughput, and network latency requirements. For an application to handle a global user base, it needs to have fast connectivity with its customers where location plays an important role. Edge locations provided by the CDN help to localize the heavy content and reduce overall latency.

[ 214 ]

Performance Considerations

Chapter 7

In Chapter 6, Solution Architecture Design Patterns, you learned how to use a CDN to put data near your user's location in the section titled cache-based architecture. There are various CDN solutions available with an extensive network of edge locations. You can use a CDN if your application is static-content-heavy, where you need to deliver large image and video content to your end user. Some of the more popular CDN solutions are Akamai, Cloudflare, and Amazon CloudFront (provided by the AWS cloud). Let's look at some DNS routing strategies to achieve low latency if your application is deployed globally.

Defining a DNS routing strategy
In order to have global reach, you may be deploying your application in multiple geographical regions. When it comes to user request routing, you want to route their requests to the nearest and fastest available server for a quick response from your application. The DNS router provides the mapping between the domain names to the IP addresses and makes sure that the requests are served by the right server when the user types in the domain name--for example, when you type amazon.com in your browser to do some shopping, your request is always routed to the Amazon application server by the DNS service.
The public cloud-like AWS provides a DNS service called Amazon Route 53, where you can define a different kind of routing policy as per your application's need. Amazon Route 53 provides DNS services to simplify domain management and zone APEX support. The following are the most used routing policies:
Simple routing policy: As the name suggests, this is the most straightforward routing policy and doesn't involve any complications. It is useful to route traffic to a single resource--for example, a web server that serves content for a particular website. Failover routing policy: This routing policy requires you to achieve high availability by configuring active�passive failover. If your application goes down in one region, then all the traffic can be routed to another region automatically. Geolocation routing policy: If the user belongs to a particular location then you can use a geolocation policy. A geolocation routing policy helps to route traffic to a specific region. Geoproximity routing policy: This is like a geolocation policy, but you have the option to shift traffic to other nearby locations when needed.

[ 215 ]

Performance Considerations

Chapter 7

Latency routing policy: If your application is running in multiple regions, you can use a latency policy to serve traffic from the region where the lowest latency can be achieved. Weighted routing policy: A weighted routing policy is used for A/B testing, where you want to send a certain amount of traffic to one region and increase this traffic as your trial proves more and more successful.
Additionally, Amazon Route 53 can detect anomalies in the source and volume of DNS queries and prioritize requests from users that are known to be reliable. It also protects your application from a DDoS attack. Once traffic passes through the DNS server, in most cases, the next stop will be a load balancer, which will distribute traffic among a cluster of servers. Let's learn about some more details regarding the load balancer.

Implementing a load balancer
The load balancer distributes network traffic across the servers to improve use concurrency, reliability, and application latency. The load balancer can be physical or virtual. You need to choose a load balancer based on your application's need. Commonly, two types of load balancer can be utilized by the application:
1. Layer 4 or network load balancer: Layer 4 load balancing routes packets based on information in the packet header--for example, source/destination IP addresses and ports. Layer 4 load balancing does not inspect the contents of a packet, which makes it less compute intensive and therefore faster. A network load balancer can handle millions of requests per second.
2. Layer 7 or application load balancer: Layer 7 load balancing inspects, and routes packets based on the full contents of the packet. Layer 7 is used in conjunction with HTTP requests. The materials that inform routing decisions are factors such as HTTP headers, URI path, and content type. This allows for more robust routing rules but requires more compute time to route packets. The application load balancer can route the request to containers in your cluster based on their distinctive port number.

[ 216 ]

Performance Considerations

Chapter 7

Depending on the environment, you can choose hardware-based load balancers, such as an F5 load balancer or a Cisco load balancer. You can also choose a software-based load balancer, such as Nginx. The public cloud provider AWS facilitates a managed virtual load balancer called Amazon Elastic load balancer (ELB). ELB can be applied at layer 7 as an application load balancer and tier 4 as a network load balancer.
A load balancer is a great way of securing your application, making it highly available by sending a request to healthy instances. It works together with autoscaling to add or remove instances as required. Let's look at autoscaling and learn how it helps to improve overall performance and the high availability of your application.

Applying autoscaling
You learned about autoscaling in Chapter 4, Principles of Solution Architecture Design. You learned about predictive autoscaling and reactive autoscaling in the section titled Design for scale. The concept of autoscaling became popular with the agility provided by the cloud computing platform. Cloud infrastructure allows you to easily scale up or scale down your server fleet based on user or resource demand.
With a public cloud platform such as AWS, you can apply autoscaling at every layer of your architecture. In the presentation layer, you can scale the web server fleet based on your requests, and at the application layer based on the server's memory and CPU utilization. You can also perform scheduled scaling if you know the traffic pattern when the server load is going to increase. At the database level, autoscaling is available for relational databases such as Amazon Aurora Serverless and the Microsoft Azure SQL database. A NoSQL database such as Amazon DynamoDB can be autoscaled based on throughput capacity.

[ 217 ]

Performance Considerations

Chapter 7

When autoscaling, you need to define the number of desired server instances. You need to define the maximum and minimum server capacity as per your application's scaling needs. The following screenshot illustrates the autoscaling configuration from AWS Cloud:

Autoscaling configuration
In the preceding autoscaling configuration setting, if three web server instances are running, it can scale up to 5 instances if the CPU utilization of servers goes above 50% and scale down to 2 instances if the CPU utilization goes below 20%. In the case of an unhealthy instance, the count will go below the desired capacity in a standard scenario. In such a case, the load balancer will monitor the instance health and will use autoscaling to provision new instances. The load balancer monitors instance health and will trigger autoscaling to provision new instances as required.
[ 218 ]

Performance Considerations

Chapter 7

Autoscaling is a good feature to have, but make sure you set up your desired configurations to limit the cost of a change in CPU usage. In the case of unforeseen traffic due to events such as a distributed denial of service (DDoS) attack, autoscaling can increase cost significantly. You should plan to protect your system for such kinds of events. You will learn more about this in Chapter 8, Security Considerations.
At the instance level, you need high-performance computing (HPC) to perform manufacturing simulation or gnome analysis. HPC performs well when you put all instances in the same network close to each other for low latency of data transfer between the node of a cluster. Between your data centers or cloud, you can choose to use your private network, which can provide an additional performance benefit. For example, to connect your data center to AWS cloud, you can use Amazon Direct Connect. Direct Connects provides 10 Gbps private fiber optics lines, where Network latency is much lower than sending data over the internet.
In this section, you have learned about various networking components that can help to improve application performance. You can optimize your application network traffic according to your user location and application demand. Performance monitoring is an essential part of your application, and you should do proactive monitoring to improve customer experience. Let's learn more about performance monitoring

Managing performance monitoring
Performance monitoring is important when you are trying to proactively understand any performance issue and reduce end user impact. You should define your performance baseline and raise the alarm to the team in the case of a threshold breach--for example, an application's mobile app open time should not be more than three seconds. Your alarm should be able to trigger an automated action to handle poorly performing components--for example, adding more nodes in a web application cluster to reduce the request load.

[ 219 ]

Performance Considerations

Chapter 7

There are multiple monitoring tools available to measure application performance and overall infrastructure. You can use a third-party tool, such as Splunk, or AWS provided Amazon CloudWatch to monitor any application. Monitoring solutions can be categorized into active monitoring and passive monitoring solutions:
With active monitoring, you need to simulate user activity and identify any performance gap upfront. Application data and workload situations are always changing, which requires continuous proactive monitoring. Active monitoring works alongside passive monitoring as you run the known possible scenarios to replicate user experience. You should run active monitoring across all dev, test, and prod environments to catch any issue before it reaches the user.
Passive monitoring tries to identify an unknown pattern in real time. For a webbased application, passive monitoring needs to collect important metrics from the browser that can cause performance issues. You can gather metrics from users regarding their geolocation, browser types, and device types to understand user experience and the geographic performance of your application. Monitoring is all about data, and it includes the ingestion, processing, and visualization of lots of data.
You will continue to learn about the various monitoring methods and tools in upcoming chapters and dive deep into monitoring and alerts in Chapter 9, Architectural Reliability Considerations.

Performance always comes with a cost, and, as a solution architect, you need to think about the trade-offs to take the right approach--for example, an organization's internal applications, such as the timesheet and HR programs, may not need very high performance compared to external products, such as e-commerce applications. An application that deals with trading (for example) needs very high performance, which requires more investment. As per your application's needs, you can balance between durability, consistency, cost, and performance
Tracking and improving performance are complex tasks, where you need to collect lots of data and analyze patterns. An access pattern helps you to make the right choice for performance optimization. Load testing is one of the methods that allows you to tweak your application configuration by simulating user load and provides you with data to make the right decisions for your application architecture. Applying continuous active monitoring in combination with passive monitoring helps you to maintain consistent performance for your application.

[ 220 ]

Performance Considerations

Chapter 7

Summary
In this chapter, you learned about the various architecture design principles that impact the performance of applications. You learned about latency and throughput at different layers of architecture and how they relate to each other. For high-performant applications, you need to have low latency and high throughput at every layer of the architecture. Concurrency helps to process a large number of requests. You also learned the difference between parallelism and concurrency and got an insight into how caching can help to improve overall application performance.
Then you learned about how to choose your technology and their working models, which can help to achieve your desired application performance. While looking at the compute option, you learned about the various processor types and their differences to help you make the right choice when selecting server instances. You learned about containers and how they can help you to utilize the resources efficiently and at the same time help to improve performance. You also learned how Docker and Kubernetes work well with each other and fit into your architecture.
In the section on choosing storage, you learned about different kinds of storage, such as block, file, and object storage and their differences. You also learned about the available storage choices in on-premise and cloud environments. Storage choice depends on multiple factors. You can enhance disk storage durability and throughput by putting multiple volumes in a RAID configuration.
In the section on choosing a database, you learned about the various database types, including relational, nonrelational, data warehouse, and data search. While looking at choosing your network, you learned about the various request routing strategies that can help you to improve network latency for your globally distributed user. You learned how load balancers and autoscaling can help you to manage a large number of user requests without compromising application performance.
In the next chapter, you will learn about how to secure your application by applying authentication and authorization. This will ensure that your data at rest and in transit and your application is protected from various kinds of threats and attacks. You will also learn about compliance requirements and how to satisfy them when designing your application. You will learn the details about security audits, alerts, monitoring, and automation.

[ 221 ]

8
Security Considerations
Security is always at the center of architecture design. Many large enterprises suffer financial loss due to security breaches when their customer data gets leaked. Organizations not only lose customer trust but also lose the entire business. There are many industrystandard compliances and regulations out there to make sure your application is secure and protects customer-sensitive data.
Security isn't just about getting through the outer boundary of your infrastructure. It's also about ensuring that your environments and their components are secured from each other. In the previous chapter, you learned about various performance-improvement aspects and technology choices for your architecture. In this chapter, you will gain an understanding of best practices to secure your application and make sure it is compliant with industrystandard regulations.
For example, in the server, you can set up a firewall that allows you to determine which ports on your instances can send and receive traffic, and where that traffic can come from. You can use firewall protection to reduce the probability that a security threat on one instance will not spread to other instances in your environment. Similar precautions are required for other services. Specific ways to implement security best practices are discussed throughout this chapter.
You will learn the following best security practices in this chapter:
Designing principles for architectural security Selecting technology for architectural security Security and compliance certifications The cloud's shared security responsibility model
You will learn various design principles applicable to secure your solution architecture. Security needs to be applied at every layer and in every component of the architecture. You will get an understanding of the right technology to select to ensure your architecture is secure at every layer.

Security Considerations

Chapter 8

Designing principles for architectural
security
Security is all about the ability to protect your system and information while delivering business value for your customers. You need to conduct an in-depth risk assessment and plan a mitigation strategy for the continuous operation of your business. The following sections talk about the standard design principles that help you to strengthen your architectural security.

Implementing authentication and authorization
control
The purpose of authentication is to determine if a user can access the system with the provided credentials of user ID and password. While authorization determines what a user can do once they are inside the system, you should create a centralized system to manage your user's authentication and authorization.
This centralized user management system helps you to keep track of the user's activity so you can deactivate them if they are no longer a part of the system. You can define standard rules to onboard a new user and remove access for inactive users. The centralized system eliminates reliance on long-term credentials and allows you to configure other security methods such as password rotation and strength.
For authorization, you should start with the principle of least privilege--it means users should not have any access to begin with, and then begin assigning them only the required access according to their job role. Creating an access group according to job role helps to manage the authorization policy in one place and apply authorization restrictions across a large number of users. For example, you can restrict the development team to have full access to the dev environment and read-only access to the production environment. If any new developer joins, they should be added to this dev group, where all authorization policies are managed centrally.
Enabling single sign-on with a centralized users' repository helps to reduce the hassle of remembering multiple passwords for your user base and eliminates any risk of password leakage. Large organizations use centralized user management tools such as Active Directory (AD) for employee authentication and authorization, to provide them access to internal enterprise applications such as the HR system, the expense system, the timesheet application, and so on.

[ 223 ]

Security Considerations

Chapter 8

In a customer-facing application, such as e-commerce and social media websites, you can use an OpenID authentication system to maintain a centralized system. You will learn about large-scale user management tools in more detail in the OAuth section of this chapter.

Applying security everywhere
Often, organizations have a main focus of ensuring the physical safety of their data center and protecting the outer networking layer from any attack. Instead of just focusing on a single outer layer, ensure that security is applied at every layer of the application.
Apply the defense-in-depth (DiD) approach, and put security at various layers of the application; for example, a web application needs to be secured from an external internet traffic attack by protecting the Enhanced Data Rates for Global Evolution (EDGE) network and Domain Name System (DNS) routing. Apply security at the load balancer and network layers to block any malicious traffic.
Secure every instance of your application by allowing only required incoming and outgoing traffic in the web application and database layer. Protect operating systems with antivirus software to safeguard against any malware attack. Apply both proactive and reactive measures of protection by putting intrusion detection and intrusion prevention systems in front of your traffic flow and Web Application Firewall (WAF) to protect your application from various kinds of attacks. You will learn more details about the various security tools to use in the Selecting technology for architectural security section of this chapter.

Reducing blast radius
While applying security measures at every layer, you should always keep your system isolated in a small pocket to reduce the blast radius. If attackers get access to one part of the system, you should be able to limit a security breach to the smallest possible area of the application. For example, in a web application, keep your load balancer in a separate network from other layers of the architecture, as that will be internet-facing. Further, apply network separation at the web, application, and database layers. In any case, if an attack happens in one layer, it will not expand to other layers of the architecture.
The same rules are applied to your authorization system to give the least privilege to users and provide only the minimum required access. Make sure to implement multi-factor authentication (MFA) so that even if there's a breach in user access, it always needs a second level of authentication to get into the system.

[ 224 ]

Security Considerations

Chapter 8

Provide minimal access to ensure that you are not exposing the entire system and provide temporary credentials to make sure access is not open for a long time. Take particular caution when providing programmatic access by putting a secure token in place, with frequent key rotation.

Monitoring and auditing everything all the time
Put the logging mechanism for every activity in your system and conduct a regular audit. Audit capabilities are often also required from various industry-compliance regulations. Collect logs from every component, including all transactions and each API call, to put centralized monitoring in place. It is a good practice to add a level of security and access limitation for a centralized logging account so that no one is able to tamper with it.
Take a proactive approach and have the alert capability to take care of any incident before the user gets impacted. Alert capabilities with centralized monitoring help you to take quick action and mitigate any incident. Monitor all user activity and application accounts to limit the security breach.

Automating everything
Automation is an essential way to apply quick mitigation for any security-rule violation. You can use automation to revert changes against desired configurations and alert the security team--for example, if someone added admin users in your system and an open firewall to an unauthorized port or IP address. Applying automation in security systems has become popular with the concept of DevSecOps. DevSecOps is about adding security at every part of application development and operation. You will learn more about DevSecOps in Chapter 12, DevOps and Solution Architecture Framework.
Create secure architectures and implement security control that is defined and managed as code. You can version-control your security as a code template, and analyze changes as required. Automated security mechanisms as software code help you scale security operations more rapidly, in a cost-effective way.

[ 225 ]

Security Considerations

Chapter 8

Protecting data
Data is at the center of your architecture, and it is essential to secure and protect it. Most of the compliance and regulation in place are there to protect customer data and identity. Most of the time, any attack has the intention of stealing the user's data. You should categorize your data as per its sensitivity level and protect it accordingly. For example, customer credit card information should be the most sensitive data and needs to be handled with the utmost care. However, a customer's first name may not be that sensitive compared to their password.
Create mechanisms and tools that should minimize the need for direct access to data. Avoid manual processing of data by applying tool-based automation that eliminates human error, especially when handling sensitive data. Apply access restrictions to the data wherever possible to reduce the risk of data loss or data modification.
Once you categorize data sensitivity, you can use the appropriate encryption, tokenization, and access control to protect the data. Data needs to be protected not only at rest but when transmitting over the network as well. You will learn about various mechanisms to protect data in the Data security section of this chapter.

Preparing a response
Keep yourself ready for any security events. Create an incident management process as per your organizational policy requirements. Incident management can differ from one organization to another and from one application to another. For example, if your application is handling Personal Identifiable Information (PII) of your customers, you need a tighter security measure in your incident response. However, if the application is handling small amounts of sensitive data, such as an inventory management application, then it will have a different approach.
Make sure to simulate the incident response to see how your security team is recovering from the situation. Your team should use automation tools for speed of detection, investigation, and response to any security event. You need to set up the alert, monitor, and audit mechanisms to do Root Cause Analysis (RCA) to prevent such events occurring again.
In this section, you learned about the general security principles to apply in your architecture for application security. In the next section, you will learn how to apply these principles using different tools and techniques.

[ 226 ]

Security Considerations

Chapter 8

Selecting technology for architectural
security
The previous section was more focused on the general rules of application security to consider while creating an architecture design, but the question is: How do we apply these rules to make the application secure during implementation? There are various tools and technologies available for each layer of your application to make it secure.
In this section, you will learn in detail about the multiple technology choices to apply in the area of user management and protection of the web, infrastructure, and data of your application. Let's start with the first area, user identity and access management.

User identity and access management
User identity and access management are vital parts of information security. You need to make sure only authenticated and authorized users are able to access your system resources in a defined manner. User management could be a daunting task as your organization and product adoption grows. User access management should differentiate and manage access to an organization's employees, vendors, and customers.
Enterprise or corporate users could be the organization's employees, contractors, or vendors. Those are specialist users who have a special privilege to develop, test, and deploy the application. In addition to that, they require access to another corporate system to do their daily job--for example, an Enterprise Resource System (ERP), a payroll system, an HR system, a timesheet application, and so on. As your organization grows, the number of users can grow from hundreds to thousands.
The end users are the customers who use your applications and have minimal access to explore and utilize the desired feature of the application--for example, players of a gaming application, users of social media applications, or customers of an e-commerce website. The count of these users could be from hundreds to thousands to millions (or even more) as the popularity of your product or application grows. The other factor is that user count can grow exponentially, which can add challenges. You need to take special care of security when exposing the application to external-facing internet traffic to protect it from various threats.

[ 227 ]

Security Considerations

Chapter 8

Let's talk about corporate user management first. You need to have a centralized repository where you can enforce security policies such as strong password creation, password rotation, and multi-factor authentication (MFA) for better user management. The use of MFA provides another means of validating someone's identity, if a password may have already compromised. Popular MFA providers include Google Authenticator, Gemalto, YubiKey, RSA SecureID, Duo, and Microsoft Authenticator.
From a user-access prospective, role-based authentication (RBA) simplifies user management; you can create user groups as per the user's role and assign an appropriate access policy. As illustrated in the following diagram, you have three groups--admin, developer, and tester--with the corresponding access policy applied to the individual group. Here, admin can access any system, including production, while developer access is limited to the dev environment, and so the tester can only access the test environment:

User group organization
As shown in the preceding diagram, when any new user joins the team, they get assigned to the appropriate group as per their role. In this way, each user has a defined set of standard access. The user group also helps to update access in case a new development environment gets introduced, and all developers need to have access to that.
Single Sign-On (SSO) is the standard process to reduce any security lapses and help to automate the system. SSO provides users with a login to the different corporate systems, with a single user ID and password. Federated Identity Management (FIM) allows users to access the system without a password with a pre-authenticated mechanism. Let's look at some more details.
[ 228 ]

Security Considerations

Chapter 8

FIM and SSO
FIM provides a way to connect the identity management system when user information is stored in the third-party identity provider (IdP). With FIM, the user only provides authentication information to the IdP, which in turn already has a trusted relationship with the service.
As illustrated in the following diagram, when a user logs in to access a service, the service provider (SP) gets credentials from the IdP, rather than getting them directly from the user:

FIM
SSO allows the use of a single sign-on, with which the user can access multiple services. Here, an SP could target an environment where you want to log in--for example, a Customer Relationship Management (CRM) application or your cloud application. An IdP could be a corporate AD. Federation allows something similar to an SSO without a password, as the federation server knows users to access information.
There are various techniques available to implement FIM and SSO. Let's look at some of the popular Identify and Access Management (IAM) choices available.
Kerberos
Kerberos is an authentication protocol that allows two systems to identify each other in a secure way and helps to implement SSO. It works in the client-server model and uses a ticket system for user identity. Kerberos has the Key Distribution Center (KDC), which facilitates authentication between two systems. The KDC consists of two logical parts--the Authentication Server (AS) and the Ticket-Granting Server (TGS).
[ 229 ]

Security Considerations

Chapter 8

Kerberos stores and maintains the secret keys of each client and server in the datastore. It establishes a secure session between two systems during their communication and identifies them with the stored secret key. The following diagram illustrates the architecture of Kerberos authentication:

Kerberos authentication
As shown in the preceding diagram, when you want to access a service, the following steps are involved:
1. The client sends an access ticket request to the AS as a plaintext request. This request contains the client ID, TGS ID, IP address, and authentication time.
2. The AS checks if your information is available in the KDC database. Once AS has found your information, it establishes a session between the client request and the TGS. The AS then replies to the client with the Ticket-Granting Ticket (TGT) and the TGS session key.
3. Now, the TGS session key asks for a password, and, given the correct password, a client can decrypt the TGS session key. However, it cannot decrypt the TGT since the TGS secret key is not available.
4. Now, the client sends the current TGT to the TGS with the authenticator. The TGS contains the session key along with the client ID and Service Principal Name (SPN) of the resource the client wants to access.
[ 230 ]

Security Considerations

Chapter 8

5. Now, the TGS again checks if the requested service address exists in the KDC database. If yes, the TSG will then encrypt the TGT and send a valid session key for the service to the client.
6. The client forwards the session key to the service to prove that the user has access, and the service grants access.
While Kerberos is an open source protocol, large enterprises like to use more managed software with robust support, such as AD. Let's look at the working mechanism of one of the most popular user management tools, Microsoft AD, which is based on the Lightweight Directory Access Protocol (LDAP).

AD
AD is an identity service developed by Microsoft for users and machines. AD has a domain controller, also known as Active Directory Domain Service (AD DS), which stores the user's and the system's information, their access credentials, and their identity. The following diagram illustrates a simple flow of the necessary authentication process:

AD authentication flow
As shown in the preceding diagram, the user login is managed by AD or any resource on the domain networks. Users first send the request to the domain controller with their credentials and communicate with the Active Directory Authentication Library (ADAL). The ADAL verifies the user credentials and sends back an access token with a continuous session for the requested service.
[ 231 ]

Security Considerations

Chapter 8

LDAP is the standard protocol that handles the tree-like hierarchical structure of information stored in directories. Active Directory Lightweight Directory Services (AD LDS) provides an LDAP interface to the directory of users and systems. For file encryption and network traffic encryption, Active Directory Certificate Services (AD CS) provides the key infrastructure functionality. Active Directory Federation Service (ADFS) provides access mechanisms for external resources such as web app logins for a large number of users.

Amazon Web Services (AWS) Directory Service
AWS Directory Service helps to connect AWS resources in your account with an existing on-premises user management tool such as AD. It helps to set up a new user management directory in the AWS cloud. AWS Directory Service facilitates a secure connection to the onpremises directory. After establishing the connection, all users can access cloud resources and on-premises applications with their already existing credentials.
AWS AD Connector is another service that helps you to connect the existing Microsoft AD to the AWS cloud. You don't need any specific directory synchronization tool. After setting up an AD connection, users can utilize their existing credentials to log on to AWS applications. Admin users can manage AWS resources, using AWS IAM.
AD Connector helps to enable MFA by integrating with your existing MFA infrastructure, such as YubiKey, Gemalto token, RSA token, and so on. For a smaller user base (fewer than 5,000 users), AWS provides Simple AD, which is a managed directory powered by Samba 4 Active Directory Compatible Server. Simple AD has common features such as user accounts management, user group management, SSO based on Kerberos, and user group policies.
In this section, you have learned a high-level overview of AD and managed AD services provided by Microsoft and Amazon. The other directory services provided by major technology companies include Google Cloud Identity, Okta, Centrify, Ping Identity, and Oracle Identity Cloud Service (IDCS).

Security Assertion Markup Language (SAML)
Earlier in this section, under FIM and SSO, you learned about IdPs and SPs (short for service providers). To access a service, the user gets validated from the IdP, which in-turn has a trusted relationship with the SP. SAML is one of the mechanisms to establish a trusted relationship between an IdP and an SP. SAML uses extensible markup language (XML) to standardize communication between an IdP and an SP. SAML enables SSO, so users can use a single credential to access multiple applications.

[ 232 ]

Security Considerations

Chapter 8

A SAML assertion is an XML document that the IdP sends to the SP with user authorization. The following diagram illustrates the flow of the SAML assertion:

User authentication using SAML
As mentioned in the preceding diagram, the following steps are taken to implement user authentication using SAML:
1. A user sends a request to access the service--for example, the Salesforce CRM application-- as a service provider.
2. The service provider (CRM application) sends a SAML request with the user information to the SAML IdP.
3. The SAML IdP pops up the SSO login page, where users enter authentication information.
4. The user access credential goes to the identity store for validation. In this case, user identify store is an AD.
5. The user identity store sends user validation status to the SAML IdP, with whom the identity store has a trusted relationship.
6. The SAML IdP sends a SAML assertion to the service provider (a CRM application) with information pertaining to user verification.
7. After receiving the SAML response, the service provider allows application access to the user.
[ 233 ]

Security Considerations

Chapter 8

Sometimes, service providers can act as an identity provider as well. SAML is very popular for establishing a relation between any identity store and service provider. All modern identity store applications are SAML 2.0-compatible, which allows them to communicate with each other seamlessly. SAML allows user identity to be federated and enables SSO for enterprise users.
However, for large user bases such as social media and e-commerce websites, OAuth (short for Open Authorization) and OpenID are more suitable. Let's learn more about OAuth and OpenID Connect.

OAuth and OpenID Connect (OIDC)
OAuth is an open standard authorization protocol that provides secure access to an application. OAuth provides secure access delegation. OAuth doesn't share password data but uses the authorization token to establish the identity between service providers and consumers. Users of an application provide access to their information without giving login credentials. While OAuth is mainly for authorization, many organizations have started adding their own mechanisms for authentication. OpenID Connect defines the authentication standard on top of OAuth authorization.
Large technology companies such as Amazon, Facebook, Google, and Twitter allow the user to share information in their account with third-party applications. For example, you can log in to a new photo app using your Facebook login and authorize the new app to access only your Facebook photo information. The following diagram illustrates an OAuth access delegation flow:

User access delegation with OAuth 2.0
[ 234 ]

Security Considerations

Chapter 8

As shown in the preceding diagram, the authentication flow follows these steps:
1. You want a photo app to get your profile photo from Facebook. 2. The photo app requests authorization to access Facebook profile photos. 3. The authorization server (which is your Facebook account in this case) creates
and displays a consent screen to you. 4. You provide your consent to the request for the photo app to access only your
Facebook profile photos. 5. After getting your approval, the authorization Facebook server sends an
authorization code back to the requesting photo app. 6. The photo app then requests an access token from the authorization server
(Facebook account) using the authorization code. 7. The authorization server identifies the photo app and checks the validity of the
authentication code. 8. If the access token is validated, the server issues an access token to the photo app. 9. The photo app can now access resources such as Facebook profile photos using
the access token.
OAuth 2.0, which is faster than OAuth 1.0 and more comfortable to implement, is now most commonly used. JSON Web Token (JWT) is a simple and accessible token format that can be used with OAuth and is popular with OpenID. JWT tokens have a JSON structure that has information about expiration time, issuer, subject, and so on. It is more robust than Simple Web Token (SWT) and simpler than SAML 2.0.
In this section, you learned about the most common user management tools and services. However, there are various other protocols and services available for user authentication and authorization. Implementation of the protocols mentioned previously can be complicated, and there is a large amount of packaged software available that makes the job easier.
Amazon Cognito is a user access management service provided by AWS that includes standard-based authorization such as SAML 2.0, OpenID Connect, and OAuth 2.0, along with an enterprise user directory that provides the ability to connect with AD. Okta and Ping Identity provide enterprise user management and the ability to communicate with various service provider tools in one place.

[ 235 ]

Security Considerations

Chapter 8

Once your application is exposed to the internet, there are always various kinds of attacks bound to happen. Let's learn about some most common attacks, and how to set up the first layer of defense for web-layer protection.

Handling web security
As user demand is changing to require 24/7 availability of services, businesses are evolving to go into online mode and adopting web application models. Web applications also help a company to gain a global customer base. Businesses such as online banking and ecommerce websites are always available, and they deal with customers' sensitive data such as payment information and payer identity.
Now, web applications are central to any business, and these applications are exposed to the world. Web applications can have vulnerabilities, which makes them exposed to cyberattacks and data breaches. Let's explore some common web vulnerabilities and how to mitigate them.
Web app security vulnerabilities
A web application is prone to security breaches as hackers orchestrate cyber-attacks from different locations and by various methods. A web application is more vulnerable to theft than a physical store location. Just as you lock and protect your physical shop, in the same way, your web app needs to protect itself from unwanted activity. Let's explore some standard methods of attack that can cause security vulnerabilities in your web application.
Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks
A DoS attack attempts to make your website unreachable to your users. To achieve a successful DoS attack, the attacker uses a variety of technologies that consume network and system resources, thus interrupting access for legitimate users. The attacker uses multiple hosts to orchestrate the attack against a single target.

[ 236 ]

Security Considerations

Chapter 8

A DDoS attack is a type of DoS attack where multiple compromised systems (typically infected with Trojans) are used to target a single system. Victims of a DDoS attack find that all their systems are maliciously used and controlled by the hacker in the distributed attack. As illustrated in the following diagram, a DDoS attack happens when multiple systems exhaust the bandwidth of resources of a targeted system:

DDoS attack
The general concept of a DDoS attack is to leverage additional hosts to amplify the requests made to the target, rendering them overprovisioned and unavailable. A DDoS attack is often the result of multiple compromised systems, whereby a botnet puts a flood of traffic in the targeted system.
The most common DDoS attack happens at the application layer, using either a DNS flood or a Secure Sockets Layer (SSL) negotiation attack. In DNS floods, attackers exhaust the resources of a DNS server with too many requests. During SSL negotiations, attackers send a large amount of unintelligible data for computationally expensive SSL decryption. The attacker can perform other SSL-based attacks to the server fleet and overburden it with unnecessary task processing.
At the infrastructure layer, a typical DDoS attack happens in the form of the following:
User Datagram Protocol (UDP) reflection: With UDP reflection, attackers spoof the target server's IP address and make a request that returns amplified significant responses from a hacked reflector server. SYN floods: With SYN floods, attackers exhaust the target server's Transmission Control Protocol (TCP) service by creating and abandoning high numbers of connections, blocking legitimate users from accessing the server.
[ 237 ]

Security Considerations

Chapter 8

Often, attackers try to get sensitive customer data, and for that purpose, they use a different kind of attack called SQL injection (SQLi) attacks. Let's learn more about them.

SQLi attacks
As the name suggests, in an SQLi attack, attackers inject malicious Structure Query Language (SQL) to get control of a SQL database and fetch sensitive user data. The attacker uses SQLi to gain access to unauthorized information, take control of an application, add new users, and so on.
Take an example of a loan-processing web application. You have loanId as a field that customers can use to get all information related to their loan finance. The typical query will look like this: SELECT * FROM loans WHERE loanId = 117. If proper care is not taken, attackers can execute a query such as SELECT * FROM loans WHERE loanId = 117 or `1=1' and get access to the entire customer database, as this query will always return the true result.
The other common method to hack user data through script injection is cross-site scripting (XSS) where a hacker impersonate himself as legitimate user. Let's explore more about it.

XSS attacks
You must have encountered phishing emails that have links impersonating a website known to you. Clicking on these links may lead to compromised data through XSS. With XSS, the attacker attaches their code to a legitimate website and executes it when the victim loads the web page. The malicious code can be inserted in several ways, such as in a URL string or by putting a small JavaScript code on the web page.
In an XSS attack, the attacker adds a small code snippet at the end of the URL or client-side code. When you load the web page, this client-side JavaScript code gets executed and steals your browser cookies. These cookies often contain sensitive information, such as the access token and authentication to your banking or e-commerce websites. Using these stolen cookies, the hacker can get into your bank account and take your hard-earned money.

Cross-Site Request Forgery (CSRF) attacks
A CSRF attack takes advantage of user identity by creating confusion. It typically tricks the user with a transaction activity in which the state gets changed--for example, changing the password of a shopping website or requesting a money transfer to your bank.

[ 238 ]

Security Considerations

Chapter 8

It is slightly different than an XSS attack as, with CSRF, the attacker tries to forge the request rather than insert a code script. For example, the attacker can forge a request to transfer a certain amount of money from the user's bank and send that link in an email to the user. As soon as users click on that link, the bank gets a request and transfers the money to the attacker's account. CSRF has minimal impact on the individual user account, but it can be very harmful if attackers are able to get into the admin account.

Buffer overflow and memory corruption attacks
A software program writes data in temporary memory area for fast processing, which is called a buffer. With a buffer overflow attack, an attacker can overwrite a portion of memory connected with the buffer. An attacker can deliberately cause a buffer overflow and access connected memory, where an application executable may be stored. The attacker can replace the executable with the actual program and take control of the entire system. Buffer overflow attacks can cause memory corruption with unintentional memory modification, which the hacker can use to inject code.
Looking at the overall application, there are more security threats that exist at the infrastructure layer, network layer, and data layer. Let's explore some standard methods to mitigate and prevent security risks at the web layer.

Web security mitigation
Security needs to be applied to every layer, and special attention is required for the web layer due to its exposure to the world. For web protection, important steps include keeping up with the latest security patches, following the best software development practices, and making sure proper authentication and authorization are carried out. There are several methods to protect and secure web applications; let's explore the most common methods.
Web Application Firewall (WAF)
WAFs are necessary firewalls that apply specific rules to HTTP and HTTPS traffic (that is, port 80 and 443). WAFs are software firewalls that inspect your web traffic and verify that it conforms to the norms of expected behavior. WAFs provide an additional layer of protection from web attacks.

[ 239 ]

Security Considerations

Chapter 8

WAF rate limiting is the ability to look at the amount or type of requests sent to your service and define a threshold that caps how many requests are allowed per user, session, or IP address. Whitelists and blacklists allow you to allow or block users explicitly. AWS WAF helps you to secure your web layer by creating and applying rules to filter web traffic. These rules are based on conditions that include HTTP headers, user geolocation, malicious IP addresses, or custom Uniform Resource Identifiers (URIs), and so on. AWS WAF rules block common web exploits such as XSS and SQLi.
AWS WAF provides a centralized mechanism in the form of rules that can be deployed across multiple websites. This means that you can create a single set of rules for an environment that has various websites and web applications running. You can reuse rules across applications instead of recreating them.
Overall, WAF is a tool that applies a set of rules to HTTP traffic. It helps to filter web requests based on data such as IP addresses, HTTP headers, HTTP body, or URI strings. It can be useful for mitigating DDoS attacks by offloading illegitimate traffic. Let's learn more about DDoS mitigation.

DDoS mitigation
Resilient architecture can help to prevent or mitigate DDoS attacks. A fundamental principle in keeping your infrastructure secure is reducing the potential number of targets that an attacker can hit. In short, if an instance doesn't need to be public, then don't make it public. An application-layer attack can spike monitoring metrics such as network utilization for your content distribution network (CDN), load balancer, and server metrics due to HTTP flood. You can apply various strategies to minimize the attack surface area:
Wherever possible, try to reduce the number of necessary internet entry points. For example, open incoming internet access to your load balancer, not web servers. Hide any required internet entry points from untrusted end users so that they cannot access them. Identify and remove any non-critical internet entry points--for example, expose file-share storage for vendors to upload data with limited access, rather than exposing it to worldwide internet traffic. Isolate the access point and apply specific restrictions policy for end user traffic compared to application management traffic. Create a decoupled internet entry point to minimize the attack surface.

[ 240 ]

Security Considerations

Chapter 8

Your primary goal is to mitigate DDoS attacks at the Edge location of the CDN. It's more challenging and costly to handle DDoS attacks if they get through to your application servers. The following diagram illustrates a DDoS mitigation example for an AWS cloud workload:

DDoS WAF sandwich mitigation strategy
The preceding diagram illustrates a WAF sandwich architecture, where the WAF appliance is staged between a load balancer to handle a DDoS attack. Frequent DDoS attacks come from attacking strategies such as SYN floods and UDP reflection, which Amazon CloudFront prevents by only accepting well-formed connections before the attacking strategy can reach your application servers. CDNs such as Amazon CloudFront help to tackle DDoS attacks by isolating them at a geographically isolated location and preventing the traffic from affecting other locations. Network firewall security helps you to control incoming and outgoing traffic at an individual server level.
As mentioned in the previous section, WAFs are used to protect web applications against exploit attacks such as XSS and SQLi attacks. In addition to this, WAFs also help to detect and prevent DDoS attacks at the web application layer.
To handle a DDoS attack, you can apply either horizontal or vertical scaling. You can take advantage of scaling in the following way:
1. First, select the right server size and configuration for your web application. 2. Second, apply a load balancer to distribute traffic among the fleet of servers and
add autoscaling to add/remove servers as required. 3. Finally, use the CDN and DNS server, as they are built to handle traffic at scale.
[ 241 ]

Security Considerations

Chapter 8

Scaling for DDoS attacks is an excellent example of why it's essential to set reasonable maximum counts for your servers. A DDoS attack could scale your servers out to a count that would be extremely costly, while still potentially not being able to avoid becoming unavailable. Having reasonable maximum limits for expectations of regular traffic spikes would prevent a DDoS attack costing your company too much money.
In this section, you learned about various security risks and vulnerabilities at the web layer and some standard methods to protect them. As security needs to be applied to every layer, let's explore more about the protection of the infrastructure layer.

Securing an application and its infrastructure
Security isn't just about getting through the outer boundary of your infrastructure. It's also about ensuring that your environments and their components are secured from each other. You should apply security at each layer of the application, such as the web, application, and data layer. You should add security controls to all of the system's resources such as load balancers, network topology, database, and all servers.
For example, in a server instance, you can set up a firewall that allows you to determine which ports on your instances can send and receive traffic. You can use this to reduce the probability that a security threat on one instance will spread to every other instance in your environment. Similar precautions should be taken with other services. Specific ways to implement this best practice are discussed throughout this section.
Application and operating system hardening
It is not possible to entirely eliminate vulnerabilities in your application, but you can limit system attacks by hardening your application's operating system, filesystem, and directory. Once attackers can get into your application, they can get root access and orchestrate an attack on the entire infrastructure. It is essential to limit attacks to the application level by restricting the directory by hardening permission. At the process level, restrict memory and CPU utilization to prevent a DOS attack.
Set the right permission at the file, folder, and file partition levels, which is the only requirement for the application to execute. Avoid giving root privilege to the application or their user. You should create a separate user and directory, with only required access for each application. Don't use common access for all applications.

[ 242 ]

Security Considerations

Chapter 8

Automate application restart by using tools and avoid a manual approach, whereby users need to log in to the server to start. You can use process control tools such as DAEMON Tools and Supervisord to automate an application restart. For a Linux operating system, a utility such as systemd or System V init scripts help to start/stop the application.

Software vulnerabilities and secure code
It is always recommended to apply the latest security patch to your operating system provided by your operating system vendor. This helps to fill any security holes in the system and protect your system from vulnerabilities where attackers are able to steal your security certificate or run arbitrary code. Make sure to integrate secure coding best practice to your software development process, as recommended by the Open Web Application Security Project (OWASP: https:// o wasp.org/www-project-t op-ten/).
Keeping your system up to date with the latest security patch is very important. It is better to automate the process of the most recent patch installation as soon as it becomes available. However, sometimes, running a security patch may break your working software, so it's better to set up a Continuous Integration and Continuous Deployment (CI/CD) pipeline with automated test and deployment. You will learn more about the CI/CD process in Chapter 12, DevOps and Solution Architecture Framework.
AWS cloud provides a system manager tool that allows you to apply security patches and monitoring of your server fleet in the cloud. You can use a tool such as auto-updates or unattended-upgrades to automate security patch installation.

Network, firewall, and trusted boundary
When it comes to protecting your infrastructure, securing the network comes into consideration first. The physical security of your IT infrastructure in the data center is to be taken care of by providers. In the case of cloud-like AWS providers, they take the utmost care of the physical security of your infrastructure. Let's talk about ensuring network security, which is your responsibility as an application owner.
To understand it better, let's take an example from a public cloud provider such as AWS and apply the same example to your on-premises or private cloud network infrastructure as well. As illustrated in the following diagram, you should apply security at every layer and define trusted boundaries around each layer, with minimal access:

[ 243 ]

Security Considerations

Chapter 8

Network configuration for infrastructure security
In the preceding diagram, the load balancer is in a public subnet, which can accept internet traffic and distribute it to the application server fleet. WAF filter traffic is based on set rules and protects your application from various attacks, as you learned in the previous section. The application server fleet and database servers are in a private subnet, which means direct internet access is not reachable to expose them to the public internet. Let's dive deep into the preceding architecture diagram and walk through each layer, as follows:
Amazon Virtual Private Cloud (VPC) provides you with logical network isolation of your infrastructure. Amazon VPC is your network environment in the cloud. It's where you will launch many of your resources. It's designed to provide greater control over the isolation of your environments and their resources from each other. You can have multiple VPCs in each account or region.
[ 244 ]

Security Considerations

Chapter 8

When you create a VPC, you specify its set of IP addresses with Classless InterDomain Routing (CIDR) notation. CIDR notation is a simplified way of showing a specific range of IP addresses. For example, 10.0.0.0/16 covers all IPs from 10.0.0.0 to 10.0.255.255, providing 65,535 IP addresses to use.
Subnets are segments or partitions of a network divided by the CIDR range. They create trusted boundaries between private and public resources. Rather than defining your subnets based on the application or functional tier (web/app/data), you should organize your subnets based on internet accessibility. A subnet allows you to define clear, subnet-level isolation between public and private resources.
In this environment, all of your resources that require direct access to the internet (public-facing load balancers, Network Address Translation (NAT) instances, bastion hosts, and so on) would go into the public subnet, while all other instances (such as database and application resources) would go into your private subnet. Use subnets to create layers of separation between tiers of resources, such as putting your application instances and your data resources into separate private subnets.
The majority of resources on AWS can be hosted in private subnets, using public subnets for controlled access to and from the internet as necessary. Because of this, you should plan your subnets so that your private subnets have substantially more IPs available compared to your public subnets.
While subnets can provide a fundamental element of segregation between resources using network Access Control List (ACL) rules, security groups can give an even more fine-grained level of traffic control between your resources, without the risk of overcomplicating your infrastructure and wasting or running out of IPs.
A routing table contains a set of rules, called routes. Routes determine which application servers are to receive network traffic. For better security, use the custom route table for each subnet.
Security groups are the virtual firewalls that control inbound and outbound traffic for one or more instances from the CIDR block range, or another security group, as designated resources. As per the principle of least privilege, deny all incoming traffic by default and create rules that can filter traffic based on TCP, UDP, and Internet Control Message Protocol (ICMP) protocols.
A Network Access Control List (NACL) is an optional virtual firewall that controls inbound and outbound traffic at the subnet level. An NACL is a stateless firewall that is compared to the security group, which is stateful. This means that if your incoming request is allowed, then the outbound request does not have to be inspected or tracked. While stateless, you have to define both inbound and outbound traffic rules explicitly.

[ 245 ]

Security Considerations

Chapter 8

Internet traffic routed through an internet gateway (IGW) to make a subnet public. By default, internet accessibility is denied for internet traffic in your environment. An IGW needs to be attached to your VPC, and the subnet's route table should define the rules to the IGW.
A private subnet blocks all incoming and outgoing internet traffic, but servers may need outgoing internet traffic for software and security patch installation. A NAT gateway enables instances in a private subnet to initiate outbound traffic to the internet and protects resources from incoming internet traffic.
A bastion host acts like a jump server, which allows access to other resources in the private subnet. A bastion host needs to be hardened with tighter security so that only appropriate people can access it. To log in to the server, always use public-key cryptography for authentication rather than a regular user ID and password method.
Many organizations typically collect, store, monitor, and analyze network flow logs for various purposes, including troubleshooting connectivity and security issues and testing network access rules. You need to monitor traffic flow to your system VPC, which includes recording incoming and outgoing traffic information from your network. VPC Flow Logs enables you to capture that information, along with accepted and rejected traffic information for the designated resource to understand traffic patterns better.
Flow Logs can also be used as a security tool for monitoring traffic that is reaching your instance. You can create alarms to notify if certain types of traffic are detected. You can also create metrics to help you to identify trends and patterns. You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in the VPC or subnet is monitored.
As you can see, there are multiple layers for security available at the network layer that can help to protect your infrastructure. Keeping resources in their isolated subnet helps to reduce the blast radius. If an attacker can penetrate one component, you should be able to restrict them to limited resources. You can use an Intrusion Detection System (IDS) and an Intrusion Prevention System (IPS) in front of your infrastructure to detect and prevent any malicious traffic. Let's learn more about them.

IDS/IPS
An IDS detects any cyber-attack happening through network traffic by recognizing an attack pattern. An IPS goes a step further and helps to stop malicious traffic proactively. You need to determine the applicability of the IDS/IPS system as per your application's requirements. An IDS can be host-based or network-based.

[ 246 ]

Security Considerations

Chapter 8

Host-based IDS
In an IDS, a host- or agent-based IDS is running on each host of your environment. It can review the activity within that host to determine if an attack has occurred and has been successful. It can do this by inspecting logs, monitoring the filesystem, monitoring network connections to the host, and so on. The software or agent then communicates with a central/command application about the health or security of the host it is monitoring.
Pros for host-based solutions include that they can deeply inspect the activity inside each host. They can horizontally scale as far as required (each host gets its own agent), and do not need to impact the performance of running applications. The cons include the additional configuration management overheads that can be introduced if managing agents on many servers, which are burdensome for an organization.
As each agent is operating in isolation, widespread/coordinated attacks can be harder to detect. To handle coordinated attacks, the system should respond immediately across all hosts, which requires the host-based solution to play well with the other components, such as the operating system and the application interface, deployed on the host.

Network-based IDS
A network-based IDS inserts an appliance into the network, through which all traffic is routed and inspected for attacks. The pros include a simple/single component that needs to be deployed and managed away from the application hosts. Also, it is hardened or monitored in a way that might be burdensome across all hosts. An individual/shared view of security exists in a single place so that the big picture can be inspected for anomalies/attacks.
However, a network-based IDS includes the performance hit of adding a network hop to applications. The need to decrypt/re-encrypt traffic to inspect it is both a massive performance hit and a security risk that makes the network appliance an attractive target. Any traffic that IDS unable to decrypt cannot inspect/detect anything.
An IDS is a detection and monitoring tool and does not act on its own. An IPS detects, accepts, and denies traffic based on set rules. IDS/IPS solutions help to prevent DDoS attacks due to their anomaly-detection capabilities that make them able to recognize when valid protocols are used as an attack vehicle. An IDS and an IPS read network packets and compare contents to a database of known threats. Continuous auditing and scanning are required for your infrastructure to proactively secure it from any attack, so let's learn more about this.

[ 247 ]

Security Considerations

Chapter 8

In this section, you learned all about securing your infrastructure from various types of attacks. The goal of these attacks is to get hold of your data. You should secure your data in such a way that an attacker is not able to acquire sensitive information even after getting hold of the data. Let's learn about data protection using security at the data layer, encryption, and backup.

Data security
In today's digital world, every system revolves around data. Sometimes, this data may contain sensitive information such as customer health records, payment information, and government identity. Securing customer data to prevent any unauthorized access is most important. There are many industries that place stress on data protection and security.
Before architecting any solution, you should define basic security practices as per the application objective, such as complying with regulatory requirements. There are several different approaches used when addressing data protection. The following section describes how to use these approaches.
Data classification
One of the best practices is to classify your data, which provides a way to categorize and handle organizational data based on levels of sensitivity. According to data sensitivity, you can plan data protection, data encryption, and data access requirements.
By managing data classification as per your system's workload requirements, you can create the data controls and level of access needed for the data. For example, content such as a user rating and review is often public, and it's fine to provide public access, but user credit card information is highly sensitive data that needs to be encrypted and put under very restricted access.
At a high level, you can classify data into the following categories:
Restricted data: This contains information that could harm the customer directly if it got compromised. Mishandling of restricted data can damage a company's reputation and impact a business adversely. Restricted data may include customer Personally Identifiable Information (PII) data such as social security numbers, passport details, credit card numbers, and payment information. Private data: Data can be categorized as confidential if it contains customersensitive information that an attacker can use to plan to obtain their restricted data. Confidential data may include customer email IDs, phone numbers, full names, and addresses.
[ 248 ]

Security Considerations

Chapter 8

Public data: This is available and accessible to everyone, and requires minimal protection--for example, customer ratings and reviews, customer location, and customer username if the user made it public.
You can have a more granular category depending on the type of industry and the nature of the user data. Data classification needs to balance between data usability versus data access. Putting different levels of access, as mentioned previously, helps to restrict only the necessary data and make sure sensitive data is not exposed. Always avoid giving direct human access to data and add some tools that can generate a read-only report for users to consume in a restrictive manner.

Data encryption
Data encryption is a method to protect your data whereby you convert your data from plaintext to encoded ciphertext format using the encryption key. To read these ciphertexts, they first need to be decrypted using the encryption key, and only authorized users will have access to those decryption keys. Commonly used key-based encryption falls into one of two categories of cryptography:
Symmetric-key encryption: With symmetric encryption algorithms, the same key is used to encrypt and decrypt the data. Each data packet is self-encrypted with a secret key. Data is encrypted while saving and decrypted during retrieval. Earlier, symmetric encryption used to be applied as per the Data Encryption Standard (DES), which used a 56-bit key. Now, the Advanced Encryption Standard (AES) is heavily used for symmetric encryption, which is more reliable as it uses a 128-bit, 192-bit, or 256-bit key.
Asymmetric-key encryption: With the help of asymmetric algorithms, two different keys can be used, one to encrypt and one to decrypt. In most cases, the encryption key is a public key and the decryption key is a private key. Asymmetric key encryption is also known as public-key encryption. Both public and private keys are unidentical, but they are paired together. The private key is only available to one user, while the public key can be distributed across multiple resources. Only the user who has a private key can decrypt the data. Rivest�Shamir�Adleman (RSA) is one of the first and most popular public keyencryption algorithms used to secure data transmissions over the network.
If you are encrypting your data with an AES 256-bit security key, it's become almost impossible to break the encryption. The only way to decrypt is by getting hands-on encryption, which means you need to secure your code and keep it in a safe place. Let's learn about some essential management methods to safeguard your encryption key.

[ 249 ]

Security Considerations

Chapter 8

Encryption key management
Key management involves controlling and maintaining your encryption key. You need to make sure that only authorized users can create and access the encryption key. Any encryption key management system handles storage, rotation, and destruction of the key in addition to access management and key generation. Key management differs depending on whether you are using a symmetric or asymmetric algorithm. The following methods are popular for key management.

Envelope encryption
Envelope encryption is a technique to secure your data encryption key. Data encryption keys are symmetric keys to increase the performance of data encryption. Symmetric encryption keys work with an encryption algorithm such as AES and produce ciphertext that you can store safely, as it is not readable by a human. However, you need to save the symmetric encryption data key along with data to use it for data decryption, as needed. Now, you need to further protect the data key in isolation, which is where envelope encryption helps you to protect it. Let's understand it in more detail with the help of the following diagram:

Envelope encryption
[ 250 ]

Security Considerations

Chapter 8

The preceding diagram illustrates the following flow to explain envelope encryption:
1. The symmetric key is generated from software or hardware. 2. The generated symmetric data key is used to encrypt plaintext data. 3. The key encrypts data using an algorithm such as AES and generates encrypted
ciphertext data. 4. The encrypted data is stored in targeted storage. 5. As the data key needs to be stored with ciphered data, the data key needs to be
encrypted further. The user gets the customer master key stored in the key management systems to encrypt the data key. 6. The data key is encrypted using the master key. Your master key is the key encryption key as it encrypts the data encryption key. Only the master key can encrypt multiple data keys, and it is securely stored in the key management systems, with restricted access. 7. The master key encrypts data key, and encrypted data key store along with ciphered data in storage, where master key securely stores in key management system with restricted access.
If a user wants to decrypt data, then they first need a master key that has, in turn, an encrypted data encryption key. This master key can be stored in a separate access system such as a hardware security module (HSM) or software-based key management service provided by cloud providers such as AWS. Let's look into this in more detail.

AWS Key Management Service (KMS)
AWS KMS uses envelope encryption whereby a unique data key encrypts customer data, and KMS master keys encrypt data keys. You can bring your key material to AWS KMS and manage user access, key distribution, and rotation from a centralized place. You can also disable unused keys, and a low number of keys helps to improve the performance of the application and encourage better key management.
AWS KMS is designed to limit access and protect master keys. KMS helps you to implement key security best practices by never storing plaintext master keys on disk or in memory. KMS also gracefully rotates the master key to secure it further.
As AWS KMS is a multitenancy key management module, a customer wants to have a dedicated key management module due to compliance. Also, the customer may have an old HSM, and they want to follow the same model. The HSM is single-tenant hardware in AWS and is called AWS CloudHSM. You can choose your own HSM vendor as well. Let's explore HSM in more depth.

[ 251 ]

Security Considerations

Chapter 8

Hardware security module (HSM)
An HSM is a device that is designed to secure encryption keys and associated cryptographic operations. An HSM is designed with physical mechanisms to protect the keys, which include tamper detection and response. In case of any key tampering, the HSM destroys the keys and prevents any security compromise.
An HSM includes logical protections to limit access controls. Logical separation helps the HSM appliance administrator to manage the device securely. Access restriction applies rules for users who can connect it to the network and provision the IP address. You can create a separate role for everyone, including security officers, appliance admin, and users.
As the loss of a key can make your data useless, you need to make sure of high availability for your HSM by maintaining at least two HSMs in different geographic locations. You can use other HSM solutions, such as SafeNet or Voltage. To protect your key, choose a managed HSM provided by cloud services such as AWS CloudHSM or CipherCloud.

Data encryption at rest and in transit
Data at rest means it is stored somewhere such as a storage area network (SAN) or network-attached storage (NAS) drive, or in cloud storage. All sensitive data needs to be protected by applying symmetric or asymmetric encryption, explained in the previous section, with proper key management.
Data in transit means data in motion and transferred over the network. You may encrypt data at rest from source and destination, but your data transfer pipeline needs to be secure when transferring data. When transferring data over an unencrypted protocol such as HTTP, it can get leaked by an attack such as an eavesdropping or man-in-the-middle (MITM) attack.
In an eavesdropping attack, the attacker captures a small packet from a network and uses it to search for any other type of information. A MITM attack is a tampering-based attack, where the attacker secretly alters the communication to start communication on behalf of the receiver. These kinds of attacks can be prevented by transferring data over SSL, using a strong protocol such as Transport Security Layer (TSL).
You will observe that most websites now use HTTPS protocol for communication, which encrypts data using SSL. By default, HTTP traffic is unprotected. SSL/TLS protection for HTTP traffic (HTTPS) is supported by all web servers and browsers. HTTP traffic is also applicable to service-oriented architectures such as Representational State Transfer (REST)- and Simple Object Access Protocol (SOAP)-based architectures.

[ 252 ]

Security Considerations

Chapter 8

SSL/TSL handshakes use certificates to exchange a public key using asymmetric encryption, and then use the public key to exchange a private key using symmetric encryption. A security certificate is issued by an acceptable Certification Authority (CA) such as Verisign. Procured security certificates need to be secured using a Public Key Infrastructure (PKI). The public cloud, such as AWS, provides an AWS Certificate Manager (ACM) managed
Non-web transmission of data over the network should also be encrypted, and this includes Secure Shell (SSH) and Internet Protocol Security (IPsec) encryption. SSH is most prevalent while connecting to servers, and IPsec is applicable to securing corporate traffic transferred over a virtual private network (VPN). File transfer should be secured using SSH File Transfer Protocol (SFTPS) or FTP Secure (FTPS), and email server communication needs to be secured by Simple Mail Transfer Protocol Secure (SMTPS) or Internet Message Access Protocol (IAMPS).
In this section, you learned about various methods to secure data at rest and in motion with different cryptographic techniques. Data backup and recovery is an important aspect of protecting your data in the case of any unforeseen incidents. You will learn more about data backup in Chapter 9, Architectural Reliability Considerations, in the Disaster recovery planning section.
There are many governing bodies available that publish compliance, which is a set of checklists to ensure customers' data security. Compliance also makes sure that organizations comply with industry and local government rules. Let's learn more about various compliance measures in the next section.

Security and compliance certifications
There are many compliance certifications depending on your industry and geographical location to protect customer privacy and secure data. For any solution design, compliance requirements are among the critical criteria that need to be evaluated. The following are some of the most popular industry-standard compliances:
Global compliance includes certifications that all organizations need to adhere to, regardless of their region. These include ISO 9001, ISO 27001, ISO 27017, ISO 27018, SOC 1, SOC 2, SOC 3, and CSA STAR for cloud security. The US government requires various kinds of compliance to handle public sector workload. These include FedRAMP, DoD SRG Level-2, 4, and 5, FIPS 140, NIST SP 800, IRS 1075, ITAR, VPAT, and CJIS.

[ 253 ]

Security Considerations

Chapter 8

Industry-level compliance of application apply to a particular industry. These include PCI DSS, CDSA, MPAA, FERPA, CMS MARS-E, NHS IG Toolkit (in the UK), HIPAA, FDA, FISC (in Japan), FACT (in the UK), Shared Assessment, and GLBA. Regional compliance certification applies to a particular country or region. These include EU GDPR, EU Model Clauses, UK G-Cloud, China DJCP, Singapore MTCS, Argentina PDPA, Australia IRAP, India MeitY, New Zealand GCIO, Japan CS Mark Gold, Spain ENS and DPA, Canada Privacy Law, and US Privacy Shield.
As you can see, there are many compliance certifications available from different regulatory bodies as per industry, region, and government policy. We are not going into details of compliance, but you need to evaluate your application with compliance requirements before starting your solution design. Compliance requirements influence the overall solution design heavily. You need to decide what kind of encryption is required, as well as logging, auditing, and location of your workload based on your compliance needs.
Logging and monitoring help to ensure robust security and compliance. Logging and monitoring are essential. If an incident occurs, your team should be notified immediately and be ready to respond to incidents. You are going to learn more about monitoring and alert methods in Chapter 10, Operational Excellence Considerations.
There are several compliance industries depending on your application geolocation, industry, and government rules. You learned about the various categories of compliance and some common compliance standards appropriate for each group. Many organizations are moving to the cloud, so it's vital to understand security in the cloud.

The cloud's shared security responsibility
model
As the cloud is becoming regularly used and many organizations are moving their workload to a public cloud such as AWS, Google Cloud Platform (GCP), and Azure, the customer needs to understand the cloud security model. Security in the cloud is a joint effort between the customer and the cloud provider. Customers are responsible for what they implement using cloud services and for the applications connected to the cloud. In the cloud, customer responsibility for application security needs depends upon the cloud offerings they are using and the complexity of their system.

[ 254 ]

Security Considerations

Chapter 8

The following diagram illustrates a cloud security model from one of the largest public cloud providers (AWS), and it's pretty much applicable to any public cloud provider:

AWS cloud shared security responsibility model
As shown in the preceding diagram, AWS handles the security of the cloud, specifically the physical infrastructures that host your resources. This includes the following:
Data centers: Non-descript facilities, 24/7 security guards, two-factor authentication, access logging and review, video surveillance, and disk degaussing and destruction. Hardware infrastructure: Servers, storage devices, and other appliances that rely on AWS services. Software infrastructure: Host operating systems, service applications, and virtualization software. Network infrastructure: Routers, switches, load balancers, firewalls, cabling, and so on. Also includes continuous network monitoring at external boundaries, secure access points, and redundant infrastructure.
The customer handles the security in the cloud, which includes the following:
Server's operating system: The operating system installed on the server could be vulnerable to attacks. Patching and maintenance of the operating system is the customer's responsibility, as software applications depend heavily upon it.
[ 255 ]

Security Considerations

Chapter 8

Application: Every application and its environments, such as dev, test, and prod, are maintained by the customer. So, handling password policies and access management is the customer's responsibility. Operating system-/host-based firewalls: Customers need to protect their entire system from external attacks. However, the cloud provides security in that area, but customers should consider an IDS or an IPS to add an extra layer of security. Network configuration and security group: The cloud provides tools to create a network firewall, but it's up to application requirements as to which traffic needs to be stopped or allowed to go through. Customers are responsible for setting up firewall rules to secure their systems from external and internal network traffic. Customer data and encryption: Data handling is the customer's responsibility, as they are more aware of the data protection that's needed. The cloud provides tools to apply for data protection by using various encryption mechanisms, but it's the customer's responsibility to apply those tools and secure their data.
The public cloud also provides various compliance certifications that apply to the hardware portions managed by them. To make your application compliant, you need to handle and complete audits for application-level complaints. As a customer, you get an additional advantage by inheriting security and compliance provided by the cloud provider.
Try to automate security best practices wherever possible. Software-based security mechanisms improve your ability to scale more rapidly, cost-effectively, and securely. Create and save a custom baseline image of a virtual server, and then use that image automatically on each new server you launch. Create an entire infrastructure that is defined and managed in a template to replicate best practices for the new environment.
The cloud provides all kinds of tools and services to secure your application in the cloud, along with in-built security at the IT infrastructure level. However, it's up to the customer how they want to utilize those services and make their application secure in the cloud. The overall cloud provides better visibility and centralized management for your IT inventory, which helps to manage and secure your system.
Security is the priority for any solution, and a solution architect needs to make sure their application is secure and protected from any attack. Security is a continuous effort. Each security incident should be treated as an improvement opportunity for the application. A robust security mechanism should have authentication and authorization controls. Every organization and application should automate responses to security events and protect infrastructure at multiple levels.

[ 256 ]

Security Considerations

Chapter 8

Summary
In this chapter, you learned about various design principles to apply security best practices for your solution design. These principles include key considerations during solution design to protect your application by putting in the appropriate access control, data protection, and monitoring. You need to apply security at every layer. Starting with user authentication and authorization, you learned about applying security at the web layer, application layer, infrastructure layer, and database layer. Each layer has a different kind of attack, and you learned various methods to protect your application with the available technology choices.
For user management, you learned about using FIM and SSO to handle corporate users, and various methods for implementation of user authentication and authorization. These choices include enterprise management services such as Microsoft's AD and AWS Directory Service. You also have options to handle millions of users, using OAuth 2.0.
At the web layer, you learned about various attack types such as DDoS, SQLi, and XSS. You learned about how to protect those attacks, using different DDoS prevention techniques and network firewalls. You learned various techniques to protect code at the application layer and ensure the security of your infrastructure. You dived deep into different network components and methods to build trusted boundaries to limit the attack radius.
You learned about data protection by putting proper data classification in place and tagged your data as confidential, private, or public data. You learned about symmetric and asymmetric algorithms and how they differ from each other. You learned about using key management to protect the public/private encryption key. Data can be in motion or sitting in storage. You learned about how to protect data in both modes. In the end, you learned about various compliance and shared security responsibility models applicable to a cloud workload.
While this chapter is about applying security best practices, reliability is another essential aspect of any solution design. To make your business successful, you want to create a reliable solution that should always be available and able to handle workload fluctuation. In the next chapter, you will learn about the best practices to make your application reliable with the available technology choices. You will learn various disaster recovery and data replication strategies to make your application more reliable.

[ 257 ]

9
Architectural Reliability
Considerations
Application reliability is one of the essential aspects of architecture design. A reliable application helps to win customer trust by making it available whenever the customer needs it. High availability is one of the mandatory criteria for online applications. Users want to browse your application anytime and complete tasks such as shopping and banking as per their convenience. Reliability is one of the essential recipes for any business to be successful.
Reliability means the ability of the system to recover from failure. It's about making your application fault-tolerant in such a way that it can recover without impacting the customer experience. A reliable system should be able to recover from any infrastructure failure or server failure. Your system should be prepared to handle any situation that could cause disruption.
In this chapter, you will learn various design principles applicable to making your solution reliable. Reliability needs to consider every component of the architecture. You will get an understanding of the right selection of technology to ensure your architecture's reliability at every layer. You will learn the following best practices for reliability in this chapter:
Design principles for architectural reliability Technology selection for architectural reliability Improving reliability with the cloud
By the end of this chapter, you will have learned about various disaster recovery techniques to ensure the high availability of your application and data replication methods for business process continuations.

Architectural Reliability Considerations

Chapter 9

Design principles for architectural reliability
The goal of reliability is to keep the impact of any failure to the smallest area possible. By preparing your system for the worst, you can implement a variety of mitigation strategies for the different components of your infrastructure and applications.
Before a failure occurs, you want to test your recovery procedures. It is essential to try to automate recovery as much as possible to reduce the possibility of human error.
The following are the standard design principles that help you to strengthen your system reliability. You will find that all reliability design principles are closely related and complement each other.

Making systems self-healing
System failure needs to be predicted in advance, and in the case of failure incidence, you should have an automated response for system recovery, which is called system selfhealing. Self-healing is the ability of the solution to automatically recover from failure. A self-sealing system detects failure proactively and responds to it gracefully with minimal customer impact. Failure can happen in any layer of your entire system, which includes hardware failure, network failure, or software failure. Usually, data center failure is not an everyday event, and more granular monitoring is required for frequent failures such as database connection and network connection failures. The system needs to monitor the failure and act to recover.
To handle failure response, first, you need to identify Key Performance Indicators (KPIs) for your application and business. At the user level, these KPIs may include the number of requests served per second or page load latency for your website. At the infrastructure level, you can define maximum CPU utilization, such as it should not go above 60%. Memory utilization should not go beyond 50% of the total available Random-Access Memory (RAM) and so on.
As you defined your KPIs, you should put the monitoring system in place to track failures and notify you as your KPIs reach the threshold. You should apply automation around monitoring so that the system can self-heal in the event of any incidents. For example, add more servers when CPU utilization reaches near 50%--proactive monitoring helps to prevent failures.

[ 259 ]

Architectural Reliability Considerations

Chapter 9

Applying automation
Automation is the key to improving your application's reliability. Try to automate everything from application deployment and configuration to the overall infrastructure. Automation provides you with agility where your team can move fast and experiment more often. You can replicate the entire system infrastructure and the environment with a single click to try a new feature.
You can plan the Auto Scaling of your application based on a schedule, for example, an ecommerce website has more user traffic on weekends. You can also automate scaling based on the user request volume to handle the unpredictable workload. Use automation to launch independent and parallel simulation jobs that will provide greater accuracy when combined with the results from the first simulation job. Repeating the same steps to configure each environment manually can be error prone. There is always a chance of human error, such as a typo, for example, in a database name.
Frequently, you need to apply the same configuration that you have on your development environment to Quality Assurance (QA) environments. There may be multiple QA environments for each stage of testing, which includes functional testing, UAT, and stress testing environments. Often, a QA tester discovers a defect caused by wrongly configured resources, which could introduce a further delay in the test schedule. Most importantly, you cannot afford to have a configuration error in production servers.
To reproduce precisely the same configuration, you may need to document a step-by-step configuration instruction. The solution to this challenge is to automate these steps by creating a script. The automation script itself can be the documentation.
As long as the script is correct, it is more reliable than manual configuration. It is certainly reproducible. Detecting unhealthy resources and launching replacement resources can be automated, and you can notify the IT operation team when resources are changed. Automation is a key design principle that needs to apply everywhere in your system.

Creating a distributed system
Monolithic applications have low reliability when it comes to system uptime, as one small issue in a particular module can bring down the entire system. Dividing your application into multiple small services reduces the impact area, so that issue is one part of the application shouldn't impact the whole system, and the application can continue to serve critical functionality. For example, in an e-commerce website, an issue with the payment service should not affect customer's ability to place orders, as payment can be processed later.
[ 260 ]

Architectural Reliability Considerations

Chapter 9

At the service level, scale your application horizontally to increase system availability. Design a system so that it can use multiple smaller components working together rather than a single monolithic system to reduce the impact area. In a distributed design, requests are handled by different components of the system, and the failure of one component doesn't impact the functioning of other parts of the system. For example, on an e-commerce website, the failure of warehouse management components will not impact the customer placing the order.
However, the communication mechanism can be complicated in a distributed system. You need to take care of system dependencies by utilizing the circuit breaker pattern. As you learned about the circuit breaker pattern in Chapter 6, Solution Architecture Design Patterns, the basic idea behind the circuit breaker is simple. You wrap a protected function call in a circuit breaker object, which monitors for failures.

Monitoring capacity
Resource saturation is the most common reason for application failure. Often, you will encounter the issue where your applications start rejecting requests due to CPU, memory, or hard disk overload. Adding more resources is not always a straightforward task as you should have additional capacity available when needed.
In a traditional on-premises environment, you need to calculate server capacity based on the assumption in advance. Workload capacity prediction becomes more challenging for a business such as a shopping website and any online business. Online traffic is very unpredictable and fluctuates heavily driven by global trends. Usually, procuring hardware can take anywhere between 3 to 6 months, and it's tough to guess capacity in advance. Ordering excess hardware will incur an extra cost as a resource is sitting idle, and a lack of resources will cause the loss of business due to application unreliability.
You need an environment where you don't need to guess capacity, and your application can scale on-demand. A public cloud provider such as AWS provides Infrastructure-as-aService (IaaS), which facilitates the on-demand availability of resources. In the cloud, you can monitor system supply and demand. You can automate the addition or removal of resources as needed. It allows you to maintain the level of resources that will satisfy demand without over-provisioning or under-provisioning.

[ 261 ]

Architectural Reliability Considerations

Chapter 9

Performing recovery validation
When it comes to infrastructure validation, most of the time, organizations focus on validating a happy path where everything is working. Instead, you should validate how your system fails and how well your recovery procedures work. Validate your application, assuming everything fails all the time. Don't just expect that your recovery and failover strategies will work. Make sure to test them regularly, so you're not surprised if something does go wrong.
A simulation-based validation helps you to uncover any potential risks. You can automate a possible scenario that could cause your system failure and prepare an incident response accordingly. Your validation should improve application reliability in such a way that nothing will fail in production.
Recoverability is sometimes overlooked as a component of availability. To improve the system's Recovery Point Objective (RPO) and Recovery Time Objective (RTO), you should back up data and applications along with their configuration as a machine image. You will learn more about RTO and RPO in the next section. In the event that a natural disaster makes one or more of your components unavailable or destroys your primary data source, you should be able to restore the service quickly and without lost data. Let's talk more about specific disaster recovery strategies to improve application reliability and associated technology choices.

Technology selection for architecture
reliability
Application reliability often looks at the availability of the application to serve users. Several factors go into making your application highly available. Fault tolerance refers to the built-in redundancy of an application's components. Scalability is how your application's infrastructure can respond to increased capacity needs to ensure your application is available and performing within your required standards.
To make your application reliable, you should able to restore service quickly and without lost data. Going forward, we are going to address the recovery process as disaster recovery. Before going into various disaster recovery scenarios, let's learn more about the Recovery Time Objective (RTO)/Recovery Point Objective (RPO) and data replication.

[ 262 ]

Architectural Reliability Considerations

Chapter 9

Planning the RTO and RPO
Any application needs to define service availability in an aspect of a Service-Level Agreement (SLA). Organizations define SLAs to ensure application availability and reliability for their users. You may want to define an SLA, saying my application should be 99.9% available in a given year or the organization can tolerate it if the application is down for 43 minutes per month, and so on. The RPO and RTO for an application is mostly driven by the defined SLA.
The RPO is the amount of data loss an organization can tolerate in the aspect of time. For example, my application is fine if it loses 15 minutes' worth of data. The RPO helps to define a data backup strategy. The RTO is about application downtime and how much time my application should take to recover and function normally after failure incidence. The following diagram illustrates the difference between the RTO and RPO:

RTO and RPO
In the preceding diagram, suppose the failure occurs at 10 A.M. and you took the last backup at 9 A.M.; in the event of a system crash, you would lose 1 hour of data. When you restore your system, there is an hour's worth of data loss, as you were taking data backups every hour. In this case, your system RPO is 1 hour, as it can tolerate living with 1 hour's worth of data loss. In this case, the RPO indicates that the maximum data loss that can be tolerated is 1. If your system takes 30 minutes to restore to the backup and bring up the system, then it defines your RTO as half an hour. It means the maximum downtime that can be tolerated is 30 minutes. The RTO is the time it takes to restore the entire system after a failure that causes downtime.
[ 263 ]

Architectural Reliability Considerations

Chapter 9

An organization typically decides on an acceptable RPO and RTO based on the user experience and financial impact on the business in the event of system unavailability. Organizations consider various factors when determining the RTO/RPO, which includes the loss of business revenue and damage to their reputation due to downtime. IT organizations plan solutions to provide effective system recovery as per the defined RTO and RPO.

Replicating data
Data replication and snapshots are the key to disaster recovery and making your system reliable. Replication creates a copy of the primary data site on the secondary site, and in the event of primary system failure, the system can fail over to the secondary system and keep working reliably. This data could be your file data stored in a NAS drive, database snapshot, or machine image snapshot. Sites could be two geo-separated on-premises systems, two separate devices on the same premises, or a physically separated public cloud.
Data replication is not only helpful for disaster recovery, but it can speed up an organization's agility by quickly creating a new environment for testing and development. Data replication can be synchronous or asynchronous.

Synchronous versus asynchronous replication
Synchronous replication creates a data copy in real time. Real-time data replication helps to reduce the RPO and increase reliability in the event of a disaster. However, it is expensive as it requires additional resources in the primary system for continuous data replication.
Asynchronous replication creates copies of data with some lag or as per the defined schedule. However, asynchronous replication is less expensive as it uses fewer resources compared to synchronous replication. You may choose asynchronous replication if your system can work with a longer RPO.
In terms of database technology such as Amazon RDS, synchronous replication is applied if we create RDS with multiple availability zone failover. For read replicas, there is asynchronous replication, and you can use that to serve report and read requests.

[ 264 ]

Architectural Reliability Considerations

Chapter 9

As illustrated in the following architecture diagram, in synchronous replication, there is no lag of data replication between the master and standby instance of the database while, in the case of asynchronous replication, there could be some lag while replicating the data between the master and reapplication instance:

Synchronous and asynchronous data replication
Let's explore some methods of data reapplication for the synchronous and asynchronous approaches.
Replication methods
The replication method is an approach to extract data from the source system and create a copy for data recovery purposes. There are different replication methods available to store a copy of data as per the storage type for business process continuation. Replications can be implemented using the following methods:
Array-based replication: In this, built-in software automatically replicates data. However, both the source and destination storage arrays should be compatible and homogenous to replicate data. A storage array contains multiple storage disks in a rack.
Large enterprises use array-based replication due to the ease of deployment and the reduction in the compute power host system. You can choose array-based replication products such as HP Storage, EMC SAN Copy, and NetApp SnapMirror.
Network-based replication: This can copy data between a different kind of heterogeneous storage array. It uses an additional switch or appliance between incompatible storage arrays to replicate data.
[ 265 ]

Architectural Reliability Considerations

Chapter 9

In network-based replication, the cost of replication could be higher as multiple players come into the picture. You can choose from networked-based replication products such as NetApp Replication X and EMC RecoverPoint.
Host-based replication: In this, you install a software agent on your host that can replicate data to any storage system such as NAS, SAN, or DAS. You can use a host-based software vendor, for example, Symantec, Commvault, CA, or Vision Solution.
It's highly popular in Small and Medium-Sized Businesses (SMBs) due to fewer upfront costs and heterogeneous device compatibility. However, it consumes more compute power as the agent needs to install on host operating system.
Hypervisor-based replication: This is VM-aware, which means it can copy the entire virtual machine from one host to another. As organizations mostly use a virtual machine, it provides a very efficient disaster recovery approach to reduce the RTO.
Hypervisor-based replication is highly scalable and consumes fewer resources than host-based replication. It can be carried out by native systems built into VMware and Microsoft Windows. You can choose a product such as Zerto to perform hypervisor-based replication or another product from one of the various vendors.
Previously, in Chapter 3, Attributes of the Solution Architecture, you learned about scalability and fault tolerance. In Chapter 6, Solution Architecture Design Patterns, you learned about various design patterns to make your architecture highly available. Now, you will discover multiple ways to recover your system from failure and make it highly reliable.

Planning disaster recovery
Disaster Recovery (DR) is about maintaining business continuation in the event of system failure. It's about preparing the organization for any possible system failure and the ability to recover from it. DR planning includes multiple dimensions, which include hardware or software failure. While planning for disaster recovery, always ensure you consider other operational failures, which include a power outage, network outage, heating and cooling system failure, physical security breach, and different incidents such as fire, flood, or human error.

[ 266 ]

Architectural Reliability Considerations

Chapter 9

Organizations invest effort and money in disaster recovery planning as per system criticality and impact. A revenue-generating application needs to be up all of the time as it has a significant impact on company image and profitability. Such an organization invests lots of effort in creating their infrastructure and training their employees for a disaster recovery situation. Disaster recovery is like an insurance policy that you have to invest and maintain even when you are not going to utilize it. Similarly, during normal operations, the infrastructure typically is under-utilized and over-provisioned.
Applications can be placed on a spectrum of complexity. There are four DR scenarios, sorted from highest to lowest RTO/RPO as follows:
Backup and restore Pilot light Warm standby Multi-site active-active
As shown in the following diagram, in DR planning, as you progress with each option, your RTO and RPO will reduce while the cost of implementation increases. You need to make the right trade-off between RTO/RPO requirements and cost as per your application reliability requirement:

Disaster recovery options spectrum
Let's explore each of the aforementioned options in detail with technology choices. Now, the public cloud, such as AWS, enables you to operate each of the preceding DR strategies cost-effectively and efficiently. Business continuity is about ensuring critical business functions continue to operate or function quickly in the event of disasters. As organizations are opting to use the cloud for disaster recovery plans, let's learn about various disaster recovery strategies between an onpremise environment and the AWS cloud.
[ 267 ]

Architectural Reliability Considerations

Chapter 9

Backup and restore
Backup is the lowest cost option but with higher RPO and RTO. This method is simple to get started and extremely cost-effective as you need backup storage. This backup storage could be a tape drive, hard disk drive, or network access drive. As your storage needs increase, adding and maintaining more hardware across regions could be a daunting task. One of the simple and cost-effective options is to use the cloud as backup storage. Amazon S3 provides unlimited storage capacity at a low cost and with a pay-as-you-go model.
The following diagram shows a basic disaster recovery system. In this diagram, the data is in a traditional data center, with backups stored in AWS. AWS Import/Export or Snowball is used to get the data into AWS, and the information is later stored in Amazon S3:

Data backup to Amazon S3 from on-premises infrastructure
You can use other third-party solutions available for backup and recovery. Some of the most popular choices are NetApp, VMware, Tivoli, Commvault, and CloudEndure. You need to take backups of the current system and store them in Amazon S3 using a backup software solution. Make sure to list the procedure to restore the system from a backup on the cloud, which includes the following:
1. Understand which Amazon Machine Image (AMI) to use and build your own as required with pre-installed software and security patches.
2. Document the steps to restore your system from a backup. 3. Document the steps to route traffic from the primary site to the new site in the
cloud. 4. Create a run book for deployment configuration and possible issues with their
resolutions.
[ 268 ]

Architectural Reliability Considerations

Chapter 9

If the primary site located on-premises goes down, you need to start the recovery process. As shown in the following diagram, in the preparation phase, create a custom Amazon Machine Image (AMI), which is pre-configured with the operating system along with the required software, and store it as a backup in Amazon S3. Store any other data such as database snapshots, storage volume snapshots, and files in Amazon S3:

Restoring systems from Amazon S3 backups in the cloud
If the primary site goes down, you can retrieve backups from Amazon S3 and bring up the required infrastructure. You can spin up Amazon EC2 server instances using golden machine image and put it behind load balancer with Auto Scaling configuration as needed. It would be a better approach to automate your infrastructure such as networking deployment and bring it up by deploying the AWS CloudFormation template. Once your servers are up and running, you need to restore data from backup. The last task is to switch over traffic to the new system by adjusting DNS records to point to AWS.
This disaster recovery pattern is easy to set up and rather inexpensive. However, in this scenario, both RPO and RTO will be high, RTO will be downtime until system gets restored from backup and start functioning, while RPO will have an amount of data loss which depends upon the backup frequency. Let's explore the next approach, pilot light, which provides improvements in your RTOs and RPOs.
Pilot light
The pilot light is the next lowest cost DR method after backup and restore. As the name suggests, you need to keep the minimum amount of core services up and running in a different region. You can spin up additional resources quickly in the event of a disaster.
[ 269 ]

Architectural Reliability Considerations

Chapter 9

You would probably actively replicate the database tier, then spin up instances from a VM image or build out infrastructure using infra as code such as CloudFormation. Just like the pilot in your gas heater, a tiny flame that is always on can quickly light up the entire furnace to heat the house.
The following diagram shows a pilot light disaster recovery pattern. In this case, the database is replicated into AWS, with Amazon EC2 instances of the web servers and application servers ready to go, but currently not running:

The pilot light data replication to DR site scenario
A pilot light scenario is pretty much similar to back up and restore, where you take the backup of most of the components and store them passively. However, you maintain active instances with a lower capacity for critical components such as a database or authentication server, which can take a significant time to come up. You need to be prepared to start all required resources automatically, which include network settings, load balancers, and virtual machine images as required. As core pieces are already running, recovery time is faster than the backup and restore method.
[ 270 ]

Architectural Reliability Considerations

Chapter 9

The pilot light is very cost-effective as you are not running all of the resources 24/7. You need to enable the replication of all critical data to the disaster recovery site--in this case, the AWS cloud. You can use the AWS Data Migration Service to replicate data between onpremise and cloud databases. For file-based data, you can use Amazon File Gateway. There are many third-party managed tools available that provide data reapplication solutions efficiently, such as Attunity, Quest, Syncsort, Alooma, and JumpMind.
Now, if the primary system fails, as shown in the following diagram, you start up the Amazon EC2 instances with the latest copy of the data. Then, you redirect Amazon Route 53 to point to the new web server:

Recovery in the pilot light method
For the pilot light method, in the case of a disaster environment, you need to bring up the resources around the replicated core dataset automatically and scale the system as required to handle the current traffic. You can choose to vertically scale up the database instance and scale out application servers with horizontal scaling using a load balancer. Finally, update the DNS record in your router to point to the new site.
A pilot light disaster recovery pattern is relatively easy to set up and inexpensive. However, in this scenario, the RTO takes a bit longer to automatically bring up a replacement system, while the RPO largely depends on the replication type. Let's explore the next approach, warm standby, which provides further improvements in your RTOs and RPOs.
[ 271 ]

Architectural Reliability Considerations

Chapter 9

Warm standby
Warm standby, also known as fully working low capacity standby, is like the next level of the pilot light. It is the option where you use the agility of the cloud to provide low-cost DR. It increases the cost but also allows data to recover more quickly by having a small subset of services already running.
You can decide whether your disaster recovery environment should be enough to accommodate 30% or 50% of production traffic. Alternatively, you can also use this for nonproduction testing.
As shown in the following diagram, in the warm standby method, two systems are running--the central system and a low-capacity system--on a cloud such as AWS. You can use a router such as Amazon Route 53 to distribute requests between the central system and the cloud system:

Warm standby scenario running an active-active workload with a low capacity
When it comes to a database, warm standby has a similar approach to pilot light, where data is continuously replicating from the main site to the disaster recovery site. However, in warm standby, you are running all necessary components 24/7; however, they do not scale up for production traffic.
[ 272 ]

Architectural Reliability Considerations

Chapter 9

Often, the organization chooses a warm standby strategy for more critical workloads, so you need to make sure there are no issues in the disaster recovery site with continuous testing. The best approach is to take the A/B testing approach, where major traffic will be handled by the main site but a small amount of traffic, approximately 1% to 5%, is routed to the disaster recovery site. It will make the disaster recovery site able to serve traffic when the primary site is down. Also, make sure to patch and update software regularly in the disaster recovery site.
As shown in the following diagram, during the unavailability of the primary environment, your router switches over to the secondary system, which is designed to automatically scale its capacity up in the event of a failover from the primary system:

Recovery phase in the warm standby scenario
In the event of a failure in the primary site, you can take a step approach, where an immediate transfer of the critical production workload to the disaster recovery site, and other non-critical workloads can be transferred later as you scale up your environment. For example, in an e-commerce business, you first need to bring up your website, which is customer-facing, and later you can bring up other systems such as warehouse management and shipping, which is working in the background to fulfill the order.
[ 273 ]

Architectural Reliability Considerations

Chapter 9

Your disaster recovery process becomes more efficient if your application is an all-in cloud, where entire infrastructures and applications are hosted in the public cloud, such as AWS. The AWS cloud allows you to use cloud-native tools efficiently; for example, you can enable a multi-AZ failover feature in the Amazon RDS database to create a standby instance in another availability zone with continuous replication. In the case of the primary database, an instance goes down, an in-built automatic failover takes care of switching the application to the standby database without any application configuration changes. Similarly, you can use automatic backup and replication options for all kinds of data protection.
A warm standby disaster recovery pattern is relatively complex to set up and expensive. The RTO is much quicker than pilot light for critical workload, however for non-critical workload it's depends upon how quickly you can scale up system, while the RPO largely depends upon the replication type. Let's explore the next approach, multi-site, which provides near-zero RTOs and RPOs.

Multi-site
Lastly, the multi-site strategy, also known as hot standby, helps you to achieve near-zero RTO and RPO. In multi-site, your disaster recovery site is an exact replica of the primary site with continuous data replication and traffic flow. It is known as multi-site architecture due to the automated load balancing of traffic across regions or between on premise and the cloud.
As shown in the following diagram, multi-site is the next level of disaster recovery to have a fully functional system running in the cloud at the same time as on-premises systems:

Multi-site scenario running an active-active workload with a full capacity
[ 274 ]

Architectural Reliability Considerations

Chapter 9

The advantage of the multi-site approach is that it is ready to take a full production load at any moment. It's similar to warm standby but running full capacity in the disaster recovery site. If the primary site goes down, all traffic can be immediately failed over to the disaster recovery site.
A multi-site disaster recovery pattern is most expensive as it requires a duplicate of everything. However, in this scenario, the RTO objective is much quicker for all workloads, while the RPO objective largely depends upon the replication type. Let's explore some best practices around disaster recovery to make sure your system is running reliably.

Applying best practices for disaster recovery
As you start thinking about disaster recovery, here are some important considerations:
Start small and build as needed: Make sure to streamline the first step of taking a backup. Most of the time, organizations lose data as they didn't have an efficient backup strategy. Take a backup of everything, whether it is your file server, machine image, or databases.
Keeping lots of active backups could increase costs, so make sure to apply a lifecycle policy to archive and delete data as per business needs. For example, you can choose to keep a 90-day active backup and after that store that in low-cost archive storage such as a tape drive or Amazon Glacier. After 1 or 2 years, you may want to set a lifecycle policy to delete the data. Compliance such as PCI-DSS may require users to store data for 7 years, and in that case, you must choose archival data storage to reduce costs.
Check your software licenses: Managing software licenses can be a daunting task, especially in the current microservice architecture environment, where you have several services running independently on their instances of virtual machines and databases. Software licenses could be associated with several installations, a number of CPUs, and several users. It becomes tricky when you go for scaling. You need to have enough licenses to support your scaling needs.
Horizontal scaling needs to add more instances with software installed, and in vertical scaling, you need to add more CPU or memory. You need to understand your software licensing agreement and make sure you have the appropriate license to fulfill system scaling. Also, you don't have to buy an excessive license, which you may not be able to utilize and costs more money. Overall, make sure to manage your license inventory like your infrastructure or software.

[ 275 ]

Architectural Reliability Considerations

Chapter 9

Test your solutions often: Disaster recovery sites are created for rare disaster recovery events and are often overlooked. You need to make sure your disaster recovery solution is working as expected in case of an event to achieve higher reliability. Compromising a defined SLA can violate contractual obligations and result in the loss of money and customer trust.
One way to test your solution often is by playing gameday. To play gameday, you can choose a day when the production workload is smaller and gather all of the team responsible for maintaining the production environment. You can simulate a disaster event by bringing down a portion of the production environment and let the team handle the situation to keep the environment up and running. These events make sure you have working backups, snapshots, and machine images to handle disaster events.
Always put a monitoring system in place to make sure automated failover to the disaster recovery site takes place if an event occurs. Monitoring helps you to take a proactive approach and improves system reliability by applying automation. Monitoring capacity saves you resource saturation issues, which can impact your application's reliability. Creating a disaster recovery plan and performing regular recovery validation helps to achieve the desired application reliability.

Improving reliability with the cloud
In previous sections, you have seen examples of a cloud workload for the disaster recovery site. Many organizations have started to choose the cloud for disaster recovery sites to improve application reliability, as the cloud provides various building blocks. Also, cloud providers such as AWS have a marketplace where you can purchase a variety of ready-touse solutions from providers.
The cloud provides data centers that are available across the geographic location at your fingertips. You can choose to create a reliability site on another continent without any hassle. With the cloud, you can easily create and track the availability of your infrastructures such as backups and machine images.
In the cloud, easy monitoring and tracking help to make sure your application is highly available as per the SLA. The cloud enables you to have fine control over IT resources, cost, and handling trade-offs for RPO/RTO requirements. Data recovery is critical for application reliability. Data resources and locations must align with RTOs and RPOs.

[ 276 ]

Architectural Reliability Considerations

Chapter 9

The cloud provides easy and effective testing of your disaster recovery plan. You inherit features available in the cloud, such as the logs and metrics mechanisms for various cloud services. Built-in metrics are a powerful tool for gaining insight into the health of your system. With all available monitoring capabilities, you can notify the team in case of any threshold breach or trigger automation for system self-healing. For example, AWS provides CloudWatch, which can collect logs and generate metrics while monitoring different applications and infrastructure components. It can trigger various automation to scale your application.
The cloud provides a built-in change management mechanism that helps to track provisioned resources. Cloud providers extend out-of-the-box capabilities to ensure applications and operating environments are running known software and can be patched or replaced in a controlled manner. For example, AWS provides AWS System Manager, which has the capability of patching and updating cloud servers in bulk. The cloud has tools to back up data, applications, and operating environments to meet requirements for RTOs and RPOs. Customers can leverage cloud support or a cloud partner for their workload handling needs.
With the cloud, you can design a scalable system, which can provide flexibility to add and remove resources automatically to match the current demand. Data is one of the essential aspects of any application's reliability. The cloud provides out-of-the-box data backup and replication tools, including machine images, databases, and files. In the event of a disaster, all of your data is backed up and appropriately saved in the cloud, which helps the system to recover quickly.
Regular interaction across the application development and operation team will help to address and prevent known issues and design gaps, which will reduce the risk of failures and outages. Always architect your applications to achieve resiliency and distribute them to handle any outages. Distribution should span different physical locations to achieve high levels of availability.

[ 277 ]

Architectural Reliability Considerations

Chapter 9

Summary
In this chapter, you learned about various principles to make your system reliable. These principles include making your system self-healing by applying rules of automation and to reduce the impact in the event of failure by designing a distributed system where the workload spans multiple resources.
Overall system reliability heavily depends on your system's availability and its ability to recover from disaster events. You learned about synchronous and asynchronous data replication types and how they affect your system reliability. You learned about various data replication methods, including array-based, network-based, host-based, and hypervisor-based. Each replication method has its pros and cons. There are multiple vendors' products available to achieve the desired data replication.
You learned about various disaster planning methods as per the organization's needs and the RTO and RPO. You learned about backup & restore method that has high RTO and RPO, and it is easy to implement. Pilot light improves your RTO/RPO by keeping critical resources such as a database active in the disaster recovery site. Warm standby and multisite maintain an active copy of a workload on a disaster recovery site and help to achieve a better RTO/RPO. As you increase application reliability by lowering the system's RTO/RTO, the system's complexity and cost increase. You learned about utilizing the cloud's built-in capability to endure application reliability.
Solution design and launch may not happen too often, but operational maintenance is an everyday task. In the next chapter, you will learn about the alert and monitoring aspects of solution architecture. You will learn about various design principles and technology choices to make your application operationally efficient and apply operational excellence.

[ 278 ]

10
Operational Excellence
Considerations
Application maintainability is one of the main aspects that a solution architect should consider during architectural design. Every new project starts with lots of planning and resources at the beginning. You may spend a few months creating and launching your application but change frequency will get reduced as your application matures. After the production launch, the application needs several things to be taken care of to keep operating. You need to continually monitor your application to find and resolve any issues on a day-to-day basis.
The operations team needs to handle application infrastructure, security, and any software issues to make sure your application is running reliably without any problems or issues. Often, an enterprise application is complex in nature, with a defined Service Level Agreement (SLA) regarding application availability. Your operations team needs to understand business requirements and prepare themself accordingly to respond to any event.
Operation excellence should be implemented across various components and layers of architecture. In modern microservice applications, there are so many moving parts involved that this makes system operations and maintenance a complicated task. Your operations team needs to put proper monitoring and alert mechanisms in place to tackle any issues. Operational issues involve coordination from several teams for preparation and resolution. Operation expenditures are one of the significant costs that an organization puts aside to run a business.

Operational Excellence Considerations

Chapter 10

In this chapter, you will learn various design principles applicable to achieve operational excellence for your solution. The operational aspect needs to consider every component of the architecture. You will get an understanding of the right selection of technologies to ensure operational maintainability at every layer. You will learn the following best practices of operational excellence in this chapter:
Designing principles for operational excellence Selecting technologies for operational excellence Achieving operational excellence in the public cloud
By the end of this chapter, you will learn about various processes and methods to achieve operational excellence. You will learn about best practices that you can apply throughout application design, implementation, and post-production to improve application operability.

Designing principles for operational excellence
Operational excellence is about running your application with the minimal possible interruption to gain maximum business value. It is about applying continuous improvements to make the system efficient.
The following sections talk about the standard design principles that can help you strengthen your system's maintainability. You will find that all operational excellence design principles are closely related and complement each other.
Automating the operation
Technology has been moving fast in recent times, and so IT operations need to keep up with that, where hardware and software inventories are procured from multiple vendors. Enterprises are building a hybrid cloud, so you need to handle both on-premises and cloud operations. All modern systems have a decidedly more extensive user base, with various microservices working together and millions of devices connected in the network. There are many moving parts in an IT operation, so this makes it difficult to run things manually.

[ 280 ]

Operational Excellence Considerations

Chapter 10

Organizations maintain agility, and operations have to be faster to avail the required infrastructure for new service development and deployment. The operations team has a more significant responsibility to keep services up and to run and recover quickly in case of an event. Now, it is required to take a proactive approach in IT operations, rather than waiting for an incident to happen and then reacting.
Your operations team can work very efficiently by applying automation. Manual jobs need to be automated so that the team can focus on more strategic initiatives rather than getting overworked with tactical work. Spinning up a new server or starting and stopping services should be automated by taking an infrastructure as code (IaC) approach. Automating active discovery and response for any security threat is most important, to free up the operations team. Automation allows the team to devote more time to innovation.
For your web-facing application, you can detect anomalies in advance before they impact your system, using machine learning prediction. You can raise an automated security ticket if someone exposes your server to the world with HTTP port 80. You can pretty much automate the entire infrastructure and redeploy it multiple times as a one-click solution. Automation also helps to avoid human error, which can occur even if a person is doing the same job repetitively. Automation is now a must-have friend for IT operations.

Making incremental and reversible changes
Operational optimization is an ongoing process, whereby continuous effort is required to identify the gap and improve upon it. Achieving operational excellence is a journey. There are always changes required in all parts of your workload to maintain it--for example, often, operating systems of your server need to be updated with the security patch provided by your vendor. Various software that your application is using needs a version upgrade. You need to make changes in the system to adhere to new compliance.
You should design your workload in such a way that it allows all system components to get updated regularly, so the system will benefit from the latest and most significant updates available. Automate your flow so that you can apply small changes to avoid any significant impact. Any changes should be reversible, to restore system working conditions in the case of any issue. Incremental changes help to do thorough testing and improve overall system reliability. Automate any change management to avoid human error and achieve efficiency.

[ 281 ]

Operational Excellence Considerations

Chapter 10

Predicting failures and responding
Preventing failures is vital to achieving operational excellence. Failures are bound to happen, and it's more critical to identify them as far in advance as possible. During architecture design, anticipate failure to make sure you design for failure so that nothing will fail. Assume that everything will fail all the time and have a backup plan ready. Perform regular pre-mortem exercises to identify any potential source of failure. Try to remove or mitigate any resource that could cause a failure during system operation.
Create a test scenario based on your SLA that potentially includes a system Recovery Time Objective (RTO) and Recovery Point Objective (RPO). Test your scenario, and make sure you understand their impact. Make your team ready to respond to any incident by simulating in a production-like scenario. Test your response procedure to make sure it is resolving issues effectively and create a confident team that is familiar with response execution.

Learning from the mistake and refining
As operational failures occur in your system, you should learn from the mistake and identify the gap. Make sure those same events do not occur again, and you should have a solution ready in case a failure gets repeated. One way to improve is by running root cause analysis, also called RCA.
During RCA, you need to gather the team and ask five whys. With each why, you peel off one layer of the problem, and, after asking subsequent why, you get to the bottom of the issue. After identifying the actual cause, you can prepare a solution by removing or mitigating the resources and update the operational runbook with the ready-to-use solution.
As your workload evolves with time, you need to make sure the operation procedure gets updated accordingly. Make sure to validate and test all methods regularly, and that the team is familiar with the latest updates in order to execute them.

Keeping operation's runbook updated
Often, a team overlooks documentation, which results in an outdated runbook. A runbook provides a guide to executing a set of actions in order to resolve issues arising due to external or internal events. A lack of documentation can make your operation peopledependent, which can be risky due to team attrition. Always establish processes to keep your system operation people-independent, and document all the aspects.
[ 282 ]

Operational Excellence Considerations

Chapter 10

Your runbook should include the defined SLA in the aspect of RTO/RPO, latency and performance, and so on. The system admin should maintain a runbook with steps to start, stop, patch, and update the system. The operations team should include the system testing and validation result, along with the procedure to respond to the event.
In the runbook, you want to keep track of all previous events and actions taken by team members to resolve them, so that any new team members can provide a quick resolution of similar incidents during operation support. Automate your runbook through the script so that it can get updated automatically as new changes roll out to the system.
Automate processes to annotate documents as a team applies changes to the system, and also after every build. You can use annotation to automate your operation, and it is easily readable by code. Business priorities and customer needs continue to change, and it's essential to design operations to support evolution over time.

Selecting technologies for operational excellence
The operations team needs to create procedures and steps to handle any operational incidents and validate the effectiveness of their actions. They need to understand the business need to provide efficient support. The operations team needs to collect systems and business metrics to measure the achievement of business outcomes.
The operational procedure can be categorized into three phases--planning, functioning, and improving. Let's explore technologies that can help in each phase.
Planning for operational excellence
The first step in the operational excellence process is to define operational priorities to focus on the high business impact area. Those areas could be applying automation, streamlining monitoring, developing team skills as workload evolves, and focusing on improving overall workload performance. These are tools and services available that crawl through your system by scanning logs and system activity. These tools provide a core set of checks that recommend optimizations for the system environment and help to shape priorities.

[ 283 ]

Operational Excellence Considerations

Chapter 10

After understating priorities, you need to design the operation, which includes the understanding of workloads to design and building the procedures to support them. The design of a workload should consist of how it will be implemented, deployed, updated, and operated. An entire workload can be viewed as various application components, infrastructure components, security, data governance, and operations automation.
While designing for an operation, consider the following best practice:
Automate your runbook with scripting to reduce human error, which creates an operating workload. Use resource identification mechanisms to execute operations based on defined criteria such as environment, various versions, application owner, and roles. Make incident responses automated so that, in the case of an event, the system should start self-healing without much human intervention. Use various tools and capabilities to automate the management of server instances and overall systems. Create script procedures on your instances to automate the installation of required software and security patches when the server gets started. These scripts are also known as bootstrap scripts.
After the operation design, create a checklist for operational readiness. These checklists should be comprehensive to make sure the system is ready for operation support when going live in production. This includes logging and monitoring, a communication plan, an alert mechanism, a team skillset, a team support charter, a vendor support mechanism, and so on. For operational excellence planning, the following are the areas where you need appropriate tools for preparation:
IT Asset Management Configuration management
Let's explore each area in more detail, to understand the available tools and processes.

IT Asset Management (ITAM)
Operational excellence planning requires the list of IT inventories and tracks their use. These inventories include infrastructure hardware such as physical servers, network devices, storage, end-user devices, and so on. You also need to keep track of software licenses, operational data, legal contracts, compliance, and so on. IT assets include any system, hardware, or information that a company is using to perform a business activity.

[ 284 ]

Operational Excellence Considerations

Chapter 10

Keeping track of IT assets helps an organization to make strategic and tactical decisions regarding operational support and planning. However, managing IT assets in a large organization could be a very daunting task. Various ITAM tools are available for the operations team to help in the asset management process. Some of the most popular ITAM tools are SolarWinds, Freshservice, ServiceDesk Plus, Asset Panda, PagerDuty, Jira Service Desk, and so on.
IT management is more than tracking IT assets. It also involves monitoring and collecting asset data continuously, to optimize usages and operation costs. ITAM makes the organization more agile by the provided end-to-end visibility and the ability to apply patches and upgrades quickly. The following diagram illustrates IT asset life cycle management (ITALM):

ITALM process
As shown in the preceding diagram, the ITALM process includes the following phases: Plan: An asset life cycle starts with planning, which is a more strategic focus to determine needs for overall IT assets and procurement methods. It includes costbenefit analysis and total cost of ownership.
[ 285 ]

Operational Excellence Considerations

Chapter 10

Procure: In the procurement phase, organizations acquire the asset based on the outcome of planning. They may also decide to develop some holdings as required--for example, in-house software for logging and monitoring.
Integrate: In this phase, an asset is installed in the IT ecosystem. It includes operation and support of the asset, and defines user access--for example, installing a log agent to collect logs from all the servers in a centralized dashboard, and restricting monitoring dashboard metrics to the IT operations team.
Maintain: In the maintenance phase, the IT operations team keeps track of assets, and acts to upgrade or migrate based on the asset life cycle--for example, applying a security patch provided by the software vendor. The other example is keeping track of end of life for licensed software, such as a plan to migrate from Windows 2008 to Windows 2016, as the old operating system is getting to the end of its life.
Retire: In the retirement phase, the operations team disposes of the end-of-life asset. For example, if an old database server is getting to the end of its life, then the team takes action to upgrade it and migrates the required user and support to the new server.
ITAM helps organizations adhere to ISO 19770 compliance requirements. It includes software procurement, deployment, upgrade, and support. ITAM provides better data security and helps to improve software compliance. It provides better communication between business units such as operation, finance, and marketing teams, and frontline staff.

Configuration management
Configuration management maintains configuration items (CI) to manage and deliver an IT service. CIs are tracked in the Configuration Management Database (CMDB). The CMDB stores and manages system component records with their attributes such as their type, owner, version, and dependency with other components. The CMDB keeps track of whether the server is physical or virtual, if the operating system is installed with its version (Windows 2012 or Red Hat Enterprise Linux (RHEL) 7.0),the owner of the server (support, marketing, or HR), and whether it has dependency on other servers such as order management, and so on.

[ 286 ]

Operational Excellence Considerations

Chapter 10

Configuration management is different from asset management. As you learned in the previous section, asset management is much faster. It manages the entire life cycle of an asset, from planning to retirement, while CMDB is a component of asset management that stores configuration records of an individual asset. As shown in the following diagram, configuration management implements the integration and maintenance part of asset management:

IT asset life cycle versus configuration management
Zooming in on configuration management, as shown in the preceding diagram, configuration management implements the deployment, installation, and support part of asset management. The configuration management tool can help the operations team to reduce downtime by providing readily available information on asset configuration. Implementing effective change management helps us to understand the impact of any changes in the environment. The most popular configuration management tools are Chef, Puppet, Ansible, Bamboo, and so on. You will learn more details about them in Chapter 12, DevOps and Solution Architecture Framework.
[ 287 ]

Operational Excellence Considerations

Chapter 10

IT management becomes easier if your workload is in a public cloud such as Amazon Web Services (AWS), Azure, or Google Cloud Platform (GCP). Cloud vendors provide inbuilt tools to track and manage IT inventories and configuration in one place. For example, AWS provides services such as AWS Config, which tracks all IT inventories that spin up as a part of your AWS cloud workload, and services such as AWS Trusted Advisor, which recommends cost, performance, and security, which you can use to decide to manage your workload.
The enterprise creates a framework such as an Information Technology Infrastructure Library (ITIL), which implements an Information Technology Service Management (ITSM) best practice. An ITIL provides a view on how to implement ITSM.
In this section, you learned about asset management and configuration management, which is part of the ITIL framework and more relevant to operational excellence. ITSM helps organizations to run their IT operations daily. You can learn more about ITIL from its governing body AXELOS by visiting their website (https:// www.axelos.c om/b estpractice-s olutions/i til). AXELOS offers ITIL certification to develop skills in the IT service management process. As you have learned about planning, let's explore the functioning of IT operations in the next section.

The functioning of operational excellence
Operational excellence is determined by proactive monitoring and quickly responding, to recover in the case of an event. By understanding the operational health of a workload, it is possible to identify when events and responses impact it. Use tools that help understand the operational health of the system using metrics and dashboards. You should send log data to centralized storage and define metrics to establish a benchmark.
By defining and knowing what a workload is, it is possible to respond quickly and accurately to operational issues. Use tools to automate responses to operational events supporting various aspects of your workload. These tools allow you to automate responses for operational events and initiate their execution in response to alerts.

[ 288 ]

Operational Excellence Considerations

Chapter 10

Make your workload components replaceable, so that rather than fixing the issue you can improve recovery time by replacing failed components with known good versions. Then, analyze the failed resources without impacting a production environment. For the functioning of operational excellence, the following are the areas where appropriate tools are needed:
Monitoring system health Handling alerts and incident response
Let's understand each area in more detail with information on the available tools and processes.

Monitoring system health
Keeping track of system health is essential to understand workload behavior. The operations team uses system health monitoring to record any anomalies in the system component, and acts accordingly. Traditionally, monitoring is limited to the infrastructure layer keeping track of the server's CPU and memory utilization. However, monitoring needs to be applied to every layer of the architecture. The following are the significant components where monitoring is applied.
Infrastructure monitoring
Infrastructure monitoring is essential and is the most popular form of monitoring. Infrastructure includes components required for hosting applications. These are the core services such as storage, servers, network traffic, load balancer, and so on. Infrastructure monitoring may consist of metrics, such as the following:
CPU usage: Percentage of CPU utilized by the server in a given period Memory usage: Percentage of random-access memory (RAM) utilized by the server in a given period Network utilization: Network packet, in and out over the given period Disk utilization: Disk read/write throughput and input/output operations per second (IOPS) Load balancer: Number of request counts in a given period

[ 289 ]

Operational Excellence Considerations

Chapter 10

There are many more metrics available, and organizations need to customize those monitoring metrics as per their application monitoring requirement. The following screenshot shows a sample monitoring dashboard for network traffic:

Infrastructure monitoring dashboard
You can see the preceding system dashboard showing a spike in one day, with color-coding applied for different servers. The operations team can dive deep in each graph and resources to get a more granular view.
Application monitoring
Sometimes, your infrastructure is all healthy except applications having an issue due to some bug in your code or any third-party software issues. You may have applied some vendor-provided operating system security patch that messed up your application. Application monitoring may include metrics, such as following:
Endpoint invocation: Number of request counts in a given period Response time: Average response time to fulfill the request Throttle: Number of valid requests spilled out as the system runs out of capacity to handle the additional requests Error: Application throw an error while responding to a request
The following screenshot shows a sample application endpoint-monitoring dashboard:
[ 290 ]

Operational Excellence Considerations

Chapter 10

Application monitoring dashboard
There could be many more metrics based on application and technology--for example, a memory garbage collection amount for a Java application, a number of HTTP POST and GET requests for a RESTful service, a count of 4XX client errors, a count of 5XX server errors for a web application, and so on.
Platform monitoring
Your application may be utilizing several third-party platforms and tools that need to be monitored. These may include the following:
Memory caching: Redis and Memcached Relational database: Oracle Database, Microsoft SQL Server, Amazon Relational Database Service (RDS), PostgreSQL NoSQL database: Amazon DynamoDB, Apache Cassandra, MongoDB Big data platform: Apache Hadoop, Apache Spark, Apache Hive, Apache Impala, Amazon Elastic MapReduce (EMR) Containers: Docker, Kubernetes, OpenShift Business intelligence tool: Tableau, MicroStrategy, Kibana, Amazon QuickSight Messaging system: MQSeries, Java Message Service (JMS), RabbitMQ, Simple Queue Service (SQS) Search: Elasticsearch, Solr search-based application
[ 291 ]

Operational Excellence Considerations

Chapter 10

Each of the aforementioned tools has its own set of metrics that you need to monitor to make sure your application is healthy as a whole. The following screenshot shows the monitoring dashboard of a relational database platform:

Platform monitoring dashboard for a relational database management system (RDBMS)
In the preceding dashboard, you can see the database has lots of write activity, which is showing that the application is continuously writing data. On the other hand, read events are relatively consistent except for some spikes.
Log monitoring
Traditionally, log monitoring was a manual process, and organizations took a reactive approach to analyze logs when issues were encountered. However, with more competition and increasing expectations from users, it has become essential to take quick action before the user notices the issue. For a proactive approach, you should have the ability to stream logs in a centralized place and run queries to monitor and identify the issue.
[ 292 ]

Operational Excellence Considerations

Chapter 10

For example, if some product page is throwing the error out, you need to know the error immediately and fix the problem before the user complains, else you will suffer a revenue loss. In the case of any network attack, you need to analyze your network log and block suspicious IP addresses. Those IPs may be sending an erroneous number of data packets to bring down your application. Monitoring systems such as AWS CloudWatch, Logstash, Splunk, Google Stackdriver, and so on provide an agent to install in your application server. The agent will stream logs to a centralized storage location. You can directly query to central log storage and set up alerts for any anomalies.
The following screenshot shows a sample network log collected in a centralized place:

Raw network log streamed in a centralized datastore
[ 293 ]

Operational Excellence Considerations

Chapter 10

You can run a query in these logs and find out the top 10 source IP addresses with the highest number of reject requests, as shown in the following screenshot:

Insight from raw network log by running query
As shown in the preceding query editor, you can create a graph and put an alarm in, if the number of rejections detected crosses a certain threshold, such as more than 5,000.
[ 294 ]

Operational Excellence Considerations

Chapter 10

Security monitoring
Security is a critical aspect of any application. Security monitoring should be considered during solution design. As you learned when we looked at security in the various architectural components in Chapter 8, Security Considerations, security needs to be applied at all layers. You need to implement security monitoring to act and respond to any event. The following significant components show where monitoring needs to be applied:
Network security: Monitor any unauthorized port opening, suspicious IP address, and activity. User access: Monitor any unauthorized user access and suspicious user activity. Application security: Monitor any malware or virus attack. Web security: Monitor a distributed denial-of-service (DDoS) attack, SQL injection, or cross-site scripting (XSS). Server security: Monitor any gap in security patches. Compliance: Monitor any compliance lapses such as violations of payment card industry (PCI) compliance checks for payment applications or the Health Insurance Portability and Accountability Act (HIPAA) for healthcare applications. Data security: Monitor unauthorized data access, data masking, and data encryption at rest and in transit.
For monitoring, you can use various third-party tools such as Imperva, McAfee, Qualys, Palo Alto Networks, Sophos, Splunk, Sumo Logic, Symantec, Turbot, and so on.
While you are putting application monitoring tools in place to monitor all components of your system, it is essential to monitor the monitoring system. Make sure to monitor the host of your monitoring system. For example, if you're hosting your monitoring tool in Amazon Elastic Compute Cloud (EC2), then AWS CloudWatch can monitor the health of EC2.

Handling alerts and incident response
Monitoring is one part of operational excellence functioning; the other part involves handing alerts and acting upon them. Using alerts, you can define the system threshold and when you want to work. For example, if the server CPU utilization reaches 70% for 5 minutes, then the monitoring tool records high server utilization and sends an alert to the operations team to take action to bring down CPU utilization before a system crash. Responding to this incident, the operations team can add the server manually. When automation is in place, autoscaling triggers the alert to add more servers as per demand. It also sends a notification to the operations team, which can be addressed later.

[ 295 ]

Operational Excellence Considerations

Chapter 10

Often, you need to define the alert category, and the operations team prepares for the response as per the alert severity. The following levels of severity provide an example of how to categorize alert priority:
Severity 1: Sev1 is a critical priority issue. A Sev1 issue should only be raised when there is a significant customer impact, for which immediate human intervention is needed. A Sev1 alert could be that the entire application is down. The typical team needs to respond to these kinds of alerts within 15 minutes and requires 24/7 support to fix the issue.
Severity 2: Sev2 is a high-priority alert that should be addressed in business hours. For example, the application is up, but the rating and review system is not working for a specific product category. The typical team needs to respond to these kinds of alerts within 24 hours and requires regular office hours' support to fix the issue.
Severity 3: Sev3 is a medium-priority alert that can be addressed during business hours over days--for example, the server disk is going to fill up in 2 days. The typical team needs to respond to these kinds of alerts within 72 hours and requires regular office hours' support to fix the issue.
Severity 4: Sev4 is a low-priority alert that can be addressed during business hours over the week-- for example, Secure Sockets Layer (SSL) certification is going to expire in 2 weeks. The typical team needs to respond to these kinds of alerts within the week and requires regular office hours' support to fix the issue.
Severity 5: Sev5 falls into the notification category, where no escalation needed, and it can be simple information--for example, sending a notification that deployment is complete. Here, no response is required in return since it is only for information purposes.
Each organization can have different alert severity levels as per their application needs. Some organizations may want to set four levels for severity, and others may go for six. Also, alert response times may differ. Maybe some organization wants to address Sev2 alerts within 6 hours on a 24/7 basis, rather than waiting for them to be addressed during office hours.

[ 296 ]

Operational Excellence Considerations

Chapter 10

While setting up an alert, make sure the title and summary are descriptive and concise. Often, an alert is sent to a mobile (as an SMS) or a pager (as a message) and needs to be short and informative enough to take immediate action. Make sure to include proper metrics data in the message body. In the message body, include information such as The disk is 90% full in production-web-1 server rather than just saying The disk is full. The following screenshot shows an example alarm dashboard:

Alarm dashboard
As shown in the preceding alarm dashboard, there is one alarm in progress where my billing charges went above 1,000 USD. The bottom three alarms have an OK status as data is collected during monitoring that is well within the threshold. Four alarms are showing Insufficient data, which means there are not enough data points to determine the state of resources you are monitoring. You should only consider this alarm good if it can collect data and move into the OK state.
Testing of incident response in the case of critical alerts is important to make sure you are ready to respond as per the defined SLA. Make sure your threshold is set up correctly so that you have enough room to address the issue, and, also, don't send too many alerts. Make sure that as soon as the issue resolved, your alert gets reset to the original setting and is ready to capture event data again.
[ 297 ]

Operational Excellence Considerations

Chapter 10

An incident is any unplanned disruption that impacts the system and customer negatively. The first response during an incident is to recover the system and restore the customer experience. Fixing the issue can be addressed later as the system gets restored and starts functioning. The automated alert helps to discover the incident actively and minimizes user impact. This can act as a failover to a disaster recovery site if the entire system is down, and the primary system can be fixed and restored later. For example, Netflix uses the Simian Army (https://netflixtechblog.com/t he-n etflix-s imian-a rmy-16e57fbab116), which has Chaos Monkey to test system reliability. Chaos Monkey orchestrates random termination of a production server to test if the system can respond to disaster events without any impact on end users. Similarly, Netflix has other monkeys to test various dimensions of system architecture, such as Security Monkey, Latency Monkey, and even Chaos Gorilla, which can simulate outage of the entire availability zone.
Monitoring and alerts are critical components to achieving operational excellence. All monitoring systems typically have an alert feature integrated with them. A fully automated alert and monitoring system improves the operations team's ability to maintain the health of the system, provide expertise to take quick action, and excel in the user experience.

Improving operational excellence
Continuous improvement is required for any process, product, or application to excel. Operational excellence needs continuous improvement to attain maturity over time. You should keep implementing small incremental changes as you perform RCA and learn a lesson from various operations' activities.
Learning from failure will help you to anticipate any operational event that may be planned (such as deployments) or unplanned (such as utilization surge). You should record all lessons learned and update remedies in your operation runbook. For operational improvement, the following are the areas where you need appropriate tools:
IT Operation Analytics (ITOA) Root cause analysis (RCA) Auditing and reporting

[ 298 ]

Operational Excellence Considerations

Chapter 10

ITOA
ITOA is the practice of gathering data from various resources to make a decision and predict any potential issue that you may encounter. It's essential to analyze all events and operational activities in order to improve. Analyzing failures will help to predict any future event and keep the team ready to provide the appropriate response. Implement a mechanism to collect the logs of operations events, various activities across workloads, and infrastructure changes. You should create a detailed activity trail and maintain an activity history for audit purposes.
A large organization could have hundreds of systems generating a massive amount of data. You need a mechanism to ingest and store all logs and event data for a length of time, such as 90 or 180 days, to get insight. ITOA uses big data architecture to store and analyze multiple terabytes of data from all over the place. ITOA helps to discover any issue that you could not find by looking at individual tools and helps to determine dependencies between various systems, providing a holistic view.
As shown in the following diagram, each system has its own monitoring tool that helps to get insights and maintains individual system components. For operation analytics, you need to ingest this data in a centralized place. All operation data collection in one place gives a single source of truth, where you can query required data and run analytics to get a meaningful insight:

Big data approach for ITOA
[ 299 ]

Operational Excellence Considerations

Chapter 10

To create an operation analytics system, you can use scalable big data storage such as Amazon Simple Storage Service (S3). You can also store data in an on-premises Hadoop cluster. For data extraction, the agent can be installed in each server, which can send all monitoring data to a centralized storage system. You can use the Amazon CloudWatch agent to collect data from each server and store it in S3. Third-party tools such as ExtraHop and Splunk can help to extract data from various systems.
Once data is collected in centralized storage, you can perform a transformation to make data ready for search and analysis. Data transformation and cleaning can be achieved using a big data application such as Spark, MapReduce, AWS Glue, and so on. To visualize the data, you can use any business intelligence tool such as Tableau, MicroStrategy, Amazon QuickSight, and so on. Here, we are talking to about building an extract, transform, and load (ETL) pipeline. You will learn more details in Chapter 13, Data Engineering and Machine Learning. You can further perform machine learning to do predictive analysis on a future event.

RCA
For continuous improvement, it is essential to prevent any error happening again. If you can identify problems correctly, then an efficient solution can be developed and applied. It's important to get to the root cause of the problem to fix the problem. Five whys is a simple, yet most effective, technique to identify the root cause of a problem.
In the five whys technique, you gather the team for a retrospective look at an event and ask five consecutive questions to identify actual issues. Take an example where data is not showing up in your application monitoring dashboard. You will ask five whys to get to the root cause.
Problem: Application dashboard not showing any data.
1. Why: Because the application is unable to connect with the database. 2. Why: Because the application is getting a database connectivity error. 3. Why: Because the network firewall is not configured to the database port. 4. Why: Because the configuring port is a manual check and infrastructure team
missed that. 5. Why: Because the team don't have the skills and tools for automation.

[ 300 ]

Operational Excellence Considerations

Chapter 10

Root Cause: Manual configuration error during infrastructure creation.
Solution: Implement a tool for automated infrastructure creation.
In the preceding example, a first-instance issue looks like it is related to the application. After the five whys analysis, it turns out to be a bigger problem and there is a need to introduce automation to prevent similar incidents. RCA helps the team to document lessons learned and continuously build upon it for operational excellence. Make sure to update and maintain your runbook-like code and share best practices across the team.

Auditing and reporting
An audit is one of the essential activities to create recommendations and identify any malicious activity in the system by internal or external interference. An audit becomes especially important if your application needs to be compliant as per regulatory body requirements--for example, PCI, HIPPA, Federal Risk and Authorization Management Program (FedRAMP), International Organization for Standardization (ISO), and so on. Most of the compliant regulatory bodies need to conduct regular audits and verify each activity going into the system to prepare a compliance report and grant a certificate.
An audit is essential to prevent and detect security events. A hacker may silently get into your system and systematically steal information without anyone noticing. Regular security audits can uncover a hidden threat. You may want to conduct a regular audit for cost optimization to identify if resources are running idle when not required. Also, determine resource demand and available capacity so that you can plan.
In addition to alert and monitoring, the operations team is also responsible for saving the system from any threat by enabling and conducting the audit. An IT audit makes sure you safeguard IT assets and license protection and that you ensure data integrity and operations adequately to achieve your organizational goal.
Auditing steps include planning, preparing, evaluation, and reporting. Any risk item needs to be highlighted in the report, and follow-ups will be conducted to address open issues. For operational excellence, the team can perform internal audit checks to make sure all systems are healthy and that proper alerts are in place to detect any incidents.

[ 301 ]

Operational Excellence Considerations

Chapter 10

Achieving operational excellence in the
public cloud
A public cloud provider such as AWS, GCP, and Azure provides many inbuilt capabilities and guidance to achieve operational excellence in the cloud. Cloud providers advocate automation, which is one of the most essential factors for operational excellence. Taking the example of the AWS cloud, the following services can help to achieve operational excellence:
Planning: Operational excellence planning includes identification of gaps and recommendation, automating via scripting, and managing your fleet of servers for patching and updates. The following AWS services help you in the planning phase:
AWS Trusted Advisor: AWS Trusted Advisor checks your workload based on prebuilt best practice and provides recommendations to implement them.
AWS CloudFormation: With AWS CloudFormation, the entire workload can be viewed as code, including applications, infrastructure, policy, governance, and operations.
AWS Systems Manager: AWS Systems Manager provides the ability to manage cloud servers in bulk for patching, update, and overall maintenance.
Functioning: Once you have created operational excellence best practice and applied automation, you need continuous monitoring of your system to be able to respond to an event. The following AWS services help you in system monitoring, alerts, and automated response:
Amazon CloudWatch: CloudWatch provides hundreds of inbuilt metrics to monitor workload operation and trigger alerts as per the defined threshold. It provides a central log management system and triggers an automated incident response.
AWS Lambda: The AWS service used to automate responses to operational events is AWS Lambda.

[ 302 ]

Operational Excellence Considerations

Chapter 10

Improving: As incidents come into your system, you need to identify their pattern and root cause for continuous improvement. You should apply the best practice to maintain the version of your scripts. The following AWS services will help you to identify and apply system improvements:
Amazon Elasticsearch: Elasticsearch helps to learn from experience. Use Elasticsearch to analyze log data to gain insight and use analytics to learn from experience.
AWS CodeCommit: Share learning with libraries, scripts, and documentation by maintaining them in the central repository as a code.

AWS provides various capabilities to run your workload and operations as code. These capabilities help you to automate operations and incident response. With AWS, you can easily replace failed components with a good version and analyze the failed resources without impacting the production environment.
On AWS, aggregate the logs of all system operation and workload activities, and infrastructure, to create an activity history, such as AWS CloudTrail. You can use AWS tools to query and analyze operations over time and identify a gap for improvement. In the cloud, resource discovery is easy, as all assets are located under the API- and web-based interfaces within the same hierarchy. You can also monitor your on-premises workload from the cloud.
Operational excellence is a continuous effort. Every operational failure should be analyzed to improve the operations of your application. By understanding the needs of your application load, documenting regular activities as a runbook, and following steps to guide issue handling, using automation, and creating awareness, your operations will be ready to deal with any failure event.

Summary
Operational excellence can be achieved by working on continuous improvement as per operational needs, and lessons learned from past events using RCA. You can achieve business success by increasing the excellence of your operations. Build and operate applications that increase efficiency while building highly responsive deployments. Use best practices to make your workloads operationally excellent.

[ 303 ]

Operational Excellence Considerations

Chapter 10

In this chapter, you learned about the design principles to achieve operational excellence. These principles advocate operation automation, continuous improvement, taking an incremental approach, predicting failure, and being ready to respond. You learned about various phases of operational excellence and corresponding to technology choices. In the planning phase, you learned about IT asset management to track the inventory of IT resources and identify dependencies between them using configuration management.
You learned about alerts and monitoring in the functioning phase of operational excellence. You got an idea about various kinds of monitoring, with examples such as infrastructure, application, log, security, and platform monitoring. You learned about the importance of alerts, and how to define alert severity and respond to it.
During the improvement phase of operational excellence, you learned about analytics in IT operations by building a big data pipeline, methods to perform RCA using the five whys, and the importance of auditing to save the system from any malicious behaviors and unnoticed threats. You learned about operational excellence in the cloud and different inbuilt tools that can be utilized for operational excellence in the AWS cloud.
As of now, you have learned best practices in the areas of performance, security, reliability, and operational excellence. In the next chapter, you will learn about best practices for cost optimization. You will also learn about various tools and techniques to optimize overall system costs and how to leverage multiple tools in the cloud to manage IT expenditure.

[ 304 ]

11
Cost Considerations
One of the primary goals of any business is to increase profitability while serving its customers. Cost is the key parameter of discussion when a project is initiated. Having an application upgrade and adding new product features heavily depends upon the amount of funding it can get. The product's cost is everyone's responsibility and needs to be considered in every phase of the product life cycle (from planning to post-production). This chapter will help you understand the best practices for optimizing costs for your IT solutions and operations.
Cost optimization is a continuous process and needs to be managed carefully without sacrificing customer experience. Cost optimization doesn't mean cost reduction but rather reducing the business risk by maximizing return on investment (ROI). You will need to understand your customer needs before planning any cost optimization and act accordingly. Often, if customers are looking for quality, they are ready to pay a higher price.
In this chapter, you will learn various design principles for the cost optimization of your solution. The cost aspect needs to be considered at every phase and component of the architecture. You will get an understanding of the right selection of technology to ensure cost optimization at every layer. You will learn the following best practices of cost optimization in this chapter:
Design principles for cost optimization Techniques for cost optimization Cost optimization in the public cloud
By the end of the chapter, you will have learned about various techniques to optimize cost without risking business agility and outcome. You will have learned various methods to monitor the cost and apply governance for cost control.

Cost Considerations

Chapter 11

Design principles for cost optimization
Cost optimization includes the ability to increase business value and minimize risk while reducing the cost of running a business. You need to plan by estimating budget and forecasting expenditure. To realize cost gain, you need to implement a cost-saving plan and closely monitor your expenditure.
You can follow several principles that help you achieve cost optimization. The following sections talk about the common design principles that help you to optimize cost. You will find that all cost optimization design principles are closely related and complement each other.

Calculating the total cost of ownership
Often, organizations tend to overlook the total cost of ownership (TCO) and take decisions based on the upfront cost to acquire software and services, known as capital expenditure (CapEx). While the upfront cost determination is essential, in the long run, the TCO matters the most. The TCO includes both CapEx and operational expenditure (OpEx), covering all the dimensions of the application life cycle. The CapEx cost includes the price organizations pay upfront to acquire services and software, while OpEx includes the cost of operation, maintenance, training, and retirement of software application. You should consider all associated costs to help to make more strategic decisions while calculating your ROI in the long run.
For example, when you buy a refrigerator, which is going to run 24/7, you look for an energy-saving rating to keep your electricity bill low. You are ready to pay a higher price upfront as you know the total cost over time will be low due to the saving in the energy bill.
Now let's take an example of a data center. There is an upfront hardware acquisition cost involved, the CapEx. However, the data center setup requires additional ongoing costs, the OpEx, which includes heating, cooling, rack maintenance, infrastructure administration, security, and so on.
For a typical use case, when you are purchasing and implementing software, consider the following costs to calculate the TCO:

[ 306 ]

Cost Considerations

Chapter 11

TCO for software
Let's look at this at a more granular level. Each TCO component has the following common costs involved for off-the-shelf software such as Oracle or MS SQL database:
Purchase and setup costs: These are the upfront cost to acquiring the software and the services to deploy software. This includes the following:
Software price includes software with user licenses Hardware cost includes purchasing a server and storage to deploy software Implantation cost includes the time and effort to get it ready for production Migration cost includes moving data to the new system
Operational and maintenance costs: This continues the cost of service to keep the software running for the business use case. This cost includes the following:
Software maintenance and support Patching and update Enhancement Data center cost to maintain hardware server Security
Human resources and training costs: This is the overhead cost to train staff so that they can use the software to address business activities. This cost includes the following:
Application admin staff IT support staff Functional and technical consultant Training cost and training tools
[ 307 ]

Cost Considerations

Chapter 11

When looking for a solution, you will have multiple choices (such as taking out a subscription for a software as a service (SaaS) product such as Salesforce CRM). The SaaS model is mostly subscription-based, so you need to determine whether you are getting the desired ROI for a more significant number of uses. You can take a hybrid approach and use the cloud to handle your hardware by choosing the Infrastructure as a Service (IaaS) option and installing off-the-shelf software. Overall, if the available software doesn't meet your requirements, you can choose to build it by yourself. In any scenario, you should calculate the TCO to make a decision where you can make the maximum ROI. Let's look at budget and forecast planning, which can help to control TCO and achieve ROI.

Planning the budget and forecast
Every business needs to plan its expenditure and calculate ROI. Planning the budget gives guidance to organizations and teams on cost control. Organizations plan a long-term budget, for 1-5 years, which helps them to run the business based on the funding required. These budgets then come down to the individual project and application levels. During solution design and development, the team needs to consider the available budget and plan accordingly. The budget helps to quantify what the business wants to achieve. The forecast provides an estimate of what the company is making.

You can consider budget planning as important strategic planning in the long run, and the forecast provides an estimate at a more tactical level to decide the business direction. In application development and operation, you can quickly lose track of the budget and overrun costs in the absence of a budget and a forecast. These two terms may be confusing, so let's understand the clear difference between a budget and a forecast:

Budget
Represents future result and cash flow for business objectives that you want to achieve
Plans for the long term, for example 1-5 years
Is adjusted less frequently, maybe once in a year, based on business drivers
Helps to decide business directions such as organization restructuring based on actual cost versus budgeted cost
Helps to determine performance by comparing planned cost versus actual cost

Forecast
Represents revenue and current situation of the business
Plans month to month or quarterly Is updated more regularly based on actual business progress Helps to adjust short-term operational costs such as additional staffing Isn't used for performance variation but for streamlining progress

Forecast information helps you to take immediate action, while the budget may become unachievable due to changes in the market. As shown in the following diagram, while you are working on day-to-day solutions, developments based on historic expenditure forecasts can prompt you to adjust the next month's cost:

[ 308 ]

Cost Considerations

Chapter 11

Billing and forecast report
In the preceding billing and forecast report, your monthly budget is $3,000 and the forecast is showing that, by the end of the month, you will overrun your budget. Here, the forecast helps you act and control cost to stay within budget. Let's look at the mechanism to improve cost-efficiency by managing demand and service in the next section.
Managing demand and service catalogs
Almost every organization has a centralized IT team, which works with internal business partners such as the application development team and support team of various business units. The IT team manages the demand for IT infrastructure, which includes the cost of all software, hardware, and support to manage application hosting. Often, business partners lack understanding of the cost drivers for the IT services that they use. For example, application development tends to overprovision their development or test environment, causing an additional cost.
Other factors that get the right sizing and demand forecasting from various organization units can help to match supply and demand. By consolidating all requirements in one place, an organization can benefit from economies of scale. You may achieve a lower variable cost because a large contract can achieve higher economies of scale. The right demand from all organization units is aggregated, which translates into lower prices.
[ 309 ]

Cost Considerations

Chapter 11

Organizations can take one of the following two approaches to manage demand and service:
Demand management: To save costs in your existing IT environments (where you may observe overspending may be prevalent), you can take the demand-led approach. It helps to improve cost efficiency in the short term, as you are not introducing many new services. You can analyze historical data to understand factors that are driving demand and capture cases of overprovisioning. You should establish a process between the IT team and business partners to streamline operational costs for IT services.
Service catalog management: If there is a demand for new services and you don't have much historical data, then you can take the service-led approach. In this approach, you need to understand the demand for the most frequently used services and create a catalog for that. For example, if the development team is asking for a Linux server with a MySQL database to create a dev environment, the IT team can create a service catalog which helps the dev team to acquire a small instance of Linux and a database server. Similarly, the IT team can identify the most common set of services and attach a granular cost to that.
Each approach can have a significant cost saving in the short and long term. However, these transformations present significant challenges as you need to change the project planning and approval process. The business and finance team need to align and understand the clear relationship between business growth and an increase in IT capacity. The cost model needs to be built around the most efficient approach by combining offerings from the cloud, on-premises, and off-the-shelf.

Keeping track of expenditure
By tracking expenditure, you can find individual system costs and tag them to the system or business owner. Transparent expenditure data helps to identify ROI and reward owners, those able to optimize resources and reduce cost. It can help you to determine what it is costing every month for a department or project.
Saving cost is a shared responsibility and you need to have a mechanism to hold everyone accountable for cost-saving. Often, organizations introduce a show-back or charge-back mechanism to share cost responsibility between organizational units.

[ 310 ]

Cost Considerations

Chapter 11

In the show-back approach, the centralized billing account informs each organization unit regarding their expenditure but doesn't charge the actual amount. In the charge-back mechanism, each business unit within an organization manages its own budget under a master payee account. The master account charges back the amount to the business units as per their IT resource consumption on a monthly basis.
When you are starting cost control for your organization, it is better to start with show-back as a stepping stone and move to charge-back as the organizational model matures. For each business unit, you should create expenditure awareness by configuring notifications, so that teams get an alert as they approach the forecasted or budgeted amount of consumption. You should create a mechanism to monitor and control your cost by appropriately assigning them to the right business initiative. Provide visibility to create accountability for cost expenditures for each team. Cost tracking will help you to understand team operations.
Each workload is different; you should use the pricing model that suits your workload to minimize cost. Establish mechanisms that ensure business objectives are achieved by applying cost optimization best practice. You can avoid overspending by defining a tagging strategy and applying the check-and-balance approach.

Continuous cost optimization
If you follow cost optimization best practices, you should have a good cost comparison with existing activity. It's always possible to reduce the cost of your applications that are migrated and matured over time. Cost optimizations should never end until the cost of identifying money-saving opportunities is more than the amount of money you are going to save. Until that point is reached, you should continually monitor your expenditure and look for new ways to save on cost. You should keep finding an area to save costs by removing idle resources.
For an architecture that is balanced in terms of its cost and performance, ensure that the cost paid for resources is well utilized and avoids any significantly underutilized IT resources such as server instances. A biased utilization metric showing exceptionally high or low cost will have an adverse impact on your organization's business.

[ 311 ]

Cost Considerations

Chapter 11

Application-level metrics for cost optimization need to be considered carefully. For example, introduce archival policies to control data storage capacity. To optimize the database, you should check for appropriate database deployment needs, such as if multilocation deployments for the database are really necessary or whether provisioned Input/Output Operations Per Second (IOPS) are applicable as per your database utilization needs. To reduce your administrative and operational overhead, you can use the SaaS model; it will help your employees to focus on applications and business activities.
To identify a gap and apply necessary changes for cost-saving, you should implement resource management and change control processes during the project life cycle. Your goal is to help your organization design the architecture as optimally and cost-effectively as possible. Keep looking for new services and features that might directly reduce your costs.

Techniques for cost optimization
To gain a competitive edge and keep up with rapid growth, enterprises are investing more in technology. With economic instability, cost optimization becomes an essential but challenging task. These companies spend a lot of time and research to reduce costs in the procurement process, operation, and vendors. Many companies even share data centers, call centers, and workspaces as a cost-saving method. Sometimes organizations delay upgrades to avoid buying new expensive hardware.
The organization can save more if it takes a broader look into the overall information technology architecture across its business units. Improving existing architecture can open doors to bring more opportunities and business to the company even if it requires a bit more adjustment in the budget. Let's identify the focus area where companies can save cost and gain opportunities to bring more revenue with techniques such as moving to the cloud, simplified architecture, virtualization, and shared resources.
Reducing architectural complexity
Organizations often lack a centralized IT architecture, resulting in each business unit trying to build its own set of tools. Lack of overall control causes a lot of duplicate systems and data inconsistency. IT initiatives in individual business units are driven by a short-term goal and are not well aligned with long-term organizational vision such as the digital transformation of the entire organization. Further, it adds complexity to maintain and upgrade those systems. Taking a simple step to define set standards and avoid duplication can help to save costs.

[ 312 ]

Cost Considerations

Chapter 11

In the following diagram, you can see a complex architecture on the left-hand side, where business units are working in their own application without any standardization, which is causing duplicate applications with a lot of dependencies. This kind of architecture results in higher cost and risk. Any new experiment takes a long time to market, which results in losing the competitive edge. A standard process can provide a holistic view and high flexibility to create an agile environment by applying automation, which helps to reduce the overall cost and results in a more significant ROI:

Architectural standardization
To reduce the architectural complexity, the first thing is to eliminate duplication and identify the function reuse across the business unit. During gap analysis of existing architecture, you will find there is so much code, so many existing components, and a project that can be reused again across the organization to support your business requirement. To reduce the complexity of IT architecture, think of an out-of-the-box solution that fits your business needs and provides an ROI. Customization should be your last approach if no other option is available.
Any new application needs to have a more accessible integration mechanism to interact with the existing system using service-oriented architecture (SOA). Harmonizing the user interface design across the application provides a set of standard UI packages, which can be reused for any new application. Similarly, other modules can be reutilized with serviceoriented design. You learned about SOA patterns in Chapter 6, Solution Architecture Design Patterns, which help you keep all the different pieces of software working separately and still communicating with each other to build a full system.
[ 313 ]

Cost Considerations

Chapter 11

In the modular approach, each team gets the responsibility of developing a service, which every team across the organization can use to avoid duplication. As an architect, you should help the team to create a service-oriented design, where each team handles individual architecture components as a service that can be developed independently. With the help of microservices architecture, you can deploy an entire application in a modular way, and if one component is not working, you can rework it without impacting the whole application. For example, a payment service developed to collect payment from a customer visiting an e-commerce website can be used to make payments to vendors in the vendor management system.
Once you set up a centralized IT architecture, taking a modular approach helps you to keep the cost down. Empowering your IT architecture team can help to align organizational units with the company's vision and support other parallel projects to follow the overall strategy. It also helps to provide consistency in other critical services that are often overlooked, such as legal, accounting, and human resources.
With the help of the IT architecture team, you can get excellent feedback and make sure that projects are aligned with business needs and requirements. By overseeing the overall architecture across teams, an architect can advise if whether there is any duplicate effort, project, process, or system that is not aligned with the business need. The centralized architecture will reduce complexity and tech debt, bring more stability, and increase quality. The overall idea of centralized architecture is to increase IT efficiency, so let's learn more about that.

Increasing IT efficiency
Nowadays, every company is using and consuming IT resources. There is too much cost used by too many servers, laptops, storage capacity, and the software license. The license is one of the resources that is sometimes underused, undiscovered, idle, or installed incorrectly, and consumes a lot of funding. A centralized IT team can lead the effort for license optimization by keeping track of used software licenses and retiring additional licenses. They can save costs by negotiating a bulk discount with the vendor.
To increase IT efficiency, you may want to cancel non-compliant projects that take additional funding and resources. Also, you should help teams to revisit the strategy to continuous support or terminate any unused and non-aligned projects. The following methods can be considered for cost optimization:
Reevaluate project having high spending but may not be well aligned with the business vision. Reshape projects have high values but not direct reports to IT strategy.
[ 314 ]

Cost Considerations

Chapter 11

De-prioritize projects that have little to no business value even though they are aligned with IT strategy. Cancel non-compliant projects with low business values. Decommission or retire unused applications. Replace old legacy systems by modernizing them to reduce high maintenance costs. Avoid duplicate projects by reutilizing existing applications. Wherever possible, consolidate data and develop the integrated data model. You will learn about maintaining a centralized data lake in Chapter 13, Data Engineering and Machine Learning. Consolidate vendor procurement across the organization to save cost on IT support and maintenance expenditure. Consolidate any system that does the same thing as payment and access management. Eliminate costly, wasteful, overprovisioned projects and expenditure.
Moving to the cloud can be an excellent consideration to increase IT resources efficiently and reduce costs. The public cloud, such as AWS, offers a pay-as-you-go model that helps you to only pay for what you are using. For example, the developer desktop can shut down during non-working hours and weekends, which can reduce workspace costs by up to 70%. The batch processing system needs to be brought up only to process jobs and can be shut down immediately afterward. It works just like you switch off any electrical appliances when not required to save electricity costs.
Applying automation is a great mechanism to increase overall IT efficiency. Automation not only helps to eliminate costly human labor but reduces the time spent performing daily routine jobs without error. Automate things wherever possible, for example, by provisioning resources, running monitoring jobs, and processing data.
Make sure to do the right trade-off to improve results while deciding to optimize costs. Let's take an example. If you are going to a theme park where you want to go on lots of good rides, then you are willing to pay a higher price as you can see the value of the money you are spending. To attract more customers, if the vendor decided to reduce the price and make adjustments by lowering the number of enjoyable rides, there is a chance that you will go to another theme park as you are looking for a good time. Here, competitors will gain an edge and attract existing customers, while the current vendor will lose business. In this case, cost reduction is adding business risk, which is not the right cost-optimization approach.

[ 315 ]

Cost Considerations

Chapter 11

Your goal should be measurable, and these measures should focus on both business output and the cost of your system. The quantitative measure helps you understand the impact of increasing output and reducing the cost. The organizational and team-level goals must align with the end users of the application. At an organizational level, the goals will be across organizational business units. At the team level, they will be more aligned with individual systems. You can set up a goal, for example, to reduce the cost per transaction or output of order by 10% every quarter or 15% every 6 months. Defining the goal ensures that systems improve over their lifetime.

Applying standardization and governance
Organizations need a strategy to analyze misalignment and overconsumption, reduce complexity, and define guidelines to use appropriate and efficient systems and implement a process wherever it is required. Creating and implementing these guidelines will help companies to develop a standard infrastructure and reduce duplicate projects and complexity.
To implement governance, you need to set up resource limits across the organization. Putting the service catalog in place with infrastructure as code helps to ensure that teams are not overprovisioned with resources beyond their allocated capacity. You should have a mechanism to understand and take action on business requirements quickly. Take both resource creation and decommission into account when applying resource limits and defining the process to change them.
Businesses operate multiple applications by various teams. Those teams can belong to different business units, within their revenue stream. The capability to determine resource costs to the application and business unit or team drives efficient usage behavior and helps reduce cost. You can define resource capacity based on cost attribution and the requirements of the group, organization unit, or department. To organize cost structure, you can use resource tagging along with account structuring.
As shown in the following screenshot, you can organize your accounts in different organization units (OUs), such as HR and Finance, and each department under the OU can have its own account. For example, here, HR has separate accounts for Payroll and Marketing, while Finance has separate accounts for Sales and Marketing:

[ 316 ]

Cost Considerations

Chapter 11

Enterprise account structure for organizational units
In the preceding account structuring strategy, you can control costs at each business unit and department level. Adopting a charge-back mechanism for each department increases accountability for cost at a more granular level, which helps to optimize cost. Account structuring helps you to apply high security and compliance standards across the organization. As each account is linked to a parent account, you can get a great deal on the mass utilization of resources from vendors by consolidating expenditure across the organization. As shown in the following screenshot, to get full cost visibility and consolidation across resources, you can tag each resource provisioned at the team level, which provides more granular control:
Resource tagging for cost visibility
[ 317 ]

Cost Considerations

Chapter 11

In the preceding diagram, you can see tagging strategy, which indicates that the given server is for application deployment and is utilized by the development team. This given server is owned by the marketing department of the finance business unit. In this way, the organization can get a granular level of cost expenditure visibility, and the team will be more frugal in their spending. However, you may want to adopt the show-back mechanism at the team level compared to the charge-back mechanism at the department and business unit level.
You can define your mechanism for tagging, where you can attach a name and value, such as resource name and owner name, to any resource. Almost every public cloud provider gives tagging capabilities out of the box. For on-premise, you can embed server metadata such as DNS name or hostname. Tagging not only helps you to organize costs but also to define a capacity limit, security, and compliance. It can be an excellent tool for inventory management and to keep an eye on the growing need for resources at every level of the organization.
Business leaders should evaluate the overall requirement to create efficient IT architectures. It requires collaboration to develop robust IT architecture and define governance across functional teams to set up accountability. Also, set up a standard to review the architecture, create the baseline for any new project initiative, and explain the process that will make sure that the system complies with the correct architecture and identify the route to improvement.
Engage all impacted stakeholders within your business in usage and cost discussions. CFO and application owners must understand resource consumption and purchasing options. Department owners must understand the overall business model and the monthly billing process. It will help to set up the direction for the business units and the whole company.
Make sure third-party vendors are aligned to your financial goals and can adjust their engagement models. Vendors should provide a cost analysis of any application they own and develop. Each team within the organization should be able to translate business, cost, or usage factors from the management into system adjustments, which help the application to implement and achieve the desired goals of the company.

Monitoring cost usage and report
Accurate cost factors help you to determine the profitability of business units and products. Cost tracking helps you to allocate resources at the right place to increase ROI. Understanding cost drivers helps you to control your business expenditure.

[ 318 ]

Cost Considerations

Chapter 11

To optimize costs, you must know your expenditure pattern across the organization. You need to have visibility of IT cost expenditures over a period of time to determine costsaving opportunities. You can take the required steps for cost optimization and understand the impact by creating a visualization of cost trends, which shows historical cost and forecasts by resources and departments across the organization. Your team needs to gather data by logging all data points, analyze them with monitoring, and then create a visualization report.
To identify cost-saving opportunities, you need detailed insight into your workload resource utilization. Cost optimization depends upon your ability to forecast future spending and put methods in place to align cost and usage as per your forecast. The following are the primary areas where you want to have data visualization for cost-saving:
Determine the most significant investments in resources Analyze and understand your expenditure and usage data Budget and forecast Receive an alert when you exceed your budgeted or forecasted thresholds
The following report is showing resources expenditure over 6 months in AWS. Looking at the visualization, you can see that data warehousing service Amazon Redshift, represented by the purple bar, is consuming maximum costs with an increase in the trend until November. As the business unit can visualize the high cost in October, it prompts the system admin to take an in-depth look at cost optimizations, where they find overprovisioned resources. The admin performs cleanup by stopping additional server instances in November, which brings down the data warehousing service cost by 90%:

Resource cost and usage report
[ 319 ]

Cost Considerations

Chapter 11

The preceding report helped business owners to understand cost patterns and take a reactive approach to cost control. The reactive approach caused hidden costs, which went undetermined for a specified period. For the proactive approach, the forecast can help to make the decision ahead of time.
The following report shows daily cost expenditure in the filled blue bars and forecast spending in the empty blue bars. Looking at the report, you can see that it is likely that cost may increase in the next couple of weeks, and you can take action to understand cost attributes to control costs:

Cost trend and cost forecast report
Monitoring your costs against the budget can give you another proactive measure to control costs. Setting up an alert when expenditure reaches a certain threshold of the budget (for example, 50% or 80%) helps you to review and adjust your ongoing costs.
[ 320 ]

Cost Considerations

Chapter 11

In the following report, you can visually determine the current cost against budgeted cost, which reached 42% in the first week of the month. At this rate, your forecast is going over 182% of the budgeted cost and requires attention to adjust ongoing expenditure:

Cost and budget report
Cost and budget reports help you to control costs by taking proactive action. Combining your actual running costs with budgets and forecasts provides a great deal of cost control on a daily basis. You can also set up an alert when your actual cost reaches a certain threshold in the budget or forecast. It alerts you proactively via email or mobile message and tells you to take proactive action to control costs.
[ 321 ]

Cost Considerations

Chapter 11

In the following screenshot, you can see an alert has been set up for when the actual cost reaches 80% of the budget. You can set up multiple alerts to get information when the cost reaches 50% or 80% of the budget or forecast:

Alert against actual cost
One way to do cost control is by right-sizing your environment with resources monitoring, and trigger alarms for over- or underutilization. Analysis of resources can be performed using monitoring tools such as Splunk or CloudWatch and custom logs, where customized metrics such as application memory utilization of your system can be monitored to perform right-sizing. Low utilization of a resource could be a criterion for identifying opportunities for cost optimization. For example, CPU utilization, RAM utilization, network bandwidth, and the number of connections to the application can be analyzed and monitored.
[ 322 ]

Cost Considerations

Chapter 11

You need to be careful when resizing your environment to make sure you are not impacting customer experience. The following are best practices to apply when you perform right-sizing:
Make sure monitoring reflects the end user experience. Select the correct period. For example, performance metrics should cover 99% of the user's requestresponse time rather than taking an average response time. Select the correct monitoring cycle, such as every hour, day, or week. For example, if you are conducting daily analysis, you might miss a weekly or monthly cycle of high utilization and under provision your system. Assess the cost of change against the cost-saving. For example, you may have to perform additional testing or engage resources to perform resizing. This costbenefit analysis will help you to assign resources.
Measure application utilization against your business requirement, for example, how many user requests are expected to come by the end of the month or during peak season. Identifying and optimizing the utilization gap leads you to save costs. For this, use the right tool that covers all dimensions from cost-saving to system utilization and impact on customer experience due to changes. And then utilize reports to understand business ROI impact due to cost changes.

Cost optimization in the public cloud
The public cloud, such as AWS, Microsoft Azure, and Google Cloud Platform (GCP), provides a great deal of cost optimization with the pay-as-you-go model. The public cloud cost model allows customers to trade capital expenses for variable expenses, paying for IT resources as they consume them. Operational expenses are usually lower due to economies of scale. It could be cost-effective to be in the cloud and get the benefit of continued price reductions that occur over time. The other advantage is that you get additional tools and functionality out of the box with a cloud provider such as AWS, which helps you to achieve better agility.
You need a different mindset when defining the cloud cost structure model as it is pretty different from traditional cost, most of which most enterprises have been following for decades. In the cloud, you have all the infrastructure available at your fingertips, which requires greater control and regulation. Clouds provide several tools for cost governance and regularization. For example, in AWS, you can set up service limits per account, so the dev team cannot utilize more than 10 servers, and production can have the required number of servers and databases with a buffer.

[ 323 ]

Cost Considerations

Chapter 11

In the cloud, all resources are associated with accounts, so it's easy to keep track of IT resource inventories in a single place and monitor their utilization. In addition to that, you get tools that can collect data across various IT resources and provide suggestions. As shown in the following screenshot, AWS Trusted Advisor crawls through all resources in the account and offers cost-saving recommendations based on resource utilization:

Cost-saving suggestions from AWS Trusted Advisor
In the preceding screenshot, Trusted Advisor has detected continuous utilization of the application server (Elastic Cloud computing, EC2) and advises buying a reserve instance by paying 1 year upfront with a 40% cost saving. Further checks have identified an underutilized database (Amazon RDS) and suggest shutting it down to make a potential saving.
The cloud can provide an excellent value proposition for cost-saving. To begin with, you can create a hybrid cloud, where you establish connectivity between your on-premises data center and the cloud. You can move development and test servers to the cloud to determine cost structure and potential savings. Once you have set up cost governance in the cloud, move more workload as per the cost-benefit analysis. However, you need to assess your workload and whether it can be moved to the cloud and define a strategy. You learned about cloud migration in Chapter 5, Cloud Migration and Hybrid Cloud Architecture Design.
[ 324 ]

Cost Considerations

Chapter 11

Increasingly, public cloud providers are offering managed services, which eliminates any infrastructure maintenance cost and overheads for alert and monitoring configurations. A managed service reduces the total costs of ownership by reducing cost as service adoption increases.

Summary
Cost optimization is a continuous effort from application inception (proof-of-concept to its implementation and post-production). You need to continuously review architectures and cost-saving efforts.
In this chapter, you learned about design principles to optimize costs. Before making any purchase decision, you should consider the total cost of ownership for the entire life cycle of software or hardware. Planning a budget and keeping track of forecasts help you to stay on the cost optimization path. Always keep track of your expenditures and look for possible opportunities for cost optimization without affecting user experience or business value.
You learned about the various techniques for cost optimization, which include reducing architectural complexity by simplifying enterprise architecture and setting a standard that everyone can follow. We recommended avoiding duplication by identifying idle and repeated resources, and take consolidation effort to negotiate the cost of bulk purchase. Apply standardization across the organization to limit resource provision and develop a standard architecture. Tracking data for your actual costs against budgets and forecasts can help you to take proactive action. You learned about various reports and alerts that can help to control costs. You also learned about cost optimization in the cloud, which can help you further to optimize value.
Automation and agility are some major factors that increase resource efficiency, and DevOps can provide a great deal of automation. In the next chapter, you will learn about various DevOps components and DevOps strategies to efficiently deploy your workload in the most automated way.

[ 325 ]

12
DevOps and Solution
Architecture Framework
In traditional environments, the development team and the IT operations team work in silos. The development team gathers requirements from business owners and develops the applications. System administrators are solely responsible for operations and for meeting uptime requirements. These teams generally do not have any direct communications during the development life cycle and each team rarely understands the processes and requirements of the other team.
Each team has its own set of tools, processes, and approaches that are redundant, and sometimes, efforts are conflicting. For example, the development and quality assurance (QA) teams can be testing the build on a specific patch of the operating system (OS). However, the operations team deploys the same build on a different OS version in the production environment, causing issues and delays in the delivery.
DevOps is a methodology that promotes collaboration and coordination between developers and operational teams to deliver products or services continuously. This approach is constructive in organizations where the teams rely on multiple applications, tools, technologies, platforms, databases, devices, and so on in the process of developing or delivering a product or service.
Although there are different approaches to the DevOps culture, all are about achieving a common goal. DevOps is about delivering a product or service in the shortest amount of time by increasing operational efficiency through shared responsibilities. DevOps helps to make delivery without compromising on quality, reliability, stability, resilience, or security. In this chapter, you will learn the various following components of DevOps:
Introducing DevOps Understanding the benefits of DevOps Understanding the components of DevOps Introducing DevOps in security

DevOps and Solution Architecture Framework

Chapter 12

Combining DevSecOps and continuous integration/continuous delivery (CI/CD) Implementing a CD strategy Implementing continuous testing in the CI/CD pipeline Using DevOps tools for CI/CD Implementing DevOps best practices
By the end of this chapter, you will learn about the importance of DevOps in application deployment, testing, and security. You will learn DevOps best practices, and different tools and techniques to implement them.

Introducing DevOps
In a DevOps (short for development and operations) approach, both the development team and the operations team work collaboratively during the build and deployment phases of the software development life cycle, sharing responsibilities, and providing continuous feedback. The software builds are tested frequently throughout the build phase on production-like environments, which allows early detection of defects.
Sometimes, you will find a software application development and its operations are handled by a single team, where engineers work across the entire application life cycle, from development and deployment to operations. Such a team needs to develop a range of skills that are not limited to a single function. Application testing and security teams may also work more closely with the operations and development teams, from the inception to the production launch of an application.
Speed enables organizations to stay ahead in the competition and address customer requirements quickly. Good DevOps practices encourage software development engineers and operations professionals to work better together. This results in closer collaboration and communication, leading to a shorter time to market (TTM), reliable release, improved code quality, and better maintenance.
Developers benefit from feedback provided by the operations teams and create strategies for testing and deployment. System administrators don't have to implement defective or untested software on production environments because they participate in the build phase. As all stakeholders in the software development and delivery life cycle collaborate, they can also evaluate the tools that they intend to use at each step of the process, to verify compatibility between the devices and also to determine whether any tools can be shared across the teams.

[ 327 ]

DevOps and Solution Architecture Framework

Chapter 12

DevOps is a combination of culture and practices. It requires organizations to change their culture by breaking down the barriers between all teams in the product development and delivery life cycle. DevOps is not just about development and operations; rather, it involves the entire organization, including management, business/application owners, developers, QA engineers, release managers, the operations team, and system administrators. DevOps is gaining popularity as the preferred operating culture, especially for organizations that deal with cloud or distributed computing.

Understanding the benefits of DevOps
The goal of DevOps is a CD model that is repeatable, reliable, stable, resilient, and secure. These properties improve operational efficiency. To achieve this goal, teams must collaborate and get involved in the development and delivery process. All technical team members should have experience with the processes and tools involved in the development pipeline. A mature DevOps process provides benefits, as shown in the following diagram:

Benefits of DevOps
[ 328 ]

DevOps and Solution Architecture Framework

Chapter 12

These benefits of DevOps are detailed further here:
Speed: Releasing product features at a quick pace helps to accommodate changing business needs of your customers and expand your market. A DevOps model helps an organization to achieve results faster. Rapid delivery: DevOps processes facilitate more efficiency by automating endto-end pipelines, from code build to code deploy and production launch. Rapid delivery helps you to innovate faster. Faster release of bug fixes and features helps you to gain a competitive edge. Reliability: DevOps processes provide all checks to ensure delivery quality and safe application updates at a rapid pace. DevOps practices such as CI and CD embed automation testing and security checks for a positive end-user experience. Scale: DevOps helps to scale your infrastructure and application on an ondemand basis by including automation everywhere. Improved collaboration: The DevOps model builds a culture of ownership whereby the team takes account of their actions. The operations and dev teams work together in a shared responsibility model. Collaboration simplifies the process and increases efficiency. Security: In an agile environment, making frequent changes requires stringent security checks. The DevOps model automates security and compliance best practices, monitors them, and takes corrective action in an automated way.
DevOps removes barriers between the developer and operations teams that used to work in silos. The DevOps model optimizes the productivity of the development team and the reliability of system operations. As teams closely collaborate, this helps to increase efficiencies and improve quality. Teams take full ownership of the services they deliver, often beyond the traditional scope of their roles, and develop thinking from a customer point of view to solve any issue.

Understanding the components of DevOps
DevOps tools and automation bring together development and system operations. The following are critical components of a DevOps practice:
CI/CD Continuous monitoring and improvement Infrastructure as code (IaC) Configuration management (CM)
[ 329 ]

DevOps and Solution Architecture Framework

Chapter 12

A best practice across all the elements is automation. Automating processes allows you to efficiently perform these operations in a fast, reliable, and repeatable fashion. Automation can involve scripts, templates, and other tools. In a thriving DevOps environment, infrastructure is managed as code. Automation enables DevOps teams to set up and tune test and production environments rapidly. Let's explore more details about each component.

CI/CD
In CI, developers commit code frequently to a code repository. The code is built frequently. Each build is tested using automated unit tests and integration tests. In CD, code changes are committed to the repository and developed frequently. Builds are deployed to test environments and are tested using automated, and possibly manual, tests. Successful builds pass tests and are deployed to staging or production environments. The following diagram illustrates the impact of CI versus CD in the software development life cycle:

CI/CD
[ 330 ]

DevOps and Solution Architecture Framework

Chapter 12

As shown in the preceding diagram, CI refers to building and unit testing stages of the software development life cycle. Every update that is committed in the code repository creates an automated build and test. CD is an essential aspect of CI which extends CI process further to deploy build in production. In CI/CD practices, several people work on the code. They all must use the latest working build for their efforts. Code repositories maintain different versions of the code and also make the code accessible to the team. You check out the code from the repository, make your changes or write new code in your local copy, compile and test your code, and then frequently commit your code back to the repository.
CI automates most of the software release process. It creates an automated flow that builds, tests, and then stages the update. However, a developer must trigger the final deployment to a live production environment that is not automated. It expands upon CD by deploying all code changes to a testing environment and/or a production environment after the build stage. If CD is implemented correctly, developers will always have a tested and deployment-ready build.
The concepts in the following diagram illustrate everything related to the automation of an application, from code commits into a code repo, to the deployment pipeline. It shows an end-to-end flow, from build to the production environment where, developer check-in the code changes in code repository which is pulled by CI server. CI server trigger the build to create deployment package with new application binaries and corresponding dependencies. These new binaries are deployed in targeted development or testing environment. Also binaries get check-in into artifact repository for safe version controlled storage:

CI/CD for DevOps
[ 331 ]

DevOps and Solution Architecture Framework

Chapter 12

In CI/CD, software development life cycle phases such as code, build, deploy, and test are automated using the DevOps pipeline. The deploy and provision phase needs to be automated using IaC scripts. Monitoring can be automated with various monitoring tools.
A robust CD pipeline also automates the provisioning of infrastructure for testing and production environments and enables monitoring and management of test and production environments. CI/CD provides multiple benefits to the team, such as improving developer productivity by saving time on building, testing, and deployment of code. It helps the dev team to detect and fix bugs quickly and launch feature updates faster in the production environment.
CD does not mean that every change committed by the developer goes into production. Instead, it means that every change is ready to go into production. When the changes are staged and tested in the stage environment, a manual approval process initiates and gives a green signal to deploy to production. Thus, in CD, deploying to production becomes a business decision and is still automated with tools.

Continuous monitoring and improvement
Continuous monitoring helps to understand application and infrastructure performance impacts on the customer. By analyzing data and logs, you can learn how code changes impact users. Active monitoring is essential in the era of 24/7 services and constant updates to both applications and infrastructure. You can be more proactive about monitoring services by creating alerts and performing real-time analysis.
You can track various metrics to monitor and improve your DevOps practice. Examples of DevOps-related metrics are:
Change volume: This is the number of user stories developed, the number of lines of new code, and the number of bugs fixed. Deployment frequency: This indicates how often a team is deploying an application. This metric should generally remain stable or show an upward trend. Lead time from development to deployment: The time between the beginning of a development cycle to the end of deployment can be used to identify inefficiencies in the intermediate steps of the release cycle. Percentage of failed deployments: The percentage of failed deployments, including the number of deployments that resulted in outages, should be a low number. This metric should be reviewed in conjunction with the change volume. Analyze potential points of failure if the change volume is low but the number of failed deployments is high.
[ 332 ]

DevOps and Solution Architecture Framework

Chapter 12

Availability: Track how many releases caused failures that possibly resulted in violations of Service-Level Agreements (SLAs). What is the average downtime for the application? Customer complain volume: The number of complain tickets filed by customers is an indicator of the quality of your application. Percentage change in user volume: The number of new users signing up to use your application and the resulting increase in traffic can help you scale your infrastructure to match the workload.
After you deploy builds to the production environment, it is essential to monitor the performance of your application continuously. As we discussed about automating environment , so let explore more details on IaC.

IaC
Provisioning, managing, and even deprecating infrastructure is a costly activity in terms of human capital. Furthermore, repeated attempts to build and modify environments manually can be fraught with errors. Whether working from prior experience or a welldocumented runbook, the tendency for a human to make a mistake is a statistical probability.
We can automate the task of creating a complete environment. Task automation can help to effortlessly complete repetitive tasks and provide significant value. With IaC, we can define our infrastructure in the form of templates. A single template may consist of a part or the entirety of an environment. More importantly, this template can be used repeatedly to create the same identical environment time and again.
In IaC, infrastructure is spun up and managed using code and CI. An IaC model helps you to interact with infrastructure programmatically at scale and avoid human errors by allowing you to automate resource configuration. That way, you can work with infrastructure in the same way that you would with code by using code-based tools. As the infrastructure is managed through code, so the application can be deployed using a standardized method, and any patches and versions can be updated repetitively without any errors. Some of the most popular infrastructure as code scripting tools are Ansible, Terraform and AWS CloudFormation.

[ 333 ]

DevOps and Solution Architecture Framework

Chapter 12

Configuration management (CM)
CM is the process of using automation to standardize resource configurations across your entire infrastructure and applications. CM tools such as Chef, Puppet, and Ansible can help you manage IaC and automate most system administration tasks, including provisioning, configuring, and managing IT resources. By automating and standardizing resource configurations across the development, build, test, and deployment phases, you can ensure consistency and eliminate failures caused by misconfiguration.

CM can also increase the productivity of your operations by allowing you to automatically deploy the same configuration to hundreds of nodes at the push of a button. CM can also be leveraged to deploy changes to configurations.

Although you can use registry settings or databases to store system configuration settings, a configuration management application allows you to maintain version control as well, in addition to storage. CM is also a way to track and audit configuration changes. If necessary, you can even maintain multiple versions of configuration settings for various versions of your software.

CM tools include a controller machine that manages server nodes. For example, Chef requires a client agent application to be installed on each server that it needs to manage, and a master Chef application installs on the controller machine. Puppet also works the same way with a centralized server. However, Ansible has a decentralized approach and doesn't require the installation of agent software on the server nodes. The following table shows a high-level comparison between the popular configuration management tools:

Mechanism
Architecture Script Language Scripting Terminology Test Execution

Ansible

Puppet

Chef

Controller machine

applies changes to Master synchronizes

servers using

changes to Puppet node

Secure Shell (SSH)

Chef workstation looks for changes in Chef servers and pushes them to Chef node

Any server can be Centralized control by

the controller

Puppet master

Centralized control by Chef server

YAML

Domain-specific on Ruby Ruby

Playbook and roles Manifests and modules

Recipes and cookbooks

Sequential order Non-sequential order Sequential order

[ 334 ]

DevOps and Solution Architecture Framework

Chapter 12

CM tools provide their own domain-specific language and set of features for automation. Some of these tools have a learning curve whereby the team has to spend some time to learn the tool.
As security is becoming a priority for any organization, so bringing complete automation security is the need of the hour. To avoid human error, organizations are moving to tight security implementation and monitoring, using the DevOps process popularly known as DevSecOps. Let's explore more about DevSecOps (short for development, security and operations) in the next section.

Introducing DevSecOps
We are now more focused on security than ever. In many situations, security is the only way to win customer focus. DevSecOps is about the automation of security and implementation of security at scale. The development team is always making changes and the DevOps team is publishing them in production (changes are often customer-facing). DevSecOps is required to ensure application security in the overall process.
DevSecOps is not there to audit code or CI/CD artifacts. Organizations should implement DevSecOps to enable speed and agility, but not at the expense of validating security. The power of automation is to increase product-feature-launch agility while remaining secure by implementing the required security measures. A DevSecOps approach results in built-in security and is not applied as an afterthought. DevOps is about adding efficiency to speed up the product launch life cycle, while DevSecOps validates all building blocks without slowing the life cycle.
To institute a DevSecOps approach in your organization, start with a solid DevOps foundation across the development environment, as security is everyone's responsibility. To create collaboration between development and security teams, you should embed security in the architecture design from inception. To avoid any security gaps, automate continuous security testing and build it into the CI/CD pipeline. To keep track of any security breach, apply to extend monitoring to include security and compliance by monitoring for drift from the design state in real time. Monitoring should enable alerting, automated remediation, and removing non-compliant resources.
Codifying everything is a basic requirement that opens up infinite possibilities. The goal of DevSecOps is to keep the pace of innovation, which should meet the pace of security automation. A scalable infrastructure needs scalable security, so it requires automatic incident response remediation to implement continuous compliance and validation.

[ 335 ]

DevOps and Solution Architecture Framework

Chapter 12

Combining DevSecOps and CI/CD
A DevSecOps practice needs to be embedded with every step of the CI/CD pipeline. DevSecOps ensures the security of the CI/CD pipeline by managing the right access and roles assigned to each server and making sure the build servers such as Jenkins are hardened to be protected from any security glitch. In addition to that, we need to make sure that all artifacts are validated, and code analysis is in place. It's better to be ready for incident response by automating continuous compliance validation and incident response remediation.
The following screenshot provides us with multiple stages to test security boundaries and catch security issues and compliance with policies as early as possible:

DevSecOps and CI/CD
At each integration point, you can identify different issues, as illustrated in the preceding diagram:
In the coding phase, scan all code to make sure no secret key or access key is hardcoded in between code lines. During the build, include all security artifacts such as the encryption key and access token management, and tag them to identify them.
[ 336 ]

DevOps and Solution Architecture Framework

Chapter 12

During the test, scan the configuration to make sure all security standards are met by test security. In the deploy and provision phase, make sure all security components are registered. Perform a checksum to make sure there are no changes in the build files. Monitor all security standards during the monitoring phase. Perform continuous audit and validation in an automated way.
DevSecOps CI/CD gives us confidence that code is validated against the corporate security policy. It helps to avoid any infrastructure and application failure in later deployment due to different security configurations. DevSecOps maintains agility and ensures security at scale without affecting DevOps' pace of innovation.

Implementing a CD strategy
CD provides seamless migration of the existing version to the new version of the application. Some of the most popular techniques to achieve through CD are:
In-place deployment: Update application in a current server. Rolling deployment: Gradually roll out the new version in the existing fleet of servers. Blue-green deployment: Gradually replace the existing server with the new server. Red-black deployment: Instant cutover to the new server from the existing server. Immutable deployment: Stand up a new set of servers altogether.
Let's explore each option in more detail.

[ 337 ]

DevOps and Solution Architecture Framework

Chapter 12

In-place deployment
In-place deployment is a method of rolling out a new application version on an existing fleet of servers. The update is done in one deployment action, thereby requiring some degree of downtime. On the other side, there are hardly any infrastructure changes needed for this update. There is also no need to update existing Domain Name System (DNS) records. The deployment process itself is relatively quick. If the deployment fails, redeployment is the only option for restoration. As a simple explanation, you are replacing the existing application version (v1) on the application infrastructure with the new version (v2). In-place updates are low-cost and fast to deploy.

Rolling deployment
With a rolling deployment, the server fleet is divided into a group, so it doesn't need to be updated at the same time. The deployment process runs both old and new versions of software on the same server fleet but with different subgroups. A rolling deployment approach helps to achieve zero downtime as, if a new version deployment fails, then only a subgroup of servers is impacted from the entire fleet, and risk is minimal because half of the fleet will still be up and running. A rolling deployment helps to achieve zero downtime; however, deployment time is little more than in-place deployment.

Blue-green deployment
The idea behind blue-green deployment is that your blue environment is your existing production environment carrying live traffic. In parallel, you provision a green environment, which is identical to the blue environment other than the new version of your code. When it's time to deploy, you route production traffic from the blue environment to the green environment. If you encounter any issues with the green environment, you can roll it back by reverting traffic to the original blue environment. DNS cutover and swapping Auto Scaling groups are the two most common methods used to re-route traffic in blue-green deployment.
Using Auto Scaling policies, you can gradually replace existing instances with instances hosting the new version of your application as your application scales out. This option is best used for minor releases and small code changes. Another option is to leverage DNS routing to perform sophisticated load balancing between different versions of our application.

[ 338 ]

DevOps and Solution Architecture Framework

Chapter 12

As illustrated in the following diagram, after creating a production environment that hosts the new version of our application, you can use the DNS route to shift a small portion of traffic to the new environment:

Blue-green deployment DNS gradual cutover
Test the green environment with a fraction of production traffic; this is called canary analysis. If the environment has functional issues, you'll be able to tell right away and switch traffic back before impacting your users significantly. Continue to gradually shift traffic, testing the ability of the green environment to handle the load. Monitor the green environment to detect issues, providing an opportunity to shift traffic back, thus limiting the blast radius. Finally, when all the metrics are right, decommission the blue environment and release the resources.
[ 339 ]

DevOps and Solution Architecture Framework

Chapter 12

Blue-green deployment helps to achieve zero downtime and provides easy rollback. You can customize the time to deploy as per your needs.

Red-black deployment
In red-black deployment, before standing up a new version of a system, first, perform canary testing. The canary replaces around 1% of its existing production system with the latest version of the application and monitors the newest version for errors. If the canary clears this initial test, the system is deemed ready for deployment.
In preparation for the switchover, a new version of the system stands up side by side with the old version of the system. The initial capacity of the new system is set manually by examining how many instances are currently running in production and setting this number as the desired capacity for the new Auto Scaling group. Once the new system is up and running, both systems are red. The current version is the only version accepting traffic.
Using the DNS service, the system is then cut over from the existing version to the new version. At this point, the old version is regarded as black; it is still running but is not receiving any traffic. If any issues are detected with the new version, then reverting becomes as simple as pointing the DNS server back to the load balancer hosting the old version.
Red-black deployment is also known as dark launch and is slightly different from bluegreen deployment. In red-black deployment, you do sudden DNS cutover from the old version to the new version, while in blue-green deployment, the DNS gradually increases traffic to the new version. Blue-green deployments and dark launches can be combined to deploy both versions of software side by side. Two separate code paths are used, but only one is activated. A feature flag activates the other code path. This deployment can be used as a beta test where you can explicitly enable the new features.

Immutable deployment
An immutable or disposable upgrade is an easier option if your application has unknown dependencies. An older application infrastructure that has been patched and re-patched over time becomes more and more difficult to upgrade. This type of upgrade technique is more common in an immutable infrastructure.

[ 340 ]

DevOps and Solution Architecture Framework

Chapter 12

During the new release, a new set of server instances are rolled out by terminating older instances. For disposable upgrades, you can set up a cloned environment with deployment services such as Chef, Puppet, Ansible, and Terraform, or use them in combination with an Auto Scaling configuration to manage the updates.
In addition to downtime, you need to consider the cost while designing your deployment strategy. Consider the number of instances you need to replace and your deployment frequency to determine the cost. Use the approach that best fits, taking your budget and downtime into consideration.
In this section, you learned about various CD strategies that help you to make your application release more efficient and hassle-free. For high-quality delivery, you need to perform application testing at every step, which often requires significant effort. A DevOps pipeline can help you to automate the testing process and increase the quality and frequency of feature releases. Let's learn more about continuous testing in the CI/CD pipeline.

Implementing continuous testing in the
CI/CD pipeline
DevOps is key for the continually changing business scenarios based on customer feedback, demand for new features, or shifts in market trends. A robust CI/CD pipeline ensures further features/feedback incorporated in less time, and customers get to use the new features faster.
With frequent code check-ins, having a good testing strategy baked into your CI/CD pipeline ensures you close that feedback loop with quality. Continuous testing is essential in balancing the CI/CD pipeline. While adding software features at a rapid pace is a good thing, ensuring that the features adhere to the right quality is achieved by continuous testing.
Unit tests form the largest amount of your testing strategy. They typically run on the developer's machine and are the fastest and cheapest. A general rule of thumb is to incorporate 70% of your testing efforts in unit testing. Bugs caught at this stage can be fixed relatively faster, with fewer complexities.

[ 341 ]

DevOps and Solution Architecture Framework

Chapter 12

Unit tests are often performed by the developer, and once code is ready, it is deployed for integration and system testing. These tests require their own environments and sometimes separate testing teams, which makes the testing process costlier. Once the team ensures that all intended features are working as expected, the operations team needs to run performance and compliance tests. These tests need production-like environments and are costlier. Also, User Acceptance Testing (UAT) needs a replica of production-like environments as well, causing more expense.
As illustrated in the following diagram, in the development phase, developers perform unit tests to test code changes/new features. Testing is usually done on a developer's machine after coding is complete. It is also recommended to run static code analysis on the code changes and do code coverage, adherence to coding guidelines, and so on. Smaller unit tests with no dependencies run faster. Therefore, the developer can find out quickly if the test has failed:

Continuous testing in CI/CD
The build phase is the first phase to test for integration between different components and individual components themselves. The build phase is also an excellent time to test if the code committed by a developer breaks any existing feature and to perform regression testing. A staging environment is a mirror of the production environment. An end-to-end system test is performed at this stage (UI, backend logic, and API are tested extensively). Performance testing tests the application performance under a particular workload. Performance tests include load tests and stress tests. UAT is also performed at this stage, in readiness for production deployment. Compliance testing is done to test for industryspecific regulatory compliance.
[ 342 ]

DevOps and Solution Architecture Framework

Chapter 12

In the production phase, a strategy such as A/B testing or canary analysis is used to test the new application version. In A/B testing, the new application version is deployed to a small percentage of production servers and tested for user feedback. Gradually, depending on how well the users receive the new application, the deployment is increased to span all production servers.

A/B testing
Often, in software development, it isn't clear which implementation of a feature will be most successful in the real world. An entire computer science discipline--Human/Computer Interaction (HCI)--is devoted to answering this question. While UI experts have several guidelines to help them design suitable interfaces, often, the best choice of design can only be determined by giving it to users and seeing whether they can use the design to complete a given task.
As shown in the following diagram, A/B testing is a testing methodology in which two or more different versions of features are given to different sets of users. Detailed metrics on the usage of each implementation are gathered, and UI engineers examine this data to determine which implementation should be adopted going forward:

Split users by feature experiment using A/B testing
[ 343 ]

DevOps and Solution Architecture Framework

Chapter 12

It's easy to launch several different versions of your application, each containing different implementations of a new feature. DNS routing can be used to send the majority of traffic to the current system, while also sending a fraction of the existing traffic to the versions of the system running the new features. DNS round-robin resolution is supported by most DNS resolvers and is an effective way to spread incoming traffic.
Load and performance testing are another important factor. For Java-based applications, you can use JMeter to load-test a relational database by issuing Java Database Connectivity (JDBC) commands. For MongoDB, you can use Mongo-Perf, which can generate a reproducible load on the database and record the response time. You can then hit the components and services that use the database and also simultaneously test the database.
One common way to measure the load on instances is through what is called microbenchmarking. In micro-benchmarking, you measure the performance of a small subcomponent of your system (or even a snippet of code) and then attempt to extrapolate general performance data from this test result. In the case of testing a server, you may test a slice of the system on a new instance type and compare that measurement to the same slice measured on your currently running system, which is now using another server type and configuration.

Using DevOps tools for CI/CD
To build a CI/CD pipeline, a developer requires various tools. These include a code editor, a source repository, a build server, a deployment tool, and orchestrating an overall CI pipeline. Let's explore some popular technology choices of developer tools for DevOps, both in the cloud and on-premises.
Code editor
DevOps is a hands-on coding role, where you often need to write a script to automate the environment. You can use the ACE editor or the cloud-based AWS Cloud9 integrated development environment (IDE); you can use a web-based code editor on your local computer or install a code editor in your local server that connects to the application environments--such as dev, test, and prod--to interact. An environment is a place where you store your project's files and where you run the tools to develop your apps. You can save these files locally on the instance or server, or clone a remote code repository into your environment. The AWS Cloud9 IDE is the cloud-native IDE provided as a managed service.

[ 344 ]

DevOps and Solution Architecture Framework

Chapter 12

The Ace editor lets you write code quickly and easily. It's a web-based code editor but provides performance similar to popular desktop-based code editors such as Eclipse, Vim, and Visual Studio Code (VSCode), and so on. It has standard IDE features such as live syntax and matching parentheses highlighting, auto-indentation and completion, toggling between tabs, integration with version control tools, and multiple cursor selections. It works with large files, having hundreds of thousands of lines without typing lag. It has built-in support for all of the popular coding languages along with debugging tools, and you can also install your own tools. For a desktop-based IDE, VS Code and Eclipse are other popular code editor options that DevOps engineers can choose.

Source code management
There are multiple choices available for your source code repository. You can set up, run, and manage your Git server, where you will be responsible for everything. You can choose to use a hosting service such as GitHub or Bitbucket. If you are looking for a cloud solution, then AWS CodeCommit offers a secure, highly scalable, and managed source control system where you can host private Git repositories.
You need to set up authentication and authorization for your code repository to provide access to authorize team members for code to read or write. You can apply data encryption in transit and at rest. When you push into the code repository (git push), it encrypts the data and then stores it. When you pull from the code repository (git pull), it decrypts the data and then sends the data back to the caller. The user must be an authenticated user with the proper access level to the code repository. Data can be encrypted in transit by transmitting through encrypted network connections using HTTPS or SSH protocols.

CI server
A CI server is also known as a build server. With teams working on multiple branches, it gets complicated to merge back into the master. CI, in this scenario, plays a key role. CI server hooks provide a way to trigger the build based on the event when code is committed to the repository. Hooks, which are incorporated in almost every version control system, refer to custom scripts that are triggered by specified necessary actions that also occur in a repository. Hooks can run either on the client side or on the server side.
Pull requests are a common way for developers to notify and review each other's work before it is merged into common code branches. A CI server provides a web interface to review changes before adding them to the final project. If there are any problems with the proposed changes, source code can be sent back to the developer to tweak as per the organization's coding requirements.
[ 345 ]

DevOps and Solution Architecture Framework

Chapter 12

As shown in the following diagram, server-side hooks in combination with the CI server are used to increase the velocity of integration:

Automation of CI
As illustrated in the preceding diagram, using post-receive, you can direct new branches to trigger tests on a CI server to verify that the new build integrates correctly and that all units function correctly. The developer is notified of test failures and then knows to merge their branch with the mainline only after the problems have been fixed. The developer can build from their branch, test the changes there, and get feedback on how well their changes work before deciding whether to merge their branch into the mainline. Running integration and unit tests significantly reduces resistance when that branch is merged into the mainline. Hooks can also be customized to test merges into the mainline and block any merges that don't pass. Integration is all accomplished best with a CI server. Jenkins is the most popular choice to build the CI server. However, you have to maintain security and patching of the server by yourself. For native cloud options and managed services, you can use managed code-build services such as AWS CodeBuild, which eliminates the need for server administration and reduces costs significantly with a pay-as-you-go model. The service scales as per your demand. Your team is empowered to focus on pushing code and lets a service build all the artifacts.
[ 346 ]

DevOps and Solution Architecture Framework

Chapter 12

As illustrated in the following diagram, you can host the Jenkins cluster in the AWS Elastic Compute Cloud (EC2) server's fleet and auto-scale as per build load:

Auto Scaling of Jenkins CI servers
The Jenkins Master offload builds to the slave node instance in the case of overload. When the load goes down, the Jenkins Master automatically terminates slave instances.
While a CI server helps you to build the right version of code from a source code repository by collaborating across team members of the development team, code deployment helps the team to get code ready for testing and release for end-user consumption. Let's learn about code deployment in more detail.
Code deployment
Once your build is ready, you can use the Jenkins server for deployment or choose AWS CodeDeploy as a cloud-native managed service. You can use other popular tools such as Chef or Puppet to create a deployment script. The options for specifying a deployment configuration are:
OneAtATime: Only a single instance in a deployment group at a time installs a new deployment. If a deployment on a given instance fails, the deployment script will halt the deployment and return an error response detailing the number of successful versus the number of failed installations. HalfAtATime: Half of the instances in the deployment group install a new deployment. The deployment succeeds if half of the instances successfully install the revision. HalfAtATime can again be a good option for production/test environments where half of the instances are updated to a new revision, and the other half remain available in production at an older revision.
[ 347 ]

DevOps and Solution Architecture Framework

Chapter 12

AllAtOnce: Each instance installs the latest revision available whenever it next polls the deployment service. This option is best used for development and test deployments as it has the potential to install a non-functioning deployment on every instance in a deployment group. Custom: You can use this command to create a custom deployment configuration specifying a fixed number of healthy hosts that must exist in a deployment group at any given time. This option is a more flexible implementation of the OneAtATime option. It allows for the possibility that a deployment may fail on one or two instances that have become corrupt or are improperly configured.
The following diagram illustrates life cycle events during deployment:

Deployment life cycle event
The deployment agent runs through a series of steps to execute a deployment. These steps are called life cycle events. In the preceding diagram, steps highlighted in blue can be controlled by human intervention; however, steps highlighted in green are automated and controlled by a deployment agent. Here are more details about each step:
ApplicationStop: In order to trigger a deployment, the first requirement is to stop the application server so that traffic stops serving while files are copied. Examples of software application servers are Tomcat, JBoss, or WebSphere servers.
[ 348 ]

DevOps and Solution Architecture Framework

Chapter 12

DownloadBundle: After stopping the application server, the deployment agent starts downloading a pre-built deployment bundle from an artifactory such as JFrog Artifactory. The artifactory stores the application binary, which can be deployed and tested for application before the new version launch.
BeforeInstall: The deployment agent triggers pre-install steps such as creating a backup of the current version and any required configuration update via a script.
Install: In this step, deployment agents start the installation--for example, running an Ant or Maven script for installation of a Java application.
AfterInstall: The deployment agent triggers this step after your application installation is completed. It may include updating post-installation configuration, such as local memory setting and log parameters.
ApplicationStart: In this step, the agent starts the application and notifies the operations team of success or failure.
ValidateService: The validation step fires after everything else is done and gives you a chance to do a sanity check on the app. It includes steps such as performing automated sanity tests and integration tests to verify if the new version of the application has installed properly. The agent also sends a notification to the team when testing is successful.
You have learned about various code deployment strategies and steps as an independent component. However, to set up an automated CI/CD pipeline, you need to stitch all DevOps steps together. Let's learn more about the code pipeline, which can help you to build an end-to-end CI/CD pipeline.

Code pipeline
The code pipeline is about orchestrating everything together to achieve continuous deployment (CD). In CD, the entire software release process is fully automated, including build and deployment to the production release. Over some time with experiments, you can set up a mature CI/CD pipeline in which the path to the production launch is automated, thus enabling rapid deployment of features and immediate customer feedback. You can use cloud-native managed services such as AWS CodePipeline to orchestrate the overall code pipeline, or you can use the Jenkins server.

[ 349 ]

DevOps and Solution Architecture Framework

Chapter 12

The code pipeline enables you to add actions to stages in your CI/CD pipeline. Each action can be associated with a provider that executes the action. The code pipeline action's categories and examples of providers are as follows:
Source: Your application code needs to be stored in a central repository with version control called source code repositories. Some of the popular code repositories are AWS CodeCommit, Bitbucket, GitHub, Concurrent Versions System (CVS), Subversion (SVN), and so on.
Build: The build tool pulls code from the source code repository and creates an application binary package. Some of the popular build tools are AWS CodeBuild, Jenkins, Solano CI, and so on. Once the build is completed, you can store binaries in an artifactory such as JFrog.
Deploy: The deployment tool helps you to deploy application binaries in the server. Some popular deployment tools are AWS Elastic Beanstalk, AWS CodeDeploy, Chef, Puppet, Jenkins, and so on.
Test: Automated testing tools help you to complete and perform postdeployment validation. Some popular test validating tools are Jenkins, BlazeMeter, Ghost Inspector, and so on.
Invoke: You can use an events-based script to invoke activities such as backup and alert. Any scripting language such as a shell script, PowerShell, and Python can be used to invoke various customized activities.
Approval: Approval is an important step in CD. You can either ask for manual approval by an automated email trigger or approval can be automated from tools.
In this section, you learned about various DevOps tools to manage the Software Development Life Cycle (SDLC) such as a code editor, a repository, and build, test, and deployment tools. As of now, you have learned about various DevOps techniques for each SDLC phase. Let's learn more about applying best practices and anti-patterns.

[ 350 ]

DevOps and Solution Architecture Framework

Chapter 12

Implementing DevOps best practices
While building a CI/CD pipeline, consider your need to create a project and add team members to it. The project dashboard provides visibility to the code flow through the deployment pipeline, monitoring the build, triggering alerts, and tracking application activities. The following diagram illustrates a well-defined DevOps pipeline:

CI/CD workflow best practice
Consider the following points while designing the pipeline:
Number of stages: Stages could be development, integration, system, user acceptance, and production. Some organizations also include dev, alpha, beta, and release stages. Type of tests in each stage: Each stage can have multiple types of tests such as unit tests, integration tests, system tests, UATs, smoke tests, load tests, smoke tests, and A/B tests at the production stage. The sequence of a test: Test cases can be run in parallel or need to be in sequence. Monitoring and reporting: Monitor system defects and failures and send notifications as failures occur. Infrastructure provisioning: Methods to provision infrastructure for each stage. Rollback: Define the rollback strategy to fall back to the previous version if required.
Having a system that requires manual intervention where it's avoidable slows down your process. So, automating your process using CD will accelerate your process.
[ 351 ]

DevOps and Solution Architecture Framework

Chapter 12

Another common anti-pattern is keeping configuration values for a build inside of the code itself, or even having developers use different tools in their build processes, which can lead to inconsistent builds between developers. It takes lots of time and effort trying to troubleshoot why particular builds work in one environment and not in others. To overcome this, it is better to store build configurations outside of code. Externalizing these configurations to tools which keeps them consistent between builds, enables better automation, and allows your process to scale much more quickly. Not using a CD process can lead to last-minute, middle-of-the-night rushes to get a build to work. Design your CD process to fail fast, to reduce the likelihood of any last-minute surprises.
Nowadays, most applications are built as a web app and utilize a cloud platform. To apply architecture best practice at each step of application development, the twelve-factor methodology can be used, as recommended by The Twelve-Factor App (https:// 12factor.net/) , the twelve-factor methodology adopted by enterprises for end-to-end development and delivery of web applications. This applies to all coding platforms regardless of programming languages. You have learned details about each factor throughout different chapters of the book.

Summary
In this chapter, you have learned about the key components of a strong DevOps practice, which includes CI, CD, and continuous monitoring and improvement. The agility of CI/CD can be achieved only by applying automation everywhere. To automate, you learned about IaC and configuration management. You also looked at various automation tools such as Chef, Puppet, and Ansible to automate configuration management.
As security is the priority, you learned about DevSecOps, which is DevOps in Security. CD is one of the key aspects of DevOps. You learned about various deployment strategies, including rolling, blue-green, and red-black deployment. Testing is another aspect of ensuring the quality of your product, and you learned about the concept of continuous testing in DevOps, and also, how A/B testing can help to improve the product by taking direct feedback from a customer in the live environment.

[ 352 ]

DevOps and Solution Architecture Framework

Chapter 12

You have learned about stages in a CI/CD pipeline. You have learned about the tools and services that you can use and best practices that you can follow for a robust CI/CD pipeline. You have learned how individual services work and also discussed how to integrate services to build a sophisticated solution.
Until this point, you have learned about various aspects of solution architecture as every organization has lots of data, and they put a great effort into getting an insight into their data. In the next chapter, you will learn about how to collect, process, and consume data to get a more in-depth insight.

[ 353 ]

13
Data Engineering and Machine
Learning
In the era of the internet and digitization, data is being generated everywhere with high velocity and quantity. Getting insight from these huge amounts of data at a fast pace is challenging. We need to innovate continuously to ingest, store, and process this data to derive business outcomes.
With the convergence of many cloud, mobile, and social technologies, advancements in many fields such as genomics and life sciences are growing at an ever-increasing rate. Tremendous value is found in mining this data for more insight. A fundamental difference between streaming systems and batch systems is the requirement to process unlimited data. Modern stream processing systems need to produce continual results at low latency on data with high and variable input rates.
The concept of big data is more than just the collection and analysis of the data. The actual value for organizations in their data is when it can be used to answer questions and used to create competitive advantages for the organization. Not all big data solutions must end in visualization. Many solutions such as Machine Learning (ML) and other predictive analytics feed these answers programmatically into other software or applications, which extract the information and respond as designed.
As with most things, getting faster results costs more, and big data is no exception. Some answers might not be needed immediately, and so the latency and throughput of the solution can be flexible enough to take hours to be completed. Other responses, such as in the fields of predictive analytics or ML, may be needed as soon as the data is available.

Data Engineering and Machine Learning

Chapter 13

In this chapter, you will learn about the following topics to handle and manage your big data and ML needs:
What is big data architecture? Designing for big data Data ingestion Data storage Data processing and analytics Data visualization The Internet of Things (IoT) What is ML? Data science and ML ML model overfitting versus underfitting Supervised and unsupervised ML model
By the end of this chapter, you will learn about how to design big data and analytics architecture. You will learn different steps of the big data pipeline including data ingestion, storage, processing, and visualization. You will learn about the basics of ML and model evaluation techniques.

What is big data architecture?
The sheer volume of collected data can cause problems. With the accumulation of more and more data, managing and moving the data along with its underlying big data infrastructure becomes increasingly difficult. The rise of cloud providers has facilitated the ability to move applications to the data. Multiple sources of data result in increased volumes, velocity, and variety. The following are some common computer-generated data sources:
Application server logs: Application logs and games Clickstream logs: From website clicks and browsing Sensor data: Weather, water, wind energy, and smart grids Images and videos: Traffic and security cameras
Computer-generated data can vary from semi-structured logs to unstructured binaries. This data source can produce pattern-matching or correlations in data that generate recommendations for social networking and online gaming in particular. You can also use computer-generated data to track applications or service behavior such as blogs, reviews, emails, pictures, and brand perceptions.
[ 355 ]

Data Engineering and Machine Learning

Chapter 13

Human-generated data includes email searches, natural language processing, sentiment analysis on products or companies, and product recommendations. Social graph analysis can produce product recommendations based on your circle of friends, jobs you may find interesting, or even reminders based on your circle of friend's birthdays, anniversaries, and so on.
In data architecture, the general flow of a significant data pipeline starts with data and ends with insight. How you get from start to finish depends on a host of factors. The following diagram illustrates a data workflow pipeline that needs to design for data architecture:

Big data pipeline for data architecture design
As shown in the preceding diagram, the standard workflow of the big data pipeline includes the following steps:
1. Data is collected (ingested) by an appropriate tool. 2. The data is stored in a persistent way. 3. The data is processed or analyzed. The data processing/analysis solution takes
the data from storage, performs operations, and then stores the processed data again.
[ 356 ]

Data Engineering and Machine Learning

Chapter 13

4. The data is then used by other processing/analysis tools or by the same tool again to get further answers from the data.
5. To make answers useful to business users, they are visualized by using a business intelligence (BI) tool or fed into an ML algorithm to make future predictions.
6. Once the appropriate answers have been presented to the user, this gives them insight into the data that they can then take and use to make further business decisions.
The tools you deploy in your pipeline determine your time-to-answer, which is the latency between the time your data was created and when you can get insight from it. The best way to architect data solutions while considering latency is to determine how to balance throughput with cost, because a higher performance and subsequently reduced latency usually results in a higher price.

Designing big data processing pipelines
One of the critical mistakes many big data architectures make is trying to handle multiple stages of the data pipeline with one tool. A fleet of servers handling the end-to-end data pipeline, from data storage and transformation to visualization, may be the most straightforward architecture, but it is also the most vulnerable to breakdowns in the pipeline. Such tightly-coupled big data architecture typically does not provide the best possible balance of throughput and cost for your needs.
It is recommended that big data architects decouple the pipeline. There are several advantages to decoupling storage and processing in multiple stages in particular, including increased fault tolerance. For example, if something goes wrong in the second round of processing and the hardware dedicated to that task fails, you won't have to start again from the beginning of the pipeline; your system can resume from the second storage stage. Decoupling your storage from various processing tiers gives you the ability to read and write to multiple data stores.
The following diagram illustrates various tools and processes to consider when designing a big data architecture pipeline:

[ 357 ]

Data Engineering and Machine Learning

Chapter 13

Tools and processes for big data architecture design
The things you should consider when determining the right tools for your big data architectures include the following:
The structures of your data The maximum acceptable latency The minimum acceptable throughput The typical access patterns of your system's end users Your data structure has an impact on both the tools you use to process it and where you store it. The ordering of your data and the size of each object you're storing and retrieving are also essential considerations. The time-to-answer is determined by how your solution weighs latency/throughput and cost.
[ 358 ]

Data Engineering and Machine Learning

Chapter 13

User access patterns are another important component to consider. Some jobs require the rapid joining of many related tables regularly, and other jobs require daily or less frequent use of stored data. Some jobs require a comparison of data from a wide range of data sources, and other jobs pull data from only one unstructured table. Knowing how your end users will most often use the data will help you determine the breadth and depth of your big data architecture. Let's dive deep into each process and the tools involved in big data architecture.

Data ingestion
Data ingestion is the act of collecting data for transfer and storage. There are lots of places that data can come from. Predominantly, data ingestion falls into one of the categories from databases, streams, logs, and files. Among these, databases are the most predominant. These typically consist of your main upstream transactional systems that are the primary data storage for your applications. They take on both relational and non-relational flavors, and there are several techniques for extracting data out of them.
Streams are open-ended sequences of time-series data such as clickstream data from websites or IoT devices, usually published into an API that we host. Logs get generated by applications, services, and operating systems. A data lake is a great place to store all of those for centralized analysis. Files come from self-hosted file systems or via third-party data feeds via FTP or APIs. As shown in the following diagram, use the type of data your environment collects and how it is collected to determine what kind of ingestion solution is ideal for your needs:

Type of data ingestion
[ 359 ]

Data Engineering and Machine Learning

Chapter 13

As shown, transactional data must be able to store and retrieve data quickly. End users need quick and straightforward access to the data, which makes app and web servers the ideal ingestion methods. For the same reasons, databases such as NoSQL and Relational Database Management Systems (RDBMS) are usually the best solutions for these kinds of processes.

Data transmitted through individual files is typically ingested from connected devices. A large amount of file data does not require fast storage and retrieval compared to transactional data. For file data, often transfer is one-way, where data is produced by multiple resources and ingested into a single object or file storage for later use.
Stream data such as clickstream logs should be ingested through an appropriate solution such as an Apache Kafka or Fluentd. Initially, these logs are stored in stream storage solutions such as Kafka, so they're available for real-time processing and analysis. Longterm storage of these logs is best in a low-cost solution such as object storage.
Streaming storage decouples your collection system (producers) from the processing system (consumers). It provides a persistent buffer for your incoming data. The data can be processed and you can pump the data at a rate dependent on your needs.

Technology choices for data ingestion
Let's looks at some popular open source tools for data ingestion and transfer:
Apache DistCp: DistCp stands for distributed copy and is part of the Hadoop ecosystem. The DistCp tool is used to copy large data within a cluster or between clusters. DistCp achieves the efficient and fast copying of data by utilizing parallel processing distribute capability which comes with MapReduce. It distributes directories and files into map tasks to copy files partitions from source to target. DistCp also does error handling, recovery, and reporting across clusters.

[ 360 ]

Data Engineering and Machine Learning

Chapter 13

Apache Sqoop: Sqoop is also part of the Hadoop ecosystem project and helps to transfer data between Hadoop and relational data stores such as RDBMS. Sqoop allows you to import data from a structured data store into HDFS and to export data from HDFS into a structured data store. Sqoop uses plugin connectors to connect to relational databases. You can use the Sqoop extension API to build a new connector, or you can use one of the included connectors that support data exchange between Hadoop and common relational database systems.
Apache Spark Streaming: Spark Streaming helps to ingest live data streams with high throughput and in a fault-tolerant, scalable manner. Spark Streaming divides the incoming data streams into batches before sending them to the Spark engine for processing. Spark Streaming uses DStreams, which are sequences of resilient distributed datasets (RDDs).
Apache Kafka: Kafka is one of the most popular open source streaming platforms that helps you publish and subscribe to a data stream. A Kafka cluster stores a recorded stream in a Kafka topic. A producer can publish data in a Kafka topic and consumers can take the outputted data stream by subscribing to the Kafka topic.
Apache Flume: Flume is open source software and is mainly used to ingest a large amount of log data. Apache Flume collects and aggregates data to Hadoop reliably and in a distributed manner. Flume facilitates streaming data ingestion and allows analytics.
Apache Flink: Flink is another open source platform for streaming data and batch data processing. Flink consists of a streaming dataflow engine that can process bounded and unbounded data stream. The bounded data stream has a defined start and end, while an unbounded data stream has a start but no end. Flink can perform batch processing as well on its streaming engine and supports batch optimizations.
There are more open source projects available for streaming, such as Apache Storm and Apache Samza, to provide a means of reliably processing unbounded streams of data.

[ 361 ]

Data Engineering and Machine Learning

Chapter 13

Ingesting data to the cloud
Public cloud providers such as AWS provide an array for big data services to store and process data on a large scale. The following are some options to move your data to the AWS cloud and utilize the scalability offered by the cloud provider:
AWS Direct Connect: AWS Direct Connect provides up to 10 Gbps of private connectivity between the AWS cloud and your data center. A dedicated network connection reduces network latency and increases bandwidth throughput. It provides more reliable network speed compared to internet connections where data has to hop through multiple routers. Direct Connect creates a cross-connect between the router managed either by you or a Direct Connect partner, depending on whether you are co-located in one of AWS Direct Connect locations, and the router in that location that AWS owns. The circuit itself provides both a public and a private Virtual Interface (VIF). You can use the private VIF to directly access the resources running within your Virtual Private Cloud (VPC) on AWS, and the public VIF to access the public endpoints for AWS services such as Amazon Simple Storage Service (S3).
AWS Snowball: If you want to transfer a large amount of data, such as hundreds of terabytes (TB) or petabytes (PB) to the cloud, it could take years over the internet. AWS Snowball provides a tamper-proof 80 TB storage appliance that can transfer a large amount of data. It works like a large hard disk that you can plug in to your on-premise data storage server, load all data, and ship it to AWS. AWS will place your data in a designated location in the cloud storage. AWS Snowball has other flavors, such as Snowball Edge, which comes with compute power along with 100 TB of storage and fulfills the use case of handling data in a remote location, such as on a cruise ship or an oil ring. It is like a small data center where you can load data and perform some analytics using the built-in compute functionality. Data can be loaded to the cloud as soon as the appliance comes online. If you have petabytes of data, then you can use Snowmobile, which is a physical 45-foot shipping container with which you can transfer 100 PB of data in one go from your data center to the AWS cloud.

[ 362 ]

Data Engineering and Machine Learning

Chapter 13

Amazon Kinesis: Amazon Kinesis offers three capabilities. The first is a place to store a raw data stream to perform any downstream processing of the records that you desire. To facilitate transferring these records into common analytic environments such as Amazon S3, ElasticSearch, Redshift, and Splunk, it offers the Amazon Kinesis Firehose service. Firehose will automatically buffer up all the records in the stream and flush out to the target as a single file or set of records based on either a time or data-size threshold that you can configure, or whichever is reached first. If you wish to perform some window-based analytics on the records in the stream, use Kinesis Analytics. Kinesis Analytics allows you to flow streams together and perform SQL operations over the records based on the time windows that you configure. The output can subsequently flow into further streams you create, so you can build an entire serverless streaming pipeline.
AWS Data Migration Service (DMS): AWS DMS makes it easy to securely migrate or replicate your databases and data warehouses to AWS. In DMS, you can create a data migration task, which will be connected to on-premise data via a source endpoint and uses AWS-provided storage such as RDS and Amazon S3 as the target endpoint. DMS supports full data dumps and ongoing change data capture (CDC). DMS also supports homogeneous (MySQL-to-MySQL) and heterogeneous (MySQL-to-Amazon-Aurora) database migrations.
AWS provides more tools such as AWS Data Sync for continuous file transfer to AWS from on-premise and AWS Transfer for SFTP to ingest data from the SFTP server securely. As you ingest the data, it needs to be put in suitable storage to fulfill the business needs. Let's learn more about techniques to choose the right storage and the available storage choices.

[ 363 ]

Data Engineering and Machine Learning

Chapter 13

Storing data
One of the most common mistakes made when setting up storage for a big data environment is using one solution, frequently an RDBMS, to handle all of your data storage requirements. You will have many tools available, but none of them are optimized for the task they need to complete. One single solution is not necessarily the best for all of your needs; the best solution for your environment might be a combination of storage solutions that carefully balance latency with the cost. An ideal storage solution uses the right tool for the right job. Choosing a data store depends upon various factors:
How structured is your data? Does it adhere to a specific, well-formed schema, as is the case with Apache web logs (logs are generally not well structured and so not suitable for relational databases), standardized data protocols, and contractual interfaces? Is it completely arbitrary binary data, as in the cases of images, audio, video, and PDF documents? Or, is it semi-structured with a general structure but with potentially high variability across the records, as in the case of JSON or CSV?
How quickly does new data need to be available for querying (temperature)? Is it a real-time scenario, where decisions are made as new records stream in, such as with campaign managers making adjustments based on conversion rates or a website making product recommendations based on user-behavior similarity? Is it a daily, weekly, or monthly batch scenario, such as in model training, financial statement preparation, or product performance reporting? Or is it somewhere in between, such as with user engagement emails, where it doesn't require real-time action, but you can have a buffer of a few minutes or even a few hours between the user action and the touchpoint?
The size of the data ingest: Is the data ingested record by record as data comes in, such as with JSON payloads from REST APIs that measure at just a few KBs at best? Is it a large batch of records arriving all at once, such as with system integrations and third-party data feeds? Or is it somewhere in between, such as with a few micro-batches of clickstream data aggregated together for more efficient processing?
Total volume of data and its growth rate: Are you in the realm of GBs and TBs, or do you intend to store PBs or even exabytes (EB)? How much of this data is required for your specific analytics use cases? Do the majority of your queries only require a specific rolling window of time? Or, do you need a mechanism to query the entirety of your historical dataset?

[ 364 ]

Data Engineering and Machine Learning

Chapter 13

What the cost will be to store and query the data in any particular location: When it comes to any computing environment, we generally see a triangle of constraints between performance, resiliency, and low cost. The better the performance and the higher the resilience that you want your storage to have, the more expensive it will tend to be. You may wish to have quick queries over petabytes of data, which is the kind of environment that Redshift can provide, but decide to settle on querying TBs of data compressed in the Parquet format using Athena to meet your cost requirements.
Finally, what type of analytic queries will run against the data? Will it be powering a dashboard with a fixed set of metrics and drill-down? Will it participate in large numerical aggregations rolled up by various business dimensions? Or, will it be used for diagnostics, leveraging string tokenization for full-text searching and pattern analysis? The following diagram combines multiple factors related to your data and the storage choice associated with it:

Understanding data storage
When you determine all characteristics of your data and understand the data structure, you can then assess which solution you need to use for your data storage. Let's learn about the various solutions for storing data.
[ 365 ]

Data Engineering and Machine Learning

Chapter 13

Technology choices for data storage
As we discussed, a single tool can't do everything. You need to use the right tool for the right job, and the data lake enables you to build a highly configurable big data architecture to meet your specific needs. Business problems are far too broad, deep, and complex for one tool to solve everything, and this is especially true in the big data and analytics space.
For example, hot data will need to be stored and processed in-memory, so caches or inmemory databases like Redis or SAP Hana are appropriate. AWS offers the ElastiCache service, providing a managed Redis or Memcached environment. NoSQL databases are ideal when facing high velocity but small-sized records, for example, user-session information or IoT data. NoSQL databases are also useful for content management to store data catalogs.

Structured data stores
Structured data stores have been around for decades and are the most familiar technology choice when it comes to storing data. Most of the transactional databases such as Oracle, MySQL, SQL Server, and PostgreSQL are row-based due to dealing with frequent data writes from software applications. Organizations often repurpose transactional database for reporting purposes, where frequent data reads are required, but much fewer data writes. Looking at high data-read requirements, there is more innovation coming into an area of query on structured data stores, such as the columnar file format, which helps to enhance data read performance for analytics requirements.
Row-based formats store the data in rows in a file. Row-based writing is the fastest way to write the data to the disk but it is not necessarily the quickest read option because you have to skip over lots of irrelevant data. Column-based formats store all the column values together in the file. This leads to better compression because the same data types are now grouped together. It also typically provides better read performance because you can skip columns that are not required.
Let's look at common choices for the structured data store. Take an example where you need to query the total number of sales in a given month from the order table, which has fifty columns. In a row-based architecture, the query will scan the entire table with all fifty columns, but in columnar architecture, the query will just scan the order sales column, thus improving data query performance. Let's look into more details about relational databases, focusing on transaction data and data warehousing to handle data analytics needs.

[ 366 ]

Data Engineering and Machine Learning

Chapter 13

Relational databases
RDBMS is more suitable for Online Transaction Processing (OLTP) applications. Some popular relational databases are Oracle, MSSQL, MariaDB, PostgreSQL, and so on. Some of these traditional databases have been around for decades. Many applications, including ecommerce, banking, and hotel booking, are backed by relational databases. Relational databases are very good at handling transaction data where complex joint queries between tables are required. Looking at transaction data needs, the relational database should adhere to the Atomicity, Consistency, Isolation, Durability (ACID) principles, as follows:
Atomicity: Atomicity means the transaction will executed fully from end to end, and, in the case of any error, the entire transaction will roll back. Consistency: Consistency means as soon as transactions are completed, all data should be committed to the database. Isolation: Isolation requires that multiple transactions can run concurrently in isolation without interfering with each other. Durability: In case of any interruption, such as a network or power failure, the transaction should able to resume the last known state.
Often, data from the relational databases are offloaded to data warehousing solutions for reporting and aggregation purposes. Let's learn more about data warehousing.

Data warehousing
Data warehouse databases are more suitable for Online Analytical Processing (OLAP) applications. Data warehouses provide fast aggregation capability over vast volumes of structured data. While these technologies, such as Amazon Redshift, Netezza, and Teradata, are designed to execute complex aggregate queries quickly, they are not optimized for high volumes of concurrent writes. So, data needs to be loaded in batches, preventing warehouses from being able to serve real-time insights over hot data.
Modern data warehouses use a columnar base to enhance query performance. Examples of this include Amazon Redshift, Snowflake, and Google Big Query. These data warehouses provide very fast query performance due to columnar storage and improve I/O efficiency. In addition to that, data warehouse systems such as Amazon Redshift increase query performance by parallelizing queries across multiple nodes and take advantage of massive parallel processing (MPP).

[ 367 ]

Data Engineering and Machine Learning

Chapter 13

Data warehouses are central repositories that store accumulations of data from one or multiple sources. They store current and historical data used to help create analytical reports for business data analytics. However, data warehouses store data centrally from multiple systems but they can not be treated as a data lake. Data warehouses handle only structured relational data while data lakes work with both structured relational data and unstructured data such as JSON, logs, and CSV data.
Data warehouse solutions such as Amazon Redshift can process petabytes of data and provide decoupled compute and storage capabilities to save costs. In addition to columnar storage, Redshift uses data encoding, data distribution, and zone maps to increase query performance. More traditional row-based data warehousing solutions include Netezza, Teradata, and Greenplum.

NoSQL databases
NoSQL databases such as Dynamo DB, Cassandra, and Mongo DB address the scaling and performance challenges that you often experience with a relational database. As the name suggests, NoSQL means a non-relational database. NoSQL databases store data without an explicit and structured mechanism to link data from different tables (no joins, foreign keys, and with normalization enforced).
NoSQL utilizes a number of data models including columnar, key-value, search, document, and graph. NoSQL databases provide scalable performance, high availability, and resilience. NoSQL typically does not enforce strict schema and every item can have an arbitrary number of columns (attributes), which means one row can have four columns, while another row can have ten columns in the same table. The partition key is used to retrieve values or documents containing related attributes. NoSQL databases are highly distributed and can be replicated. NoSQL databases are durable and don't experience performance issues when highly available.

[ 368 ]

Data Engineering and Machine Learning

Chapter 13

SQL versus NoSQL databases
SQL databases have been around for decades and most of us are probably already very familiar with relational databases. Let's learn some significant differences between SQL and NoSQL databases:

Properties SQL Databases

NoSQL Databases

Data model

In SQL databases, the relational model normalizes data into tables containing rows and columns. A schema includes tables, number of columns, relationships between tables, index, and other database elements.

NoSQL databases do not enforce a schema. A partition key is commonly used to retrieve values from column sets. It stores semistructured data such as JSON, XML, or other documents such as data catalogs and file indexes.

Transaction

SQL-based traditional RDBMS support and are compliant with the transactional data properties of ACID.

To achieve horizontal scaling and data model flexibility, NoSQL databases may trade some ACID properties of traditional RDBMS.

SQL-based RDBMS were used to

optimize storage when the storage was

expensive and to minimize the footprint For NoSQL, performance depends

on disk. For traditional RDBMS,

upon the underlying hardware

Performance performance has mostly relied on the cluster size, network latency, and

disk. To achieve performance query

how the application is calling the

optimizations, index creation and

database.

modifications to the table structure are

required.

Scale

SQL-based RDBMS databases are easiest to scale vertically with high configuration hardware. The additional effort requires relational tables to span across distributed systems such as performing data sharding.

NoSQL databases are designed to scale horizontally by using distributed clusters of low-cost hardware to increase throughput without impacting latency.

Depending upon the of your data, there are various categories of NoSQL data stores that exists to solve a specific problem. Let's understand the types of NoSQL databases.

[ 369 ]

Data Engineering and Machine Learning

Chapter 13

Types of NoSQL data store
Following are the major NoSQL databases types:
Columnar databases: Apache Cassandra and Apache HBase are the popular columnar databases. The columnar data store helps you to scan a particular column when querying the data, rather than scanning the entire row. If an item table has 10 columns with one million rows and you want to query the number of a given item available in inventory, then the columnar database will just apply the query to the item quantity column rather than scanning the entire table. Document databases: Some of the most popular document databases are MongoDB, Couchbase, MarkLogic, Dynamo DB, and Cassandra. You can use a document database to store semi-structured data in JSON and XML formats. Graph databases: Popular graph database choices include Amazon Neptune, JanusGraph, TinkerPop, Neo4j, OrientDB, GraphDB, and GraphX on Spark. A graph database stores vertices and links between vertices called edges. Graphs can be built on both relational and non-relational databases. In-memory key-value stores: Some of the most popular in-memory key-value stores are Redis and Memcached. They store data in memory for readheavy applications. Any query from an application first goes to an in-memory database and, if the data is available in the cache, it doesn't hit the master database. The in-memory database is good for storing user-session information, which results in complex queries and frequently requests data such as user profiles.
NoSQL has many use cases, but to build a data search you need to index all your data. Let's learn more about search data stores.

Search data stores
The Elasticsearch service is one of the most popular search engines for big data use cases such as clickstream and log analysis. Search engines work well for warm data that can be queried in an ad hoc fashion across any number of attributes, including string tokens. Elasticsearch is a very popular search engine. General binary or object storage is appropriate for files that are unstructured, not indexable, and otherwise opaque without specialized tools that understand their format.

[ 370 ]

Data Engineering and Machine Learning

Chapter 13

Amazon Elasticsearch Service manages the administration of Elasticsearch clusters and provides API access. It also provides Kibana as a visualization mechanism to conduct a search on indexed data stores in the Elasticsearch cluster. AWS manages capacity, scaling, and patching of the cluster, removing any operational overhead. Log search and analysis is a popular big data use case where Elasticsearch helps you to analyze log data from websites, servers fleet, IoT sensors, and so on. Elasticsearch is utilized by a large variety of applications in industry such as banking, gaming, marketing, application monitoring, advertisement technology, fraud detection, recommendations, and IoT.

Unstructured data stores
When you look at the requirements for an unstructured data store, it seems that Hadoop is a perfect choice because it is scalable, extensible, and very flexible. It can run on consumer hardware, has a vast ecosystem of tools, and appears to be cost effective to run. Hadoop uses a master-and-child-node model, where data is distributed between multiple child nodes and the master node co-ordinates jobs for running queries on data. The Hadoop system is based on massively parallel processing (MPP), which makes it fast to perform queries on all types of data, whether it is structured or unstructured.
When a Hadoop cluster is created, each child node created from the server comes with a block of the attached disk storage called a local Hadoop Distributed File System (HDFS) disk store. You can run the query against stored data using common processing frameworks such as Hive, Ping, and Spark. However, data on the local disk persists only for the life of the associated instance.
If you use Hadoop's storage layer (that is, HDFS) to store your data, then you are coupling storage with compute. Increasing storage space means having to add more machines, which increases your compute capacity as well. For maximum flexibility and cost effectiveness, you need to separate compute and storage and scale them both independently. Overall object storage is more suited to data lakes to store all kinds of data in a cost-effective and performant manner. Cloud-based data lakes backed by object storage provide flexibility to decouple compute and storage. Let's learn more about data lakes.

Data lakes
A data lake is a centralized repository for both structured and unstructured data. The data lake is becoming a popular way to store and analyze large volumes of data in a centralized repository. It stores data as is, using open source file formats to enable direct analytics. As data can be stored as is in its current format, you don't need to convert data into a predefined schema, which increases the speed of data ingestion. As illustrated in the following diagram, the data lake is a single source of truth for all data in your organization:
[ 371 ]

Data Engineering and Machine Learning

Chapter 13

Object store for data lake
The following are the benefits of a data lake: Data ingestion from various sources: Data lakes let you store and analyze data from various sources such as relational, non-relational database, and streams in one centralized location for a single source of truth. This answers questions such as why is the data distributed in many locations? and where is the single source of truth? Collecting and efficiently storing data: A data lake can ingest any kind of data structure, including semi-structured and unstructured data without the need of any schema. This answers questions such as how can I ingest data quickly from various sources and in various formats, and store it efficiently at scale? Scale up with the volume of generated data: Data lakes allow you to separate the storage layer and compute layer to scale each component separately. This answers questions such as how can I scale up with the volume of data generated?
[ 372 ]

Data Engineering and Machine Learning

Chapter 13

Applying analytics to data from different sources: With a data lake, you can determine schema on read and create a centralized data catalog on data collected from various resources. This enables you to perform quick ad hoc analysis. This answers questions such as is there a way I can apply multiple analytics and processing frameworks to the same data?
You need an unlimited scalable data storage solution for your data lake. Decoupling your processing and storage provides a significant number of benefits, including the ability to process and analyze the same data with a variety of tools. Although this may require an additional step to load your data into the right tool, using Amazon S3 as your central data store provides even more benefits over traditional storage options.
The beauty of the Data Lake is that you are future-proofing your architecture. Twelve months from now, there may be new technology you want to use. With your data in the data lake, you can insert this new technology into your workflow with minimal overhead. By building modular systems in your big data processing pipeline, with common object storage such as Amazon S3 as the backbone, you can replace specific modules when they become obsolete or when a better tool becomes available.
One tool can not do everything. You need to use the right tool for the right job, and data lakes enable you to build a highly configurable big data architecture to meet your specific needs. Business problems are far too broad, deep, and complex for one tool to solve everything, and this is especially true in the big data and analytics space.

Processing data and performing analytics
Data analytics is the process of ingesting, transforming, and visualizing data to discover useful insights for business decision-making. Over the previous decade, more data is collected and customers are looking for greater insight into their data. These customers also wanted this insight in the least amount of time, and sometimes even in real time. They wanted more ad hoc queries to answer more business questions. To answer these questions, customers needed more powerful and efficient systems.
Batch processing typically involves querying large amounts of cold data. In batch processing, it may take hours to get answers to business questions. For example, you may use batch processing to generate a billing report at the end of the month. Stream processing in real time typically involves querying small amounts of hot data and it takes only a short amount of time to get answers. MapReduce-based systems such as Hadoop are examples of platforms that support the batch jobs category. Data warehouses are examples of platforms that support the query engine category.

[ 373 ]

Data Engineering and Machine Learning

Chapter 13

Streaming data processing activities ingest a sequence of data and incrementally update functions in response to each data record. Typically, they ingest continuously produced streams of data records, such as metering data, monitoring data, audit logs, debugging logs, website clickstreams, and location-tracking events for devices, people, and physical goods.
The following diagram illustrates a data lake pipeline for processing, transforming, and visualizing data using the AWS cloud tech stack:

Data lake ETL pipeline for big data processing
Here, the Extract, Transform, Load (ETL) pipeline uses Amazon Athena for ad hoc querying of data stored in Amazon S3. The data ingested from various data sources (for example, web application servers) generate log files that persist into S3. These files are then transformed and cleansed into a set form required for meaningful insights using Amazon Elastic MapReduce (EMR) and loaded into Amazon S3.
These transformed files are loaded into Amazon Redshift using the COPY command and visualized using Amazon QuickSight. Using Amazon Athena, you can query the data directly from Amazon S3 when the data is stored and also after transformation (that is, with aggregated datasets). You can visualize the data in Amazon QuickSight. You can easily query these files without changing your existing data flow.
Let's looks at some popular tools for data processing.
[ 374 ]

Data Engineering and Machine Learning

Chapter 13

Technology choices for data processing and
analysis
Following are some of the most popular data processing technologies, which help you to perform transformation and processing for a large amount of data:
Apache Hadoop uses a distributed processing architecture in which a task is mapped to a cluster of commodity servers for processing. Each piece of work distributed to the cluster servers can be run or re-run on any of the servers. The cluster servers frequently use HDFS to store data locally for processing. In the Hadoop framework, Hadoop takes a big job, splits it into discrete tasks, and process them in parallel. It allows for massive scalability across an enormous number of Hadoop clusters. It's also designed for fault tolerance, where each of the worker nodes periodically reports its status to a master node, and the master node can redistribute work from a cluster that doesn't respond positively. Some of the most popular frameworks used with Hadoop are Hive, Presto, Pig, and Spark.
Apache Spark is an in-memory processing framework. Apache Spark is a massively parallel processing system with different executors that can take apart a Spark job and run tasks in parallel. To increase the parallelism of a job, add nodes to the cluster. Spark supports batch, interactive, and streaming data sources. Spark uses directed acyclic graphs (DAGs) for all the stages during the execution of a job. The DAGs can keep track of the transformations of your data or lineage of the data during the jobs and efficiently minimizes the I/O by storing the DataFrames in memory. Spark is also partition-aware to avoid networkintensive shuffles.
Hadoop User Experience (HUE) enables you to run queries and scripts on your cluster through a browser-based user interface instead of the command line. HUE provides the most common Hadoop components in a user interface. It enables browser-based viewing and tracking of Hadoop operations. Multiple users can access the cluster via Hue's login portal, and administrators can manage access manually or with LDAP, PAM, SPNEGO, OpenID, OAuth, and SAML2 authentication. HUE allows you to view logs in real time and provides a metastore manager to manipulate Hive metastore contents.

[ 375 ]

Data Engineering and Machine Learning

Chapter 13

Pig is typically used to process large amounts of raw data before storing it in a structured format (SQL tables). Pig is well suited to ETL operations such as data validation, data loading, data transformation, and combining data from multiple sources in multiple formats. In addition to ETL, Pig also supports relational operations such as nested data, joins, and grouping. Pig scripts can use unstructured and semi-structured data (such as web server logs or clickstream logs) as input. In contrast, Hive always enforces a schema on input data. Pig Latin scripts contain instructions on how to filter, group, and join data, but Pig is not intended to be a query language. Hive is better suited to querying data. The Pig script compiles and runs to transform the data based on the instructions in the Pig Latin script.
Hive is an open source data warehouse and query package that runs on top of a Hadoop cluster. SQL is a very common skill that helps the team to make an easy transition into the big data world. Hive uses a SQL-like language called Hive Query language (HQL), which makes it easy to query and process data in a Hadoop system. Hive abstracts the complexity of writing programs in a coding language such as Java to perform analytics jobs.
Presto is a Hive-like query engine but it is much faster. It supports the ANSI SQL standard, which is easy to learn and the most popular skill set. Presto supports complex queries, joins, and aggregation functions. Unlike Hive or MapReduce, Presto executes queries in memory, which reduces latency and improves query performance. You need to be careful while selecting the server capacity for Presto, as it needs to have high memory. A Presto job will restart in the event of memory spillover.
HBase is a NoSQL database developed as a part of the open source Hadoop project. HBase runs on HDFS to provide non-relational database capabilities for the Hadoop ecosystem. HBase helps to store large quantities of data in columnar format with compression. Also, it provides a fast lookup because large portions of the data cache are kept in memory while cluster instance storage is still used.
Apache Zeppelin is a web-based editor for data analytics built on top of the Hadoop system, also known as Zeppelin Notebook. It uses the concept of an interpreter for its backend language and allows any language to be plugged into Zeppelin. Apache Zeppelin includes some basic charts and pivot charts. It's very flexible in terms of any output from any language backend that can be recognized and visualized.

[ 376 ]

Data Engineering and Machine Learning

Chapter 13

Ganglia is a Hadoop-cluster monitoring tool. However, you need to install Ganglia on the cluster during launch. The Ganglia UI runs on the master node, which you can see using an SSH tunnel. The Ganglia is an open source project designed to monitor clusters without impact on their performance. Ganglia can help to inspect the performance of the individual servers in your cluster and the performance of clusters as a whole.
JupyterHub is a multi-user Jupyter notebook. Jupyter notebooks are one of the most popular tools among data scientists to perform data engineering and ML. The JupyterHub notebook server provides each user with their Jupyter notebook web-based IDE. Multiple users can use their Jupyter notebooks simultaneously to write and execute code for exploratory data analytics.
Amazon Athena is an interactive query service for running queries on Amazon S3 object storage using standard ANSI SQL syntaxes. Amazon Athena is built on top of Presto and extends ad hoc query capabilities as a managed service. The Amazon Athena metadata store works like the Hive metadata store so that you can use the same DDL statements from the Hive metadata store in Amazon Athena. Athena is a serverless and managed service, which means all infrastructure and software handling and maintenance is taken care of by AWS and you can directly start running your query in the Athena web-based editor.
Amazon Elastic MapReduce (EMR) is essentially Hadoop in the cloud. You can utilize the Hadoop framework with the power of the AWS cloud using EMR. EMR supports all the most popular open source frameworks including Apache Spark, Hive, Pig, Presto, Impala, Hbase, and so on. EMR provides decoupled compute and storage which means you don't have to always keep running a large Hadoop cluster; you can perform data transformation and load results into persistent Amazon S3 storage and shut down the server. EMR provides autoscaling and saves you from the administrative overhead of installing and updating servers with various software.
AWS Glue is a managed ETL service, which helps in data processing, data cataloging, and ML transformations to find duplicate records. AWS Glue Data Catalog is compatible with the Hive data catalog and provides a centralized metadata repository across a variety of data sources including relational databases, NoSQL, and files. AWS Glue is built on top of a warm Spark cluster and provides ETL as a managed service. AWS Glue generates code in PySpark and Scala for common use cases, so that you are not starting from scratch to write ETL code. Glue job-authoring functionality handles any error in the job and provides logs to understand underlying permission or data formatting issues. Glue provides workflow, which helps you to build an automated data pipeline with simple drag and drop functionality.

[ 377 ]

Data Engineering and Machine Learning

Chapter 13

Data analysis and processing are huge topics that warrant a book on their own. In this section, you had a very high-level overview of popular and common tools used for data processing. There are many more proprietary and open source tools available. As a solution architect, you need to be aware of various tools available on the market to make the right choice for your organization's use case.
To identify data insights, business analysts can create reports and dashboards and perform ad hoc queries and analysis. Let's learn about data visualization in the next section.

Visualizing data
Data insights are used to answer important business questions such as revenue by customer, profit by region, or advertising referrals by site, among many others. In the big data pipeline, enormous amounts of data are collected from a variety of sources. However, it is difficult for companies to find information about inventory per region, profitability, and increases in fraudulent account expenses. Some of the data you continuously collect for compliance purposes can also be leveraged for generating business.
The two significant challenges of BI tools are the cost of implementation and the time it takes to implement a solution. Let's look at some technology choices for data visualization.
Technology choices for data visualization
Following are some of the most popular data visualization platforms, which help you to prepare reports with data visualization as per your business requirements:
Amazon QuickSight is a cloud-based BI tool for enterprise-grade data visualizations. It comes with a variety of visualization graph presets such as a line graphs, pie charts, treemaps, heat maps, histograms, and so on. Amazon QuickSight has a data-caching engine known as Super-fast, Parallel, In-memory Calculation Engine (SPICE), which helps to render visualizations quickly. You can also perform data preparation tasks such as renaming and removing fields, changing data types, and creating new calculated fields. QuickSight also provides ML-based visualization insights and other ML-based features such as auto forecast predictions.

[ 378 ]

Data Engineering and Machine Learning

Chapter 13

Kibana is an open source data visualization tool used for stream data visualization and log exploration. Kibana offers close integration with Elasticsearch and uses it as a default option to search for data on top of the Elasticsearch service. Like other BI tools, Kibana also provides popular visualization charts such as histograms, pie charts, and heat maps, and offers built-in geospatial support.
Tableau is one of the most popular BI tools for data visualization. It uses a visual query engine, which is a purpose-built engine, used to analyze big data faster than traditional queries. Tableau offers a drag and drop interface and the ability to blend data from multiple resources.
Spotfire uses in-memory processing for faster response times, which enables an analysis of extensive datasets from a variety of resources. It provides the ability to plot your data on a geographical map and share it on Twitter. With Spotfire recommendations, it inspects your data automatically and makes suggestions about how to best visualize it.
Jaspersoft enables self-service reporting and analysis. It also offers drag and drop designer capability.
PowerBI is a popular BI tool provided by Microsoft. It provides self-service analytics with a variety of visualization choices.
Data visualization is an essential and massive topic for solution architects. As a solution architect, you need to be aware of the various tools available and make the right choice as per your business requirements for data visualization. This section provided a very highlevel overview of popular data visualization tools.
As internet connectivity is increasing, there are small devices everywhere with small memory and compute capacities. These devices connect various physical entities and there is a need to collect and analyze data from millions of these connected devices. For example, weather data collected from various sensors can be utilized to forecast weather for wind energy and farming. Let's cover some more details about IoT, which is the growing global network of small interconnected devices.

[ 379 ]

Data Engineering and Machine Learning

Chapter 13

Understanding IoT
IoT refers to a network ecosystem of physical devices that have an IP address and are connected to the internet. While IoT devices are growing rapidly in number, growing with them is the complexity of leveraging your IoT devices correctly. IoT helps organizations to perform a variety of tasks such as predictive maintenance, monitoring connected buildings and city systems, energy efficiency monitoring, and safeguarding manufacturing facilities, among others. You need to ingest data from IoT sensors, store them for analysis either via streaming data or stored data, and provide results quickly.
These are some of the most critical challenges to any IoT device architecture. You need to ensure the security and management of devices. Cloud providers have managed service offerings to achieve scalability to millions of devices. Let's look into AWS IoT offerings to understand the working of IoT systems. Because IoT solutions can be complex and multidimensional, you need to remove the complexity of implementing IoT in the business and help customers to securely connect any number of devices to the central server.
The AWS cloud helps in processing and acting upon device data and reading and setting device state at any time. AWS provides the infrastructure to scale as needed, so organizations can gain insight into their IoT data, build IoT applications and services that better serve their customers, and help move their businesses toward full IoT exploitation. The following diagram illustrates the components of AWS IoT:

AWS IoT
[ 380 ]

Data Engineering and Machine Learning

Chapter 13

The following are details in each IoT component and how are they connected as shown in the preceding diagram:
IoT Greengrass: AWS IoT Greengrass is installed on edge devices and helps to send IoT message to the AWS cloud.
The IoT Device SDK: The AWS IoT Device SDK helps to connect IoT devices to your application. The IoT Device SDK provides an API to connect and authenticate devices to application. It helps to exchange messages between device and AWS IoT cloud services using the MQTT or HTTP protocols. The IoT Device SDK supports C, Arduino, and JavaScript.
Authentication and authorization: AWS IoT facilitates mutual authentication and encryption to exchange data with only authorized devices. AWS IoT uses authentication mechanisms such as SigV4 and X.509 certificates. You can attach authentication to all connected devices by attaching a certificate and handle authorization remotely.
IoT message broker: The message broker supports the MQTT and HTTP protocols and establishes secure communication between IoT devices and cloud services such as the AWS IoT Rules Engine, Device Shadows, and other AWS services.
The IoT Rules Engine: The IoT Rules Engine helps to setup managed data pipelines for IoT data processing and analytics. The Rules Engine looks at IoT data to perform streaming analytics and connect to other AWS storage services such as Amazon S3, DynamoDB, ElasticSearch, and so on.
Device Shadow Service: Device Shadow Service helps you to maintain a device's status when it is offline due to loss of network connectivity in a remote area. As soon as the device comes online, it can resume its state from Device Shadow. Any application connected to the device can continue working by reading data from the shadow using a RESTful API.
Device Registry: The Device Registry helps to identify IoT devices and helps to manage millions of devices at scale. The Registry stores device metadata such as the version, manufacturer, and reading method (Fahrenheit versus Celsius), and so on.
As of now, you've learned about various business analytics services that aim at answering questions about past events. But businesses also need to answer questions about the possibilities of future events, which is done using ML. Let's learn more details about ML.

[ 381 ]

Data Engineering and Machine Learning

Chapter 13

What is ML?
Let's say your company wants to send marketing offers to potential customers for a new toy launch and you have been tasked to come up with a system to identify whom to target for the marketing campaign. Your customer base could be millions of users to which you need to apply predictive analytics, and ML can help you to solve such a complex problem.
ML is about using technology to discover trends and patterns and compute mathematical predictive models based on past factual data. ML can help to solve complex problems such as the following:
When you may not know how to create complex code rules to make a decision. For example, if you want to recognize people's emotions in image and speech, there are just no easy ways to code the logic to achieve that. When you need human expertise to analyze a large amount of data for decisionmaking, but the volume of data is too large for a human to do it efficiently. For example, with spam detection, while a human can do it, the amount of data volume makes it impractical to quickly do this manually. When relevant information may only become available dynamically in cases where you need to adapt and personalize user behaviors based on individual data. Examples are individualized product recommendations or website personalization. When there are a lot of tasks with a lot of data available but you cannot track the information fast enough to make a rule-based decision--for example, in fraud detection and natural language processing.
Humans handle data prediction based on the results of their analyses and their experience. Using ML, you can train a computer to provide expertise based on available data and get a prediction based on new data.
The main idea behind ML is to make available a training dataset to an ML algorithm and have it predict something from a new dataset, for example, feeding some historical stock market trend data to an ML model and having it predict how the market will fluctuate in the next 6 months to 1 year.
In previous sections, you learned about the various tools to process the data. ML is all about data--the better quality the data you can feed in for training, the better the prediction you get. Let's learn how data science goes hand in hand with ML in the next section.

[ 382 ]

Data Engineering and Machine Learning

Chapter 13

Working with data science and ML
ML is all about working with data. The quality of the training data and labels is crucial to the success of an ML model. High-quality data leads to a more accurate ML model and the right prediction. Often in the real world, your data has multiple issues such as missing values, noise, bias, outliers, and so on. Part of data science is the cleaning and preparing of your data to get it ready for ML.
The first thing about data preparation is to understand business problems. Data scientists are often very eager to jump into the data directly, start coding, and start producing insights. However, without a clear understanding of the business problem, any insights you develop have a high chance of becoming a solution which is unable to address a problem. It makes much more sense to start with a clear user story and business objectives before getting lost in the data. After building a solid understanding of the business problem, you can begin to narrow down the ML problem categories and determine whether ML will be suitable to solve your particular business problem.
Data science includes data collection, analysis, preprocessing, and feature engineering. Exploring the data provides us with necessary information such as data quality and cleanliness, interesting patterns in the data, and likely paths forward once you start modeling.
As shown in the following diagram, data preprocessing and learning to create a ML model are interconnected--your data preparation will heavily influence your model, while the model you choose heavily influences the type of data preparation you will do. Finding the correct balance is highly iterative and is very much an art (or trial and error):

ML workflow
[ 383 ]

Data Engineering and Machine Learning

Chapter 13

As shown in the preceding diagram, the ML workflow includes the following phases:
Preprocessing: In this phase, the data scientist preprocesses the data and divides it into training, validation, and testing datasets. Your ML model gets trained with the training dataset to fit the model, and is evaluated using the validation dataset. Once the model is ready, you can test it using a testing dataset. Taking into the amount of data and your business case, you need to divide the data into training, testing, and validation sets, perhaps keeping 70% of the data for training, 10% for validation, and 20% for testing.
Features are independent attributes of your dataset that may or may not influence the outcome. Feature engineering involves finding the right feature, which can help to achieve model accuracy. The label is your target outcome, which is dependent on feature selection. To choose the right feature, you can apply dimensionality reduction, which filters and extracts the most effective feature for your data.
Learning: In the learning phase, you select the appropriate ML algorithm as per the business use case and data. The learning phase is the core of the ML workflow, where you train your ML model on your training dataset. To achieve model accuracy, you need to experiment with various hyperparameters and perform model selection. Evaluation: Once your ML model gets trained in the learning phase, you want to evaluate the accuracy with a known dataset. You use the validation dataset kept aside during the preprocessing phase to assess your model. Required model tuning needs to be performed as per the evaluation result if your model prediction accuracy is not up to the exceptions as determined by validation data. Prediction: Prediction is also known as inference. In this phase, you deployed your model and started making a prediction. These predictions can be made in real time or in batches.
As per your data input, often, the ML model can have overfitting or underfitting issues, which you must take into account to get the right outcome.

[ 384 ]

Data Engineering and Machine Learning

Chapter 13

Evaluating ML models � overfitting versus underfitting
In overfitting, your model fails to generalize. You will determine the overfitting model when it performs well on the training set but poorly on the test set. This typically indicates that the model is too flexible for the amount of training data, and this flexibility allows it to memorize the data, including noise. Overfitting corresponds to high variance, where small changes in the training data result in big changes to the results.
In underfitting, your model fails to capture essential patterns in the training dataset. Typically, underfitting indicates the model is too simple or has too few explanatory variables. An underfit model is not flexible enough to model real patterns and corresponds to high bias, which indicates the results show a systematic lack of fit in a certain region.
The following graph illustrates the clear difference between overfitting versus underfitting as they correspond to a model with good fit:

ML model overfitting versus underfitting
In the preceding graphs, the ML model is trying to categorize between two data point categories illustrated by the red points and green crosses. The ML model is trying to determine whether a customer will buy a given product or not. The graph shows predictions from three different ML models. You can see an overfitted model (on the right) traversing through all red data points in training and failing to generalize the algorithm for real-world data outside of the training dataset. On the other hand, the underfitted model (on the left) leaves out several data points and produces an inaccurate result. A good model (shown in the middle) provides clear predictions of the data points in most of the cases. Creating a good ML model is like creating art and you can find the right fit with model tuning.
[ 385 ]

Data Engineering and Machine Learning

Chapter 13

The ML algorithm is at the heart of the overall ML workflow, which is categorized into supervised and unsupervised learning.

Understanding supervised and
unsupervised ML
In supervised learning, the algorithm is given a set of training examples where the data and target are known. It can then predict the target value for new datasets, containing the same attributes. For supervised algorithms, human intervention and validation are required, for example, in photo classification and tagging.
In unsupervised learning, the algorithm is provided with massive amounts of data, and it must find patterns and relationships between the data. It can then draw inferences from datasets.
In unsupervised learning, human intervention is not required, for example, autoclassification of documents based on context. It addresses the problem, where correct output is not available for training examples, and the algorithm must find patterns in data using clustering.
Reinforcement learning is another category where you don't tell the algorithm what action is correct, but give it a reward or penalty after each action in a sequence, for example, learning how to play soccer.
Following are the popular ML algorithm types used for supervised learning:
Linear regression: Let's use the price of houses as a simple example to explain linear regression. Say we have collected a bunch of data points that represent the prices of houses and the sizes of the houses on the market, and we plot them on a two-dimensional graph. Now we try to find a line that best fits these data points and use it to predict the price of a house of a new size. Logistic regression: Estimates the probability of the input belonging to one of two classes, positive and negative. Neural networks: In a neural network, the ML model acts like the human brain where layers of nodes are connected to each other. Each node is one multivariate linear function, with a univariate nonlinear transformation. The neural network can represent any non-linear function and address problems that are generally hard to interpret, such as image recognition. Neural networks are expensive to train but fast to predict.

[ 386 ]

Data Engineering and Machine Learning

Chapter 13

K-nearest neighbors: It chooses the number of k neighbors. Find the k-nearest neighbors of the new observation that you want to classify and assign the class label by majority vote. For example, you want to categorize your data in five clusters, so your k value will be five. Support Vector Machines (SVM): Support vectors are a popular approach in research, but not so much in industry. SVMs maximize the margin, the distance between the decision boundary (hyperplane), and the support vectors (the training examples closest to the boundary). SVM is not memory efficient because it stores the support vectors, which grow with the size of the training data. Decision trees: In a decision tree, nodes are split based on features to have the most significant Information Gain (IG) between the parent node and its split nodes. The decision tree is easy to interpret and flexible; not many feature transformations are required. Random forests and ensemble methods: Random forest is an ensemble method where multiple models are trained and their results combined, usually via majority vote or averaging. Random forest is a set of decision trees. Each tree learns from a different randomly sampled subset. Randomly selected features are applied to each tree from the original features sets. Random forest increases diversity through the random selection of the training dataset and a subset of features for each tree, and it reduces variance through averaging.
K-means clustering uses unsupervised learning to find data patterns. K-means iteratively separates data into k clusters by minimizing the sum of distances to the center of the closest cluster. It first assigns each instance to the nearest center and then re-computes each center from assigned instances. Users must determine or provide the k number of clusters.
Zeppelin and Jupyter are the most common environments for data engineers doing data discovery, cleansing, enrichment, labeling, and preparation for ML model training. Spark provides the Spark ML library, containing implementations of many common high-level estimator algorithms such as regressions, page rank, k-means, and more.
For algorithms that leverage neural networks, data scientists use frameworks such as TensorFlow and MxNet, or higher-level abstractions such as Keras, Gluon, or PyTorch. Those frameworks and common algorithms can found in the Amazon SageMaker service, which provides a full ML model development, training, and hosting environment.
Data scientists leverage the managed Jupyter environment to do data preparation, set up a model training cluster with a few configuration settings, and start their training job. When complete, they can one-click-deploy the model and begin serving inferences over HTTP. ML model development is performed almost exclusively these days on files in HDFS, and thus querying the Amazon S3 Data Lake directly is the perfect fit for these activities.

[ 387 ]

Data Engineering and Machine Learning

Chapter 13

Machine learning is a very vast topic and warrants a full book to understand in more detail. In this section, you just learned about an overview of machine learning models.

Summary
In this chapter, you learned about big data architecture and components for big data pipeline design. You learned about data ingestion and various technology choices available to collect batch and stream data for processing. As the cloud is taking a central place in storing the vast amounts of data being produced today, so you learned about the various services available to ingest data in the AWS cloud ecosystem.
Data storage is one of the central points when it comes to handling big data. You learned about various kinds of data stores, including structured and unstructured data, NoSQL, and data warehousing, with the relevant technology choices associated with each. You learned about data lake architecture and benefits.
Once you collect and store data, you need to perform data transformation to get insight into that data and visualize your business requirements. You learned about data processing architecture along with technology choices to choose open source and cloud-based data processing tools as per your data requirements. These tools help to get data insight and visualization as per the nature of your data and organizational requirements.
Now, there are millions of small devices connected to the internet, referred to collectively as the IoT. You learned about the various components available in the cloud to collect, process, and analyze IoT data to produce meaningful insights. You learned about the ML workflow, which includes data preprocessing, modeling, evaluation, and prediction. Also, you learned about supervised and unsupervised learning with an overview of various popular ML algorithms and available ML frameworks.
With time, organizations tend to accumulate the technology debt, and many legacy applications are sitting in the data center, creating costs and consuming resources. In the next chapter, you will learn about legacy application transformation and modernization. You will learn about challenges with legacy systems and the techniques used to modernize them.

[ 388 ]

14
Architecting Legacy Systems
Legacy systems are the applications that have been deployed in your data center for decades without undergoing many changes. In a fast-changing technology environment, these systems get outdated and are challenging to maintain. Legacy systems are not only defined by their age but sometimes by their inability to meet growing business needs, due to the underlying architecture and technology.
Often, large enterprises deal with legacy applications to run crucial day-to-day business tasks. These legacy systems are spread across industries such as healthcare, finance, transportation, and supply chain industries, and so on. Companies have to spend heavily on maintenance and support of these systems, which warrants the need to architect legacy systems. Rearchitecting and modernizing legacy applications helps organizations to be more agile and innovative, and also optimizes cost and performance.
In this chapter, you will learn about challenges and issues with legacy applications, and techniques to rearchitect them. Rewriting complex legacy applications may pose an additional risk of business disruption, so you will learn about refactoring applications or considering the option to migrate into a more flexible infrastructure. The following major topics will be covered in this chapter:
Learning the challenges of legacy systems Defining a strategy for system modernization Looking at legacy system modernization techniques Defining a cloud migration strategy for legacy systems
By the end of the chapter, you will have learned about various challenges and modernization drivers for legacy systems. You will learn various strategies and techniques for the modernization of legacy systems. As the public cloud is becoming a go-to strategy for many organizations, you will learn about cloud migration of legacy systems.

Architecting Legacy Systems

Chapter 14

Learning the challenges of legacy systems
A legacy application puts significant challenges in front of an organization. On the one hand, there are critical applications that an organization has been using for decades, and, on the other hand, there are legacy applications holding back the organization's pace of innovation.
Now, in a huge competitive environment, the end users are looking for the most modern, technologically advanced applications. All new features usually come with the latest software, and legacy applications limit your ability to add those features and provide benefits to end users. The following diagram shows some significant challenges that organizations are facing with legacy systems:

Challenges with a legacy system
As illustrated, the following points are the significant challenges that you will face with legacy systems:
Difficulty in keeping up with user demand Higher cost of maintenance and update Shortage of skills and documentation Vulnerable to corporate security issues Incompatibility with other systems Before we dive into the solution, it's better to understand the issues clearly. Let's explore more about the challenges of a legacy system to understand these better.
[ 390 ]

Architecting Legacy Systems

Chapter 14

Difficulty in keeping up with user demand
Customer focus is the key to business success, and being unable to keep up with the latest technology trends can harm a business significantly. You can take the example of Nokia mobile phones, which used to lead the world mobile-phone market. As smartphones came into play nearly a decade ago, Nokia still stuck with a legacy system, and this resulted in near bankruptcy. It was a similar story with Kodak--one of the largest businesses in the photo-camera industry. Kodak was unable to move with digital innovation and adopt this into its systems, which resulted in Kodak becoming bankrupt in 2012. There are many such examples where large enterprises have been unable to survive due to a lack of legacy modernization and innovation.
In the current climate of fast-changing technology and fierce competition, users are very demanding. Now, organizations have to change as per the user's terms, as they have multiple demands. As technology moves, the user moves with it and starts using the most recent and popular app. Your competitor can jump ahead if they are providing new features as per the user demand.
A legacy system also poses challenges for enterprise applications with an internal user base. An old system that was built on mainframes mostly uses the command line, which is not very user-friendly in the digital age, whereas new-generation workers demand a more user-friendly system to perform their routine tasks. However, you may face significant resistance from management, who may have been working with legacy systems for decades and are settled with this.

Higher cost of maintenance and update
As legacy systems have been all set up and working for decades, they may look less expensive. But over time, the total cost of ownership turns out to be higher, as support and updates of older systems are usually more costly. Often, those updates are not available out of the box, and lots of manual workarounds are required to maintain the system. Most legacy systems are not very automation-friendly, resulting in more human effort.
Legacy systems mostly have a large chunk of proprietary software, which results in significantly higher license fees. In addition to that, older software no longer receives support from providers, and buying additional support out of the life cycle could be very costly. On the other hand, modern systems mostly adopt open source technologies that drive the cost down. The operational outage from a legacy system can take more time to recover from and drives up operational expenses. People with the skill set to maintain legacy systems (such as DB2, COBOL, Fortran, Delphi, Perl, and so on) are hard to find, which can increase hiring costs and system risk significantly.
[ 391 ]

Architecting Legacy Systems

Chapter 14

Legacy systems are pretty significant in the aspect of code. Unused code adds another layer of unnecessary maintenance and complexity to a system. Legacy applications have been in operation for decades, and over time, many new changes will have been accommodated without code being cleaned, which amounts to lots of technical debt. Any initiative to reduce technical debt could be risky due to unknown impacts and dependencies. As a result, organizations are forced to invest in unnecessary code and system maintenance due to fear of breaking the system by making any major changes.
However, modernizing legacy systems may be costly due to unknown dependencies and outages. Careful cost-benefit analysis (CBA) needs to be taken into consideration, along with determining the return on investment (ROI) when deciding to proceed with modernization. As stakeholders don't see the immediate benefit of modernization, procuring finances for legacy modernization can be challenging.

Shortage of skills and documentation
Legacy technologies (such as mainframes) have multiple complex components that depend on each other. These are extensive proprietary and costly servers that are not readily available if someone wants to develop skills on their own. It is challenging to retain application-development resources, and even more challenging to hire people with handson experience in old technology and operating systems.
Often, legacy systems are two or more decades older, and most of the workforce with those skills has retired. Also, these systems don't have the proper documentation to keep up the record of years of work. There are chances of significant knowledge loss as an older workforce rotates with a newer workforce. A lack of knowledge makes it riskier to change the system due to unknown dependencies. Any small feature requests are challenging to accommodate, due to system complexity and skill-set shortages.
New cutting-edge technologies such as big data, machine learning, and Internet of Things (IoT) mostly build around new technology platforms. As new technologies are not well integrated with legacy systems, an organization may lose out to a competitor if not able to use the full capabilities of emerging technologies. A modern system helps to build an organization brand as an innovative company where most of the new generation of the workforce wants to work, and they lose interest in working with a legacy system. Development and training is an even more significant source of expense for legacy technologies.

[ 392 ]

Architecting Legacy Systems

Chapter 14

Often, automation helps to reduce costs by reducing human effort. There are many tools available around modern systems to build automation--such as DevOps pipelines, code review, and automation testing--that a legacy system may not be able to utilize, resulting in additional cost.

Vulnerable to corporate security issues
Security is the top priority for any organization and system. A legacy application that runs on an old operating system (such as Windows XP or Windows 2008) is more vulnerable to security issues due to lack of vendor support. Software vendors continuously determine new security threats and release patches to accommodate them in the latest software version, to secure them. Any legacy software that is announced as End of Life (EOL) from a vendor doesn't get a new security patch, which leaves your application running in the old software version, exposed to a number of security threats.
System health checks are often ignored for legacy applications, which make them more vulnerable to be the target of security attacks. The skills gap makes it difficult to provide continuous support and help, which means systems are run in an insecure manner. A single vulnerability can pose a high risk of exposing your application, database, and critical information to attackers.
In addition to a security vulnerability, legacy applications are hard to maintain due to compliance. As compliances keep changing with time to enforce more tight security around data handling and usage, legacy systems require changes to adhere to local governance and compliance needs.
For example, the new European Union's General Data Protection Regulation (GDPR) compliance requires each system to avail features where a user can request to delete their data. While modern systems can provide these features out of the box in an automated and self-service manner, in legacy systems this may need to be performed manually and becomes more complex. Adhering to compliance needs can lead to more operation costs and time-consuming maintenance.

[ 393 ]

Architecting Legacy Systems

Chapter 14

Incompatibility with other systems
In addition to end users, every system needs to integrate with other IT systems. Those systems may be a part of different departments, clients, partners, or suppliers. The various systems need to exchange data in a standard format that evolves over time. Almost every few years, files and data format standards get changed to increase data exchange efficiency, and most systems require changes to adopt these. Hard-to-change legacy systems that stick to using an old format could result in system incompatibility and a system that your supplier and partner may not want to use. The inability to accommodate standard needs adds greater risk to businesses due to complex workarounds and lost productivity.
Adding a workaround for simple business needs may make a system more complex. Modern systems are built on a service-oriented architecture, which makes it easier to accommodate any new requirement by adding a new service independently. Old systems are often built on a monolithic architecture, and adding any new feature means you need to rebuild and test the entire system.
Modern architectures are API-oriented and can be easily integrated with another system to offload heavy lifting. For example, a taxi-booking app uses Google Maps for Global Positioning System (GPS) navigation or Facebook and Twitter for user authentication. A lack of APIs makes these integrations harder in a legacy system, resulting in complex custom code.
As more load increases from another dependent upstream system, a legacy application can face a scalability issue. Often, legacy applications are built on a monolithic architecture and are hardware-dependent. Scalability is a big challenge with a monolithic system, as it cannot scale horizontally due to hardware dependency and vertical scaling being limited to the maximum system capacity. Breaking monolithic applications into microservices can solve scaling challenges and help keep up with demand.
In addition to software maintenance, legacy applications are also costly for hardware infrastructure as they run on a particular version. They spread across multiple databases with duplicate data and similar functionality. Due to their monolithic nature, it's hard to perform consolidation and use the flexibility of cloud-based infrastructure to save costs. Let's look at the approach to the modernization of legacy systems.

[ 394 ]

Architecting Legacy Systems

Chapter 14

Defining a strategy for system modernization
Often, a legacy system gets left out of an overall enterprise digital strategy, and issues get addressed on a need basis. Taking a reactive approach holds back organizations from executing overall system modernization and benefits.
If your legacy system has serious business challenges such as security and compliance issues or is unable to address the business need, you can take a big-bang approach. In the big-bang method, you can build a new system from scratch and shut down the old system. This approach has more risk but addresses a business need that can be mitigated from the existing legacy system.
The other approach you can take is a phased approach, where you upgrade one module at a time and keep running both old and new systems. A phased approach has less risk but takes a long time and may be more expensive as you need to maintain both environments, with additional network and infrastructure bandwidth.
Taking any of these approaches can provide various benefits once the modernization of an application is completed. Let's look at some critical benefits of system modernization.

Benefits of system modernization
Creating a future digital strategy by addressing the growing need for legacy system modernization can have many advantages, as shown in the following diagram:

Benefits of legacy system modernization
[ 395 ]

Architecting Legacy Systems

Chapter 14

The following are the significant benefits of an application modernization:
Customer satisfaction: Using the latest technology gives a better user interface (UI) and omnichannel experience. You don't need to build different variations of the UI; it can be built once and deployed across devices such as laptops, tablets, and smartphones. A fast and slick UI leads to better customer experience and business growth.
Future-proof business strategy: Your application modernization allows you to be more agile and innovative. The team can accommodate the changing needs of the business comfortably and evolve with new technology.
Stay ahead of the competition: Users always looking for the latest stuff and tend to move into the new application, which gives a better experience. The modernization of your application helps you to stay ahead of the competition by adding the latest trends. For example, voice integration is extensively being provided in apps, and you can enhance security with face detection. This is only possible when your application is adopting the latest technology.
Applicating reliability and performance: Every new version of a software API and an operating system tries to address and improve performance issues. Using the latest software and hardware helps you to achieve better performance, scalability, and high availability. Application modernization helps you to reduce operational outage and enhance security.
Ability to use cutting-edge technology: Legacy systems prevent you from getting insight from data that could help you to grow your business significantly. By modernizing your database and creating a data lake, you can perform big data and machine learning to get all kinds of insight. This also helps you to retain employees when people get the opportunity to work in new technologies.
Cost saving: Overall, any modernization leads to cost-saving by reducing operational maintenance and providing a more natural upgrade. Utilization of open source software reduces licensing costs, hardware flexibility helps to adopt a cloud pay-as-you-go model, and automation helps to reduce the human resources needed for routine jobs and improves overall efficiency.
However, there are several benefits of legacy system modernization, but these could be very complex and require lots of effort. A careful assessment needs to be conducted to take the right approach. Let's explore more on the assessment techniques of a legacy application.

[ 396 ]

Architecting Legacy Systems

Chapter 14

Assessment of a legacy application
There may be multiple legacy systems in an organization, with tens of thousands, to millions, of lines of code. In a modernization approach, a legacy system needs to align with the business strategy and the initial cost of investment. Also, there is a possibility to reutilize some parts of it or completely write it from scratch, but the first step is to conduct the assessment and understand the overall system better. The following points are the primary areas that solution architects need to focus on when conducting an assessment:
Technology assessment: As a solution architect, you need to understand the technology stack used by the existing system. If the current technology in use is entirely outdated and lacks vendor support, then you might need to replace it entirely. In the case of a better version of the technology being available, then you can consider upgrading. Often, newer versions are backward-compatible, with minimal changes required.
Architecture assessment: You need to understand the overall architecture to make it future-proof. There may be a case where you determine a minor upgrade in the technology, but the overall architecture is monolithic and not scalable. You should audit the architecture in the aspects of scalability, availability, performance, and security. You may find significant architecture changes are required to align the application with business needs.
Code and dependency assessment: Legacy systems often have 100,000 lines of code in a monolithic setting. Various modules tied to each other make the system very complicated. The code appears not to be in use in one module might impact some other modules if removed without much due diligence. These code lines may have been written decades back and have missed regular refactoring and review. Even if the technology and architecture look fine, you need to determine if the code is upgradable and maintainable. We also need to understand if any UI-related upgrade is required to make the user experience better.
As a solution architect, you want to determine dependencies across various modules and code files. Modules may tightly couple, and you need to define an approach to perform simultaneous upgrades when modernizing the overall architecture.

[ 397 ]

Architecting Legacy Systems

Chapter 14

Defining the modernization approach
For stakeholders, there may be no immediate incentive for application modernization. You need to choose the most cost-effective method and deliver results faster. The following diagram shows the modernization approach:

Legacy system modernization approach
After your system assessment, you need to understand the existing architecture pattern and limitations. As per your tech stack, you need to evaluate migration tools. For example, you may choose to use an emulator for mainframe migration or vCenter if rehosting your application to VMware. You can select various modernization approaches and create a proof of concept (POC) to identify any gaps. Some approaches are listed here:
Architecture-driven modernization: Architecture-driven approach requires to achieve the most agility. Often, an architectural approach is languageindependent and platform-independent by applying service-oriented patterns, which gives the development team the flexibility to be more innovative. You may want to choose this approach if you determine significant architectural changes from your assessment. Start implementing the most critical feature first, and build a POC to decide on gaps and effort required. Take the microservices approach to achieve scalability and ensure better integration with other systems, depending on the system. System re-engineering: In the re-engineering approach, the solution architect needs to understand the legacy system deeply and perform reverse engineering to build a new modernized application. You need to be sure to make technology choices that help you to create a future-proof system. You may want to take this approach if the legacy system is over-complicated and requires long-term projects. Start with application modernization first and upgrade the database as a final cutover in a phased approach. You need to build a mechanism where both legacy and upgraded modules co-exist, with the ability to communicate in a hybrid manner.
[ 398 ]

Architecting Legacy Systems

Chapter 14

Migration and enhancements: You can take migration and minor enhancement approaches if your existing system technology works relatively well but is restricted due to hardware limitation and cost. For example, you can lift and shift the entire workload to the cloud for better infrastructure availability and cost optimization. In addition to that, a cloud provider extends several out-of-the-box tools, which helps you to make changes more frequently and apply better automation. A migration approach helps you to modernize your application with less effort and makes it future-proof, where it stays relevant for the long term. However, lift and shift has its limitations, and may not be suited for all kinds of workload.

Documentation and support
For the long-term sustainability of a new system and graceful migration to it, make sure to prepare proper documentation and support. Document your coding standards, which everyone can follow and which helps to keep the new system up to date. Keep your architecture documents as working artifacts and keep them updated as technology trends change. Keeping your system up to date will ensure that you don't fall into the legacy system modularization situation again.
Prepare a comprehensive runbook to support new and old systems. You may want to keep the old system for some time until the new system can accommodate all business requirements and run satisfactorily. Update the support runbook, and make sure that you don't lose knowledge due to employee attrition, and that the overall knowledge base is not processed in a people-dependent manner.
Keeping track of system dependencies helps you to determine the impact of any changes in the future. Prepare training content to train staff on the new system and make sure they can support it in case of an operational outage.

[ 399 ]

Architecting Legacy Systems

Chapter 14

Looking at legacy system modernization
techniques
As per your existing application analysis, you can take a different approach to upgrade your legacy system. The most straightforward approach will be migration and rehosting, where you don't need to make many changes in the existing system. However, a simple migration may not solve the long-term problem or provide a benefit. You can take a more complex approach, such as rearchitecting or redesigning the entire application if the system is no longer meeting the business need. The following diagram illustrates the effort and impact of the various methods:

Legacy system modernization techniques
Let's look in more detail at the various modernization techniques shown in the preceding diagram.
Encapsulation, rehosting, and re-platforming
Encapsulation is the simplest approach, and you may want to take this if the system is business-critical and needs to communicate with other applications running on the latest technology. In the encapsulation approach, you need to build an API wrapper around your legacy system, which will allow other business applications to communicate with a legacy application. An API wrapper is a common approach whereby you start migrating your applications to the cloud but need to keep the legacy application in the on-premises data center for modernization in the later phase. You can choose the encapsulation option if your legacy code is well written and maintained, but, again, you will not be able to get the benefit of technology advancement and hardware flexibility.
[ 400 ]

Architecting Legacy Systems

Chapter 14

The rehosting approach is also among the most straightforward approaches, whereby you want to migrate your application into another hardware provider such as the Cloud without any changes in code. Again, as with encapsulation, the rehosting option can save some cost due to vendor contracts but may not give you benefits from technology advancement and hardware flexibility. An organization often takes this approach when it needs to move out of an existing contract quickly. For example, you can take the first step to the cloud in phase one and go for application modernization in phase two.
The re-platforming approach may get a bit more complex than the rehosting approach and provides the immediate benefit of a new operating system. Organizations often choose this approach if the server is going End of Life (EOL), where no support is available and an upgrade becomes necessary to handle security issues. For example, if Windows Server 2008 is going EOL, you may want to upgrade the operating system to the Windows 2012 or 2016 version. You need to rebuild your binaries with the new operating system and perform testing to make sure everything works properly, but there are no significant changes in the code as such. Again, as with rehosting, re-platforming may not give you benefits from technology advancement. However, it will allow you to have continuous support from the vendor.
While the preceding three approaches are the simplest ones, they are not able to provide the full benefit of the application upgrade. Let's look at approaches that help you to take full advantage of application modernization.

Refactoring and rearchitecting
In the refactoring approach, you can refactor your code to accommodate the new system. In refactoring, the overall architecture will be the same, yet you are upgrading your code to make it more suited for the latest version of the programming language and operating system. You can refactor the portion of code to apply automation and perform feature enhancement. You may want to take this approach if your technology is still relevant and able to accommodate business needs with code changes.
In the rearchitecting approach, you decide to change the system architecture by reutilizing the existing code as much as possible. For example, you want to create a microservices architecture out of your existing monolithic architecture. You can take one module at a time and convert it into a service-oriented architecture by giving each module a RESTful endpoint. The rearchitecting option helps you to achieve the desired scalability and reliability; however, overall performance results may be average due to the reutilization of existing code.

[ 401 ]

Architecting Legacy Systems

Chapter 14

Redesigning and replacing
The redesigning approach is most complex but provides maximum benefit. You can choose this approach if the legacy system is completely outdated and is not able to accommodate business needs at all. With redesigning, you need to build the entire system from scratch while keeping the overall scope intact. The following diagram shows the legacy mainframe system migration to AWS Cloud:

Legacy mainframe system modernization to the cloud
Here, a legacy mainframe system is rearchitected and refactored to similar cloud services as a modernization approach. Building a cloud-native application helps you utilize and fully benefit from cloud services in aspects of scalability, performance, reliability, and cost. It helps your team to be more agile and innovative by accommodating rapidly changing technology in your system.
[ 402 ]

Architecting Legacy Systems

Chapter 14

Redesigning a legacy system requires a long-term project with lots of effort and increased cost. Before kicking off a large modernization effort, as a solution architect, you should do careful analysis if any Software-as-a-Service (SaaS) product or commercially available offthe-shelf (COTS) products are able to handle your business need with relatively lower cost. It is essential to do a CBA for redesign versus purchase before proceeding with the redesigning option.
Sometimes, it's more beneficial to replace the existing legacy system with new third-party software. For example, your organization may have a decade-old Customer Relationship Management (CRM) system that is not able to scale and provide the desired feature. You may look for the option to subscribe to SaaS products such as Salesforce CRM to replace the legacy system. SaaS products are subscription-based and offer per-user licenses, so they may be the right choice if you have a smaller number of users. For a vast enterprise with thousands of users, it may be more cost-effective to build its application. You should conduct a CBA to understand ROI when investing in SaaS products.

Defining a cloud migration strategy for
legacy systems
As the cloud is becoming ever-more popular, more organizations are looking to migrate into the cloud for their legacy application modernization needs. You learned about various cloud migration techniques in Chapter 5, Cloud Migration and Hybrid Cloud Architecture Design. Cloud provides you with the flexibility to scale your application while keeping costs low and helps to achieve desirable performance, high availability, and reliability while maintaining application security.

[ 403 ]

Architecting Legacy Systems

Chapter 14

Cloud providers such as Amazon Web Services (AWS) provide many options out of the box, which can help you to modernize your system. For example, you can take a serverless approach to build a microservice using the AWS Lambda function and Amazon API Gateway, using Amazon DynamoDB as a backend. We discussed various legacy system modernization techniques in the previous section, as well as all of the applications in the context of moving to the cloud. The flow illustrated in the following diagram will help you decide whether to use cloud migration to modernize your legacy application:

Cloud migration path for legacy system modernization
As shown in the preceding diagram, if your application is still heavily used by businesses and is generating revenue, you may want to continue with minimal changes. In that situation, you can refactor your application into the cloud or you can re-platform it into the cloud if the server is going EOL.
[ 404 ]

Architecting Legacy Systems

Chapter 14

In case you don't want to make any changes in existing applications to sustain business, and still want to move to the cloud entirely to save and optimize costs, then take the lift and shift approach to rehost the legacy application in the cloud. If your legacy application is replaceable, then you can buy a cloud-native SaaS version of the product and retire your legacy application. Sometimes, you may want to retain your legacy system in the onpremises data center if there are too many business dependencies and it cannot move into the cloud due to incompatibility.
You should perform a total cost of ownership (TCO) analysis to understand the advantages of moving to the cloud. It is recommended to take the most complex module of the legacy application and build a POC to make sure your entire system will be cloudcompatible before starting the full project. A detailed POC that covers the critical business cases will help you to identify any gaps and reduce migration risk significantly.

Summary
In this chapter, you learned about various challenges with legacy applications and why it is essential to modernize your legacy application. You learned about different benefits an organization can get by upgrading their application into the latest technology. Application modernization can be a complicated and risky task but is often worth the effort.
The outcome you get from the upgrade is a trade-off for the amount of investment and energy you put into it. Before defining the modernization approach, it's essential to understand your legacy system thoroughly. You learned various assessment attributes of an application in the aspects of technology, architecture, and code.
After the assessment, the next step is to define the modernization approach. You learned about various modernization approaches, including architecture-driven, system reengineering, and migration approaches. You also learned about multiple techniques of system modernization, which included the simplest approaches (encapsulation and rehosting) and complex approaches (rearchitecting and redesigning). Cloud can provide a significant value proposition, and you learned about the decision-making approach you need to take for modernization on the cloud.
You focused on the various technical aspects of solution architecture; however, documentation is one of the critical elements of architecture design to keep your system maintainable in the long run. In the next chapter, you will learn about various documentation required for a solution architect to prepare, contribute, and maintain to maximize business value.

[ 405 ]

15
Solution Architecture Document
In previous chapters, you learned about various aspects of solution architecture design and optimization. As the solution architect works on the design, it is important to have consistent communication for successful application delivery. The solution architect needs to communicate a solution design to all technical and non-technical stakeholders.
The Solution Architecture Document (SAD) provides an end-to-end view of application and helps everyone to be on the same page. In this chapter, you will learn about various aspects of the SAD, which addresses the need for all stakeholders associated with the development of the application.
You will learn about the structure of the SAD and other types of documents of which the solution architect needs to be aware, such as the request for proposal (RFP), where the solution architect needs to provide input to make strategic decisions. You will learn the following topics to gain a deeper understanding of the documentation involved in solution architecture:
Purpose of the SAD Views of the SAD Structure of the SAD IT procurement documentation for a solution architecture
By the end of this chapter, you will learn about the SAD, its structure, and the various details that need to be accommodated in the documentation. You will learn about various IT procurement documentation such as the RFP, the request for information (RFI), and the request for quotation (RFQ), in which a solution architect participates to provide feedback.

Solution Architecture Document

Chapter 15

Purpose of the SAD
The need for architecture documentation often gets ignored, and teams start working on implementation without understanding the overall architecture. A SAD provides a broad view of the overall solution design to keep all stakeholders informed.
The SAD helps to achieve the following purposes:
Communicate the end-to-end application solution to all stakeholders. Provide high-level architecture and different views of the application design to address the application's service-quality requirements such as reliability, security, performance, and scalability. Provide traceability of the solution back to business requirements and look at how the application is going to meet all functional and non-functional requirements (NFRs). Provide all views of the solution required for design, build, testing, and implementation. Define the impacts of the solution for estimation, planning, and delivery purposes. Define the business process, continuation, and operations needed for a solution to work uninterrupted after the production launch.
SADs not only define the purpose and goal of the solution but also address critical components such as solution constraints, assumptions, and risks that often get overlooked by the implementation team. The solution architect needs to make sure they create the document in an easy language that business users can understand and relate business context with technical design. Documentation helps to retain knowledge due to resource attrition and makes the overall design process a people-independent one.
For existing applications where modernization effort is needed, a SAD presents an abstract view of current and future architecture, along with a transition plan. The solution architect understands the existing system dependencies and documents them to uncover any potential risk in advance. The migration plan helps businesses to understand the tools and technology required to handle the new system and plan resources accordingly.

[ 407 ]

Solution Architecture Document

Chapter 15

During solution design, the solution architect conducts various assessments by building a proof of concept (POC) or through market research. A SAD should list all architecture assessments and their impact, along with the choice of technology. A SAD presents a conceptual view of the current and target state of the solution design and maintains a record of change. Let's understand various aspects of a SAD, in the next section.

Views of the SAD
The solution architect needs to create a SAD in such a way that it should be understandable by both business users and technical users. A SAD bridges the communication gap between the business user and the development team to understand the function of the overall application. The best way to capture all stakeholders' input is by putting yourself in their situation and looking at problems from the stakeholders' perspective. The solution architect evaluates both the business and technical aspects of architecture design so that they can take cognizance of all technical and non-technical users' requirements.
As illustrated in the following diagram, the holistic view of the SAD comprises of various views derived from business requirements, to cover different aspects:

SAD views
[ 408 ]

Solution Architecture Document

Chapter 15

Solution architects can choose standard diagrams such as a Unified Modeling Language (UML) diagram or a block diagram from Microsoft Visio to represent various views. Overall, the diagram should be easy to read and understandable by all business and technical stakeholders. A SAD should include the following views, wherever possible, to address everyone's needs:
Business View: Architecture design is all about addressing business concerns and solving business purposes. The Business View shows the value proposition of the overall solution and product. To simplify, the solution architect may choose to detect high-level scenarios related to business and present these as a use-case diagram. The Business View also describes stakeholders and the required resources to execute the project. You can define the Business View as a use-case view as well.
Logical View: This presents various packages on the system so that business users and designers can understand the various logical components of the system. The logical view offers a chronicled order of the system in which it should build. It shows how the multiple packages of the system are connected and how the user can interact with them. For example, in a banking application, the user first needs to authenticate and authorize using a security package, and then log in to the account using the account package, or apply for a loan using a loan package, and so on. Here, each package represents a different module and can be built as a microservice.
Process View: This presents more details, showing how the key processes of the system work together. It can be reflected using a state diagram. The solution architect can create a sequence diagram if you want to show more details. In a banking application, a process view can present the approval of a loan or account.
Deployment View: This presents how the application is going to work in the production environment. It shows how different components of the system (such as network firewall, load balancer, application servers, database, and so on) are connected. The solution architect should create a simple block diagram that business users can understand. You can add more details to the UML deployment diagram to show various node components and their dependencies for technical users, such as the development and DevOps teams. The deployment view represents the physical layout of the system.

[ 409 ]

Solution Architecture Document

Chapter 15

Implementation View: This is the core of the SAD, and represents architectural and technology choices. The solution architect needs to put the architecture diagram here--for example, if it is 3-tier, N-tier, or event-driven architecture, along with the reasoning behind it. You also need to detail technology choices--for example, using Java versus Node.js, along with the pros and cons of using them. You want to justify the resources and skills required to execute the project in the implementation view. The development team uses an implementation view to create a detailed design such as a class diagram, but that doesn't need to be part of the SAD.
Data View: As most applications are data-driven, this makes the data view important. The data view represents how data is going to flow between the different components and how it will be stored. It can also be used to explain data security and data integrity. The solution architect can use the entityrelationship (ER) diagram to show the relationship between different tables and schemas in the database. The data view also explains the reports and analytics needed.
Operational View: This explains how the system is going to be maintained postlaunch. Often, you define service-level agreements (SLAs), alert and monitoring functionality, a disaster recovery plan, and a support plan for the system. The operational view also provides details of how system maintenance is going to be carried out, such as by deployment of a bug fix, patching, backup and recovery, handling security incidents, and so on.
All the views listed make sure the SAD covers all aspects of the system and stakeholders. You may choose to include additional views--such as a physical architecture view, a network architecture view, and a security (controls) architecture view, and so on--as per the stakeholder's requirement. As a solution architect, you need to provide a comprehensive view of system functioning and understanding. Let's explore the structure of the SAD in more detail, in the next section.

[ 410 ]

Solution Architecture Document

Chapter 15

Structure of the SAD
The structure of the SAD can differ from project to project as per stakeholder requirements and the nature of the project. Your project could be creating a new product from the ground, modernizing a legacy application, or moving the entire system to the cloud. For each project, the SAD document may differ, but, overall, it should consider various stakeholders' views and consider the necessary sections, as shown in the following screenshot:

Structure of a SAD
[ 411 ]

Solution Architecture Document

Chapter 15

In the preceding SAD structure, you can see different sections covering multiple aspects of solution architecture and design. The solution architect may choose to add additional subsections or remove some sections as per the project requirement. For example, you can add another introduction section to talk about the document's purpose, with a summary. For a transition project, you may add a subsection to present the existing architecture and compare it with the target architecture, and so on. Let's look into the details of each section.

Solution overview
In the solution overview section, you need to give a brief introduction about the solution in a couple of paragraphs, describing the functioning of the solution and its different components at a very high level. It's nice to add a high-level block diagram, showing various components in one place. The following diagram illustrates the solution overview of an e-commerce platform:

Solution overview of an e-commerce platform
[ 412 ]

Solution Architecture Document

Chapter 15

You need to provide a brief about each component in simplified language so that the business user can understand the overall working of the solution. Major subsections include:
Solution purpose: This provides a brief about a business concern that the solution is solving and the justification to build a given solution. Solution scope: This states the business scope that the proposed solution will address. Clarity describes out-of-scope items that the solution will not accommodate. Solution assumptions: List down all the assumptions based on which solution architect came up with the solution--for example, minimum network bandwidth availability. Solution constraints: List all technical, business, and resource constraints. Often, constraints come from industry and government compliances, and these need to be listed in this section. You can also highlight the risk and mitigation plan. Solution dependencies: List all upstream and downstream dependencies. For example, an e-commerce website needs to communicate with a shipping system such as UPS or FedEx to ship a package to customers. Key architecture decisions: List major problem statements and the corresponding proposed solution options. Describe the pros and cons of each option, why a particular decision was made, and the rationale behind it.
After giving a solution overview, you want to relate it to the business context. Let's look at the business context view in more detail, in the next section.

Business context
In the business context section, the solution architect needs to provide a high-level overview of business capabilities and requirements that the solution is going to address. This section only contains an abstract view of requirements. Detailed requirements need to be a part of a separate requirements document. However, the external link of the requirements document can be provided here. You should include the following primary subsections:
Business capabilities: Provide a brief description of business capabilities for which the solution is being designed. Make sure to include the benefits of capabilities and how they will address customer needs. Key business requirements: List all key business concerns that the solution is going to address. Provide a high-level view of key requirements and add a reference to the detailed requirements document.
[ 413 ]

Solution Architecture Document

Chapter 15

Key business processes: Solution architects should show key processes with a business process document. The following diagram illustrates a simplified view of an e-commerce application business process model:

Business process diagram of an e-commerce platform
Business stakeholders: List stakeholders who are directly or indirectly impacted by the project. This includes sponsors, developers, end users, vendors, partners, and so on.
[ 414 ]

Solution Architecture Document

Chapter 15

NFRs: Solution architects need to focus more on NFRs as these often get missed by the business user and development team. At a high level, an NFR should include:
Scalability: How can the application scale as workload fluctuates? (For example, scale from 1,000 transactions per second to 10,000 transactions per second in a given day or month.)
Availability and reliability: What is acceptable downtime for system availability? (For example, 99.99% availability or 45 minutes' downtime per month.)
Performance: What is the performance requirement? Where can the system handle the load increase without impacting the enduser experience? (For example, the catalog page needs to load within 3 seconds.)
Portability: Can the application run on multiple platforms without any additional work? (For example, the mobile app needs to run in the iOS and Android operating systems.)
Capacity: What is the maximum workload that the application can handle? (For example, the maximum number of users, the number of requests, expected response time and expected application load, and so on.)

The conceptual view of architecture is a sweet spot that provides a good system overview for both business and technical stakeholders. Let's learn more about the conceptual view in more detail.

Conceptual solution overview
The conceptual solution overview section provides an abstract-level diagram that captures a big-picture view of the whole solution, which includes both business and technical aspects. It provides a basis for analyses and trade-off studies that can help refine and optimize the solution architecture in sufficient detail, to support solution design and implementation. The following diagram illustrates a conceptual architecture diagram of an e-commerce platform:

[ 415 ]

Solution Architecture Document

Chapter 15

Conceptual architecture diagram of an e-commerce platform
The preceding diagram shows an abstract view of significant modules and information flow between them. The conceptual architecture provides a good understanding of the overall architecture for both business and technical users. However, technical users need further architectural depth. Let's dive deeper into the solution architecture, in the next section.
Solution architecture
The solution architecture section dives deep into each part of the architecture and provides different views that the technical team can use to create a detailed design and work on implementation. These views could target different user groups such as developers, infrastructure engineers, DevOps engineers, security engineers, user experience (UX) designers, and so on.
[ 416 ]

Solution Architecture Document

Chapter 15

Let's get into the following major subsections to learn more details:
Information architecture: This section provides a user navigation flow to the application. At a high level, the solution architect needs to put in an application navigation structure. As shown in the following diagram, for an e-commerce website, it is taking three clicks for the user to navigate to the desired page:

Informational architecture diagram of an e-commerce platform
Solution architects can add more details such as website navigation, taxonomy, or a high-level wireframe that UX designers can use to generate a detailed wireframe. Application architecture: This section targets the development team. It provides more implementation details upon which a software architect or development team can build a detailed design. The following diagram shows the application architecture for an e-commerce website, with technology building blocks such as caching, networking, content distribution, data store, and so on:
[ 417 ]

Solution Architecture Document

Chapter 15

Application architecture diagram of an e-commerce platform
For an application modernization architecture, this section lists all application modules that need to retire, retain, re-platform, and transform. Data architecture: This section is primarily utilized by the database admin and development team to understand database schemas and how tables are related to each other. Often, this section includes an ER diagram, as shown in the following screenshot:
ER diagram of an e-commerce platform
[ 418 ]

Solution Architecture Document

Chapter 15

The data architecture section lists all data objects that need to be considered during application development.
Integration architecture: This section mainly targets vendors, partners, and other teams. For example, as shown in the following diagram, it shows all integration points with other systems for an e-commerce application:

Integration architecture diagram of an e-commerce platform
The integration architecture section lists all upstream and downstream systems, and dependencies among them, regarding your application. Infrastructure architecture: This section is primarily targeted at the infrastructure team and system engineers. The solution architect needs to include the deployment diagram, which can give a view of the logical server location and its dependencies. For example, the following diagram illustrates the production deployment diagram for an e-commerce application. You can produce a separate diagram for other environments such as dev, quality assurance (QA), and User Acceptance Testing (UAT) environments:
[ 419 ]

Solution Architecture Document

Chapter 15

Deployment diagram of an e-commerce platform
This section lists all server configuration, databases, networks, and switches to deploy the application.
Security architecture: This section includes all the security and compliance aspects of the application, including:
Identity and Access Management (IAM) such as Active Directory (AD), user authentication, authorization management, and so on. Infrastructure security such as firewall configuration, intrusion prevention system (IPS)/intrusion detection system (IDS) needed, antivirus software, and so on. Application security such as WAF, distributed denial-of-service (DDoS) protection, and so on. Data security at rest and in-transit using Secure Sockets Layer (SSL), encryption algorithms, key management, and so on.
Overall, the solution architect can include an application threat model to identify any potential vulnerabilities such as cross-site scripting (XSS), SQL injection (SQLi), and so on, and plan to protect the application from any security threat.
Solution delivery
The solution delivery section includes essential considerations to develop and deploy a solution. It can consist of the following major subsections:
Development: This section is essential for the development team. It talks about development tools, programming language, code repository, code versioning, and branching, with the rationale behind choices.
[ 420 ]

Solution Architecture Document

Chapter 15

Deployment: This section mainly focuses on DevOps engineers, and talks about the deployment approach, deployment tools, various deployment components, and deployment checklist, with the rationale behind choices.
Data migration: This section helps the team to understand data migration and the ingestion approach, scope of data migration, various data objects, data ingestion tools used, source of data and data format, and so on.
Application decommissioning: This section lists existing systems that need to be decommissioned and an exit strategy for the current system if the return on investment (ROI) is not being realized. The solution architect needs to provide an approach and timeline for decommissioning the old system and carry out an overall impact assessment.
The SAD includes a development approach and tools. However, it does not include an application-level detailed design, such as a class diagram or adding pseudocode, as such details need to handled by the software architect or senior developer under the corresponding software application details design document. As a solution gets deployed, it needs to be managed in production. Let's learn about the details that go into the solution management section.

Solution management
The solution management section is focused on production support and ongoing system maintenance across other non-product environments. The solution management section is primarily targeted at the operations management team. This section addresses the following areas:
Operational management such as system patching and upgrades of dev, test, staging, and prod environments. Tools to manage application upgrades and new releases. Tools to manage system infrastructure. System monitoring and alerts; operations dashboard. Production support, SLA, and incident management. Disaster recovery and Business Process Continuation (BPC).
During solution design, a solution architect needs to do research and collect data to validate the right solution. Such kinds of additional details can be put in the Appendix section. Let's learn more details of the Appendix section of a SAD.

[ 421 ]

Solution Architecture Document

Chapter 15

Appendix section of SAD
Like every business proposal document, a SAD also has an Appendix section that is pretty open, to put any data that supports your choices regarding the overall architecture and solution. In the Appendix section, the solution architect can include open issues, any research data such as the outcome of the POC, tools comparison data, vendors' and partners' data, and so on.
In this topic, you got a good overview of the SAD structure with different sections. A SAD should include the major sections mentioned previously; however, the solution architect may choose to exclude some sections or include additional sections as per organization and project requirements. As with other documents, it's essential to continue to iterate upon SADs and look for an opportunity to improve. More robust SADs lead to well-defined implementation guidelines and reduce any risk of failure.
A SAD is a running document that gets created during the initial stages and is kept up to date over the years based on various changes throughout the application life cycle. In addition to the SAD, solution architecture often gets involved in a significant procurement proposal that has a specific requirement and is known as a request for x (RFx) document. Let's familiarize ourselves with RFx documents.

IT procurement documentation for a
solution architecture
IT procurement documents are popularly known as RFx documents. This a term that includes different stages of the procurement process. When you refer to RFx, it references the formal requesting process. RFx documents are categorized as RFP, RFI, or RFQ documents.

[ 422 ]

Solution Architecture Document

Chapter 15

Solution architects are often involved in the procurement process to provide their input or lead them. These procurements may be related to outsourcing, contracting, procuring a software such as a database or development tools, or buying SaaS solutions. As these documents could be highly technical and have a long-term broad impact, the solution architect needs to provide input, or respond to any procurement requirement and prepare the invite. Let's understand the difference between different RFx documents, as follows:
RFI: RFI comes early in the procurement process, where buyers invite information from different vendors to make an informed decision regarding their choice of procurement for a later stage. An RFI document collects information about the capabilities of the various suppliers, where the buyer can compare all suppliers in a similar parameter and proceed to the next proposal steps with shortlisted suppliers. RFP: In this process, shortlisted suppliers from the RFI process have more information about the outcome of the project. An RFP document is more open than an RFI one, where suppliers can provide the best way to acquire solutions for the buyer. The supplier can include multiple choices, with pros and cons of each approach. RFQ: In this process, buyers narrow down the requirement compared to the RFP and list down the exact requirement of work, equipment, and supplies. Suppliers need to provide a cost for the listed requirements, and the buyer can choose the best quotation among them to award the contract.
RFP is the most popular choice, as often, to speed up the process, buyer's organization choose to ask for the RFP document only from potential vendors. In such a situation, the RFP document needs to have the structure in place so that that buyer can put a clear comparison between preferred vendors in terms of capabilities, solution approach, and cost to make a quick decision.
Due to technicalities of procurement in IT organizations, solution architects play an essential role in evaluating vendors' capabilities and approaches from the buyer side or responding to RFP documents from the supplier side.

[ 423 ]

Solution Architecture Document

Chapter 15

Summary
The purpose of a SAD is to keep all stakeholders on the same page and get formal agreement on solution design and requirements. As stakeholders comprise of both business and technical users, you learned about various views of the SAD that the solution architect needs to consider. You need to include views for non-technical users, such as business, process, and logical views. For technical users, include views such as application, development, deployment, and operational views.
You learned about the detailed structure of the SAD, with major sections and subsections. Various sections of the SAD include details such as an overview of the solution, business, and conceptual architecture. You also learned about various architecture views such as application, data, infrastructure, integration, and security, with reference to the architecture diagram. You learned about other sections for solution delivery consideration and operation management.
It was a long journey of learning. You are almost at the end of the book, but before closing, you need to learn some tips to becoming a solution architect and continuing to improve on your knowledge.
In the next and final chapter, you will learn about various soft skills such as communication style, ownership, critical thinking, and continuous learning techniques to become a better solution architect.

[ 424 ]

16
Learning Soft Skills to Become
a Better Solution Architect
In the previous chapters, you learned about how a solution architect needs to accommodate all stakeholders' needs. Even if the solution architect's role is a technical one, they need to work across the organization, from senior management to the development team. To be a successful solution architect, soft skills are essential and critical factors.
A solution architect should keep themself up-to-date with current technology trends, keep evolving their knowledge, and always be curious to learn new things. You can become a better solution architect by applying continuous learning. In this chapter, you will learn about methods to learn new technologies, and how to share and contribute back to the technical community.
A solution architect needs to define and present an overall technical strategy to address business concerns, which requires excellent presentation skills. A solution architect needs to work across business and technical teams to negotiate the best solution, which requires excellent communication skills. In this chapter, you will learn the soft skills a solution architect must have, such as:
Acquiring pre-sales skills Presenting to C-level executives Taking ownership and accountability Defining strategy execution and Objectives and Key Results (OKRs) Thinking big Being flexible and adaptable Design thinking Being a builder by engaging in coding hands-on Becoming better with continuous learning Being a mentor to others Becoming a technology evangelist and thought leader

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

By the end of this chapter, you will learn about the various soft skills required for a solution architect to be successful in the role. You will learn about a method to acquire strategic skills (such as pre-sales and executive communication), and develop design thinking and personal leadership skills (such as thinking big and ownership). You will learn about techniques to establish yourself as a leader and continue improving your skill set.

Acquiring pre-sales skills
Pre-sales is a critical phase for complex technology procurement, whereby the customer collects detailed information to make a buying decision. In the customer organization, a solution architect is involved in the pre-sales cycle to procure technology and infrastructure resources from various vendors. In the vendor organization, the solution architect needs to respond to customers' requests for proposals (RFP) and present a potential solution to acquire new business for an organization. Pre-sales requires a unique skill set that combines strong technical knowledge with soft skills, including:
Communication and negotiation skills: Solution architects need to have excellent communication skills to engage the customer with the correct and latest details. Presenting precise details of the solution along with industry relevance helps customers to understand how your solution can address their business concerns. Solution architects work as a bridge between the sales and technical teams, which makes communication and coordination a critical skill.
Solution architects also need to get an agreement by collaborating with customers and internal teams, which requires excellent negotiation skills. In particular, strategic-level decisions have a significant impact across multiple groups, where solution architects need to negotiate between the team, work on trade-offs, and come up with an optimizing solution.
Listening and problem-solving skills: Solution architects need to have strong analytical skills to identify the right solution as per the customer need. The first thing is to listen to and understand customer use cases by asking the right questions to create a good solution. You need to understand gaps and come up with a solution to result in immediate business impact with long-term returns on investment (ROIs). For some customers, performance is more important, while others may be more focused on cost, based on their application user base. The solution architect needs to provide the right solution as per their customer's primary key performance indicator (KPI) goal.

[ 426 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Customer-facing skills: Often, the solution architect needs to work with both the internal team and the external customer's team. They influence stakeholders at all levels, from C-level executives to development engineers. They present solutions and demos to senior management, where they look at your proposal more from a business-prospecting perspective.
C-level executive support and commitment to initiatives always result in the success of the adopted solution, which makes customer-facing skills very important. The C-level executive needs details of the solution in a defined timebound meeting, and the solution architect needs to utilize the allotted time to their best advantage. You will learn more information about the executive conversation in the next section of this chapter--Presenting to C-level executives.
Working with teams: The solution architect establishes a relationship with both the business team and the product team. To prepare an optimal application, the solution architect needs to work with the business team and technical team at all levels. The solution architect needs to be a good team player and work with multiple teams, share ideas, and find a way of working.
The aforementioned skills are not only required for pre-sales but are also applicable to the solution architect's day-to-day job functions. Solution architects come from a technical background, and, being in such a role, they need to acquire critical skills to communicate at an executive level. Let's learn more about the executive conversation in the next section.

Presenting to C-level executives
A solution architect needs to handle various challenges from a technical and business perspective. However, one of the most challenging tasks could be to get executive buy-in. Senior executives such as the Chief Executive Officer (CEO), Chief Technology Officer (CTO), Chief Financial Officer (CFO), and Chief Information Officer (CIO) are regarded as C-level as they have a tight schedule and need to make lots of high-stack decisions. As a solution architect, you may have lots of details to present, but your C-level meetings are very time-bound. Here, they need to make the maximum value of their meeting in the allotted time slot.

[ 427 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

The primary question is: How to get senior executives' attention and support in a limited time? Often, during any presentation, people tend to put a summary slide at the end, while, in the case of executive meetings, your time may further reduce as per their priority and agenda. The key to an executive presentation is to summarize the primary points upfront in the first 5 minutes. You should prepare in such a way that if your 30-minutes slot reduces to 5 minutes, you should still be able to convey your points and get buy-in for the next step.
Explain your agenda and meeting structure even before the summary. Executives ask lots of questions to make proper utilization of their time, and your agenda should convey that they will get the chance to ask a clarification question. Support your summary based on facts and data that align with their industry and organization. Keep details with you in case they want to dive deep into a particular area; you should be able to pull up and show all data.
Don't try to present everything in detail by stating information that may seem relevant from your perspective but maybe doesn't make much sense for an executive audience. For example, as a solution architect, you may focus more on benefits from the technical implementation. However, senior management focuses more on ROI by reducing operational overhead and increasing productivity. You should be ready to answer the following questions that concern executives more:
How the proposed solution will benefit our customers?: Business revolves around the customer, while executives are looking at their company growth, but that is only possible if their customers are satisfied. Make sure to do your research on their customer base and their needs. Be ready to present benefits backed by reliable data.
What assumption did you make to baseline the solution?: Often, these meetings are at the initial phase when you may not have enough details. Solution architects always need to make some assumptions to baseline the solution. List down your hypothesis in bullet points, and have a mitigation plan associated with it in case things don't work as per assumption.
What will be my ROI?: Executives are always looking for ROI by determining the total cost of ownership (TCO). Be ready with data to provide an estimated cost of ownership, solution maintenance cost, training cost, overall cost savings, and so on.
What happens if we continue as it is today and do nothing?: Senior management may go into extreme vetting mode to identify ROI. They want to understand if the investment is worth it. You need to be ready with your market research--for example, technology trends, customer trends, and competitive situation.

[ 428 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

What will be our competitor's reaction in regard to your solution?: Competition is everywhere, and often, the executive worries more about it. They want to understand if your solution is innovative to beat the competition and give their organization the edge. It's better to do some upfront research and add competitiveness data relating to their industry and customer base.
What is your suggestion, and how can I help?: You should always have a crisp list of action items as the next step while providing your suggestion. You need to get buy-in from executives and make them feel involved by asking for help. For example, you can ask the CIO to connect you with the engineering team or product team to take an overall solution to the next step.
Till now, in this chapter, we have talked about various soft skills such as communication, presentation, listening, and so on. Let's now look more at the leadership skills a solution architect should have as a technical leader for the organization.

Taking ownership and accountability
Taking ownership and positioning yourself as a leader helps you to win trust with accountability. Ownership doesn't mean that you need to execute things alone; it is more about taking new initiatives and holding on to them as it is your organization. You can have ideas that can benefit your organization in terms of productivity, agility, cost-saving, and increasing the customer base. Sometimes, you may not have the time or resources to execute your idea, but you should always try to bring it forward as a new initiative, and engage others for execution.
Accountability is about taking responsibility to drive the outcome. Ownership and accountability go hand in hand, where you are not only creating initiative but working on getting the result. People can trust you to execute any job and drive results. Accountability helps you to build trust with your customers and team, which ultimately results in a better work environment and achieving a goal.
As a solution architect, when you take ownership it helps you to see things from the customer's and sponsor's perspective. You feel motivated and a part of something meaningful that you enjoy doing. Make sure to define and create key successes and the objective key result. The goal/objective should be measurable using specific key results, and they must be time-bound. Let's learn more about Objectives and Key Results (OKRs).

[ 429 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Defining strategy execution and OKRs
Strategy execution is complex and challenging. Excelling in strategy execution is essential for realizing the organizational vision, mission, and goals. The idea needs to be brought into actionable elements to keep teams aligned and everyone moving in the same direction. Goal setting and management of goals is one of the best-established ways to get things done in an organization.
OKRs are principles and practice (vision and execution) of goal setting. OKR is a strategy management system that focuses on strategy execution. OKR is a simple framework that lets you define the organization's primary strategy and its priorities. Objectives are the principles, and key results are the practice--it is a what and how of organizational vision. OKRs are based on four superpowers, as illustrated in the following diagram:

Superpowers of OKRs
OKRs' superpowers include:
Focus: Start with the question: What are our main priorities, and where should people concentrate their efforts? Commit to what truly matters and provide clarity on what is essential. Alignment: Make goals public and transparent. Connect with the team and get cross-team, bottom-up, and sideways alignment. Tracking: Visually track down the key results of each objective, down to the percentage point.
[ 430 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Stretching Goals: Create ambitious goals to achieve something remarkable. Stretching goals allows people to reimagine and rethink.
OKRs provide visibility and a meaningful outcome to all stakeholders at various levels, from executive sponsors to teams. OKRs make the vision and mission of the organization clear. Team members that are working on day-to-day activities need visibility and clarity to the mission. They need to see how their everyday work has an impact on that organizational mission. The OKR framework allows you to define this link and provide visibility and meaning for everyone who is on the team.

Thinking big
Solution architects should have the ability to see the big picture and think ahead. A solution architect creates a foundation upon which the team puts building blocks and launches the product. Thinking big is one of the critical skills that solution architects should possess to think about the long-term sustainability of an application. Thinking big doesn't mean you need to take a very unrealistic goal. Your goal should be high enough to challenge you and bring you out of your comfort zone. Thinking big is critical for success at both a personal and an organizational level.
You should never doubt your capability while thinking big. Initially, it may seem challenging to achieve, but as you start working toward the goal, you will find the way. Believe in yourself and you will notice that others start supporting and believing in you. Thinking big helps to inspire people around you to become a part of your success. Set up long-term goals, such as Where do you want to see yourself and your organization in the next decade? Take one step at a time to gear a short-term goal to a long-term goal.
Once you set up the stretching goal by thinking big, it will help you to take large initiatives and explore new challenges. However, to deliver the result, you need support from your peers and team, who can provide you with the right feedback and extend help as needed. Become a person whom people want to help; and, of course, this is a two-way door. To get help, you need to be open to helping others. Adaptability is another critical skill for solution architects to work with others. Let's learn more about it.

[ 431 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Being flexible and adaptable
Adaptability and flexibility go hand in hand, and you need to be flexible to adapt to the new environment, working culture, and technology. Adaptability means you are always open to new ideas and to working with the team. Teams may adopt a process and technology that is best suited for them. As a solution architect, you need to be flexible in accommodating team requirements during solution design.
A simple example of flexibility in a technical implementation can be facilitated by a microservices architecture. In a microservices architecture, each service communicates with the others via a standard RESTful API over the HTTP protocol. Different teams may choose to write code in a different language of their choice, such as Python, Java, Node.js, or .NET. The only requirement is that teams need to expose their APIs securely so that the entire system can build upon utilizing them.
To get a more innovative solution, you need a different mindset and perspective to look into the problem. Encouraging teams to fail fast and innovate helps an organization to be competitive. The personal traits of flexibility are demonstrated by:
Thinking about various solutions to solve a problem with the team and take the best approach. Helping team members to offload their work. Volunteering to fill up a place if a team member needs to take time off for weeks due to personal work reasons. Being able to collaborate effectively with teams across different locations and time zones.
You need to be open-minded and adaptable to changes in technology and processes. You may face resistance when bringing change to your team or organization. You need to encourage others to be flexible and convey the importance of change. For example, when an organization wants to move its workload from on-premises to cloud, they often face a situation of resistance, as people have to learn a new platform. You need to explain the value proposition of the cloud and how it will help them to be more agile and innovate faster.
As a solution architect, you need to be adaptable to carry out multiple assignments and set the right priority for execution. You should have the ability to adjust to the situation and work under pressure. A solution architect needs to have critical design thinking to create an innovative solution. Let's learn more about design thinking in the next section.

[ 432 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Design thinking
A solution architect has the primary role of system design, which makes design thinking an essential skill. Design thinking is one of the most successful approaches adopted across industries to solve a challenging and unclear problem. Design thinking helps you to look at problems and solutions from a different perspective, which you might not have considered in the first instance. Design thinking is more focused on delivering results by providing a solution-based approach to solve the problem. It helps to pretty much question the problem, solution, and associated risk, to come up with the most optimized strategy.
Design thinking helps you to redefine problems in a more human-centric way by putting yourself in place of end users and customers. The following diagram illustrates the primary principles of design thinking:

Principles of design thinking
The following points are some design-thinking principles: Emphasis on people: Collect feedback from various users and put yourself in their place to understand the problem from a different perspective.
[ 433 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Cross-collaboration: Bring in people from different backgrounds to look for problems in a diversified way, and make sure solutions accommodate everyone's needs.
Think through the design process: Understand the overall design process, with clear goals and methods.
Show and tell: Present your thoughts in visuals so that it will be easy to grasp for everyone in the room.
Define the problem clearly: Create a well-defined and clear vision for a given challenge, which can help others understand clearly and encourage them to contribute more.
Experiment often: Create a prototype to understand the implementation of the idea in real-life situations. Adopt a fail-fast strategy and experiment more often.
Bias for action: The ultimate design to deliver a solution rather than just thinking. Be proactive in pushing forward and coming up with activities that can result in a workable solution.
Design thinking has a solid foundation to apply empathy and create a holistic view of the given problem. To adopt design thinking, there is a five-phase model proposed by d.school (https://dschool.stanford.e du/resources/g etting-s tarted-with-design-t hinking). They are a pioneer in teaching and applying design thinking. The following diagram illustrates the five phases of design thinking:

Five phases of design thinking
[ 434 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Design thinking is an iterative approach that needs to evolve continuously. The output from one phase can recursively be input to other phases until the solution gets solidified. A brief overview of the phases follows:
Empathize: Empathy is the building block and foundation of design in the human context. To empathize, you should observe your user behaviors and engage with them to understand the actual issue. Try to immerse yourself in--and experience--the problem by putting yourself in the situation.
Define: Empathizing helps to define the problem as you experience the user's needs and the problem they are facing. In the define mode, you apply your insight and define the problem clearly, which can fuel brainstorming to find an innovative yet simple solution.
Ideate: The ideation phase is about moving from problem to solution. You work with the team to find various alternative solutions by challenging assumptions. You need to get an obvious solution out of your head and work collaboratively to find all possible solutions, which allows for innovation.
Prototype: The prototype phase helps to convert ideas into a concrete solution. Prototyping can provide lots of learning and help to resolve disagreements by showing a proof of concept (POC). It helps to find out gaps and risks. You should build a quick prototype without lots of investment, which allows you to handle failure and increase learning.
Test: The test phase is about getting feedback on your solution and reiterating accordingly. The test phase helps to redefine the solution and learn more about your users.
Design thinking accommodates all the phases required to come up with a logical and practical solution. You can relate the phases and principles of design thinking in your real life when designing an application architecture. There is special stress on prototyping, as that is the only way to solidify your proposal and existing solutions with data and facts. A solution architect's primary job is to understand the business concern and create a technical solution design with a prototype that the team can implement. To build a prototype, the solution architect needs to get their hands dirty and engage in coding hands-on. Let's learn more about it.

[ 435 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Being a builder by engaging in coding
hands-on
A solution architect is a builder who learns by doing. A prototype is worth a thousand pictures. It helps to reduce miscommunication and ideate solutions. Presenting a POC and prototyping is an integral part of the solution architect's role. Prototyping is the presolution phase, which helps to deepen your understanding of the application design and user. It helps you to think and build multiple solution paths. With the testing of the prototype, you can refine your solution and inspire others, such as teams, customers, and investors, by demoing your vision.
A solution architect is a technical leader who works closely with the development team. In the empowered agile team of developers, a solution architect needs to show a piece of code as a POC, in addition to a PowerPoint presentation. A solution architect doesn't need to be part of the development team but works in collaboration to convey the solution to the dev team in their language. Successful delivery is only possible if the solution architect can understand the deep technical aspect of a solution that comes with continuous coding, hands-on.
A solution architect is often seen as a mentor and player-coach; having some hands-on coding helps them to establish credibility. A solution architect needs to take a strategic decision regarding which programming languages and tools the team should use. A handson approach helps to identify any gaps that may not fit for your team or solution need--always learning new technology helps the solution architect to make a better decision on behalf of the organization. Let's learn more about the techniques of continuous learning.

Becoming better with continuous learning
Solution architects need to continually absorb new knowledge and enhance their skill set to help the organization in better decision making. Continuous learning keeps you relevant and builds confidence. It opens up your mind and changes prospects. Learning could be challenging with a full-time job and a busy family life. Continuous learning is about developing the habit of always learning something new, whereby you have to be motivated and disciplined. You first need to set up learning goals and apply effective time management to achieve them. This often slips through the net when you get busy with regular daily work.

[ 436 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Everyone has their own style of learning. Some people may like formal education; some may read books; others may want to listen to and watch tutorials. You need to find the learning style that is most effective for you and suited to your lifestyle. For example, you can choose to listen to audiobooks and tutorials when commuting to work. You can read books during a business-trip flight or watch video tutorials during exercise hours in the gym. Overall, you need to make some adjustments to put time aside from your busy work life for continuous learning. Here are some of the ways to engage yourself in constant learning:
Learning new technologies, frameworks, and languages by trying them out: Solution architects are the builders and are ready to experiment hands-on. As a successful solution architect, you need to keep learning new technologies by building a small POC. Getting an understanding of modern programming languages and frameworks will help you to provide the best advice on technology adoption for an organization and team.
Learning new skills by reading books and tutorials: Online learning has brought a revolution and has made it easy to learn and dive deep in any area. You now have massive knowledge bases at your fingertips, to learn anything. An online platform such as Udemy or Coursera provides thousands of video tutorial courses in all areas that you can watch online or download to your device for offline learning.
Similarly, there are millions of books available in Kindle to read anytime and anywhere. Audiobook platforms such as Audible and Google Play's audiobooks can help you to listen to the book during your commute. There are so many convenient resources available that there is no excuse not to apply continuous learning.
Keeping up with technology news and developments by reading articles on websites and blogs: The best way to keep yourself updated with technology trends is by subscribing to technical news and blogs. TechCrunch.com, Wired.com, and Cnet.com are some of the popular websites to get the latest technology trends. A major newspaper such as CNBC or The New York Times, BBC News and CNN channels, and so on have technology articles that give a good insight into industry trends. You can subscribe to blogs for new learning in the respective technology area. For example, for cloud platform learning, you can subscribe to Amazon Web Services (AWS) blogs, which has thousands of articles and use cases in the area of AWS Cloud, and similar blogs are available from other public clouds such as Azure and Google Cloud Platform (GCP).

[ 437 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Writing your blog, whitepaper, and book: Sharing knowledge is the best way to learn as you think through use cases when trying to present to others. Publishing blogs and articles in popular blog-publishing platforms such as medium.com, Blogger, and Tumblr helps you to share your learning and also learn from others. Active participation in question-and-answer platforms helps you to find an alternative solution for any given problem. Some popular question/answer platforms are Quora, Reddit, StackOverflow, Stack Exchange, and so on.
Solidify your knowledge by teaching others: Teaching others helps you to collaborate and get a different perspective of your knowledge. Often, use cases asked by participants give you different ways of finding a solution. Running a full-day workshop with a hands-on lab and concept building helps you to solidify your learning and learn with others.
Taking online classes: Sometimes, you want to go for formal learning to be more disciplined, and you want to be flexible. Online courses provide flexibility and help you to adjust to other priorities and save time. Online courses can offer you an organized way to learn new technology and help to enhance knowledge.
Learning from teammates: Teammates share the same context, and you spend most of the day with them. Learning with team members can help to speed up your learning. The team can adopt a divide-and-conquer strategy whereby each team member can share the topics among them and present dive-deep brownbag sessions. Brown-bag sessions are a standard method used by many organizations to conduct regular learning sessions among team members. Each team member shares their new learning in a weekly brown-bag learning session, and everyone quickly learns new topics. Attending and participating in user groups and conferences: All large vertical industry and technology organizations conduct a conference to provide insight on new technology trends and hands-on sessions. Participating in industry conferences and user group meetings helps to develop networking and understand technology trends. Some of the large technology conferences from industry leaders include AWS re:Invent, Google Cloud Next, Microsoft Ignite, SAP SAPPHIRE, Strata Data conference, and so on. You can create a local user group and conduct a meet-up in your local area, which will help you to collaborate with professionals across industries and organizations.
A solution architect plays a technical leadership role, and a good leadership warrant to prepare more leaders like you, which is possible through mentorship. Solution architects should play a player-coach role and mentor others. Let's look at this in more detail.

[ 438 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

Being a mentor to others
Mentoring is about helping others and setting them up for success based on your learning and experience. It is an effective way to develop leaders by having one-to-one mentor/mentee relationships. To be a good mentor, you need to establish an informal communication style where the mentee can develop a comfort zone. The mentee can seek advice in multiple areas such as career development, or in personal aspects such as worklife balance. You should do an informal needs assessment and set up mutual goals and expectations.
Mentorship is more about listening. Sometimes, people need someone to listen to them and advise as required. You should listen carefully first and understand their point of view. Help them to make their own decisions as this will make them feel more accomplished. As a good mentor, when advising for a career, you need to be open to advise what is the best fit for the mentee, even if it may not necessarily be the best fit for the company. Always provide honest, constructive feedback to help them identify gaps and overcome them.
The critical trait of a mentor is the ability to inspire people. Often, people may choose you as a mentor if they see a role model in you. Help your mentee to realize their full potential without putting your view forward, and help them achieve what they never thought of earlier. There are always mutual benefits to being a mentor; you also learn a lot from mentees about people's behaviors and growth. Being a mentor to others will ultimately help you to become a better leader and person.

Becoming a technology evangelist and
thought leader
Technology evangelism is about being an expert, to advocate technology and your product. Some organizations with a large product base roll out a separate technology evangelist role, but often, a solution architect needs to take the role of an evangelist as part of their job. As a technology evangelist, you need to be between people to understand real-world problems and advocate your technology to solve their business concerns.
Technology evangelism involves participating in an industry conference as a public speaker and promoting your respective platform. It allows you to become a thought leader and an influencer, which can help the organization to increase the adoption of its platform and product. Public speaking is one of the critical skills required for a solution architect, in order to interreact on various public platforms and present in front of a large audience.

[ 439 ]

Learning Soft Skills to Become a Better Solution Architect

Chapter 16

An evangelist also creates and publishes content such as blog posts, whitepapers, and microblogs to advocate their product. They socialize the content to increase adoption and interreact with the user to understand their feedback. An evangelist works backward from the customer and communicates feedback to the internal team to help to make the product better. With time, as an evangelist, you will refine the message that works in the best interests of the organization.
Overall, a solution architect is a role with multiple responsibilities, and taking more ownership will help you to better succeed in your career.

Summary
In this chapter, you learned about the various soft skills required for a solution architect to be successful. A solution architect needs to have pre-sales skills such as negotiation, communication, problem-solving, and listening, which help them to support the pre-sales cycle for the organization, such as with the RFP. You learned about the presentation skills required for executive conversation and buy-in.
You learned about the strategic understanding that a solution architect should have to define key objectives and results for an organization. To execute at various levels, solution architects should have the ability to think big and be flexible and adaptable. You learned details about solution architects taking ownership and being accountable for their actions.
A solution architect's role has the primary responsibility of architecture design. You learned about design thinking, with its principles and phases. You also learned about the importance of continuous learning and different techniques to keep learning and keep yourself up-to-date with market trends. You also learned about the additional responsibilities of the solution architect--to work as a mentor and evangelist.
It was a long journey where you went through 16 chapters to learn all about solution architects, from their roles and responsibilities to a different aspect of solution design and architecture optimization. I hope you have learned a lot, and that it will help you to develop your career as a solution architect or help you to succeed in your current role.
Happy learning!!!

[ 440 ]

Other Books You May Enjoy
If you enjoyed this book, you may be interested in these other books by Packt:
Software Architect's Handbook Joseph Ingeno ISBN: 978-1-78862-406-0
Design software architectures using patterns and best practices Explore the different considerations for designing software architecture Discover what it takes to continuously improve as a software architect Create loosely coupled systems that can support change Understand DevOps and how it affects software architecture Integrate, refactor, and re-architect legacy applications

Other Books You May Enjoy
AWS SysOps Cookbook - Second Edition Eric Z. Beard, Rowan Udell, Et al ISBN: 978-1-83855-018-9
Secure your account by creating IAM users and avoiding the use of the root login Simplify the creation of a multi-account landing zone using AWS Control Tower Master Amazon S3 for unlimited, cost-efficient storage of data Explore a variety of compute resources on the AWS Cloud, such as EC2 and AWS Lambda Configure secure networks using Amazon VPC, access control lists, and security groups Estimate your monthly bill by using cost estimation tools Learn to host a website with Amazon Route 53, Amazon CloudFront, and S3
[ 442 ]

Other Books You May Enjoy
Leave a review - let other readers know what you think
Please share your thoughts on this book with others by leaving a review on the site that you bought it from. If you purchased the book from Amazon, please leave us an honest review on this book's Amazon page. This is vital so that other potential readers can see and use your unbiased opinion to make purchasing decisions, we can understand what our customers think about our products, and our authors can see your feedback on the title that they have worked with Packt to create. It will only take a few minutes of your time, but is valuable to other potential customers, our authors, and Packt. Thank you!
[ 443 ]

Index

A
A/B testing 343, 344 accelerated processing unit (APU) 202 Access Control List (ACL) 245 accessibility 69 accountability 429 Active Directory (AD) 223, 420 Active Directory Authentication Library (ADAL) 231 Active Directory Certificate Services (AD CS) 232 Active Directory Domain Service (AD DS) 231 Active Directory Federation Service (ADFS) 232 Active Directory Lightweight Directory Services (AD
LDS) 232 Active Server Page (ASP) 142 agent-based solutions 115 agentless solutions 115 Agile manifesto 49, 50 Agile methodology
need for 48, 49 agile tools
burndown chart 52 definition of Done 53 planning poker 52 product backlog 52 sprint board 52 agile architecture 54 process and terminology 50 scrum team 51 sprint ceremonies 51 versus waterfall 53, 54 alert automating 98 alerting mechanisms 104 Amazon Dynamo DB 212 Amazon Elastic Block Store (EBS) 210

Amazon Elastic Cloud Compute (EC2) 202 Amazon Elastic Container Repository (ECR) 203 Amazon Elastic Containers Service (ECS) 183,
203 Amazon Elastic File Storage (EFS) 210 Amazon Elastic Kubernetes (EKS) 205 Amazon Elastic Kubernetes Service (EKS) 183 Amazon Elastic load balancer (ELB) 217 Amazon Elasticsearch Service (Amazon ES) 214 Amazon Machine Image (AMI) 268 Amazon Redshift 319 Amazon Route 53 215 Amazon Simple Notification Service (SNS) 164 Amazon Simple Queue Service (SQS) 161 Amazon Simple Storage Service (S3) 155, 209,
300, 362 Amazon Web Services (AWS) 20, 137, 192, 288,
315, 323, 404, 437 anti-patterns, in solution architecture
avoiding 187, 188, 189 Apache Kafka 360 app caching pattern 174, 175 application architecture
database, handling in 184, 185 application layer 143 application monitoring
about 290 example 290 application optimization considerations 131 Application Programming Interface (API) 150 application testing automating 98 application-specific integrated circuit (ASIC) 201 architect evangelist 32 architectural reliability, design principles about 259

automation, applying 260 capacity, monitoring 261 distributed system, creating 260, 261 recovery validation, performing 262 self-sealing system, making 259 architectural security technology, selecting 227 architecture design for performance 85, 86 architecture performance, principles caching, applying 197, 198 concurrency, handling 196, 197 latency, reducing 192, 193, 194 throughput, improving 194, 195 architecture performance principles, designing for 192 architecture reliability data replication, creating 264 disaster recovery (DR), planning 266, 267 improving, with cloud 276, 277 technology selection 262 architecture scaling 59, 60 array-based replication 265 Asset Panda 285 asynchronous data replication versus synchronous data replication 264, 265 Atomicity, Consistency, Isolation, Durability (ACID)
367 attributes, solution architecture
accessibility 69 budget 76 business continuity 65 compliance 73 cost optimization 76 disaster recovery 65 elasticity 57 extensibility 67, 68 fault-tolerance 64 high availability 62 interoperability 70, 71 maintainability 72 operational excellence 72 portability 70, 71 redundancy 64

resiliency 62 reusability 67, 68 scalability 57 security 73 usability 69 authentication 74 Authentication Server (AS) 229 authorization 74 automating 98, 99 automation 330 applying 260 AWS Certificate Manager (ACM) 253 AWS cloud shared security responsibility model about 254, 256 AWS responsibilities 255 customer responsibilities 255 AWS CodeCommit 345 AWS Data Migration Service (DMS) 363 AWS Data Sync 363 AWS Key Management Service (KMS) 251 AWS Trusted Advisor 324
B
best practices, for securing application about 242 application and operating system, hardening 242 firewall and trusted boundary, configuring 243, 245 IDS/IPS, using 246 software vulnerabilities and secure code, applying 243
big data architecture 355, 356, 357 big data processing pipelines
designing 357, 358, 359 big-bang approach 395 bits per second (bps) 194 blue-green deployment 338, 339 bounded contexts 156 budget
about 76 versus forecast 308 buffer 239 build phase 342 build server 345 bulkheads pattern

[ 445 ]

implementing 176, 177 business continuity 65 Business Intelligence (BI) 34, 357 Business Process Continuation (BPC) 421
C
C-level executives 427 cache aside pattern 175 cache distribution pattern
in three-tier web architecture 169, 170 cache proxy pattern 171, 172 cache-based architecture
application caching 168 building 166, 167, 168 client side 168 database caching 168 DNS cache 168 layer 168 wed caching 168 caching 86 canary analysis 339 capacity monitoring 261 capital expenditure (CapEx) 9, 306 CD strategy blue-green deployment 338, 339 immutable deployment 340, 341 implementing 337 in-place deployment 338 red-black deployment 340 rolling deployment 338 Center for Financial Industry Information Systems
(FISC) 8 Center of Excellence (CoE) 112 central processing unit (CPU) 200 Certification Authority (CA) 253 challenges, of legacy systems
about 390 difficulty, in keeping up with user demand 391 higher cost, of maintenance and update 391,
392 incompatibility, with other systems 394 skills and documentation, shortage 392, 393 vulnerable, to corporate security issues 393 change data capture (CDC) 363

Chaos Monkey 298 charge-back mechanism 310 check-and-balance approach 311 Chief Executive Officer (CEO) 427 Chief Financial Officer (CFO) 427 Chief Information Officer (CIO) 427 Chief Technology Officer (CTO) 427 CI/CD pipeline
continuous testing, implementation 341, 342, 343
circuit breaker pattern 176 Classless Inter-Domain Routing (CIDR) 245 cloud architect 31 cloud computing models
Infrastructure as a Service (IaaS) 22 Platform as a Service (PaaS) 22 Software as a Service (SaaS) 22 cloud data migration 124, 125, 126 cloud migration strategy, cloud-native approach about 108 refactor 109 repurchase strategy 109 cloud migration strategy, Lift and Shift approach about 106 rehost 106 relocate 107, 108 replatform 107 cloud migration strategy cloud-native approach 108 creating 104, 105, 106 for legacy systems 403, 405 Lift and Shift approach 106 retain or retire strategy 110 retain strategy 110 retire strategy 111, 112 cloud migration application migration, performing to cloud 124 application optimization, in cloud 131, 132 application, designing 121, 122, 123 cloud application, operating 130, 131 cutover 127, 128 information, analyzing 115, 116 integration 127, 128 migration plan, creating 117, 118, 119, 120 steps 113

[ 446 ]

steps for 112, 113 validation 127, 128 workload, discovering 113, 114, 115 cloud providers 137 cloud service offering 23 cloud-based AWS Cloud9 integrated development
environment (IDE) 344 cloud-native Amazon RDS 123 cloud-native architecture
benefits 102, 103, 104, 137 designing 135, 136, 137 cloud-native monitoring 104 cloud architecture reliability 277 architecture reliability, improving with 276 CloudWatch 322 commercially available off-the-shelf (COTS) 403 compliance 73 concurrency about 195 handling 196, 197 Concurrent Versions System (CVS) 350 configuration items (CI) 286 configuration management (CM) 334, 335 Configuration Management Database (CMDB) 286 configuration management tools comparison 334 constraints overcoming 95, 96 container-based deployment about 179, 180, 182, 183, 184 benefits 180, 181, 182 content distribution network (CDN) 60, 74, 83,
168, 170, 192, 197, 240 continuous cost optimization 311 continuous integration and continuous deployment
(CI/CD) about 72, 243, 326, 330, 331, 332 combining, with DevSecOps 336, 337 continuous learning 436, 437, 438 cost optimization, design principles about 306 budget, planning 308 continuous cost optimization 311 demand management 310

forecast, planning 308 service catalog management 310 total cost of ownership (TCO), calculating 306,
308 track of expenditure, keeping 310, 311 cost optimization, techniques about 312 architectural complexity, reducing 312, 313, 314 cost usage and report, monitoring 318, 319,
320, 321, 322, 323 governance, implementing 316 IT efficiency, increasing 314, 316 standardization, applying 317, 318 cost optimization about 76, 305 in public cloud 323, 324 cost-benefit analysis (CBA) 392 cross-site scripting (XSS) 74, 238, 295, 420 Customer Relationship Management (CRM) 127,
229, 403 cutover process 128
D
d.school 434 dark launch 340 dashboards 288 data analytics
about 373, 374 technology choices 375, 376, 377, 378 data architect 34 Data Encryption Standard (DES) 249 data encryption asymmetric-key encryption 249 symmetric-key encryption 249 data ingestion about 359, 360 technology choices for 360, 361 to cloud 362, 363 data lakes about 371, 373 benefits 372 data processing about 373, 374 technology choices 375, 376, 378 data replication

[ 447 ]

creating 264 data science
working with 383, 384 data security
about 75, 248 data classification 248 data encryption 249, 252 encryption key management 250 data storage about 364, 365 selecting, factors 92 technology choices 366 using 92, 94 data tier 143 data visualization about 378 technology choices 378, 379 data warehousing 367, 368 data-driven design 94, 95 database layer 144 database scaling 61, 62 database handling, in application architecture 184, 185 DDoS attack SYN floods 237 User Datagram Protocol (UDP) reflection 237 defense-in-depth (DiD) approach 224 Department of Defense Cloud Computing Security
Requirements Guide (DoD SRG) 8 deployment automation 99 design principles, for architectural security
about 223 authentication and authorization control,
implementing 223 automating 225 blast radius, reducing 224 data protection 226 monitoring and auditing mechanism 225 response, preparing 226 security, applying 224 design thinking about 433 phases 435 principles 433 development phase 342

DevOps architect 36 DevOps in Security (DevSecOps)
about 326, 335 combining, with CI/CD 336, 337 DevOps tools, using for CI/CD about 344 CI server 345, 346, 347 code deployment 347, 348, 349 code editor 344 code pipeline 349, 350 source code management 345 DevOps-related metrics examples 332 DevOps about 327, 328 benefits 328, 329 best practices, implementing 351, 352 components 329 configuration management (CM) 334, 335 continuous integration/continuous delivery
(CI/CD) 330, 331, 332 Infrastructure-as-a-Code (IaaC) 333 monitoring and improvement 332, 333 digital signal processor (DSP) 202 direct-attached storage (DAS) 209 directed acyclic graphs (DAGs) 375 disaster recovery (DR) about 65, 126 best practices, applying for 275, 276 planning 266, 267 disk mirroring 210 distributed denial-of-service (DDoS) 74, 83, 295 distributed system creating 260, 261 DNS routing strategy 215, 216 Docker 203 Domain Name Server (DNS) 177 Domain Name System (DNS) 83, 168, 224, 338 DR scenarios about 267 backup and restore 268, 269 multi-site strategy 274, 275 pilot light 269, 271 warm standby 272, 273, 274

[ 448 ]

E
Elastic Compute Cloud (EC2) 295, 347 Elastic IP (EIP) 178 Elastic Load Balancing (ELB) 173 Elastic MapReduce (EMR) 291, 374 Elastic Network Interface (ENI) 178 Elasticsearch, LogStash, and Kibaba (ELK) 213 encapsulation 400 encryption key management, methods
AWS Key Management Service (KMS) 251 envelope encryption 250 HSM 252 end-of-life (EOL) 393 Enhanced Data Rates for Global Evolution (EDGE)
224 Enterprise Resource System (ERP) 227 enterprise solution architect 29 entity-relationship (ER) 410 envelope encryption 250, 251 event stream model 165, 166 event-driven architecture
creating 163 event stream model 165, 166 publisher/subscriber model 163, 164 exabytes (EB) 364 extensibility 67, 68 extensible markup language (XML) 232 extract, transform, and load (ETL) 34, 133, 300,
374 ExtraHop 300
F
fault-tolerance 64, 65 Federal Risk and Authorization Management
Program (FedRAMP) 8, 301 Federated Identity Management (FIM) 228 field-programmable gate array (FPGA) 201 Finance Data (PCI) 35 floating IP pattern
creating 178, 179 Fluentd 360 forecast
versus budget 308 Freshservice 285

FTP Secure (FTPS) 253 fully working low capacity stand-by 272 Function as a Service (FaaS) 22, 135, 155, 192,
199
G
G-Cloud 8 General Data Protection Regulation (GDPR) 8,
393 generalists 27 Global Positioning System (GPS) 394 Google Cloud Platform (GCP) 20, 22, 138, 192,
199, 254, 288, 323, 437 graphical processing unit (GPU) 200
H
Hadoop Distributed File System (HDFS) 371 Hadoop User Experience (HUE) 375 hard-disk drive (HDD) 193, 198, 208 hardware security module (HSM) 251 Health Insurance Portability and Accountability Act
(HIPAA) 8, 35, 295 high availability (HA)
about 62 architecture, achieving 64 high-availability database pattern 186, 187 high-performance computing (HPC) 219 Hive Query language (HQL) 376 horizontal scaling 57 host-based IDS 247 host-based replication 266 Human/Computer Interaction (HCI) 343 hybrid cloud 20 hybrid cloud architecture creating 133, 134, 135 hypervisor-based replication 266
I
Identity and Access Management (IAM) 97, 229, 420
Identity Cloud Service (IDCS) 232 identity provider (IdP) 229 immutable deployment 340, 341 immutable infrastructure
canary testing 87, 88

[ 449 ]

creating 87 in-place deployment 338 Information Gain (IG) 387 Information Security Registered Assessors
Program (IRAP) 8 Information Technology Infrastructure Library (ITIL)
131, 288 Information Technology Service Management
(ITSM) 131, 288 infrastructure architect 32, 33 Infrastructure as a Service (IaaS) 22, 31, 192,
261, 308 infrastructure as code (IaC) approach 281, 333 infrastructure monitoring
about 289 example 289 infrastructure security 75 input/output operations per second (IOPS) 86,
195, 207, 289, 312 International Organization for Standardization
(ISO) 8, 301 Internet Control Message Protocol (ICMP) 245 internet gateway (IGW) 246 Internet Message Access Protocol (IAMPS) 253 Internet of Things (IoT)
about 34, 137, 355, 380, 381, 392 components 381 Internet Protocol (IP) 177 Internet Protocol Security (IPsec) 253 interoperability 70, 71 intrusion detection system (IDS) 33, 75, 246, 420 intrusion prevention system (IPS) 33, 75, 246,
420 IT Asset Management (ITAM) 284, 285 IT infrastructure
automating 98 IT Operation Analytics (ITOA) 298, 299 IT procurement documents
for solution architecture 422, 423 ITAM tools 285
J
Java Database Connectivity (JDBC) 344 Java Server Page (JSP) 142 JavaScript Object Notation (JSON) 11, 152

Jira Service Desk 285 job observer pattern 162, 163 JSON Web Token (JWT) 235
K
key performance indicators (KPIs) 34, 119, 259, 426
Kubernetes 204, 205 Kubernetes cluster 205
L
legacy system modernization techniques about 400 encapsulation 400 re-platforming 401 rearchitecting 401 redesigning 402, 403 refactoring 401 rehosting 401 replacing 402, 403
legacy systems cloud migration strategy for 403, 405
Lightweight Directory Access Protocol (LDAP) 231 live migration cutover 128, 129 load balancer
implementing 216, 217 Local Area Network (LAN) 33, 264 log monitoring 292, 293, 294 logging
automating 98 logic tier 143 loose coupling 88, 89, 90
M
Machine Learning (ML) 354, 382 working with 383, 384
maintainability 72 man-in-the-middle (MITM) attack 252 massive parallel processing (MPP) 200, 367 Memcached
versus Redis 175, 176 mentoring 439 metrics 288 micro-benchmarking 344 microservice architecture

[ 450 ]

about 11 best practices 157 creating 156, 157 Microsoft Azure 138, 323 Microsoft Visio 409 minimum viable product (MVP) 96 ML model overfitting versus ML models underfitting 385 ML model underfitting versus ML model overfitting 385 monitoring automating 98 MoSCoW 95 multi-factor authentication (MFA) 224, 228 Multi-Level Protection Scheme (MLPS) 8 multi-site strategy 274, 275 multi-tenant SaaS-based architecture creating 144, 145, 146 data level isolation 145 database level isolating 145 row level isolation 145 table level isolation 145 Multi-Tier Cloud Security (MTCS) 8 multitier architecture 141
N
n-tier layered architecture application layer 142, 143 building 141, 142 database layer 142, 143, 144 web layer 142
Net Present Value (NPV) 114 Network Access Control List (NACL) 245 Network Address Translation (NAT) 245 network architect 33 Network Interface Card (NIC) 178 network propagation 193 network security 74 network transmission medium 193 network-attached storage (NAS) 252 network-based IDS 247 network-based replication 265 Nginx 217 non-functional requirement (NFR)
about 17, 407

consideration 39 defining 38, 40 nonrelational databases (NoSQL) 212 NoSQL data store types 370 NoSQL databases about 368 versus SQL Databases 369 versus SQL databases 369
O
OAuth 234, 235 object-oriented analysis and design (OOAD) 68 Objectives and Key Results (OKRs)
about 430 superpowers 430 on-premises 20 online analytical processing (OLAP) 212, 213, 367 online transactional processing (OLTP) 211, 367 Open Web Application Security Project (OWASP)
243 OpenID Connect 234, 235 OpenShift 205 operating system (OS) 326 operational excellence, designing principles
about 280 documentation, keeping 282, 283 failures, predicting 282 failures, responding 282 improvements, keeping 282, 283 incremental changes, making 281 learning, from mistakes 282 operation, automating 280, 281 reversible changes, making 281 operational excellence, functioning about 288 alerts, handling 295, 297 incident response 295 system health, monitoring 289 operational excellence, improvement tools auditing 301 IT Operation Analytics (ITOA) 299, 300 Root cause analysis (RCA) 300 operational excellence, improvment tools reporting 301
[ 451 ]

operational excellence about 72 achieving, in public cloud 302, 303 achieving, services 302, 303 configuration management 286, 287, 288 improving 298 IT Asset Management (ITAM) 284, 286 planning 283, 284 technologies, selecting 283
operational expenditure (OpEx) 9, 306 organization units (OUs) 316 Organizational Security (SOC2) 35 ownership
taking 429
P
page cache 198 PagerDuty 285 parallel processing (MPP) 371 pay-as-you-go model 346 payment card industry (PCI) 295 Payment Card Industry Data Security Standard
(PCI DSS) 8, 76 performance monitoring
managing 219 performance optimization, computational choice
going serverless 205, 206 server instance, selecting 200, 202 working, with containers 203 performance optimization, database data search, building 213, 214 nonrelational databases (NoSQL) 212 online analytical processing (OLAP) 212, 213 online transactional processing (OLTP) 211 performance optimization, networking choice autoscaling, applying 217, 218, 219 DNS routing strategy 215, 216 load balancer, implementing 216, 217 performance optimization, storage working, with block storage 207 working, with cloud data storage 208, 209, 210 working, with file storage 208 working, with network area storage 208 working, with object storage 208, 209, 210 working, with SAN 207

performance optimization computational choice, creating 199 database, selecting 210 networking choice, making 214, 215 storage, selecting 207 technology, selecting for 199
Personally Identifiable Information (PII) 76, 121, 226
petabytes (PB) 362 phased approach 395 pilot light 270 Platform as a Service (PaaS) 22, 31, 205 platform monitoring
about 291 example 291 point of presence (PoP) 84 portability 70, 71 pre-sales skills acquiring 426, 427 predictive scaling 79, 80, 81 presentation tier 142 private clouds 20 private data 248 process control tools DAEMON Tools 243 Supervisord 243 production phase 343 proof of concept (POC) 44, 398, 408, 435 public cloud about 19, 20 architecture 21, 22 cost optimization 323, 324 operational excellence, achieving 302, 303 providers 22 public data 249 Public Key Infrastructure (PKI) 253 public-key encryption 249 publisher/subscriber model 163, 164
Q
quality assurance (QA) 260, 326, 419 queue-based architecture, patterns
about 161, 162 advantages 162 job observer pattern 162, 163

[ 452 ]

queuing chain pattern 160 queue-based architecture
building 159 consumer 160 message 160 message broker 160 producer 160 queue 160 terminology 160 queuing chain pattern 160, 161, 162
R
random-access memory (RAM) 166, 259, 289 re-platforming 401 reactive scaling 82, 83 real-time voting application reference architecture
158, 159 rearchitecting 401 Recovery Point Objective (RPO) 36, 47, 65, 186,
262, 282 recovery point objectives (RPO)
planning 263, 264 Recovery Time Objective (RTO)
about 36, 47, 65, 186, 262, 282 planning 263, 264 recovery validation performing 262 Red Hat Enterprise Linux (RHEL) 286 red-black deployment 340 redesigning 402, 403 Redis versus Memcached 175, 176 redundancy 64, 65 refactoring 401 examples 109 rehost 106 rehosting 401 Relational Database Management Systems
(RDBMS) 360 Relational Database Service (RDS) 291 relational databases 367 reliability 258 relocate 107, 108 rename distribution pattern 170, 171 replaceable resources

immutable infrastructure, creating 87 using 86, 87 replacing 403 replatform about 107 technique 107 replication methods about 265 array-based replication 265 host-based replication 266 hypervisor-based replication 266 network-based replication 265 Representational State Transfer (REST) 11, 91,
149, 252, 401, 432 repurchase
examples 110 request for information (RFI) 10, 406 request for quotation (RFQ) 406 request for x (RFx) 422 requests for proposals (RFP) 10, 406, 426 resiliency 62 resilient architecture
building 83, 85 resilient distributed datasets (RDDs) 361 responsibilities, solution architect
about 37, 38 engaging, with stakeholders 41 maintenance, ensuring 47 non-functional requirements, defining 38, 40 post-launch operability, launching 47 proof of concept (POC), developing 44 prototype, developing 44 solution delivery life cycle 45 solutions, designing 45, 46 technology selections, making 44 user requirements, analyzing 38 various architecture constraints, handling 41, 42 various architecture constraints, handling,
handling 43 working, as technology evangelist 47 working, with stakeholders 41 RESTful web service architecture 152 restricted data 248 Return on Investment (ROI) 12, 14, 42, 109, 305,
392, 421, 426

[ 453 ]

reusability 67, 68 revolution per minute (RPM) 195 rewrite proxy pattern 173, 174 Rivest�Shamir�Adleman (RSA) 249 role-based authentication (RBA) 228 roles, agile scrum team
development team 51 product owner: 51 Scrum Master 51 Scrum Team 51 rolling deployment 338 root cause analysis (RCA) about 226, 298, 300 refining 282 router hops 193
S
Salesforce CRM 308 scalability 57 scaling
capacity dilemma 58 horizontal scaling 57 vertical scaling 57 scope creep 43 search data stores 370, 371 Secure Socket Layer/Transport Layer Security
(SSL/TLS) 75 Secure Sockets Layer (SSL) 237, 296, 420 security architect
about 35 responsibilities 35 Security Assertion Markup Language (SAML) 232,
233, 234 security automation 99 security monitoring
about 295 components 295 security about 73 adding 97, 98 self-sealing system making 259 server fleet elasticity 61 server migration 126, 127 serverless architecture

building 154, 155, 156 Service Level Agreement (SLA) 263, 279, 333,
410 Service Principal Name (SPN) 230 service providers (SPs) 229, 232 service-oriented architecture (SOA) 11, 79, 90,
91, 92, 140, 148, 313 ServiceDesk Plus 285 short for Open Authorization (OAuth) 234 show-back mechanism 310 Simian Army
reference link 298 Simple Mail Transfer Protocol Secure (SMTPS)
253 Simple Object Access Protocol (SOAP) 11, 91,
149, 252 Simple Queue Service (SQS) 291 Simple Web Token (SWT) 235 Single Sign-On (SSO) 228 single tenancy 144 Small and Medium Size Businesses (SMBs) 266 SOA-based e-commerce website architecture
building 153, 154 SOAP Envelope
about 149 message body 150 parts 150 SOAP header 150 SOAP web service architecture 149, 150, 151 Software as a Service (SaaS) 31, 109, 144, 308,
403
22 Software Development Life Cycle (SDLC) 350 SolarWinds 285 solid-state drive (SSD) 198, 208 solution architect roles
architect evangelist 32 cloud architect 31 data architect 34 DevOps architect 36 enterprise solution architect 29 infrastructure architect 32, 33 network architect 33 security architect 35 technical architect 30 types 26, 28, 29

[ 454 ]

solution architect about 6, 30 builder, by engaging in coding hands-on 436 in agile organization 48 responsibilities 37 roles 26
solution architecture document (SAD) about 406 Appendix section 422 business context section 413, 414, 415 conceptual solution overview section 415, 416 purpose 407, 408 solution architecture section 416, 417, 418, 419, 420 solution delivery section 420 solution management section 421 solution overview section 412, 413 structure 411, 412 views of 408, 409, 410
solution architecture about 7 benefit 13, 14 best technology platform, selecting 15 business needs, addressing 14 business requirement 9 cost and budget 9 creating, reasons 10 end user requirement 9 evolution 11 global compliance requirement 8 globally distributed team 8 in public cloud 19 IT infrastructure requirement 9 IT procurement documentation for 422 IT procurement documents for 423 non-functional requirements (NFRs), addressing 17, 18, 19 project lifecycle, managing 17 project timeline 9 quality of delivery, addressing 15 resource and cost management, handling 16 significance 12 solution constraints and issues, addressing 16 solution delivery, managing 17 solution implementation component 9

solution maintenance 9 technology selection 9 source code repositories 350 specialists 27 Splunk 300, 322 sprint ceremonies (scrum ceremonies) backlog grooming 51 Sprint Daily Standup 51 Sprint demonstration 52 sprint planning 51 Sprint retrospect 52 SQL databases versus NoSQL databases 369 SQL injection 74 SQL injection (SQLi) 238, 420 SSH File Transfer Protocol (SFTPS) 253 staging environment 342 stateless and stateful architecture designs building 146, 147, 148 static content scaling 60 Statistical Analysis System(SAS) 62 stepped approach 395 Storage Area Network (SAN) 125, 207, 252, 264 strategy execution 430 Structure Query Language (SQL) 238 structured data stores 366 SubversioN (SVN) 350 Super-fast, Parallel, In-memory Calculation Engine
(SPICE) 378 supervised ML
about 386, 387 types 386 Support Vector Machines (SVM) 387 synchronous data replication versus asynchronous data replication 264, 265 system architecture Chaos Gorilla 298 Latency Monkey 298 Security Monkey 298 system modernization approach, defining 398, 399 assessment, of legacy application 397 benefits 395, 396 documentation 399 strategy 395

[ 455 ]

support 399
T
TCO component human resources and training costs 307 operational and maintenance costs 307 purchase and setup costs 307
technical architect 30 technology evangelist 32
becoming 439 technology, for architectural security
about 227 application, securing 242 data security 248 user identity and access management 227, 228 web security, handling 236 templates 333 tensor processing unit (TPU) 201 tera floating point operation (TFLOP) 200 terabytes (TB) 362 thinking big 431 thought leader becoming 439 three-tier architecture 141 three-tier web architecture cache distribution pattern 169, 170 Ticket-Granting Server (TGS) 229 Ticket-Granting Ticket (TGT) 230 time to market (TTM) 327 total cost of ownership (TCO) 306, 405, 428 Transmission Control Protocol (TCP) 237 Transport Security Layer (TSL) 252 Twelve-Factor App URL 352
U
Unified Modeling Language (UML) 409 Uniform Resource Identifier (URI)
about 240 using 152 Unique Resource Locator (URL) 150 unstructured data stores 371 unsupervised ML 386, 387 usability 69 User Acceptance Testing (UAT) 128, 342, 419

user experience (UX) 416 user identity and access management
AD 231 Amazon Web Services (AWS) Directory Service
232 FIM 229 Kerberos 229, 230, 231 OAuth 234 OpenID Connect 234 Security Assertion Markup Language (SAML)
232, 233, 234 SSO 229 user interface (UI) 396
V
vertical scaling 57 Virtual Interface (VIF) 362 Virtual Private Cloud (VPC) 362 Virtual Private Network (VPN) 33 Visual Studio Code (VSCode) 345 VMotion 108 VMware Cloud (VMC) 108 VPC Flow Logs 246
W
WAF sandwich architecture 241 warm standby 274 web app security vulnerabilities
about 236 buffer overflow and memory corruption attack
239 Cross-Site Request Forgery (CSRF) attacks
238, 239 Denial of Service (DoS) 236 Distributed Denial of Service (DDoS) attacks 236 SQLi attacks 238 XSS attacks 238 Web Application Firewall (WAF) 74, 83, 224 web layer 142 web security mitigation about 239 DDoS mitigation 240, 242 WAFs 239 Web Application Firewall (WAF) 240 web security

[ 456 ]

about 74 app vulnerabilities 236 handling 236 mitigation 239 Web Services Description Language (WSDL) 150

web-based microservice architecture 11 Wide Area Network (WAN) 33 workload
scaling 79 Write once read many (WORM) 207
