title: How to do GDPR with smart contracts and/or blockchain
author: Randy Gingeleski
slug: blockchain-gdpr
summary: Is it possible to be GDPR compliant when developing with blockchain? Kinda.
category: policy
tags: privacy,law,policy
date: 2019-01-01
modified: 2019-01-01
template: blog_page


title: How to do GDPR with smart contracts and/or blockchain
author: Randy Gingeleski
slug: blockchain-gdpr
summary: Is it possible to be GDPR compliant when developing with blockchain? Kinda.
category: policy
tags: privacy,law,policy
date: 2018-01-01
modified: 2018-01-01
template: blog_page


There's more to GDPR than obnoxiously informing you websites are using cookies.

Let's step through each tenet of GDPR and talk through how they relate to blockchain (d)apps.

As of this writing, you can find the actual GDPR legislation (EU Regulation 2016/679 of the European Parliament) [**here in many different languages**](https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1532348683434&uri=CELEX:02016R0679-20160504). I found it helpful to read verbatim instead of relying on others' interpretations.

With that said, we'll be summarizing a bit. And remember we're really talking *Ethereum* below.

Some of the issues we run into might not be prevalent with permissioned distributed ledger technology (i.e. R3's Corda).

## Mandatory breach notifications

**Compatibility with blockchain** = High

A data breach, defined as an event which would "result in a risk for the rights and freedoms of individuals", mandates notification to customers and controllers within 72 hours of awareness.

This seems unlikely to occur with blockchain applications but should be possible.

## Right to access; data portability

**Compatibility with blockchain** = High

Anyone who has data about them in the application has a right to access it at any time.

Given the transparent - sometimes *hyper* transparent - nature of blockchain apps, this doesn't seem hard to comply with.

## Right to be forgotten

**Compatibility with blockchain** = Low to Moderate

Seemingly the biggest obstacle to developing on blockchain *and* being GDPR compliant is the regulation's "right to be forgotten." This says that someone protected by GDPR can tell the data controller to delete their data at any time.

This is tough with blockchain, as you can imagine, given that immutable history is a major part of it.

Imagine someone is developing an on-chain social network. (No, seriously, please imagine that for the sake of this exercise.)

Amongst other things, you are dealing with images of participants. Forget the other data for now. You *could* write the binary image data on-chain. But this makes it virtually impossible to just erase the stuff later.

What you might do to be more GDPR compliant is store the participants' images in Amazon S3 bucket(s). Then put a hash of the image data on the blockchain. That way you can properly erase images of people covered by GDPR *and* still have some blockchain-verifiability.

(Fork this post on Github if you've got a better example but the core concept of relating off-chain binary data to the chain via hash still goes)

## Privacy by design; privacy by default

**Compatibility with blockchain** = None to Low

We're still at the beginning stages of on-chain secrets. For the time being I still consider there to be no secrets in Ethereum world when threat modeling.

Depending on your interpretation of the privacy by design and default parts of GDPR, these hold zero to minimal compatibility with blockchain/Ethereum applications.

Let's look at Article 25 which declares this. Here are the first 2 out of 3 paragraphs, which are the ones that matter. Bolding is done by me and highlights the parts I regard as tough to do with an Ethereum application.

> 1.  Taking into account the state of the art, the cost of implementation and the nature, scope, context and purposes of processing as well as the risks of varying likelihood and severity for rights and freedoms of natural persons posed by the processing, the controller shall, both at the time of the determination of the means for processing and at the time of the processing itself, implement appropriate technical and **organisational measures, such as pseudonymisation**, which are designed to implement **data-protection principles, such as data minimisation**, in an effective manner and to integrate the necessary safeguards into the processing in order to meet the requirements of this Regulation and protect the rights of data subjects.

To use their examples, I don't think you can do pseudonumisation and data minimisation without now having off-chain data. That divergence from transparency goes against the idea of doing an Ethereum application in the first place. But I guess that depends on what you present as the value-add of blockchain.

If it's less to do with data and more about assuring how data is processed, this might not be a big deal. We could call that "low" compatibility.

But consider again the first point. Data would have to be off-chain. The integrity of that is now tough to assure with our blockchain. I think we'd have to say "none".

> 2.  The controller shall implement appropriate technical and organisational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed. That obligation applies to the amount of personal data collected, the extent of their processing, **the period of their storage and their accessibility**. In particular, such measures shall ensure that by default personal data are **not made accessible without the individual's intervention to an indefinite number of natural persons**.

Remember what we discussed regarding the right to be forgotten - blockchains don't forget.

And re-emphasizing what we said about paragraph 1, everything's open unless you have off-chain data, and that goes against the spirit of transparency.

On-chain secrets might help with this.

## Data protection officer

**Compatibility with blockchain** = None

A final thing worth mentioning from GDPR is this concept of a data protection officer. See Article 30 where this comes up.

You need to actually label someone a data protection officer. They get certain responsibilities regarding everything GDPR mandates.

This will depend on your application's business logic but seems near impossible to comply with.

Ethereum is not a permissioned blockchain. Everyone comes to the network with the same entitlement (flat access control).

It's tough to single out one person to have extra data protecting abilities. I'm not sure what this would look like.

You could have functions that do something with data, check incoming addresses trying to hit that function, and attempt access control on it that way. With the officer's address...? I'm spitballing.

That doesn't address the problem of data being stored in the history of the chain. What can this officer do to protect data, really? Secrets on the blockchain might help once we get to that point.

## Conclusion

If you write an Ethereum application that's really leveraging the hyper-transparent spirit of blockchain, good luck complying with GDPR. I don't see you being able store personal information compatibly.

Things seem like they'd get easier with a permissioned DLT system (again I'll mention Corda from R3). But even then you have some hang-ups like the right to be forgotten.

Overall I feel your ability to do blockchain *and* GDPR is "kinda not really".
