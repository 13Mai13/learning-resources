# Open Source Licenses 

- [Open Source Licenses](#open-source-licenses)
  * [General definition](#general-definition)
  * [What is a license and why do I need one?](#what-is-a-license-and-why-do-i-need-one-)
  * [Types of licences](#types-of-licences)
  * [Resources](#resources)


## General definition

*  Open Source simply means availability of the source code of a project. 
* OSI's open source defintion: 
    * Free redistribution.
    * Source code availabilty.
    * Derivatives allowed.
    * No limitations on who may use it and for what. 
    * No additional license in place
    * Not depend on a specific distribution format, tecnology or presence of other works

* This doesn't mean you can't charge for it. 

## What is a license and why do I need one? 

* Any work that you create by default makes you the copyright holder of it. That means only you are allowed to distribute whatever you created.

* If you want to transfer this right to other people as well, you can do that via a so-called license. Consider it a set of rules that define how others may use, distribute, modify and otherwise interact with the work you created, and under what terms.

## Types of licences 

### "Copyleft" licenses: GPL, AGPL, LGPL

You can require anyone who modifies your work to share its own source code as well. Having to adhere to similar term *being viral*. 

* GLP or GNU: 
    * Derivatives must be distributed under compatible terms 
    * Rules out any claims of warranty (so you cannot be sued)
    * States that any kind of attribution must be kept in place.
    * The license and its siblings are OSI.
    * Commercial use is no problem

* AGPL or Affero GNU Public License:
    * Expands on the virality clause.
    * Even if derivatives are only accessed through a network connection their sources must be made available under compatible terms. 
* LGPL or Lesser GNU Public License:
    *  Dials back the virality.
    *  Derivatives only linking against the work don't have to share under the same license terms.
    * "linking" has been a debate. But in general the idea here is that as long as your work is only used like a library and not directly build upon, the virality clause doesn't trigger. 

## Permissive license

Family of quite permissive Open Source Licenses that are not viral but still offer attribution and protection against liability. 

* All of them require that attribution must be kept in place, warranty & liability are strictly ruled out. 

* Commercial use is no problem at all. 

* The differences between the members of this family lie in permission of patent claims and trademark use. 

* The devil here is truly in the details.

* MIT: The [MIT License](https://opensource.org/license/mit/) is pretty short, and pretty simple.
    * You are allowed to do anything you want with MIT-licensed code, as long as you include the original license somewhere in your derivative. 
    *  Have a COPYING or LICENSE file that says something like "[project] includes code from foobaz, which is licensed under the MIT license:" with the original license following.

* [Apache](https://opensource.org/license/apache-2-0/):
    * Notably, if you change any Apache-licensed code, you must state so. There are also rules about use of the project name. 
    * The Apache license is notable among open-source licenses for including language dealing with patents. 

* Apache vs MIT: 

However, Apache 2.0 gives you both a copyright AND a patent license. MIT gives you only a copyright license.

## Creative Commons

Creative Commons is a bit like a choose-your-own-adventure of licensing. you have a base license which rules out warranty, and various modules that you can attach to it as well if you want. 

* BY: requires the author to be stated

* SA: any derivatives must be "shared alike", so under the same license terms - this is the virality module

* NC: commercial use is forbidden - if this module is included, the license is no longer Open Source under the OSI definition.

* ND: derivatives are forbidden - if this module is included, the license is also no longer Open Source under the OSI definition. 

The license is **not itself OSI approved**. 

## Public Domain

All copyright claims have been forfeit.

* There is a huge downside to it: no warranty waive.
* You really do not want to make yourself vulnerable to legal threats simply for having written some code that caused someone issues due to a bug. 
* At the very least consider something like the Unlicense because it at least contains the warranty waiver and thus protects you from liability. 

## Resources

* [This](https://github.com/readme/guides/open-source-licensing) article
* [Open source definition from Open Source Initiave](https://opensource.org/osd/)
* [Apache vs MIT](https://www.quora.com/Whats-the-difference-between-Apache-v2-0-and-MIT-license-What-are-the-major-consequences-of-using-Apache-software-over-MIT)
* [Get a license explanied](https://www.tldrlegal.com/)