---
software_dev: core
---

# Programming Ruby 3.3 (preview)

> **Author(s):** Rappin · **Category:** 01_languages_and_fundamentals · **Language:** English

---

Early Praise for Programming Ruby 3.3: The Pragmatic Programmers' Guide
The book has such breadth and depth, making it a useful long-term companion. I'd say this is a big win for the Ruby community.  Stefan Magnuson
Software Developer
Programming Ruby 3.3: The Pragmatic Programmers' Guide is a valuable resource to anyone looking to get started with developing software tools and systems in Ruby. Thanks to thorough technical explanations accompanied by demonstrative code examples, this book will equip you with a mastery of all the building blocks of Ruby and help you unlock its full power.  Nishant Roy
Engineering Manager
I'm ecstatic to see the book that inspired an entire generation of Rubyists revived. I'm excited to see--and use--what the next generation of readers builds thanks to this.  Kevin Murphy
Software Developer

We've left this page blank to make the page numbers the same in the electronic and
paper books.
We tried just leaving it out, but then people wrote us to ask about the missing pages.
Anyway, Eddy the Gerbil wanted to say "hello."

Programming Ruby 3.3
The Pragmatic Programmers' Guide Noel Rappin
with Dave Thomas
The Pragmatic Bookshelf
Dallas, Texas

Many of the designations used by manufacturers and sellers to distinguish their products are claimed as trademarks. Where those designations appear in this book, and The Pragmatic Programmers, LLC was aware of a trademark claim, the designations have been printed in initial capital letters or in all capitals. The Pragmatic Starter Kit, The Pragmatic Programmer, Pragmatic Programming, Pragmatic Bookshelf, PragProg and the linking g device are trademarks of The Pragmatic Programmers, LLC.
Every precaution was taken in the preparation of this book. However, the publisher assumes no responsibility for errors or omissions, or for damages that may result from the use of information (including program listings) contained herein.
Our Pragmatic courses, workshops, and other products can help you and your team create better software and have more fun. For more information, as well as the latest Pragmatic titles, please visit us at http://pragprog.com. For our complete catalog of hands-on, practical, and Pragmatic content for software developers, please visit https://pragprog.com.

The team that produced this book includes:

Publisher:

Dave Thomas

COO:

Janet Furlow

Managing Editor: Tammy Coron

Development Editor: Katharine Dvorak

Copy Editor:

Corina Lebegioara

Indexing:

Potomac Indexing, LLC

Layout:

Gilson Graphics

For sales, volume licensing, and support, please contact support@pragprog.com.

For international rights, please contact rights@pragprog.com.

Copyright � 2024 The Pragmatic Programmers, LLC.
All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form, or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior consent of the publisher.
ISBN-13: 978-1-68050-982-3 Encoded using the finest acid-free high-entropy binary digits. Book version: P1.0--January 2024

Contents

Preface . . . . . . . . . . . . . . . xiii Acknowledgments . . . . . . . . . . . . xvii

Part I -- Facets of Ruby

1. Getting Started . . . . . . . . . . . . . . 3

Installing Ruby

3

Installing Ruby for Windows

7

Running Ruby

11

Creating Ruby Programs

12

Getting More Information about Ruby

14

What's Next

15

2. Ruby.new . . . . . . . . . . . . . . . 17

Ruby Is an Object-Oriented Language

17

Some Basic Ruby

19

Arrays and Hashes

22

Symbols

24

Control Structures

25

Regular Expressions

26

Blocks

28

