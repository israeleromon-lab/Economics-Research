# AI and Economic Growth in Nigeria: An Empirical Look at SME Credit

## 1. Introduction

Nigeria is Africa's largest economy, but despite the top-line GDP growth over the last twenty years, getting that wealth to actually spread around is still a huge problem. A massive chunk of the adult population doesn't use formal banking. Small and Medium Enterprises (SMEs) are the backbone of the economy—making up over 80% of jobs and about half the GDP—yet they struggle constantly to get loans. Banks usually blame this on high costs and the fact that most of these small businesses don't have collateral or a formal credit history.

Lately, Artificial Intelligence (AI) and machine learning are starting to change how this works. Instead of needing a traditional credit score, FinTech companies are using AI models to look at alternative data: things like mobile phone top-ups, utility bills, and digital payment histories. This lets them figure out if someone is a good candidate for a loan much faster and cheaper.

In this paper, we wanted to look at what happens when AI starts intersecting with the broader economy in Nigeria. We focused on a few specific questions:
1. Does better digital infrastructure (which you need for AI) actually lead to more credit for SMEs?
2. How does all this digital and financial technology relate to the country's overall GDP?
3. What's holding back the wider, safer use of AI in the Nigerian financial sector?

To figure this out, we pulled historical data from the World Bank covering broadband penetration, GDP growth, and how much credit the private sector is getting.

## 2. Literature Review

There's a lot of talk about AI in emerging markets right now, but specific research on Nigeria is still pretty sparse.

### 2.1. Tech and Growth
Most global reports suggest AI will add trillions to the economy by 2030. In places like Africa, people often talk about AI as a way to "leapfrog" older technologies. But when you look at the Oxford Insights AI Readiness Index, the reality is a bit more sobering. While the tech scene in Lagos is booming, Nigeria still struggles with basics like reliable electricity and fast internet outside major cities, which are absolute requirements for running heavy AI models.

### 2.2. Financial Inclusion 
Groups like EFInA track financial inclusion closely, and their data shows that while things are getting better (thanks to mobile money), rural areas and women are still getting left behind. SMEDAN consistently points out that lack of financing is the number one reason small businesses fail. Traditional banks just aren't built to lend to informal vendors.

### 2.3. Algorithmic Credit Scoring
This is where the literature starts getting interesting. Researchers have found that machine learning can chew through unstructured data and predict loan defaults for people with "thin files" pretty accurately. Some studies even show that alternative scoring approves more loans without driving up default rates compared to old-school banking methods.

### 2.4. What's Missing?
While we know AI works in theory, and we know Nigeria has a credit problem, there isn't much hard data showing the link between digital readiness and actual credit access over time in Nigeria. That's the gap we're trying to fill here.

## 3. Methodology

Since there isn't a massive, neat dataset labeled "AI usage by Nigerian SMEs," we had to use macro-level proxies to test our ideas:
- **Digital Readiness**: We used fixed broadband subscriptions. If you don't have internet, you aren't using cloud AI.
- **SME Credit Access**: We used the World Bank metric for "Domestic credit to private sector (% of GDP)".
- **Economic Impact**: Annual GDP growth percentage.

We grabbed the data from the World Bank Open Data platform, cleaned it up in Python, and ran a standard Pearson correlation to see if these trends move together.

## 4. Results and Discussion

Running the numbers gave us a few interesting takeaways.

### 4.1. Better Internet = More Credit
Our correlation matrix showed a positive link (0.37) between broadband subscriptions and credit to the private sector. This makes sense. As the country's digital backbone gets stronger, it paves the way for FinTechs to run the AI algorithms needed to score and lend to people who were previously off the grid. Basically, better tech infrastructure seems to open up the lending taps.

### 4.2. The GDP Disconnect
On the flip side, we saw a slight negative correlation (-0.13) between digital readiness and short-term GDP growth. This might sound weird at first, but Nigeria's GDP is famously tied to global oil prices. A dip in oil can tank the GDP even if the tech sector is doing great. Also, digital upgrades usually take a few years to actually show up in national productivity numbers.

## 5. Conclusion and Policy Ideas

AI, especially algorithmic credit scoring, is a real chance to fix Nigeria's SME lending problem. Our data points to a clear link: when you improve digital infrastructure, private sector credit goes up. But it's not going to fix the whole economy overnight.

Based on what we found, here's what should happen next:
1. **Focus on the Basics**: The government needs to push broadband outside of just Lagos and Abuja. You can't have an AI revolution on 2G networks.
2. **Regulatory Sandboxes**: The Central Bank of Nigeria needs to give FinTechs a safe space to test these AI lending models so they can innovate without breaking banking laws.
3. **Watch Out for Bias**: Algorithms can be biased. We need local rules to make sure AI doesn't end up discriminating against rural farmers or women who might not have a massive digital footprint.