Reading and `Riting

30

Command-Line Arguments

30

Commenting Ruby

31

What's Next

31

3. Classes, Objects, and Variables . . . . . . . . . . 33

Defining Classes

33

Objects and Attributes

36

Classes Working with Other Classes

42

Specifying Access Control

45

Variables

48

Reopening Classes

49

What's Next

51

Contents � vi

4. Collections, Blocks, and Iterators . . . . . . . . . . 53

Arrays

53

Hashes

56

Digging

58

Word Frequency: Using Hashes and Arrays

58

Blocks and Enumeration

62

What's Next

83

5. More about Methods . . . . . . . . . . . . 85

Defining a Method

85

Calling a Method

93

What's Next

99

6. Sharing Functionality: Inheritance, Modules, and Mixins . . . . 101

Inheritance and Messages

101

Modules

105

Inheritance, Mixins, and Design

115

What's Next

116

7. Basic Types: Numbers, Strings, and Ranges . . . . . . . 117

Numbers

117

Strings

120

Ranges

125

What's Next

127

8. Regular Expressions . . . . . . . . . . . . 129

What Regular Expressions Let You Do

129

Creating and Using Regular Expressions

129

Regular Expression Patterns

132

Regular Expression Syntax

134

What's Next

142

9. Expressions . . . . . . . . . . . . . . 143

Operator Expressions

143

Command Expressions

146

Assignment

146

Conditional Execution

150

Loops and Iterators

157

Pattern Matching

163

What's Next

170

10. Exceptions . . . . . . . . . . . . . . 171

The Exception Class

171

Handling Exceptions

172

Raising Exceptions

175

Using Catch and Throw

177

What's Next

178

11. Basic Input and Output . . . . . . . . . . . . 179

What Is an I/O Object?

179

Contents � vii

Opening and Closing Files

179

Reading and Writing Files

180

Talking to Networks

185

What's Next

186

12. Threads, Fibers, and Ractors . . . . . . . . . . 187

Multithreading with Threads

188

Running Multiple External Processes

196

Creating Fibers

200

Understanding Ractors

202

What's Next

206

13. Testing Ruby Code . . . . . . . . . . . . . 207

Why Unit Test?

207

Testing with Minitest

208

Structuring Tests

212

Creating Mock Objects in Minitest

215

Organizing and Running Tests

217

Testing with RSpec

219

What's Next

228

Part II -- Ruby in Its Setting

14. Ruby from the Command Line . . . . . . . . . . 231

Calling the Ruby Command

231

Ruby Command-Line Options

233

Making Your Code an Executable Program

237

Processing Command-Line Arguments to Your Code

237

Accessing Environment Variables

242

Where Ruby Finds Its Libraries

244

Using the Rake Build Tool

245

The Build Environment

249

What's Next

249

15. Ruby Gems . . . . . . . . . . . . . . 251

Installing and Managing Gems

251

Using Bundler to Manage Groups of Gems

254

Writing and Packaging Your Own Code into Gems

261

Organizing Your Source Code

266

Distributing and Installing Your Code

272

What's Next

275

16. Interactive Ruby . . . . . . . . . . . . . 277

Using irb

278

Navigating irb

280

Configuring irb

283

What's Next

288

Contents � viii

17. Debugging Ruby . . . . . . . . . . . . . 289

Printing Things

289

The Ruby Debugger

290

Pry

293

Debugging Performance Issues with Benchmark

296

What's Next

297

18. Typed Ruby . . . . . . . . . . . . . . 299

What's a Type?

299

Official Ruby Typing with RBS

301

Ruby Typing with Sorbet

307

What's Next

311

19. Documenting Ruby . . . . . . . . . . . . 313

Documenting with RDoc

313

Adding RDoc to Ruby Code

316

Running RDoc

320

Documenting with YARD

321

What's Next

324

Part III -- Ruby Crystallized

20. Ruby and the Web . . . . . . . . . . . . . 327

Ruby's Web Utilities

327

Templating with ERB

329

Serving Ruby Code to the Web

332

Ruby in the Browser with Web Assembly

340

What's Next

342

21. Ruby Style . . . . . . . . . . . . . . 343

Written Ruby Style

343

Using RuboCop

348

Using Standard

353

Ruby Style in the Large

354

Duck Typing

356

What's Next

369

22. The Ruby Object Model and Metaprogramming . . . . . . 371

Understanding Objects and Classes

371

Defining Singleton Methods

374

Inheritance and Visibility

380

Modules and Mixins

381

Metaprogramming Class-Level Macros

387

Using instance_eval and class_eval

396

Using Hook Methods

399

A Metaprogramming Example

405

Top-Level Execution Environment

407

What's Next

408

Contents � ix

23. Reflection and Object Space . . . . . . . . . . 409

Looking at Objects

409

Looking at Classes

411

Calling Methods Dynamically

413

System Hooks

415

Tracing Your Program's Execution

417

Behind the Curtain: The Ruby VM

419

Marshaling and Distributed Ruby

420

What's Next

425

Part IV -- Ruby Language Reference

24. Language Reference: Literal Types and Expressions . . . . . 429

Source Layout

429

Ruby Literals

432

Regular Expressions

440

Names

445

Values, Variables, and Constants

447

Expressions, Conditionals, and Loops

453

25. Language Reference: Objects and Classes Method Definition Invoking a Method Aliasing Defining Classes Defining Modules Access Control Blocks, Closures, and Proc Objects Exceptions Catch and Throw Typed Ruby

. . . . . . . 465 465 470 475 476 478 480 480 484 486 487

Part V -- Ruby Library Reference

26. Library Reference: Core Data Types . . . . . . . . . 495

Dates and Times

495

Math

502

Numbers

503

Random and SecureRandom

510

Regexp

511

Strings

523

Symbols

534

27. Library Reference: Ruby's Object Model . . . . . . . . 537

BasicObject

537

Class

540

Comparable

540

Kernel

541

Contents � x

Method

551

Module

552

Object

557

28. Library Reference: Enumerators and Containers . . . . . . 561

Array

561

Enumerable

568

Enumerator

577

Hash

579

Set

584

29. Library Reference: Input, Output, Files, and Formats . . . . . 587

CSV

587

Dir

590

File

593

FileUtils

597

IO

600

JSON

609

Pathname

611

StringIO

612

Tempfile

613

URI

614

YAML

616

30. Library Reference: Ruby on Ruby . . . . . . . . . 619

Benchmark

619

Data

621

Delegator and SimpleDelegator

622

Logger

623

ObjectSpace

624

Observable

625

OpenStruct

627

PP

627

Prism

628

Ripper

630

Singleton

632

Struct

632

Unbound Method

634

Part VI -- Appendixes

A1. Troubleshooting Ruby . . . . . . . . . . . . 637

Common Issues

637

Debugging Tips

640

A2. I Can't Look It Up! . . . . . . . . . . . . . 641

A3. Command-Line Basics . . . . . . . . . . . . 645

The Command Prompt

645

Folders, Directories, and Navigation

645

Contents � xi

A4. Ruby Runtimes . . . . . . . . . . . . . 649

Just-in-Time Compilers

649

TruffleRuby

651

JRuby

652

mRuby

653

Other Runtimes

654

A5. Ruby Changes . . . . . . . . . . . . . . 655

Version 2.0

655

Version 2.1

655

Version 2.2

656

Version 2.3

656

Version 2.4

656

Version 2.5

656

Version 2.6

656

Version 2.7

656

Version 3.0

657

Version 3.1

657

Version 3.2

657

Version 3.3

657

Index . . . . . . . . . . . . . . . . 659

Preface
This is the fifth edition of Programming Ruby, which many Ruby developers call "The Pickaxe Book." It covers Ruby up to and including Ruby 3.3.
Since the previous edition of this book, Ruby has continued to grow and evolve. New syntax has been added; old syntax has been refined. Major new features, such as pattern matching and type signatures, are now part of the language. Tools that didn't exist or were in their early stages of development then are now in constant use by Ruby developers around the world. The entire ecosystem is thriving.
The Pickaxe Book continues to be your guide to learning Ruby the language and understanding how Ruby's parts work together and how you can use the most popular and important Ruby tools.
Why Ruby?
When Dave Thomas and Andy Hunt wrote the first edition, they explained the appeal of Ruby. Among other things, they wrote, "When we discovered Ruby, we realized that we'd found what we'd been looking for. More than any other language with which we have worked, Ruby stays out of your way. You can concentrate on solving the problem at hand, instead of struggling with compiler and language issues. That's how it can help you become a better programmer: by giving you the chance to spend your time creating solutions for your users, not for the compiler."
That belief is even stronger today. More than thirty years after Ruby's first release on February 24, 1993, Ruby still enables developers to focus on their solutions--from the smallest utility script to the services of companies with billions of dollars in revenue. Ruby can support it all.
A Word about Ruby Versions
This edition of The Pickaxe Book documents Ruby up to and including Ruby 3.3. New Ruby version releases come out annually on December 25. The book's code was developed against Ruby 3.3, preview 2, but we don't expect substantial changes in the released version of Ruby 3.3.
In this book, we don't typically note what version of Ruby introduced a new feature, but you can find a brief list of the largest changes in Appendix 5, Ruby Changes, on page 655. We recommend referring to the Ruby Evolution page by Victor Shepelev at https://rubyreferences.github.io/rubychanges/evolution.html for a full listing of the changes implemented since Ruby 2.0.
report erratum � discuss

Preface � xiv

Exactly what version of Ruby did we use to write this book? Let's ask Ruby:

$ ruby -v ruby 3.3.0dev (2023-11-01T17:47:26Z master 909afcb4fc) [arm64-darwin23]

This illustrates an important point. Most of the code samples you see in this book are executed each time we format the book. When you see output from a program, that output was produced by running the code and inserting the results into the book.

Notation Conventions

Literal code examples are shown using a sans-serif font:

class SampleCode def run #... end
end

In this book, a class name followed by a hash followed by a method name, as in Fred#do_something, is a reference to an instance method (in this case, the method do_something of class Fred). Class methods are written with a dot as in Fred.new, and Fred.EOF is a class constant. In other Ruby documentation, you may see class methods written as Fred::new. This is perfectly valid Ruby syntax; we just happen to think that Fred.new is less distracting to read and is much more common to see in practice.
The decision to use a hash character to indicate instance methods was a tough one. It isn't valid Ruby syntax, but we thought that it was important to differentiate between the instance and class methods of a particular class. When you see us use File.read, you know we're talking about the class method read. When, instead, we use File#read, we're referring to the instance method read. This convention is standard in most Ruby discussions and documentation.

When discussing various commands or Ruby snippets, we'll refer to variable parts of the commands by including them in angle brackets. So, if we say rbenv global <VERSION>, that means the section in the brackets is not a literal part of the command, and you'd replace it with the actual value you wanted to use, for example, rbenv global 3.3.0.
This book contains many snippets of Ruby code. Where possible, we've tried to show what happens when they run. In some cases, we show the value of expressions on the same line as the expression. Here's an example:

a=1 b=2 a+b

# => 3

Here, you can see that the result of evaluating a + b is the value 3, shown in a comment at the end of the line, # => 3. If you typed this fragment of code into a file and executed it using Ruby, you wouldn't see the value 3 output--you'd need to use a method such as puts to have the values written to the program's output.

a=1 a+2

# => 1 # => 3

If the program produces more complex output, we show it after the program code:

report erratum � discuss

Road Map � xv
3.times { puts "Hello!" }
produces: Hello! Hello! Hello!
In some of the library documentation, we wanted to show where spaces appear in the output. You'll see these spaces as  characters.
Unless we're trying to make a point or highlight a specific language feature, Ruby code examples have been formatted to match the rules of the Standard gem1.
Command-line invocations are shown with literal text in a regular font, and the parameters you supply are shown in an italic font. Optional elements are shown in brackets.
ruby < flags >* progname < arguments >*
In keeping with the style of previous editions of the book, we use the word we when referring to the authors collectively in the body of the book. Many of the words come from the first four editions, and I (Noel) don't want to claim any credit for Dave Thomas's, Andy Hunt's, and Chad Fowler's previous work. That said, opinions on recent Ruby features, even when prefaced by "we," are just my (Noel's) opinions and are not an attempt to put words in the mouths of the previous authors.
Road Map
The main text of this book is divided into five parts, each with its own personality and each addressing different aspects of the Ruby language.
Part I, Facets of Ruby, is a Ruby tutorial. It starts with notes on getting Ruby running on your system followed by a short chapter on the terminology and concepts that are unique to Ruby. The initial chapter also includes enough basic syntax so that the other chapters will make sense. The rest of the tutorial is a top-down look at Ruby. There we talk about classes and objects, types, expressions, and all the other things that make up the language. We end with a chapter on unit testing.
Part II, Ruby in Its Setting, investigates one of the great things about Ruby, which is how well it integrates with its environment. Here you'll find practical information on using Ruby: using the interpreter options, working with irb, documenting your Ruby code, type checking, and packaging your Ruby gems so that others can enjoy them.
Part III, Ruby Crystallized, contains more advanced material. Here you'll find all the details about using Ruby for the web, Ruby style, the concept of duck typing, the object model, metaprogramming, reflection, and object space. You could probably speed-read this the first time through, but we think you'll come back to it as you start to use Ruby in earnest.
Part IV, Ruby Language Reference, includes more complete notes on syntax and fuller documentation of language features discussed in the first three parts.
Part V, Ruby Library Reference, isn't a complete reference of the entire Ruby library--that's much more readily available at https://docs.ruby-lang.org/en--but it's a map to the most commonly used and most useful features of the library.
1. https://github.com/testdouble/standard
report erratum � discuss

Preface � xvi
How should you read this book? Well, depending on your level of expertise with programming in general and object-oriented programming in particular, you may initially want to read just a few portions of the book. Here are our recommendations. If you're a beginner, you may want to start with the tutorial material in Part I. Keep the library reference close at hand as you start to write programs. Get familiar with the basic classes such as Array, Hash, and String. As you become more comfortable in the environment, you may want to investigate some of the more advanced topics in Part III. If you're already comfortable with JavaScript, Python, or Java, then we suggest reading Chapter 1, Getting Started, on page 3, which talks about installing and running Ruby, followed by the introduction in Chapter 2, Ruby.new, on page 17. From there, you may want to take the slower approach and keep going with the tutorial that follows, or you can skip ahead to the details starting in Part III, followed by the language reference in Part IV and the library reference in Part V. Experts, gurus, and "I-don't-need-no-stinking-tutorial" types can dive straight into the language reference in Chapter 24, Language Reference: Literal Types and Expressions, on page 429, skim through the library reference, and then use the book as a (rather attractive) coffee coaster. Of course, nothing is wrong with starting at the beginning and working your way through page by page. And don't forget: if you run into a problem that you can't figure out, help is available. For more information, see Appendix 1, Troubleshooting Ruby, on page 637.
Resources
Visit the Ruby website at http://www.ruby-lang.org to see what's new. You can find a list of community resources, including the official mailing list and Discord server, at https://www.rubylang.org/en/community. And we'd certainly appreciate hearing from you. Comments, suggestions, errors in the text, and problems in the examples are all welcome. Email us at rubybook@pragprog.com. If you find errors in the book, you can add them to the errata page at https://devtalk.com/books/ programming-ruby-3-2-5th-edition/errata. If you're reading the PDF version of the book, you can also report an erratum by clicking the link in the page footers. You'll find links to the source code for almost all of the book's code examples at https://www.pragprog.com/titles/ruby5. With all that out of the way, let's start learning about Ruby.
report erratum � discuss

Acknowledgments
In January 2001, I bought myself a programming book as a birthday present. It had a pickaxe on the cover, and it was written by the two people who wrote The Pragmatic Programmer. It was about this new programming language from Japan that I had heard about on the Extreme Programming mailing list, and which sounded very interesting.
I can't thank Dave Thomas and Andy Hunt enough. It's hard to even begin to list what I've gained from purchasing that initial book and from my association with The Pragmatic Bookshelf. Thanks also to Chad Fowler for his work on subsequent versions of the book. I inherited a great book from the three of you, and I hope this version will continue to bring people into the Ruby language and the Ruby community.
The path from buying a book on a whim to being the person updating that book more than 20 years later doesn't happen without a lot of help.
As much as I love Ruby the language, I also love Ruby the community and the many, many people who I've come to know through Ruby. The risk of starting to list people is that I'm sure I will inadvertently leave somebody out, but I want to particularly thank Gregg Pollack, Jason Seifer, Avdi Grimm, James Edward Gray II, Betsy Haibel, Justin Searls, Marty Haught, Kerri Miller, Brian Hogan, Ray Hightower, Fable Tales, Matt Polito, Even Light, Allison McMillan, and Jim Remsik. There are many more I could list--thank you to all of you.
Mark Guzdial was my graduate advisor and the person who encouraged me to write about programming and teach programming.
This is somehow the seventh title I've worked on with Katharine Dvorak as the editor. As always, she makes working on the book easier and helps structure the book into its most coherent form. Dave Rankin at The Pragmatic Bookshelf was the person who agreed to let me work on this book. Thanks so much for the opportunity and the vote of confidence.
The following people reviewed all or part of the book, and their feedback and knowledge have made this a better and more accurate book: Jean Boussier, Avdi Grimm, Chris Houhoulis, Gabi Jack, Bernard Kaiflin, Brian Lesperance, Stefan Magnuson, Kevin Murphy, Ryan Prinz, Nishant Roy, Victor Shepelev, and Brandon Weaver.
Everything in my life is better because of my family. Thanks to my children, Amit and Elliot, who have enriched my life in so many ways. And something beyond thanks to my wife Erin, these small sentences can't express how much I love you and how much your love and support mean to me.
report erratum � discuss

Part I
Facets of Ruby
Welcome to Ruby! Part I is a tutorial covering all the Ruby you'll need to be able to understand a good-sized Ruby application. We'll explore the most important parts of the syntax and the standard library, and go beyond the basics in a couple of places where Ruby has a particularly interesting or powerful tool at hand.

CHAPTER 1
Getting Started
We're going to spend a lot of time in this book talking about the Ruby language. Before we do, we want to make sure you can get Ruby installed and running on your computer. That way, you can try the sample code and experiment on your own as you read along. If you want to learn Ruby you should get into the habit of writing code as you're reading.
If you aren't comfortable with using a command line, we can help. Please turn to Appendix 3, Command-Line Basics, on page 645, and we'll give you all the information you need to get started.
Installing Ruby
There is a good chance your operating system already has Ruby installed. Try typing ruby --version at a command prompt--you may be pleasantly surprised. But you're likely to find that the Ruby version is out of date. For example, at the time of this writing, MacOS ships with Ruby 2.6.10, which is multiple versions behind the current Ruby.
The examples in this book are written against Ruby 3.3. While most of the code will work in older versions of Ruby, for performance and security reasons you should try to get on the most current version. Refer to Appendix 5, Ruby Changes, on page 655, for a listing of the features added and changes made to Ruby at each iteration.
You can install Ruby in a variety of different ways, so providing general installation instructions becomes a little bit of a choose-your-own-adventure story. Most of the examples in this book assume you're using a Linux- or Unix-style system that responds to Linux-style commands. This includes all Linux distributions, macOS, Windows systems running Windows Subsystem for Linux (WSL),1 and most Docker2 containers as well as cloud-based development environments such as Replit.3
That said, Ruby does run on Windows. The process for managing a Ruby installation on Windows is different, and we'll cover it in full detail later in this chapter.
Please note that the tooling for Ruby's installation does change frequently, and some of the specific instructions might be out of date or replaced by newer tools.
1. https://docs.microsoft.com/en-us/windows/wsl/install 2. https://www.docker.com 3. https://replit.com
report erratum � discuss

Chapter 1. Getting Started � 4
Opting Out of Installation If you don't want to install anything on your computer for some reason, you can take advantage of cloud-based development environments such as Replit or GitHub Codespaces. These environments enable you to write your code in a browser and run it against a cloud-based virtual machine.
Installing Ruby with the rbenv Version Manager
To facilitate our installation of Ruby, we'll use a version manager, which is a tool that allows you to install and switch between multiple Ruby versions on the same machine. There are many reasons to use a version manager to handle your Ruby installation. Being able to easily switch between multiple versions of Ruby gives you the flexibility to work with multiple projects that might have been written at different times. In addition, the version managers have been created for easy installation, so installing multiple Ruby versions with a version manager is easier than installing a single version by itself. More powerful and easier to use is a hard combination to beat. If you're interested in downloading only one version of Ruby, you can find system-by-system instructions at https://www.ruby-lang.org/en/ documentation/installation. The tool we'll use in this book is called rbenv.4 Rbenv isn't the only Ruby version manager, but it's probably the most commonly used these days. Other commonly used version managers are RVM5 and chruby.6 (And yes, having competing tools named "RVM" and "rbenv" is confusing.) If you're using version management for multiple languages, you might want to look at a project called asdf, which unifies different languages' version managers,7 and is rapidly becoming more popular within Ruby.
We'll install rbenv through the conveniently provided rbenv-installer program. If executing somebody else's shell script makes you nervous, you can inspect the script at https://github.com/ rbenv/rbenv-installer/blob/main/bin/rbenv-installer before you run it.
From a command terminal, enter this command all on one line (the line is split here for pagewidth reasons):
$ curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash
Curl is a command-line tool for accessing URLs and doing something useful with the return value--in this case, retrieving a shell script from the rbenv GitHub repo and passing it along to a bash shell to be executed.
This script will install rbenv using the appropriate package manager for your system, and will also install a helper program called ruby-build that will manage the download and installation of different Ruby versions.
The installation command might produce a lot of output--especially if you're on a MacOS system that uses the Homebrew package manager. On a Mac, it should end with the following (a Windows user under WSL might see something different):
4. https://github.com/rbenv/rbenv 5. https://rvm.io 6. https://github.com/postmodern/chruby 7. https://asdf-vm.com
report erratum � discuss

Installing Ruby � 5
All done! Note that this installer does NOT edit your shell configuration files: 1. Run `rbenv init' to view instructions on how to configure rbenv for your shell. 2. Launch a new terminal window after editing shell configuration files.
Following instructions, run rbenv init. This is the output on a Mac running zshell (your instructions may be different):
$ rbenv init # Load rbenv automatically by appending # the following to ~/.zshrc:
eval "$(rbenv init - zsh)"
No matter what your setup is, what you should get in this instruction is:
� The file that contains the shell configuration you need to update � The text you need to put at the end of the file
You need to put the suggested line of text at the end of your configuration file and open a new terminal window. The change only takes effect when a window is loaded, so the easiest way to get rbenv started is to open a new terminal window. If you have any questions about how to use the terminal, see Appendix 3, Command-Line Basics, on page 645.
Now, let's install a specific Ruby version.
Installing Rubies with rbenv Rbenv allows you to see a list of the Ruby versions you'll most likely want to install with the command rbenv install -l. Here's the current list (as I write this, 3.3.0 is not fully released):
$ rbenv install -l 2.7.8 3.0.6 3.1.4 3.2.2 jruby-9.4.2.0 mruby-3.2.0 picoruby-3.0.0 truffleruby-22.3.1 truffleruby+graalvm-22.3.1
Only latest stable releases for each Ruby implementation are shown. Use 'rbenv install --list-all / -L' to show all local versions.
This list has the most up-to-date patch versions of various Ruby implementations. You can see the current minor versions for the major Ruby versions 2.7, 3.0, 3.1, 3.2, and 3.3. (When talking about different Ruby implementations, the main one is sometimes called CRuby and other times called MRI, for "Matz's Ruby Interpreter.") There are also other versions we're not going to talk about much here. JRuby8 is a Ruby version that runs on the Java Virtual Machine. Mruby is a special limited build of Ruby for running on embedded hardware. TruffleRuby9 is an implementation of the language that is focused on high performance.
Our interest right now is Ruby 3.3.0, which we can install with the command rbenv install 3.3.0. (If Ruby 3.3.0 isn't out as you read this, you can use 3.2.2 or 3.3.0-dev.) If you don't see
8. https://www.jruby.org 9. https://github.com/oracle/truffleruby
report erratum � discuss

Chapter 1. Getting Started � 6
the most current version of Ruby on the list, and you've installed rbenv previously, you may get instructions on how to update ruby-build to get newer Ruby versions in your list. Note that none of the rbenv commands require us to have superuser access or to use sudo. One of the joys of the Ruby version managers, including rbenv, is that they do everything inside your home directory--you don't have any special system privileges to install or use new Ruby versions.
$ rbenv install 3.3.0 To follow progress, use 'tail -f <REDACTED>' or pass --verbose Installing openssl-3.1.0... Installed openssl-3.1.0 to /Users/noel/.rbenv/versions/3.3.0 Installing ruby-3.3.0... ruby-build: using readline from homebrew ruby-build: using gmp from homebrew Installed ruby-3.3.0 to /Users/noel/.rbenv/versions/3.3.0
Your output may be slightly different, depending on the exact version number and whether you're re-installing the Ruby version. We can verify that the Ruby version has been installed with rbenv versions, for example:
$ rbenv versions * system
3.3.0
The system here is the pre-defined Ruby for the operating system if such a thing exists, and the asterisk shows which version is currently active. Right now, the system Ruby is still active. Let's change that.
Switching Rubies with rbenv This is where we start to see the payoff. Once different Ruby versions are installed, rbenv allows us multiple ways to switch the Ruby version we're using. The command rbenv local <version> changes the Ruby version for the directory you're in:
$ ruby --version ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.arm64e-darwin22] $ rbenv local 3.3.0 $ ruby --version ruby 3.3.0 (2023-11-02T22:34:58Z master ac8ec004e5) [arm64-darwin23]
If the new Ruby you think you've installed doesn't seem to be available, you may need to run the command rbenv rehash. This command produces no output, but it does enable rbenv to use the newly installed Ruby. This setting for the directory persists even if you leave the directory and come back. (If you don't want the change to persist beyond the current session, you can use rbenv shell <VERSION> instead of rbenv local.)
report erratum � discuss

Installing Ruby for Windows � 7
$ cd .. $ cd test $ ruby --version ruby 3.3.0 (2023-11-02T22:34:58Z master ac8ec004e5) [arm64-darwin23]
Rbenv accomplishes this by putting a file in the directory called .ruby-version, which only contains the version number of the Ruby you've set for that directory.
% cat .ruby-version 3.3.0
This file also works in reverse. If you have rbenv installed and you change to a directory that contains a .ruby-version file, one of two things will happen. Rbenv will either automatically change to that Ruby version if it's installed or warn you that the directory expects an uninstalled Ruby if it isn't. Many Ruby projects use a .ruby-version file to specify their Ruby version, and it's respected by all the Ruby version managers. If you want to set a default Ruby version for directories that don't specify their own, you can do so with rbenv global <version>. This may be more work than you were expecting to install Ruby. If all you ever wanted to do was use a single version of Ruby, we'd agree. But what you've done here is give yourself an incredible amount of flexibility. Maybe in the future, a project comes along that uses Ruby 2.7.5, per its .ruby-version file. That's not a problem--use rbenv install 2.7.5, and rbenv will automatically pick up the version from the .ruby-version file.
What Is rbenv Actually Doing?
Rbenv attempts to provide its dynamic behavior with as little change to your regular terminal environment as possible. A Unix terminal uses a global environment variable called PATH to determine what directories it looks in for executable programs when you type a command. If you look in your configuration file for your terminal, you'll likely see the PATH variable being modified. When the rbenv init command is executed as part of your terminal setup, it inserts a directory at the front of your PATH, so that your operating system will look in the rbenv directory before looking anyplace else. That directory has a set of what rbenv calls shims--small programs that match all the executable commands in all your Ruby versions. (The reason why you may need to run rbenv rehash after installing a new Ruby is to refresh this directory.) When you call a Ruby command like ruby or (as you'll see in a minute) irb, the rbenv shim is encountered first, and it dynamically chooses which Ruby is active, usually based on the presence of a .ruby-version file. Then the command is handed off to the actual executable program in that current version. You can see these actual versions, they live in your home directory at ~/.rbenv/versions.
Installing Ruby for Windows
Ruby isn't available as a default option in Windows the way it's in Unix distributions or MacOS, but it can be installed and used and can interact with the underlying environment to automate Windows-specific resources.
report erratum � discuss

Chapter 1. Getting Started � 8
We're going to focus on two ways to install Ruby on Windows: using the Windows Subsystem for Linux (WSL)10, which allows you to run a Linux command-line terminal in your Windows system, and using RubyInstaller11 to install a Windows application that lets you execute Ruby programs.
The two different kinds of Ruby can both be installed on the same machine and have different purposes. Using WSL gives you a command shell that's effectively a Linux distribution, allowing you to seamlessly use any of the other Ruby tooling in this book. Using RubyInstaller gives you access to Ruby from within a regular Windows PowerShell prompt, allowing you to execute Ruby programs from File Explorer, and giving you access to Windows-specific libraries.
No matter which way you want to run Ruby, you should also install Windows Terminal so that you have a fully-featured terminal program available. You can download Windows Terminal at https://docs.microsoft.com/en-us/windows/terminal/install, where you'll also find instructions on how to make it your default terminal program. From Windows Terminal, you can set up new command-line sessions using either Microsoft's PowerShell or the WSL shell. (You can also use Visual Studio Code's terminal to run either kind of command line.)
Also, if you need a brief tutorial on how Unix command lines work, see Appendix 3, Command-Line Basics, on page 645.
Using Windows Subsystem for Linux
Windows Subsystem for Linux (WSL) allows you to run a Linux distribution binary inside your Windows setup without incurring the performance penalty of using a virtual machine or Docker container. WSL defines the wiring between the Linux OS commands and the Windows OS, allowing you to run your favorite Linux distribution from a command line transparently without having to deal with the Windows part at all. You can also have editing tools like Visual Studio Code or RubyMine interact with WSL as they run your Ruby code.
We're going to cover the basics of how to use WSL here, but if you need more information, the official documentation is available from Microsoft.12
Installing WSL The first step in using Ruby with WSL is installing WSL itself. According to the WSL website, you need to be running Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11 for this to work. We're installing WSL version 2 here.
You need to open an administrator Windows command terminal--it doesn't matter whether it's PowerShell or the regular terminal, but it does have to be an administrator shell. In Windows 11, the easiest way to get an admin shell is to right-click on the start menu and select the "Windows Terminal (Administrator)" option, which will open Windows Terminal in an admin shell. Depending on your Windows version, you may get prompted to say whether you'll allow the program to make changes to your system. Say yes.
From the admin shell, type the command wsl --install. This will give us the default Linux installation, which is Ubuntu. The session looks like this when it's through, but it may take a little time to get through the download and installation process.
10. https://docs.microsoft.com/en-us/windows/wsl 11. https://rubyinstaller.org 12. https://docs.microsoft.com/en-us/windows/wsl
report erratum � discuss

Installing Ruby for Windows � 9
PS C: \Users\noelr> wsl --install Installing: Virtual Machine Platform Virtual Machine Platform has been installed. Installing: Windows Subsystem for Linux Windows Subsystem for Linux has been installed. Downloading: WSL Kernel Installing: WSL Kernel WSL Kernel has been installed. Downloading: GUI App Support Installing: GUI App Support GUI App Support has been installed. Downloading: Ubuntu The requested operation is successful. Changes will not be effective until the system is rebooted
Reboot the system. This may take some time.
When the system comes back up, open Windows Terminal. The pull-down menu in the tab bar should now give you the option of an Ubuntu prompt. You may get prompted to do a sudo apt-get update to update programs in the Ubuntu distribution.
You'll then get prompted to create a Unix account for WSL:
Installing, this may take a few minutes. Please create a default UNIX user account. The username does not need to match your Windows username For more information visit: httos://aka.ms/wslusers Enter new UNIX username:
The username isn't in any way connected to your Windows account--it's a brand-new account for the Linux distribution you've installed using WSL. After you enter the username, you'll be prompted for the password. You won't get challenged for the password every time you open a WSL terminal, but you should write it down just in case because someday you may want to sudo something, and you'll get asked for your password before getting superuser rights. (Ask us how we know.) That said, don't depend on this password being super-secure by default; the root WSL user has no password.
At this point, you can use Windows Terminal to open a WSL terminal by clicking the downward arrow next to the + in the tab bar and selecting Ubuntu from the menu.
Installing Ruby under WSL We're partway there, but the default Ubuntu installation doesn't include Ruby or a version manager. These instructions are adapted from https://gorails.com/setup/windows/10#linux-subsystem.
The Ubuntu distribution uses a package manager called apt-get to distribute its applications. We need to install some dependencies:
$ sudo apt-get update $ sudo apt-get install git-core curl $ sudo apt-get install zlib1g-dev build-essential libssl-dev $ sudo apt-get install libreadline-dev libyaml-dev libsqlite3-dev sqlite3 $ sudo apt-get install libxml2-dev libxslt1-dev libcurl4-openssl-dev $ sudo apt-get install software-properties-common libffi-dev
report erratum � discuss

Chapter 1. Getting Started � 10
The first line updates apt-get itself so you can get the most current version of everything, and the following lines install the packages that Ruby will need. Note that you can do all those installs on a single line (we're splitting it up here for page-width purposes).
At this point, you should be able to install the rbenv version manager using the instructions in Installing Ruby with the rbenv Version Manager, on page 4. The GoRails site mentioned before has slightly different rbenv instructions, they should both work.
Using WSL and Ruby You should be good to go, as you can confirm by opening up a new WSL terminal and typing irb. Within WSL, you can use any of the Unix tools that we've described elsewhere in this book.
Ruby programs can be invoked using ruby from the WSL command line as we'll discuss in Chapter 14, Ruby from the Command Line, on page 231. Where it gets a little bit tricky is in sharing files. WSL sets up what is, in effect, its own file system. For performance reasons, you're encouraged to keep all the files you use in WSL code in the WSL file system (as apparently file read and write between the two systems is expensive).
That said, it is possible to share files. Windows files are set up in WSL under the mnt directory (short for "mount point"). Your C: drive is /mnt/c. You can access Windows files using that path as a prefix. Other drives, like network drives, can also be connected to a mount point, but it doesn't happen by default.
From the Windows side, WSL files show up in File Explorer under their own "Linux" heading. You can right-click those files and open them in a Windows editor, but you can't directly invoke them in WSL from the Windows file system. (You could, in theory, create a shortcut that invokes a terminal and a single bash command to run a WSL file.)
Visual Studio Code has a WSL extension that you can install that allows you to load a WSL directory from the regular Windows version of Visual Studio Code. Run that directory using the WSL ruby, and use the WSL terminal as a prompt. Similarly, RubyMine allows you to connect to WSL as a remote interpreter, open a WSL project, and run it using the WSL Ruby.
Using RubyInstaller
Although WSL is nice, and it's great to be able to seamlessly integrate with existing Ruby tooling, from the point of view of a Windows user, it does have some drawbacks. WSL has some performance overhead, including taking up a lot of memory. It also doesn't integrate with the Windows system directly, meaning that you can't do Windows-specific things.
A native Ruby installation is available for Windows, and it's simply called RubyInstaller.13 RubyInstaller is a regular Windows installer that gives you a regular Windows executable Ruby interpreter that you can use to run Ruby code.
Installing Ruby with RubyInstaller You can download RubyInstaller from https://rubyinstaller.org, where you can find versions corresponding to each Ruby patch version for both x64 and x86 machines. There are versions both with and without Devkit, which is an add-on that allows Ruby gems that

13. https://rubyinstaller.org

report erratum � discuss

Running Ruby � 11
have native C-language extensions to be compiled. A couple of prominent Ruby gems have extensions, so we recommend the Devkit version.
Once the installer has downloaded, run it and you'll get a standard Windows installer. You'll have options to "Add Ruby executables to your PATH" and "Associate .rb and .rbw files with this Ruby installation," both of which we recommend. You'll then have the option to install "Ruby RI and HTML documentation" and the "MSYS2 development toolchain," which again, we recommend. At the end, you'll be asked to run "ridk install" to set up the development toolchain. Doing so will give you a pop-up window that will ask you which MSYS2 components to install and to confirm the defaults are what you want (which they are, so keep them). Press ENTER to start the MSYS2 installation. After the installation finishes that phase, it'll prompt you again. If the brackets in the prompt are empty, pressing ENTER will finish the installation.
Using Ruby with RubyInstaller At this point, from a regular Windows terminal, you can run ruby and irb with the same options as we'll discuss in Chapter 14, Ruby from the Command Line, on page 231, and Chapter 16, Interactive Ruby, on page 277.
You'll find two versions of the Ruby interpreter in the RubyInstaller distribution. The ruby version is meant to be used at a command prompt (DOS shell or PowerShell), as in the Unix version. For applications that read and write to the standard input and output, this is fine. This means that any time you run ruby, you'll get a DOS shell even if you don't want one--Windows will create a new command prompt window and display it while Ruby is running.
This may not be appropriate behavior if, for example, you double-click a Ruby script that uses a graphical interface or if you're running a Ruby script as a background task or from inside another program. In these cases, you'll want to use rubyw. This is the same as ruby except that it doesn't provide standard in, standard out, or standard error and doesn't launch a DOS shell when run.
On Windows 11, you can also run Ruby code by right-clicking Ruby files in File Explorer.
Running Ruby
Now that Ruby is installed, you'd probably like to run some programs. Unlike compiled languages, you have two ways to run Ruby: you can type in code interactively, or you can create program files and run them. Typing in code interactively is a great way to experiment with the language, but for code that's more complex or code that you'll want to run more than once, you'll need to create program files and run them. But, before we go any further, let's test to see whether Ruby is installed. Bring up a fresh command prompt, and type this:
$ ruby --version ruby 3.3.0dev (2023-11-01T17:47:26Z master 909afcb4fc) [arm64-darwin23]
Technically, you can run Ruby interactively by typing ruby at the shell prompt. You'll get a blank line in response, and you can type your Ruby code there.
$ ruby puts "Hello, world!" ^D Hello, world!
report erratum � discuss

Chapter 1. Getting Started � 12
In this example, we typed in a single line of Ruby. That line consists of two parts. The first part, puts, is the name of a method. A method is a pre-defined chunk of code. In this case, the puts method is one of several methods defined for us by Ruby. The second part, "Hello, world!", is text surrounded by double quotes, which is called a string. Combining the two, the Ruby code puts "Hello, world!" calls the method puts with the argument "Hello, world!". The puts method then outputs that argument back to the terminal--puts is short for "outPUT String".
On the next line, we typed an end-of-file character (Ctrl+D on our system), which exited the program and caused what we typed to be evaluated. Using Ruby like this works, but it only shows responses if you explicitly print them out. Also, it's painful if you make a typo, and you can't see what's going on as you type.
Happily, there's a better way to interact with Ruby.
Interactive Ruby, or irb, is the tool of choice for executing Ruby interactively. Irb is a complete Ruby shell, with command-line history, line-editing capabilities, and job control. (In fact, it has its own chapter in this book: Chapter 16, Interactive Ruby, on page 277.) You run irb from the command line. Once it starts, type in Ruby code. It will show you the value of each expression as it evaluates it. Exit an irb session by typing exit or Ctrl+D.
Here's a sample session:
$ irb irb(main):001:1* def sum(n1, n2) irb(main):002:1* n1 + n2 irb(main):003:0> end => :sum irb(main):004:0> sum(3, 4) => 7 irb(main):005:0> sum("cat", "dog") => "catdog" irb(main):006:0> exit
In the first three lines of this session, we're defining a method called sum. The act of defining that method returns a value called :sum, which is a Ruby symbol matching the name of the method. We'll talk more about symbols and method names later. In line 4 of the input, we're calling the method, first with arguments 3 and 4, returning 7, then in line 5 with arguments "cat" and "dog". In Ruby, adding strings concatenates them, so the line returns the string "catdog". Then we exit on line 6.
If you try this in Ruby 3.1 or higher, you'll notice that irb attempts to offer autocompletion of variable names or commands, and also color codes, neither of which is easy to show in a book.
We recommend that you get familiar with irb--it's a great way to explore Ruby concepts and debug your code, and it'll make your experience with Ruby more fun.
Creating Ruby Programs
The most common way to write Ruby programs is to put the Ruby code in one or more text files. You'll use a text editor or an Integrated Development Environment (IDE) to create and maintain these files--many popular editors, including Visual Studio Code, vim, Sublime Text, and RubyMine, feature Ruby support. You'll then run the files either from within the
report erratum � discuss

Creating Ruby Programs � 13
What about Docker?
If you're using Ruby on a larger project or with a larger team, there's a good chance that Docker is part of your development environment. Docker is a tool that allows you to define and run containers. A container is a way to package all the dependencies needed to run code--it's a virtual operating system inside your computer. Using Docker, you can simulate a Linux environment no matter what operating system you're running. A full description of Docker is out of this book's scope. But, if you're already familiar with Docker in general, it's worth mentioning that Docker maintains images with different Ruby versions pre-installed. You can always get to the latest released version with ruby:latest, and you can go straight to a Dockerized irb prompt with docker run -it ruby irb. Running external Ruby files in the Docker container is doable as well but requires a little more Docker knowledge.
editor or from the command line. Both techniques are useful. You might run single-file programs from within the editor and more complex programs from the command line. Let's create a short Ruby program and run it. Open a terminal window and create an empty directory somewhere, perhaps you could call it pickaxe. Then, using your editor of choice, create the file myprog.rb, containing the following text:
pickaxe/myprog.rb puts "Hello, Ruby Programmer" puts "It is now #{Time.now}"
Note that the second string contains the text Time.now between curly braces, not parentheses. You can run a Ruby program from a file as you would any other shell script or program in another scripting language like Python. Run the Ruby interpreter, giving it the script name as an argument:
$ ruby myprog.rb Hello, Ruby Programmer It is now 2023-11-02 17:15:44 -0500
On Unix systems, you can use the "shebang" notation as the first line of the program file. If your system supports it, you can avoid hard-coding the path to Ruby in the "shebang" line by using #!/usr/bin/env ruby, which will search your path for ruby and then execute it.
#!/usr/bin/env ruby puts "Hello, Ruby Programmer" puts "It is now #{Time.now}"
If you make this source file executable (using, for instance, chmod +x myprog.rb), Unix lets you run the file as a program:
$ ./myprog.rb Hello, Ruby Programmer It is now 2023-11-02 17:15:44 -0500
You can do something similar under Microsoft Windows using file associations, and you can run Ruby GUI applications by double-clicking their names in Windows Explorer.
report erratum � discuss

Chapter 1. Getting Started � 14
Getting More Information about Ruby
As the volume of the Ruby libraries has grown, it has become impossible to document them all in one book; the standard library that comes with Ruby now contains more than 9,000 methods. The official Ruby documentation is at https://docs.ruby-lang.org, with official pages for the different versions of the core and standard library located there. irb will also give you documentation of standard method names as you type. Much of this documentation is generated from comments in the source code using a tool called RubyDoc, which we'll look at in Chapter 19, Documenting Ruby, on page 313. The RubyDoc site at https://www.rubydoc.info contains documentation for Ruby projects that use RubyDoc. Third-party libraries in the Ruby world are called gems, and the official listing of Ruby gems is at https://rubygems.org. We'll talk lots more about gems in Chapter 15, Ruby Gems, on page 251. There is also a command-line tool for the Ruby core documentation called ri. To find the documentation for a class, type ri <classname>. For example, the following is the beginning of the summary information for the String class. If you type ri with no arguments, you get a prompt asking you for a class.
= String < Object -----------------------------------------------------------------------= Includes: Comparable (from ruby core) (from ruby core) -----------------------------------------------------------------------A String object has an arbitrary sequence of bytes, typically representing text or binary data. A String object may be created using String::new or as literals. String objects differ from Symbol objects in that Symbol objects are designed to be used as identifiers, instead of text or data.
It goes on to list all the methods of String. You can also try a method name:
$ ri strip = .strip (from ruby core) === Implementation from String ------------------------------------------------------------------------
str.strip -> new_str -----------------------------------------------------------------------Returns a copy of the receiver with leading and trailing whitespace removed.
report erratum � discuss

What's Next � 15

Whitespace is defined as any of the following characters: null, horizontal tab, line feed, vertical tab, form feed, carriage return, space.

" hello ".strip #=> "hello"

"\tgoodbye\r\n".strip #=> "goodbye"

"\x00\t\n\v\f\r ".strip #=> ""

"hello".strip

#=> "hello"

You can then exit the listing by typing q.

What's Next

Now that you're up and running, it's time to learn how Ruby works. First, we'll do a quick overview of the main features of the language.

report erratum � discuss

CHAPTER 2
Ruby.new
Many books on programming languages look about the same. They start with chapters on basic types: integers, strings, and so on. Then they look at expressions like 2 + 3 before moving on to if and while statements and loops. Then, perhaps around Chapter 7 or 8, they'll start mentioning classes. We find that somewhat tedious.
Instead, when we designed this book, we had a grand plan. We wanted to document the language from the top down, starting with classes and objects and ending with the nittygritty syntax details. It seemed like a good idea at the time. After all, most everything in Ruby is an object, so it made sense to talk about objects first.
Or so we thought.
Unfortunately, it turns out to be difficult to describe a language top-down. If you haven't covered strings, if statements, assignments, and other details, it's difficult to write examples of classes. Throughout our top-down description, we kept coming across low-level details we needed to cover so that the example code would make sense.
So we came up with another grand plan (they don't call us pragmatic for nothing). We'd still describe Ruby starting at the top. But before we did that, we'd add a short chapter that described all the common language features used in the examples along with the special vocabulary used in Ruby--a mini-tutorial to bootstrap us into the rest of the book. And that mini-tutorial is this chapter.
Ruby Is an Object-Oriented Language
Let's say it again. Ruby is an object-oriented language. In programming terms, an object is a thing that combines data with the logic that manipulates that data, and a language is "objectoriented" if it provides language constructs that make it easy to create objects. Typically, object-oriented languages allow their objects to define what their data is, define their functionality, and provide a common syntax to allow other objects to access that functionality.
Many languages claim to be object-oriented, and those languages often have a different interpretation of what object-oriented means and a different terminology for the concepts they employ. Unlike other object-oriented languages such as Java, JavaScript, and Python, all Ruby types are objects, and there are no non-object basic types that behave differently.
Before we get too far into the details, let's briefly look at the terms and notations that we'll be using to talk about Ruby.
report erratum � discuss

Chapter 2. Ruby.new � 18

When you write object-oriented programs, you're looking to model concepts from the outside world or from your logical domain. During this modeling process, you'll discover categories of related data and behavior that need to be represented in code. In a system representing a jukebox, the concept of a "song" could be such a category. A song might combine state (for example, the name of the song) and methods that use that state (perhaps a method to play the song). In Ruby, you'd define a class called Song to represent the general case of what songs do.
Once you have these classes, you'll typically want to create a number of separate instances of each. For the jukebox system containing a class called Song, you'd have separate instances for popular hits with different names such as "Ruby Tuesday," "Enveloped in Python," "String of Pearls," "Small Talk," and so on. Each of these instances has its own state but shares the common behavior of the class. The word object is often used interchangeably with instance.
In Ruby, instances are created by calling a constructor, which is a special method associated with a class. The standard constructor is called new. As we'll see later in Chapter 3, Classes, Objects, and Variables, on page 33, the new method is defined for you by Ruby, and you don't need to define it on your own. You might create instances like this:

song1 = Song.new("Ruby Tuesday") song2 = Song.new("Enveloped in Python") # and so on

These instances are both derived from the same class, but they each have unique characteristics. Every object has a unique object identifier (abbreviated as object id), accessible via the property object_id. In this example, if you were to check song1.object_id and song2.object_id, you'd find they have different values.

For each instance, you can define instance variables, variables with values that are unique to that instance. These instance variables hold an object's state. Each of our songs, for example, will have an instance variable that holds that song's title.

Within each class, you can define instance methods. Each method is a chunk of functionality that may be called in the context of the class and usually from outside the class, although you can set constraints on what methods can be used externally. These instance methods have access to the object's instance variables and hence to the object's state. A Song class, for example, might define an instance method called play. If a variable referenced a particular Song instance, you'd be able to call that instance's play method and play that song.

Syntactically, a method is invoked using dot syntax, here are some examples:

intro/puts_examples.rb "gin joint".length "Rick".index("c") 42.even? sam.play(song)

# => 9 # => 2 # => true # => "duh dum, da dum de dum ..."

Each line shows a method being called. The item before the dot is called the receiver of the method, and what comes after the period is the name of the method to be invoked. The first example asks the string "gin joint" for its length. The second asks a different string to find the index within it of the letter c. The third line asks the number 42 if it's even (the question mark is part of the method name even?). Finally, we ask an object called sam to play us a song

report erratum � discuss

Some Basic Ruby � 19

(assuming there's an existing variable called sam that references an appropriate object which we've defined elsewhere).

When we talk about methods being sent, we often say that we send a message to the object. The message contains the method's name along with any arguments the method may expect. The object responds to the message by invoking the method with that name. This idea of expressing method calls in the form of messages to objects comes from the programming language Smalltalk. When an object receives a message, it looks into its own class for a corresponding method. If found, that method is executed. If the method isn't found, Ruby goes off to look for it--we'll get to that in Method Lookup, on page 113.

It's worth noting here a major difference between Ruby and other object-oriented languages. In Java, for example, you'd find the absolute value of some number by calling a separate function and passing in that number. You could write this:

num = Math.abs(num);

// Java code

In Ruby, the ability to determine an absolute value is built into the numbers class which takes care of the details internally. You send the message abs to a number object and let it do the work:

num = -1234

# => -1234

positive = num.abs # => 1234

The same applies to all Ruby objects. In Python, you'd write len(name), but in Ruby, it would be name.length, and so on. This consistency of behavior is what we mean when we say that Ruby is a pure object-oriented language with no basic types.

Some Basic Ruby

Not everybody likes to read heaps of boring syntax rules when they're picking up a new language, so we're going to cheat. In this section, we'll hit the highlights--the stuff you'll need to know if you're going to write Ruby programs. Later, in Part IV, Ruby Language Reference, on page 427, we'll go into all the gory details.

Let's start with a short Ruby program. We'll write a method that returns a personalized greeting. We'll then invoke that method a couple of times:

intro/hello1.rb def say_hello_goodbye(name)
result = "I don't know why you say goodbye, " + name + ", I say hello" return result end
# call the method puts say_hello_goodbye("John") puts say_hello_goodbye("Paul")
produces:
I don't know why you say goodbye, John, I say hello I don't know why you say goodbye, Paul, I say hello

As the example shows, Ruby syntax is uncluttered. You don't need semicolons at the ends of statements as long as you put each statement on a separate line. Ruby comments start with a # character and run to the end of the line. Code layout is up to you; indentation isn't

report erratum � discuss

Chapter 2. Ruby.new � 20
significant. That said, two-character indentation--spaces, not tabs--is the overwhelming choice of the Ruby community.
Methods are defined with the keyword def, followed by the method name--in this case, the name is say_hello_goodbye--and then the method's parameters between parentheses. (In fact, the parentheses are optional, but we recommend you use them.) Ruby doesn't use braces to delimit the bodies of compound statements and definitions. Instead, you finish the body with the keyword end. Our method's body is pretty short. The first line concatenates the literal string "I don't know why you say goodbye, " and the parameter name and the literal string ", I say hello" and assigns the result to the local variable result. The next line returns that result to the caller. Note that we didn't have to declare the variable result; it sprang into existence when we assigned a value to it.
Having defined the method, we invoke it twice. In both cases, we pass the result to the method puts, which simply outputs its argument followed by a newline (moving on to the next line of output):
I don't know why you say goodbye, John, I say hello I don't know why you say goodbye, Paul, I say hello
The line puts say_hello_goodbye("John") actually contains two method calls: one to the method say_hello_goodbye with the argument "John" and the other to the method puts whose argument is the result of the call to say_hello_goodbye . Why does one call have its arguments in parentheses while the other doesn't? In this case, it's purely a matter of taste--the puts method is available to all objects and is often written without parentheses around its argument. Ruby doesn't require parentheses unless they are directly needed for the interpreter to parse the statement the way you want. The following lines are equivalent:
puts say_hello_goodbye("John") puts(say_hello_goodbye("John"))
Life isn't always simple, and precedence rules can make it difficult to know which argument goes with which method invocation. So, we recommend using parentheses in all but the simplest cases. You'll see that Ruby programs often omit the parentheses when the method doesn't have an explicit receiver and only has one argument.
This example also shows Ruby string objects. Ruby has many ways to create a string object, but the most common is to use string literals, which are sequences of characters between single or double quotation marks. The two forms differ in the amount of processing Ruby does on the string while constructing the literal. In the single-quoted case, Ruby does very little. With a few exceptions, what you enter in the string literal becomes the string's value.
In the double-quoted case, Ruby does more work. First, it looks for substitution sequences that start with a backslash character and replaces them with some binary value. The most common of these substitutions is \n, which is replaced with a newline character. When a string containing a newline is output, that newline becomes a line break:
puts "Hello and goodbye to you,\nGeorge"
produces: Hello and goodbye to you, George
report erratum � discuss

Some Basic Ruby � 21

The second thing that Ruby does with double-quoted strings is expression interpolation. Within the string, the sequence #{EXPRESSION} is replaced by the value of EXPRESSION. We could use this to rewrite our previous method:

def say_hello_goodbye(name) result = "I don't know why you say goodbye, #{name}, I say hello" return result
end puts say_hello_goodbye("Ringo")
produces:
I don't know why you say goodbye, Ringo, I say hello

When Ruby constructs this string object, it looks at the current value of name and substitutes it into the string. Arbitrarily complex expressions are allowed in the #{...} construct. In the following example, we invoke the capitalize method, defined for all strings, to output our parameter with a leading uppercase letter:

def say_hello_goodbye(name) result = "I don't know why you say goodbye, return result
end puts say_hello_goodbye("john")

#{name.capitalize}, I say hello"

produces: I don't know why you say goodbye, John, I say hello

For more information on strings and the other Ruby standard types, see Chapter 7, Basic Types: Numbers, Strings, and Ranges, on page 117.

We could simplify our say_hello_goodbye method some more. In the absence of an explicit return statement, the value returned by a Ruby method is the value of the last expression evaluated, so we can get rid of the temporary variable and the return statement altogether.

def say_hello_goodbye(name) "I don't know why you say goodbye, #{name}, I say hello"
end puts say_hello_goodbye("Paul")
produces: I don't know why you say goodbye, Paul, I say hello

This version is considered more idiomatic, by which we mean that it's more in line with how expert Ruby programmers have chosen to write Ruby programs. Idiomatic Ruby tends to lean into Ruby's shortcuts and specific syntax. A good clearinghouse for the guidelines for idiomatic Ruby style can be found in the documentation for the Standard gem at https://github.com/testdouble/standard, which has been used for the code in this book (except where we deliberately break its rules to make a point).
We promised that this section would be brief. We have one more topic to cover: Ruby names. For brevity, we'll be using some terms (such as class variable) that we aren't going to define here. But, by talking about the rules now, you'll be ahead of the game when we actually come to discuss class variables and the like later.
Ruby uses a convention that may seem strange at first: the first characters of a name indicate how broadly the variable is visible. Local variables, method parameters, and method names

report erratum � discuss

Chapter 2. Ruby.new � 22
should all start with a lowercase letter or an underscore (Ruby itself has a couple of methods that start with a capital letter, but in general this isn't something to do in your own code).
Global variables are prefixed with a dollar sign, $, and instance variables begin with an "at" sign, @. Class variables start with two "at" signs, @@. Although we talk about global and class variables here for completeness, you'll find they are rarely used in Ruby programs. There's a lot of evidence that global variables make programs harder to maintain. Class variables aren't as dangerous as global variables, but they are still tricky to use safely--people tend not to use them much because they often use easier ways to get similar functionality. Finally, class names, module names, and other constants must start with an uppercase letter. Samples of different names are given in Table 1, Example variable, class, and constant names, on page 23.
Following this initial character, a name can contain any combination of letters, digits, and underscores, with the exception that the character following an @ sign may not be a digit. But, by convention, multiword instance variables are written with underscores between the words, like first_name or zip_code, and multiword class names are written in MixedCase (sometimes called CamelCase) with each word capitalized, like FirstName or ZipCode. Constant names are written in all caps, with words separated by underscores, like FIRST_NAME or ZIP_CODE. Method names may end with the characters ?, !, and =.
Arrays and Hashes
Ruby provides a few different ways to combine objects into collections. Most of the time, you'll use two of them: Arrays and Hashes. An Array is a linear list of objects, you retrieve them via their index, which is the number of their place in the array, starting at zero for the first slot. A Hash is an association, meaning it's a key/value store where each value has an arbitrary key, and you retrieve the value via that key. Both arrays and hashes grow as needed to hold new elements. Any particular array or hash can hold objects of differing types; you can have an array containing an integer, then a string, then a floating-point number, as we'll see in a minute.
You can create and initialize a new array object using an array literal--a set of elements between square brackets. Given an array object, you can access individual elements by supplying an index between square brackets, as the next example shows. Note that Ruby array indices start at zero.
a = [1, 'cat', 3.14] # array with three elements puts "The first element is #{a[0]}"
# set the third element a[2] = nil puts "The array is now #{a.inspect}"
produces: The first element is 1 The array is now [1, "cat", nil]
You may have noticed that we used the special value nil in this example. In many languages, the concept of nil (or null) means "no object." In Ruby, that's not the case; nil is an object, just like any other. It's an object that represents the concept of nothing. Anyway, let's get back to arrays and hashes.
report erratum � discuss

Arrays and Hashes � 23

Local Variable: Instance Variable: Class Variable: Global Variable: Class Name: Constant Name:

name fish_and_chips x_axis thx1138 _x _26 @name @point_1 @X @_ @plan9 @@total @@symtab @@N @@x_pos @@SINGLE $debug $CUSTOMER $_ $plan9 $Global String ActiveRecord MyClass FEET_PER_MILE DEBUG

Table 1--Example variable, class, and constant names

Ruby hash syntax is similar to array syntax. A hash literal uses braces rather than square brackets. The literal must supply two objects for every entry: one for the key and the other for the value. Most generically, the key and value are separated by =>, but we'll see that a shortcut syntax is commonly used.

For example, you could use a hash to map musical instruments to their orchestral sections.

instrument_section = { "cello" => "string", "clarinet" => "woodwind", "drum" => "percussion", "oboe" => "woodwind", "trumpet" => "brass", "violin" => "string"
}

The thing to the left of the => is the key, and the thing to the right is the corresponding value. Keys in a particular hash must be unique; you can't have two entries for "drum." The keys and values in a hash can be arbitrary objects. You can have hashes where the values are arrays, other hashes, and so on. The order of the keys in the hash is stable and will always match the order in which the keys were added to the hash. If you assign a new value to a key, the old value is erased.

Hashes are indexed using the same square bracket notation as arrays.

instrument_section["oboe"] instrument_section["cello"] instrument_section["bassoon"]

# => "woodwind" # => "string" # => nil

The default behavior of a hash when indexed by a key it doesn't contain is to return nil, representing the absence of a value.
Sometimes you'll want to change this default behavior. For example, if you're using a hash to count the number of times each different word occurs in a file, it's convenient to have the default value be zero. Then you can use the word as the key and increment the corresponding hash value without worrying about whether you've seen that word before. This can be done by specifying a default value when you create a new, empty hash:

histogram = Hash.new(0) # The default value is zero histogram["ruby"] # => 0 histogram["ruby"] = histogram["ruby"] + 1 histogram["ruby"] # => 1

report erratum � discuss

Chapter 2. Ruby.new � 24
Symbols
Often, when programming, you need to use the same string over and over. Perhaps the string is a key in a Hash, or maybe the string is the name of a method. In that case, you'd probably want the access to that string to be immutable so its value can't change, and you'd also want accessing the string to be as fast and use as little memory as possible.
This brings us to Ruby's symbols. Symbols aren't exactly optimized strings, but for most purposes, you can think of them as special strings that are immutable, are only created once, and are fast to look up. Symbols are meant to be used as keys and identifiers, while strings are meant to be used for data.
A symbol literal starts with a colon and is followed by some kind of name:
walk(:north) look(:east)
In this example, we're using the symbols :north and :east to represent constant values in the code. We don't need to declare the symbols or assign them a value--Ruby takes care of that for you. The value of a symbol is equivalent to its name.
Ruby also guarantees that no matter where they appear in your program, symbols with the same name will have the same value--indeed, they'll be the same internal object. As a result, you can safely write the following:
def walk(direction) if direction == :north # ... end
end
Because their values don't change, symbols are frequently used as keys in hashes. We could write our previous hash example using symbols as keys:
intro/hash_with_symbol_keys.rb instrument_section = {
:cello => "string", :clarinet => "woodwind", :drum => "percussion", :oboe => "woodwind", :trumpet => "brass", :violin => "string" } instrument_section[:oboe] # => "woodwind" instrument_section[:cello] # => "string" # Note that strings aren"t the same as symbols... instrument_section["cello"] # => nil
Note from the last line that a symbol key is different from a string key, and access via one won't result in a value associated with the other.
Symbols are so frequently used as hash keys that Ruby has a shortcut syntax. You can use name: value pairs to create a hash instead of name => value if the key is a symbol:
report erratum � discuss

Control Structures � 25
intro/hash_with_symbol_keys_19.rb instrument_section = {
cello: "string", clarinet: "woodwind", drum: "percussion", oboe: "woodwind", trumpet: "brass", violin: "string" } puts "An oboe is a #{instrument_section[:oboe]} instrument"
produces: An oboe is a woodwind instrument
This syntax was added, in part, for programmers familiar with JavaScript and Python, both of which use a colon as a separator in key/value pairs.
Control Structures
Ruby has all the usual control structures, such as if statements and while loops. Java or JavaScript programmers may be surprised by the lack of braces around the bodies of these statements. Instead, Ruby uses the keyword end to signify the end of a body of a control structure:
intro/weekdays.rb today = Time.now
if today.saturday? puts "Do chores around the house"
elsif today.sunday? puts "Relax"
else puts "Go to work"
end
produces: Go to work
One thing you might find unusual is that in the second clause Ruby uses the keyword elsif--one word, missing an "e"--to indicate "else if". Breaking that keyword up into else if would be a syntax error.
Similarly, while statements are terminated with end and loop as long as the condition on the line with the while is true:
num_pallets = 0 weight = 0 while weight < 100 && num_pallets <= 5
pallet = next_pallet() weight += pallet.weight num_pallets += 1 end
Most lines that look like statements in Ruby are actually expressions that return a value, which means you can use those expressions as conditions. For example, the Kernel method gets returns the next line from the standard input stream or nil when the end of the file is
report erratum � discuss

Chapter 2. Ruby.new � 26
reached. Because Ruby treats nil as a false value in conditions, you could write the following to process the lines in a file:
while (line = gets) puts line.downcase
end
The assignment statement sets the variable line to the result of calling gets, which will either be the next line of text or nil. Then the while statement tests the value returned by the assignment statement, which is the value assigned. When the value is nil, that means the output has no further lines and the while loop terminates.
Ruby statement modifiers are a useful shortcut if the body of an if or while statement is a single expression. Write the expression, followed by if or while and the condition. For example, here's a single-line if statement:
if radiation > 3000 puts "Danger, Will Robinson"
end
Here it is again, rewritten using a statement modifier:
puts "Danger, Will Robinson" if radiation > 3000
Similarly, this while loop:
square = 4 while square < 1000
square = square * square end
becomes this more concise version:
square = 4 square = square * square while square < 1000
The if version of these modifiers is perhaps most commonly used as a guard clause at the beginning of a method, as in return nil if user.nil?. The while version is much less commonly used.
Regular Expressions
Most of Ruby's built-in types will be familiar to all programmers. A majority of languages have strings, integers, floats, arrays, and so on. But not all languages have built-in support for regular expressions the way that Ruby or JavaScript do. This is a shame because regular expressions, although cryptic, are a powerful tool for working with text. And having them built in rather than tacked on through a library interface, makes a big difference.
Entire books have been written about regular expressions (for example, Mastering Regular Expressions by Jeffrey Friedl), so we won't try to cover everything in this short section. Instead, we'll look at a few examples of regular expressions in action. You'll find more coverage of regular expressions in Chapter 8, Regular Expressions, on page 129.
A regular expression is a way of specifying a pattern of characters to be matched in a string. In Ruby, you typically create a regular expression by writing a pattern between slash
report erratum � discuss

Regular Expressions � 27

characters (/pattern/). And, Ruby being Ruby, regular expressions are objects and can be manipulated as such.
For example, you could write a pattern that matches a string containing the text Ruby or the text Rust using the following regular expression:

/Ruby|Rust/

The forward slashes delimit the pattern, which consists of the two things we're matching, separated by a pipe character (|). In regular expressions, the pipe character means "either the thing on the right or the thing on the left," in this case either Ruby or Rust. You can use parentheses within patterns, just as you can in arithmetic expressions, so this pattern matches the same set of strings:

/Ru(by|st)/

You can also specify repetition within patterns. /ab+c/ matches a string containing an a followed by one or more b_s, followed by a _c. Change the plus to an asterisk, and /ab*c/ creates a regular expression that matches one a, zero or more b_s, and one _c.

You can also match one of a group of characters within a pattern. Some common examples are character classes such as \s, which matches a whitespace character (space, tab, newline, and so on); \d, which matches any digit; and \w, which matches any character that may appear in a typical word. A dot (.) matches (almost) any character. A table of these character classes appears in Table 2, Character class abbreviations, on page 137.
We can put all this together to produce some useful regular expressions:

/\d\d:\d\d:\d\d/

# a time such as 12:34:56

/Ruby.*Rust/

# Ruby, zero or more other chars, then Rust

/Ruby Rust/

# Ruby, exactly one space, and Rust

/Ruby *Rust/

# Ruby, zero or more spaces, and Rust

/Ruby +Rust/

# Ruby, one or more spaces, and Rust

/Ruby\s+Rust/

# Ruby, one or more whitespace characters, then Rust

/Java (Ruby|Rust)/ # Java, a space, and either Ruby or Rust

Once you've created a pattern, it seems a shame not to use it. The match operator =~ can be used to match a string against a regular expression. If the pattern is found in the string, =~ returns its starting position; otherwise, it returns nil. This means you can use regular expressions as conditions in if and while statements. For example, the following code fragment writes a message if a string contains the text Ruby or Rust:

line = gets if line =~ /Ruby|Rust/
puts "Programming language mentioned: #{line}" end

Both strings and regular expressions have a match? method which is synonymous with the =~ operator:

line = gets if line.match?(/Ruby|Rust/)
puts "Scripting language mentioned: #{line}" end

The match? form is probably more common in modern Ruby.

report erratum � discuss

Chapter 2. Ruby.new � 28

The part of a string matched by a regular expression can be replaced with different text using one of Ruby's substitution methods:

line = gets

newline = line.sub(/Python/, 'Ruby')

# replace first 'Python' with 'Ruby'

newerline = line.gsub(/Python/, 'Ruby') # replace every 'Python' with 'Ruby'

You can replace every occurrence of JavaScript and Python with Ruby using this:
line = gets newline = line.gsub(/JavaScript|Python/, 'Ruby')

We'll have a lot more to say about regular expressions as we go through the book.

Blocks

This section briefly describes one of Ruby's particular strengths--blocks. A code block is a chunk of code you can pass to a method, as if the block were another parameter. This is an incredibly powerful feature, allowing Ruby methods to be extremely flexible. One of this book's early reviewers commented at this point: "This is pretty interesting and important, so if you weren't paying attention before, you should probably start now." We still agree.
Syntactically, code blocks are chunks of code that can be delimited one of two ways: between braces or between do and end. This is a code block at the end of a message call:

foo.each { puts "Hello" }

This is also a code block at the end of a message call:

foo.each do club.enroll(person) person.socialize
end

The two kinds of block delimiters have different precedence: the braces bind more tightly than the do/end pairs, a fact that will almost never make a difference in your code. In practice, the standard you'll most often see is braces used for single-line blocks and do/end used for multiline blocks.
You can pass a block as an argument to any method call even if the method doesn't do anything with the block. You do this by starting the block at the end of the method call, after any other parameters. For example, in the following code, the block containing puts "Hi" is associated with the call to the method greet (which we don't show here):

greet { puts "Hi" }

If the method has parameters, they appear before the block, and you can only pass one block per method call. In Blocks and Enumeration, on page 62, we'll see other ways to manage blocks and arbitrary chunks of code.
verbose_greet("Dave", "loyal customer") { puts "Hi" }

A method can then invoke an associated block one or more times using the Ruby yield statement. The yield statement invokes the block that was passed to the method, passing control to the code inside the block.

report erratum � discuss

Blocks � 29
The following example shows a block call in action. We define a method that calls yield twice. We then call this method, putting a block on the same line after the call, and after any arguments to the method. You can think of the association of a block with a method as a kind of argument passing. This works on one level, but it isn't really the whole story. The block is effectively an entire other method that can be invoked or passed forward as an argument to another method. For example:
intro/block_example.rb def call_block
puts "Start of method" yield yield puts "End of method" end
call_block { puts "In the block" }
produces: Start of method In the block In the block End of method
In this example, the code in the block (puts "In the block") is executed twice, once for each call to yield passing control to the block.
You can provide arguments to yield, and they'll be passed to the block. Within the block, you list the names of the parameters to receive these arguments between vertical bars (|params...|). The following example shows a method calling its associated block twice, passing the block two arguments each time:
intro/block_example2.rb def who_says_what
yield("Dave", "hello") yield("Andy", "goodbye") end
who_says_what { |person, phrase| puts "#{person} says #{phrase}" }
produces: Dave says hello Andy says goodbye
You can use code blocks to package code to implement a later callback. Code blocks can be used to pass around chunks of code. They are used throughout the Ruby standard library to allow methods to perform an action on successive elements from a collection such as an array. The act of doing something similar to all objects in a collection is called enumeration in Ruby; other languages call this iteration.
animals = ["ant", "bee", "cat", "dog"] # create an array animals.each { |animal| puts animal } # iterate over the contents
produces: ant bee cat dog
report erratum � discuss

Chapter 2. Ruby.new � 30
Many of the looping constructs that are built into languages such as Java and JavaScript are method calls in Ruby, with the methods invoking an associated block zero or more times:
["cat", "dog", "horse"].each { |name| print name, " " } 5.times { print "*" } 3.upto(6) { |i| print i } ("a".."e").each { |char| print char } ("a".."e").each { print _1 }
produces: cat dog horse *****3456abcdeabcde
In the first line, we ask an array to call the block once for each of its elements. Next, the object 5 calls a block five times, printing * each time. Rather than use for loops, the third example shows that in Ruby we can ask the number 3 to call a block, passing in successive values until it reaches 6. Finally, we use Ruby's literal syntax for ranges of values to have the range of characters from a to e invoke a block using the method each. We show that example twice: once using Ruby's normal block parameter syntax and once using Ruby's shortcut for block parameters, which we'll see in Blocks, on page 65.
Reading and `Riting
Ruby comes with a comprehensive library to manage input and output (I/O). But, in most of the examples in this book, we'll stick to a few simple methods. We've already come across methods that write output: puts writes its arguments with a newline after each; p also writes its arguments but will produce more debuggable output. Both can be used to write to any I/O object, but, by default, they write to the standard output stream.
You can read input into your program in many ways. Probably the most traditional one is to use the method gets--short for "get string"--which returns the next line from your program's standard input stream:
line = gets print line
Because gets returns nil when it reaches the end of input, you can use its return value in a loop condition. Notice that in the following code the condition to the while is an assignment. We store whatever gets returns into the variable line and then test to see whether that returned value was nil or false before continuing:
while (line = gets) print line
end
In Chapter 11, Basic Input and Output, on page 179, we'll talk more about how to read and write from a file or other data source.
Command-Line Arguments
When you run a Ruby program from the command line, you can pass in arguments. These are accessible from your Ruby code in two different ways.
First, the global array ARGV contains each of the arguments passed to the running program. Create a file called cmd_line.rb that contains the following:
report erratum � discuss

Commenting Ruby � 31
puts "You gave #{ARGV.size} arguments" p ARGV
When we run it with arguments, we can see that they get passed in:
$ ruby cmd_line.rb ant bee cat dog You gave 4 arguments ["ant", "bee", "cat", "dog"]
Often, the arguments to a program are the names of files that you want to process. In this case, you can use a second technique: the variable ARGF is a special kind of I/O object that acts like all the contents of all the files whose names are passed on the command line (or standard input if you don't pass any filenames). We'll look at that some more in ARGF, on page 238.
Commenting Ruby
Ruby has two ways of adding comments to source code, one of which you'll use, and the other you'll almost certainly not use. The common one is the # symbol--anything after that symbol until the end of the line is a comment and is ignored by the interpreter. If the next line continues the comment, it needs its own # symbol. Ruby also has a rarely used multiline comment, where the first line starts with =begin and everything is a comment until the code reaches =end. Both the =begin and =end must be at the very beginning of the line, they cannot be indented. While we did just say that Ruby ignores comments, Ruby uses a small number of "magic comments" for configuration options on a per-file basis. These comments have the form of # directive: value and must appear in the file before the first line of the actual Ruby code. The most commonly used magic comment is # frozen_string_literal: true. If this directive is true, then every string literal that doesn't have an interpolation inside it'll automatically be frozen, as though freeze was called on it. You might also see an # encoding: VALUE directive, which specifies the encoding for string and regular expression literals inside that particular file. Ruby also has a # warn_indent: BOOLEAN flag that will throw code warnings if a file's indentation is mismatched. There's an experimental directive called # sharable_constant_value: which affects how values are shared using the Ractor multithreading tools.
What's Next
We finished our lightning-fast tour of some of the basic features of Ruby. We took a look at objects, methods, strings, containers, and regular expressions. We saw some simple control structures and looked at some rather nifty iterators. We hope this chapter has given you enough ammunition to be able to attack the rest of this book. It's time to move on and move up--up to a higher level. Next, we'll be looking at classes and objects, things that are at the same time both the highest-level constructs in Ruby and the essential underpinnings of the entire language.
report erratum � discuss

CHAPTER 3
Classes, Objects, and Variables
From the examples we've shown so far, you may be wondering about our earlier assertion that Ruby is an object-oriented language. Well, here is where we justify that claim. We're going to be looking at how you create classes and objects in Ruby and at some of the ways that Ruby is more flexible than other object-oriented languages. In Ruby Is an Object-Oriented Language, on page 17, we state that everything we manipulate in Ruby is an object. And every object in Ruby was instantiated either directly or indirectly from a class. In this chapter, we'll look in more depth at creating and manipulating those classes.
Defining Classes
Let's give ourselves a simple problem to solve. Suppose we're running a secondhand bookstore. Every week, we do stock control. A gang of clerks uses portable bar-code scanners to record every book on our shelves. Each scanner generates a comma-separated value (CSV) file containing one row for each book scanned. The row contains (among other things) the book's ISBN and price. An extract from one of these files looks something like this:
tut_classes/stock_stats/data.csv "Date","ISBN","Price" "2013-04-12","978-1-9343561-0-4",39.45 "2013-04-13","978-1-9343561-6-6",45.67 "2013-04-14","978-1-9343560-7-4",36.95
Our job is to take all the CSV files and work out how many of each title we have, as well as the total list price of the books in stock. Whenever you're designing an Object-Oriented system, a good first step is to identify the domain concepts you're dealing with. Typically the domain concepts--which could represent a physical object, a process, or some other kind of entity--become classes in your final program, and then individual examples of those concepts are instances of these classes. It seems pretty clear that we'll need something to represent each data reading captured by the scanners. Each instance of this class will represent a particular row of data, and the collection of all of these objects will represent all the data we've captured.
report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 34
Let's call this class BookInStock. (Remember, class names start with an uppercase letter, and method names normally start with a lowercase letter.) Here's how we declare that class in Ruby using the keyword class:
class BookInStock end
As we saw in the previous chapter, we can create new instances of this class using the method `new`:
a_book = BookInStock.new another_book = BookInStock.new
After this code runs, we'd have two distinct objects, both instances of class BookInStock. But there's nothing to distinguish one instance from the other, aside from the fact that they have different internal object IDs. Worse, these objects don't yet hold any of the information we need them to hold.
The best way to fix this is to provide the class with an initialize method. This method lets us set the state of each object as it's constructed. We store this state in instance variables inside the object. (Remember instance variables? They're the ones that start with an @ sign.) Because each object in Ruby has its own distinct set of instance variables, each object can have its own unique state.
Here's our updated class definition:
class BookInStock def initialize(isbn, price) @isbn = isbn @price = Float(price) end
end
The initialize method is special in Ruby programs. When you call BookInStock.new to create a new object, Ruby allocates some memory to hold an uninitialized object and then calls that object's initialize method, passing through all arguments that were passed to new. This gives you a chance to write code that sets up your object's state.
For class BookInStock, the initialize method takes two parameters. These parameters act like local variables within the method, so they follow the local variable naming convention of starting with a lowercase letter. But, as local variables, they'd just evaporate once the initialize method returns, so we need to transfer them into instance variables. This is common behavior in an initialize method--the intent is to have our object set up and usable by the time initialize returns.
This method also illustrates something that often trips up newcomers to Ruby. Notice how we say @isbn = isbn. It's easy to imagine that the two variables here, @isbn and isbn, are somehow related. It looks like they have the same name, but they don't. The former is an instance variable, and the "at" sign is actually part of its name.
Finally, this code illustrates a basic piece of validation. The Float method takes its argument and converts it to a floating-point number, terminating the program with an error if that conversion fails. Later in the book, we'll see other, more resilient, ways to handle these exceptional situations. (We know that we shouldn't be holding prices in inexact old floats.
report erratum � discuss

Defining Classes � 35
Ruby has classes that hold fixed-point values exactly, but we want to look at classes, not arithmetic, in this section.)
What we're doing here is saying that we want to accept any object for the price parameter as long as that parameter can be converted to a float. We can pass in a float, an integer, or even a string containing the representation of a float, and it'll work. Let's try this now. We'll create three objects, each with a different initial state. The p method prints out an internal representation of an object. Using it, we can see that in each case our parameters got transferred into the object's state, ending up as instance variables:
tut_classes/stock_stats/book_in_stock_1.rb class BookInStock
def initialize(isbn, price) @isbn = isbn @price = Float(price)
end end
b1 = BookInStock.new("isbn1", 3) p b1
b2 = BookInStock.new("isbn2", 3.14) p b2
b3 = BookInStock.new("isbn3", "5.67") p b3
produces: #<BookInStock:0x0000000102f99720 @isbn="isbn1", @price=3.0> #<BookInStock:0x0000000102f99180 @isbn="isbn2", @price=3.14> #<BookInStock:0x0000000102f98fa0 @isbn="isbn3", @price=5.67>
Why did we use the p method to write out our objects, rather than puts? Well, let's repeat the code using puts:
tut_classes/stock_stats/book_in_stock_1a.rb class BookInStock
def initialize(isbn, price) @isbn = isbn @price = Float(price)
end end
b1 = BookInStock.new("isbn1", 3) puts b1
b2 = BookInStock.new("isbn2", 3.14) puts b2
b3 = BookInStock.new("isbn3", "5.67") puts b3
produces: #<BookInStock:0x0000000104739628> #<BookInStock:0x0000000104739150> #<BookInStock:0x0000000104738fe8>
Remember, puts writes strings to your program's standard output. When you pass it an object based on a class you wrote, it doesn't know what to do with the object yet, so it uses a simple
report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 36
expedient: it writes the name of the object's class, followed by a colon and the object's unique object identifier, which is a hexadecimal number. It puts the whole lot inside #<...>.
Our experience tells us that during development we'll be printing out the contents of a BookInStock object many times, and the default formatting leaves something to be desired. Fortunately, Ruby has a standard message, to_s, that it sends to any object it wants to render as a string. The default behavior of to_s, defined in the Object class, is the ClassName, then the colon, and then the object ID behavior we just described. So, when we pass one of our BookInStock objects to puts, the puts method calls to_s in that object to get its string representation.
If we want a different behavior, we can override the default implementation of to_s to give us a better rendering of our objects (we'll talk more about how this works in Chapter 6, Sharing Functionality: Inheritance, Modules, and Mixins, on page 101):
tut_classes/stock_stats/book_in_stock_2.rb class BookInStock
def initialize(isbn, price) @isbn = isbn @price = Float(price)
end
def to_s "ISBN: #{@isbn}, price: #{@price}"
end end
b1 = BookInStock.new("isbn1", 3) puts b1 b2 = BookInStock.new("isbn2", 3.14) puts b2 b3 = BookInStock.new("isbn3", "5.67") puts b3
produces: ISBN: isbn1, price: 3.0 ISBN: isbn2, price: 3.14 ISBN: isbn3, price: 5.67
The p method actually has a different method it calls on objects, and that method is named inspect. The difference is that inspect is designed to produce a representation that's useful to a developer when debugging, and to_s is supposed to produce a human-readable one for more general output.
Something's going on here that's both trivial and profound. See how the values we set into the instance variables @isbn and @price in the initialize method are subsequently available in the to_s method? That shows how instance variables work--they're stored with each object and available to all the instance methods of those objects.
Objects and Attributes
The BookInStock objects we've created so far have an internal state (the ISBN and price). That state is private to those objects--no other object can access an object's instance variables. In general, this is a Good Thing. It means that the object is solely responsible for maintaining its own consistency. (We feel obligated to note here that there's no such thing as
report erratum � discuss

Objects and Attributes � 37
perfect privacy in Ruby, and you shouldn't depend on Ruby's language privacy for security purposes.)
A totally secretive object is pretty useless--you can create it, but then you can't do anything with it. You'll normally define methods that let you access and manipulate the state of an object, allowing the outside world to interact with the object. These externally visible facets of an object are called its attributes.
For our BookInStock objects, the first thing we may need is the ability to find out the ISBN and price (so we can count each distinct book and perform price calculations). One way of doing that is to write accessor methods:
tut_classes/stock_stats/book_in_stock_3.rb class BookInStock
def initialize(isbn, price) @isbn = isbn @price = Float(price)
end
def isbn @isbn
end
def price @price
end # .. end
book = BookInStock.new("isbn1", 12.34) puts "ISBN = #{book.isbn}" puts "Price = #{book.price}"
produces: ISBN = isbn1 Price = 12.34
Here we've defined two accessor methods to return the values of the two instance variables. The method isbn, for example, returns the value of the instance variable @isbn because the last (and only) thing executed in the method is the expression that evaluates the @isbn variable. Later, in Method Bodies, on page 86, we'll look at a shorter syntax for declaring one-line methods.
As far as other objects are concerned, there's no difference between calling these attribute accessor methods or calling any other method. This is great because it means that the internal implementation of the object can change without the other objects needing to be aware of the change.
Because writing accessor methods is such a common idiom, Ruby provides convenient shortcuts.
The method attr_reader creates these attribute reader methods for you:
tut_classes/stock_stats/book_in_stock_4.rb class BookInStock
attr_reader :isbn, :price
def initialize(isbn, price)
report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 38
@isbn = isbn @price = Float(price) end
# .. end
book = BookInStock.new("isbn1", 12.34) puts "ISBN = #{book.isbn}" puts "Price = #{book.price}"
produces: ISBN = isbn1 Price = 12.34
This is the first time we've used symbols in this chapter. As we discussed in Symbols, on page 24, symbols are a convenient way of referencing a name. In this code, you can think of :isbn as meaning the name isbn and of plain isbn as meaning the value of the variable. In this example, we named the accessor methods isbn and price. The corresponding instance variables are @isbn and @price. These accessor methods are identical to the ones we wrote by hand earlier--they'll return the value of the instance variable whose name matches the name of the accessor method. These methods only allow you to read the attribute, but not to change it.
There's a common misconception that the attr_reader declaration actually declares instance variables. It doesn't. It creates the accessor methods, but the variables themselves don't need to be declared. An instance variable pops into existence when you assign a value to it, and any instance value that hasn't been assigned a value returns nil when accessed. Ruby completely decouples instance variables and accessor methods, as we'll see in Attributes Are Just Methods without Arguments, on page 40.
Writing to Attributes
Sometimes you need to be able to set an attribute from outside the object. For example, let's assume that we have to discount the price of some titles after reading in the raw scan data.
In other languages like C# and Java that restrict access to instance variables, you'd do this with setter functions:
// Java code class JavaBookInStock {
private double _price; public double getPrice() {
return _price; } public void setPrice(double newPrice) {
_price = newPrice; } } b = new JavaBookInStock(....); b.setPrice(calculate_discount(b.getPrice()));
In Ruby, the attributes of an object can be accessed via the getter method, and that access looks the same as any other method. We saw this earlier with phrases such as book.isbn. So, it seems natural that setting an attribute's value looks like a normal variable assignment
report erratum � discuss

Objects and Attributes � 39

such as book.isbn = "new isbn". You enable that assignment by creating a Ruby method whose name ends with an equals sign. A method so named can be used as the target of assignments:

tut_classes/stock_stats/book_in_stock_5.rb class BookInStock
attr_reader :isbn, :price

def initialize(isbn, price) @isbn = isbn @price = Float(price)
end

def price=(new_price) @price = new_price
end

# ... end

book = BookInStock.new("isbn1", 33.80)

puts "ISBN

= #{book.isbn}"

puts "Price

= #{book.price}"

book.price = book.price * 0.75

# discount price

puts "New price = #{book.price}"

produces:

ISBN

= isbn1

Price

= 33.8

New price = 25.349999999999998

The assignment book.price = book.price * 0.75 invokes the method price= in the book object, passing it the discounted price as an argument. If you create a method whose name ends with an equals sign, that name can appear on the left side of an assignment. (The Ruby parser will ignore whitespace between the end of the name and the equals sign, which is how book.price = gets parsed to the method named price=.) You can even treat the setter method like a regular method invocation if you want--book.price = 1.50 is identical to the somewhat odder-looking book.price=(1.50).
Again, Ruby provides a shortcut for creating these simple attribute-setting methods. If you want a write-only accessor, you can use the form attr_writer, but that's fairly rare. You're far more likely to want both a reader and a writer for a given attribute, so you'll use the handydandy attr_accessor method:

tut_classes/stock_stats/book_in_stock_6.rb class BookInStock
attr_reader :isbn attr_accessor :price

def initialize(isbn, price) @isbn = isbn @price = Float(price)
end # ... end

book = BookInStock.new("isbn1", 33.80)

puts "ISBN

= #{book.isbn}"

puts "Price

= #{book.price}"

report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 40

book.price = book.price * 0.75 puts "New price = #{book.price}"

produces:

ISBN

= isbn1

Price

= 33.8

New price = 25.349999999999998

# discount price

In this example, the line attr_accessor :price creates both the getter method that allows you to write puts book.price and the setter method that allows you to write book.price = book.price * 0.75

Attributes Are Just Methods without Arguments
These attribute-accessing methods don't have to be just mere wrappers around an object's instance variables. For example, you may want to access the price as an exact number of cents rather than as a floating-point number of dollars.

tut_classes/stock_stats/book_in_stock_7.rb class BookInStock
attr_reader :isbn attr_accessor :price

def initialize(isbn, price) @isbn = isbn @price = Float(price)
end

def price_in_cents (price * 100).round
end # ... end

book = BookInStock.new("isbn1", 33.80)

puts "Price

= #{book.price}"

puts "Price in cents = #{book.price_in_cents}"

produces:

Price

= 33.8

Price in cents = 3380

We multiply the floating-point price by 100 to get the price in cents and then use the round method to convert it to an integer. Why? Because floating-point numbers don't always have an exact internal representation. When we multiply 33.8 by 100, we get 3379.99999999999954525265. The Integer method would truncate this to 3379. Calling round ensures we get the best integer representation. This is a good example of why you want to use BigDecimal, not Float, in financial calculations. See Chapter 26, Library Reference: Core Data Types, on page 495, for more on BigDecimal.

We can take this even further and create a writing method parallel to the reader method, mapping the value to the instance variable internally:

tut_classes/stock_stats/book_in_stock_8.rb class BookInStock
attr_reader :isbn attr_accessor :price

report erratum � discuss

Objects and Attributes � 41

def initialize(isbn, price) @isbn = isbn @price = Float(price)
end

def price_in_cents (price * 100).round
end

def price_in_cents=(cents) @price = cents / 100.0
end # ... end

book = BookInStock.new("isbn1", 33.80)

puts "Price

= #{book.price}"

puts "Price in cents = #{book.price_in_cents}"

book.price_in_cents = 1234

puts "Price

= #{book.price}"

puts "Price in cents = #{book.price_in_cents}"

produces:

Price

= 33.8

Price in cents = 3380

Price

= 12.34

Price in cents = 1234

Here we've used attribute methods to create a virtual instance variable. To the outside world, price_in_cents seems to be an attribute like any other. Internally, though, it has no corresponding instance variable.
This is more than a curiosity. In his landmark book, Object-Oriented Software Construction, Bertrand Meyer calls this the Uniform Access Principle. By hiding the difference between instance variables and calculated values, you're shielding the rest of the world from the implementation of your class. You're free to change how things work in the future without impacting the millions of lines of code that use your class--for example, you could switch from a float to a BigDecimal and the users of this class would never need to know. This is a big win.

Attributes, Instance Variables, and Methods
The previous section's description of attributes may leave you thinking that they're nothing more than methods--why'd we need to invent a fancy name for them? In a way, that's absolutely right. An attribute is just a method. Sometimes an attribute simply returns the value of an instance variable. Sometimes an attribute returns the result of a calculation. And sometimes those funky methods with equals signs at the end of their names are used to update the state of an object. So, the question is, where do attributes stop and regular methods begin? What makes something an attribute and not just a plain old method? Ultimately, that's one of those "how many angels can fit on the head of a pin" questions. Here's a personal take.
When you design a class, you decide what internal state it has and also how that state is to appear on the outside to users of your class. The internal state is held in instance variables. The external state is exposed through methods we're calling attributes. And the other actions

report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 42

your class can perform are just regular methods. It isn't a crucially important distinction, but by calling the external state of an object its attributes, you're helping clue people in on how they should view the class you've written.

Classes Working with Other Classes

Our original challenge was to read in data from multiple CSV files and produce various simple reports. So far, all we have is BookInStock, a class that represents the data for one book.
During object-oriented design, you identify external things and make them classes in your code. But there's another source of classes in your designs--the classes that correspond to things inside your code itself. For example, we know that the program we're writing will need to consolidate and summarize CSV data feeds. But that's a passive statement. Let's turn it into a design by asking ourselves what does the summarizing and consolidating. And the answer (in our case) is a CSV reader. Let's make it into a class as follows:

class CsvReader def initialize # ... end
def read_in_csv_data(csv_file_name) # ...
end
def total_value_in_stock # ...
end
def number_of_each_isbn # ...
end end

We'd call it using something like this:

reader = CsvReader.new

reader.read_in_csv_data("file1.csv")

reader.read_in_csv_data("file2.csv")

:

:

:

puts "Total value in stock = #{reader.total_value_in_stock}"

We need to be able to handle multiple CSV files, so our reader object needs to accumulate the values from each CSV file it is fed. We'll do that by keeping an array of values in an instance variable. And how shall we represent each book's data? Well, we just finished writing the BookInStock class, so that problem is solved. The only other question is how we parse data in a CSV file. Fortunately, Ruby comes with a good CSV library, which we'll cover in detail in Chapter 29, Library Reference: Input, Output, Files, and Formats, on page 587. Given a CSV file with a header line, we can iterate over the remaining rows and extract values by name:

tut_classes/stock_stats/csv_reader.rb class CsvReader
def initialize @books_in_stock = []
end

report erratum � discuss

Classes Working with Other Classes � 43
def read_in_csv_data(csv_file_name) CSV.foreach(csv_file_name, headers: true) do |row| @books_in_stock << BookInStock.new(row["ISBN"], row["Price"]) end
end end
Because you're probably wondering what's going on, let's dissect that read_in_csv_data method. On the first line, we tell the CSV library to open the file with the given name. The headers: true option tells the library to do two things. One is to parse the first line of the file as the names of the columns. The other is to parse each row into a hash with the column names as the keys and the row values as the values.
The library then reads the rest of the file, passing each row in turn to the block (the code between do and end). Inside the block, we extract the data from the ISBN and Price columns and use that data to create a new BookInStock object. We then append that object to an instance variable called @books_in_stock (the << operator does different things in Ruby, in this case, it means "append to an array"). And where does that variable come from? It's an array that we created in the initialize method.
Again, this is the pattern you want to aim for. Your initialize method sets up an environment for your object, leaving it in a usable state. Other methods then use that state.
If you encounter an error along the lines of "`Float': can't convert nil into Float (TypeError)" when you run this code, you likely have extra spaces at the end of the header line in your CSV data file. The CSV library is pretty strict about the formats it accepts.
Let's turn this from a code fragment into a working program. We're going to organize our source into three files. The first, book_in_stock.rb, will contain the definition of the class BookInStock. The second, csv_reader.rb, is the source for the CsvReader class. Finally, a third file, stock_stats.rb, is the main driver program. We'll start with book_in_stock.rb:
tut_classes/stock_stats/book_in_stock.rb class BookInStock
attr_reader :isbn, :price
def initialize(isbn, price) @isbn = isbn @price = Float(price)
end
def price_in_cents (price * 100).round
end end
We're keeping the price_in_cents method so we can do money arithmetic without accumulating floating-point errors.
Here's the csv_reader.rb file. The CsvReader class has two external dependencies, which are the standard CSV library and the BookInStock class that's in the file book_in_stock.rb. Ruby has a couple of helper methods that let us load external files.
tut_classes/stock_stats/csv_reader.rb require "csv" require_relative "book_in_stock"
report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 44
class CsvReader def initialize @books_in_stock = [] end
def read_in_csv_data(csv_file_name) CSV.foreach(csv_file_name, headers: true) do |row| @books_in_stock << BookInStock.new(row["ISBN"], row["Price"]) end
end
def total_value_in_stock # later we'll see easier ways to sum a collection sum = 0.0 @books_in_stock.each { |book| sum += book.price_in_cents } sum / 100.0
end
def number_of_each_isbn # ...
end end
In this file, we use the require method to load in the Ruby CSV library from the Ruby standard library. We also use require_relative to load in the book_in_stock file we wrote. We use require_relative for this because the location of the file we're loading is easiest to define relative to the file we're loading it from--they're both in the same directory.
We're using price_in_cents to compute the total value.
And finally, here's our main program, in the file stock_stats.rb:
tut_classes/stock_stats/stock_stats.rb require_relative "csv_reader"
reader = CsvReader.new
ARGV.each do |csv_file_name| $stderr.puts "Processing #{csv_file_name}" reader.read_in_csv_data(csv_file_name)
end
puts "Total value = #{reader.total_value_in_stock}"
Again, this file uses require_relative to bring in the library it needs (in this case, the csv_reader.rb file). It uses the ARGV variable to access the program's command-line arguments, loading CSV data for each file specified on the command line.
We can run this program using the CSV data that we used in the code on page 33:
$ ruby stock_stats.rb data.csv Processing data.csv Total value = 122.07
Do we need three source files for this? Not necessarily. But as your programs grow (and almost all programs grow over time), you'll find that large files start to get cumbersome. You'll also find it harder to write automated tests against the code if it's in a monolithic chunk. Finally, you won't be able to reuse classes if they're all bundled into the final program. As a result, it's fairly common to only have one Ruby class per individual file.
report erratum � discuss

Specifying Access Control � 45
Let's get back to our discussion of classes.
Specifying Access Control
When designing the interface for a class, it's important to consider how much of your class you'll expose to the outside world. Allow too much access into your class, and you risk increasing the amount that different classes depend on each other's internal implementation, which is called coupling. Users of your class will be tempted to rely on details of your class's implementation rather than on its logical interface. The good news is that the only easy way to change an object's state in Ruby is by calling one of its methods. If you control access to the methods, you control access to the object. A good rule of thumb is never to expose methods that could leave an object in an invalid state.
Ruby gives you three levels of access control:
� Public methods can be called by anyone--no access control is enforced. Methods are public by default (except for initialize, which is always private).
� Protected methods can be invoked only by objects of the defining class and its subclasses. Access is kept within the family. We'll talk more about subclasses in Chapter 6, Sharing Functionality: Inheritance, Modules, and Mixins, on page 101.
� Private methods cannot be called with an explicit receiver--the receiver is always the current object, also known as self. This means that private methods can be called only in the context of the current object, and with self as the explicit receiver or with the implicit receiver. You can't invoke another object's private methods with normal dot syntax. (But there are ways around this using metaprogramming tools that we'll discuss in Chapter 22, The Ruby Object Model and Metaprogramming, on page 371)
The difference between "protected" and "private" is fairly subtle and is different in Ruby than in other common object-oriented languages. If a method is protected, it may be called by any instance of the defining class or its subclasses. If a method is private, it may be called only within the context of the calling object--it's never possible to access another object's private methods directly, even if the object is of the same class as the caller. In practice, it's somewhat rare to see "protected" in use.
Access control in Ruby is determined dynamically, as the program runs, not statically when the program is compiled or interpreted. You'll get an access violation only when the code attempts to execute the restricted method.
You specify access levels to methods within the class or module definitions using one or more of the three access methods: public, protected, and private. You can use each function in three different ways.
If called with no arguments, the three functions set the default access control of subsequently defined methods. This is probably familiar behavior if you're a C# or Java programmer, where you'd use keywords such as public to achieve the same effect. Although this usage looks like a keyword, in Ruby, the access control is actually a method.
class MyClass # default is "public" def method1 # This method is public end
report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 46
protected # subsequent methods will be "protected" def method2
# This method is protected end
private # subsequent methods will be private" def method3
# This method is private end
public # subsequent methods will be "public" def method4
# this method is public end end
Since the default access for methods is public, it's rare to use public explicitly to denote access control.
As a matter of style, the methods after the call to an access method like public are typically not indented--you aren't defining a block, only the access status of subsequent methods.
Alternatively, you can set access levels of named methods by listing them as arguments to the access control functions:
class MyClass def method1 end
def method2 end # ... and so on
public :method1, :method4 protected :method2 private :method3 end
This mechanism is somewhat rare in practice, but it does enable the third way to declare access in Ruby.
We've mentioned that most statements in Ruby return a value. In particular, defining a method with def returns a value--the name of the new method as a symbol. As a result, you can declare access directly preceding a method definition.
class MyClass def method1 # This method is public end
protected def method2 # This method is protected
end
report erratum � discuss

Specifying Access Control � 47
private def method3 # This method is private
end
public def method4 # This method is public
end end
What's happening here is that the def method2 statement is returning the value :method2, which is immediately passed as an argument to protected, resulting in protected :method2, and making that method, and only that method, protected. Access declared this way doesn't propagate down the file, it only applies to the method that the access modifier directly precedes.
We prefer this last form because it's much more explicit about the access level of each method. That said, the first form is older, and currently more common in code you're likely to see.
It's time for some examples. Perhaps we're modeling an accounting system where every debit has a corresponding credit. Because we want to ensure that no one can break this rule, we'll make the methods that do the debits and credits private, and we'll define our external interface in terms of transactions.
class Account attr_accessor :balance
def initialize(balance) @balance = balance
end end
class Transaction def initialize(account_a, account_b) @account_a = account_a @account_b = account_b end
def transfer(amount) debit(@account_a, amount) credit(@account_b, amount)
end
private def debit(account, amount) account.balance -= amount
end
private def credit(account, amount) account.balance += amount
end end
savings = Account.new(100) checking = Account.new(200)
transaction = Transaction.new(checking, savings) transaction.transfer(50)
report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 48
Protected access is used when objects need to access the internal state of other objects of the same class. For example, we may want to allow two individual Account objects to compare their balances directly but to hide those balances from the rest of the world (perhaps because we present them in a different form):
class Account protected attr_reader :balance # accessor method 'balance' but make it protected
def greater_balance_than?(other) @balance > other.balance
end end
Because balance is protected, it's available only within Account objects.
Variables
Now that we've gone through the trouble of creating all these objects, let's make sure we don't lose them. Variables are used to keep track of objects; each variable holds a reference to an object. Let's confirm this with some code:
person = "Tim" puts "The object in 'person' is a #{person.class}" puts "The object has an id of #{person.object_id}" puts "and a value of '#{person}'"
produces: The object in 'person' is a String The object has an id of 60 and a value of 'Tim'
On the first line, Ruby creates a new string object with the value Tim. A reference to this object is placed in the local variable person. A quick check shows that the variable has indeed taken on the personality of a string, with a class, an object ID, and a value.
So, is a variable an object? In Ruby, the answer is "no." A variable is simply a reference to an object. Objects float around in a big pool somewhere (the operating system's heap, most of the time) and are pointed to by variables. Let's make the example slightly more complicated:
person1 = "Tim" person2 = person1 person1[0] = 'J'
puts "person1 is #{person1}" puts "person2 is #{person2}"
produces: person1 is Jim person2 is Jim
What happened here? We changed the first character of person1 (Ruby strings are mutable, unlike Java's), but both person1 and person2 changed from Tim to Jim.
It all comes back to the fact that variables hold references to objects, not the objects themselves. Assigning person1 to person2 doesn't create any new objects; it simply copies person1's object reference to person2 so that both person1 and person2 refer to the same object, as shown in the illustration on page 49.
report erratum � discuss

person1 = "Tim"

person1

Reopening Classes � 49
String
Tim

person2 = person1

person1 person2

String
Tim

person1[0] = "J"

person1 person2

String
Jim

Assignment aliases objects, potentially giving you multiple variables that reference the same object.

Can't this cause problems in your code? It can, but not as often as you'd think (objects in Java, for example, work exactly the same way). In the previous example, for instance, you could avoid aliasing by using the dup method of String, which creates a new string object with identical contents:

person1 = "Tim" person2 = person1.dup person1[0] = "J" puts "person1 is #{person1}" puts "person2 is #{person2}"
produces:
person1 is Jim person2 is Tim

You can also prevent anyone from changing a particular object by freezing it. Attempt to alter a frozen object, and Ruby will raise a RuntimeError exception:

person1 = "Tim" person2 = person1 person1.freeze person2[0] = "J"

# prevent modifications to the object

produces:
from prog.rb:4:in `<main>' prog.rb:4:in `[]=': can't modify frozen String: "Tim" (FrozenError)

Numbers and symbols are always frozen in Ruby, so those values are always immutable.

Reopening Classes

While we're talking about classes in Ruby, we feel like we should at least mention one of the most unique features of Ruby's class structure: the ability to reopen a class definition and add new methods or variables to it at any time, even classes that are part of the thirdparty tools or the standard library.
In other words, if you have something like this in Ruby:

report erratum � discuss

Chapter 3. Classes, Objects, and Variables � 50

class Book attr_accessor :title
# and a bunch of other stuff end

Later, you can do this:

class Book def uppercase_title title.upcase end
end

If you declare class Book and a Book class already exists, Ruby won't give an error, and the new definitions in the second declaration will be added to the existing class. This is true even if the existing class is part of Ruby itself. This process of reopening classes to add or change methods is colloquially known as monkey-patching.
Typically, you'd only extend a class like this if the original class isn't part of your code, but it's reasonably common in Ruby to use this method to add utility functions to core classes or the standard library. Ruby on Rails, for example, does this a lot.
To give an example, Ruby on Rails defines a method called squish, which clears excessive whitespace in a string, so if you have this:

"This

string

has

whitespace"

It becomes "This string has whitespace." By monkey-patching, Rails can define the method like this:

class String def squish # implementation end
end

And then call it using str.squish like any other method.
The alternative, which many other languages use, is to define a utility class or classes and define a class method on them, which looks like this:
class StringUtilities def self.squish(str) # implementation end
end

Which you would then call with StringUtilities.squish(str).
This example shows the advantage of allowing classes to reopen--the ability to add and easily use utility methods is convenient. It's nice to not have to know which methods are defined by Rails and which of the many possible utility classes a method might be in.
That said, this is something to be done with caution--many teams don't allow it in their own code without a clear reason. And you should be wary of using monkey-patching to change the behavior of existing methods, rather than adding new methods as we did here.

report erratum � discuss

What's Next � 51
Monkey-patching can make the behavior of code unpredictable. It can be hard to tell where behavior is defined, and these changes are global, meaning that if two files define the same method, the last defined one will win, leading to potentially hard-to-find bugs. Later in Chapter 22, The Ruby Object Model and Metaprogramming, on page 371, we'll talk about refinements, a Ruby feature that gives you the benefit of reopening classes, but also limits the scope of your changes.
What's Next
There's more to say about classes and objects in Ruby. We still have to look at class methods and concepts such as mixins and inheritance. We'll do that in Chapter 6, Sharing Functionality: Inheritance, Modules, and Mixins, on page 101. But, for now, know that everything you manipulate in Ruby is an object and that objects start their lives as instances of classes. And one of the most common things we do with objects is to create collections of them. But that's the subject of our next chapter.
report erratum � discuss

CHAPTER 4
Collections, Blocks, and Iterators

Most real programs have to manage collections of data: the people in a course, the songs in your playlist, the books in the store, and so on. Ruby comes with two classes that are commonly used to handle these collections: arrays and hashes. A Ruby array is an ordered collection of data. A Ruby hash is a key/value pair, equivalent to a Python dictionary, a Java Map, or a JavaScript object. Mastery of these two classes, and their large interfaces, is an important part of being an effective Ruby programmer.
But it isn't only these two classes that give Ruby its power when dealing with collections. Ruby also has a block syntax that lets you encapsulate chunks of code. When paired with collections, these blocks can build powerful iterator constructs. In this chapter, we'll look at the two collection classes as well as the blocks and iterators.

Arrays

The class Array holds a collection of object references. Each object reference occupies a position in the array, identified by an integer index. You can create arrays by using literals or by explicitly creating an Array object. A literal array is a comma-delimited list of objects between square brackets:

a = [3.14159, "pie", 99]

a.class # => Array

a.length # => 3

a[0]

# => 3.14159

a[1]

# => "pie"

a[2]

# => 99

a[3]

# => nil

You can create an empty array with either [] or by directly calling Array.new:

b = Array.new

b.class # => Array

b.length # => 0

b[0] = "second"

b[1] = "array"

b

# => ["second", "array"]

report erratum � discuss

Chapter 4. Collections, Blocks, and Iterators � 54

As the example shows, array indices start at zero. Index an array with a non-negative integer, and it returns the object at that position, or it returns nil if nothing is there. Index an array with a negative integer, and it counts from the end, with -1 being the last element of the array.

a = [1, 3, 5, 7, 9]

a[-1]

# => 9

a[-2]

# => 7

a[-99] # => nil

The following diagram shows array access in a different way:

positive negative

0

1

2

3

4

5

6

-7

-6

-5

-4

-3

-2

-1

a=

[ "ant", "bat", "cat", "dog", "elk", "fly", "gnu" ]

a[2] a[-3] a[1..3] a[1...3] a[-3..-1] a[4..-2]

[ "bat", [ "bat",

"cat" "elk"
"cat", "dog" ] "cat" ]
[ "elk", [ "elk",

"fly", "gnu" ] "fly" ]

Arrays are accessed using the [] operator. As with most Ruby operators, this operator is implemented as a method, specifically, an instance method of class Array. The last two lines of this example are equivalent:

a = [3.14159, "pie", 99]

a[0]

# => 3.14159

a.[](0) # => 3.14159

The last line of code treats [] as a normal method. In practice, you wouldn't write code like the last line, we just wanted to show how flexible Ruby is.

You can index arrays with a pair of numbers, [start, count]. This returns a new array consisting of references to count the number of objects starting at position start:

a = [1, 3, 5, 7, 9] a[1, 3] # => [3, 5, 7] a[3, 1] # => [7] a[-3, 2] # => [5, 7]

You can also index arrays using ranges, in which the start and end positions are separated by two or three dots. The two-dot form includes the end position; the three-dot form doesn't. We'll talk more about ranges in Chapter 7, Basic Types: Numbers, Strings, and Ranges, on page 117.
a = [1, 3, 5, 7, 9] a[1..3] # => [3, 5, 7] a[1...3] # => [3, 5] a[3..3] # => [7] a[-3..-1] # => [5, 7, 9]

report erratum � discuss

Arrays � 55

The [] operator has a corresponding []= operator, which lets you set elements in the array. If used with a single integer index, the element at that position is replaced by whatever is on the right side of the assignment. Any gaps that result will be filled with nil:

a = [1, 3, 5, 7, 9] a[1] = 'bat' a[-3] = 'cat' a[3] = [9, 8] a[6] = 99

#=> [1, 3, 5, 7, 9] #=> [1, "bat", 5, 7, 9] #=> [1, "bat", "cat", 7, 9] #=> [1, "bat", "cat", [9, 8], 9] #=> [1, "bat", "cat", [9, 8], 9, nil, 99]

Again, []= is a regular method, and you could write it as a.[]=(index, new_value).
If the index to []= is two numbers (a start and a length) or a range, then those elements in the original array are replaced by whatever is on the right side of the assignment. If the length of the selected elements on the left is zero, the right side is inserted into the array before the start position; no elements are removed. If the right side is itself an array, its elements are used in the replacement. The array size is automatically adjusted if the index selects a different number of elements than are available on the right side of the assignment.

a = [1, 3, 5, 7, 9] a[2, 2] = "cat" a[2, 0] = "dog" a[1, 1] = [9, 8, 7] a[0..3] = [] a[5..6] = 99, 98

#=> [1, 3, 5, 7, 9] #=> [1, 3, "cat", 9] #=> [1, 3, "dog", "cat", 9] #=> [1, 9, 8, 7, "dog", "cat", 9] #=> ["dog", "cat", 9] #=> ["dog", "cat", 9, nil, nil, 99, 98]

In the line a[2, 2] = "cat", the subarray starting at index 2 and of length 2, which is [5, 7], is replaced by cat. In the next line, the subarray [2, 0] is of length 0, so dog is inserted at index 2. Then the subarray represented by [1, 1], which is [3], is replaced by [9, 8, 7] being inserted in the array. Notice that the entire right-side array isn't inserted as one element, rather each element in the right-hand side is inserted individually. The last two lines are similar, but they use ranges instead of a start and a length.

It's common to create arrays of short words, but that can be a pain, what with all the quotes and commas. Fortunately, Ruby has a shortcut, %w, which does just what we want:
Instead of this:

a = ["ant", "bee", "cat", "dog", "elk"]

a[0]

# => "ant"

a[3]

# => "dog"

You can use %w followed by a delimiter and then by space-separated individual words.

a = %w[ant bee cat dog elk]

a[0]

# => "ant"

a[3]

# => "dog"

You can use any character after %w as the delimiter. If it's something with a pair, like a bracket or parenthesis, then the array will continue until the other side of the pair. If you don't use a pair, the array will continue until it reaches the same character again.

If you want an array of symbols instead of strings, Ruby has a similar %i shortcut:

report erratum � discuss

Chapter 4. Collections, Blocks, and Iterators � 56

a = %i[ant bee cat dog elk]

a[0]

# => :ant

a[3]

# => :dog

Arrays have a large number of other useful methods. Using them, you can treat arrays as stacks, sets, queues, dequeues, and first-in-first-out (FIFO) queues. (Ruby also has a dedicated Set class, which we'll cover in Chapter 28, Library Reference: Enumerators and Containers, on page 561.)

For example, push and pop add and remove elements from the end of an array, so you can use the array as a stack:

stack = []

stack.push "red"

stack.push "green"

stack.push "blue"

stack

# => ["red", "green", "blue"]

stack.pop # => "blue"

stack.pop # => "green"

stack.pop # => "red"

stack

# => []

Similarly, unshift and shift add and remove elements from the beginning of an array. Combine shift and push, and you have a first-in-first-out (FIFO) queue.

queue = [] queue.push "red" queue.push "green" queue.shift # => "red" queue.shift # => "green"

The first and last methods return (but don't remove) the n entries at the head or end of an array. If you don't pass an argument, the default number is one.

array = [1, 2, 3, 4, 5, 6, 7]

array.first # => 1

array.first(4) # => [1, 2, 3, 4]

array.last

# => 7

array.last(4) # => [4, 5, 6, 7]

We'll look at more array methods later on in Array, on page 561.

Hashes

Hashes (sometimes known as associative arrays, maps, or dictionaries) are similar to arrays in that they are indexed collections of object references. But, while you index arrays with integers, you index a hash with objects of any type, most often symbols and strings but also regular expressions or anything else in Ruby. When you store a value in a hash, you actually supply two objects: the index, which is called the key, and the value, or entry, to be stored with that key. You can subsequently retrieve the entry by indexing the hash with the same key value that you used to store it.

report erratum � discuss
