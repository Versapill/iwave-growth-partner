#!/usr/bin/env python3
"""Builds the service pages in /services from the content below.

Edit the SERVICES / TESTIMONIALS / CASES data, then run from the project folder:

    python3 tools/build_services.py

Every page shares the same header, footer, styles (assets/site.css) and theme
(assets/tailwind.config.js) as the homepage.
"""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "services"
SITE = "https://www.iwave.digital"  # live domain, used for canonical URLs, share tags and structured data
BOOKING_URL = "https://cal.com/iwave-digital/discovery-call"
EMAIL = "nick@iwave.digital"

ARROW = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>'
CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5L20 7"/></svg>'
PLUS = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M12 5v14M5 12h14"/></svg>'

# ----------------------------------------------------------------- testimonials
# Testimonials without a photo in assets/testimonials/ show the person's initials instead.
TESTIMONIALS = {
    "anne": ("Anne Casanova", "Fractional CMO",
             "A professional, flexible partner who knows what he is doing. We saw a 150% increase in booked calls due to his LinkedIn system. Highly recommend!"),
    "monica": ("Monica Ducu", "Business Consulting & Coaching",
               "I've worked with Nick for 8 months and it was the best investment ever. With his AI outreach system, we consistently had 2-4 qualified booked calls every week on LinkedIn."),
    "elmira": ("Elmira Abushayeva", "Co-Founder at Mavuus & Fractional CMO",
               "Nick is an exceptional marketing professional - a rare combination of creativity and discipline, technically strong, and forward-thinking with AI-powered solutions."),
    "roland": ("Roland Esquivel", "VP Global Sales & Marketing at POMS Corporation",
               "Nick scaled our outbound and focused on key personas in our industry, resulting in 10x outbound monthly contacts, always on time and above expectations."),
    "brian": ("Brian Thompson", "Co-Founder at Keeyora",
              "They have built an outreach system that generated 40+ qualified meetings for us in just a few months. It gave us a consistent flow of conversations with the right SaaS prospects."),
    "kirstie": ("Kirstie Lough", "Founder at Whitson Marketing & Fractional CMO",
                "Nick has been an invaluable partner in generating leads through LinkedIn for me and my clients - creative, reliable, and easy to collaborate with."),
    "andrius": ("Andrius Balkunas", "CEO and Founder at ParcelABC",
                "The iWave Digital team took our social media presence to the next level. Our reach more than doubled, and we started getting more inbound leads. Helped us grow to 17k followers!"),
    "daniel": ("Daniel Dico", "Founder at OERP Canada",
               "iWave Digital team has played an important role in strengthening our brand visibility - proactive, easy to work with, and genuinely cares about delivering quality work."),
}

# ----------------------------------------------------------------- case studies
CASES = {
    "poms": dict(logo="poms", name="POMS Corporation", w=151, h=44, bg="bg-brand", metric="10×", label="monthly outbound contacts",
                 title="Outbound that reaches the right personas",
                 body="We scaled POMS's outbound around the key personas in their industry, growing monthly outbound contacts tenfold, delivered on time and above expectations."),
    "keeyora": dict(logo="keeyora", name="Keeyora", w=180, h=35, bg="bg-sky-dark", metric="40+", label="qualified meetings in a few months",
                    title="A steady flow of SaaS sales conversations",
                    body="An outreach system that gave Keeyora a consistent flow of conversations with the right SaaS prospects, generating 40+ qualified meetings in just a few months."),
    "parcelabc": dict(logo="parcelabc", name="ParcelABC", w=169, h=39, bg="bg-ink", metric="17k", label="followers, with reach more than doubled",
                      title="Social media that drives inbound leads",
                      body="We took ParcelABC's social presence to the next level: reach more than doubled, inbound leads increased and the audience grew to 17k followers."),
}

# ----------------------------------------------------------------- services
# icon: inner SVG markup (24x24, stroke). tone: "brand" or "sky".
SERVICES = [
    dict(
        slug="linkedin-client-acquisition", tone="brand",
        name="LinkedIn Client Acquisition System", title_a="Win clients on LinkedIn", title_b="with one repeatable system",
        icon='<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
        summary="A done-for-you LinkedIn system that combines profile branding, daily content and AI-powered outbound to book calls with your ideal clients.",
        intro="LinkedIn is where the real opportunity is right now. We build your authority with content and run an AI-powered outbound engine that puts you in front of the people you actually want to talk to, so qualified calls land in your calendar every week.",
        best_for=["Founders and fractional professionals who sell high-value services",
                  "Agencies and consultants who want a predictable flow of new clients",
                  "Funded B2B companies ready to turn LinkedIn into a sales channel"],
        pillars_intro="Authority content and outbound work as one system, so every message feels like a warm follow-up instead of a cold pitch.",
        pillars=[("Profile branding", "Re-designing your profile.",
                  "Your profile is the first thing a lead checks before they book a call. If it doesn't read like an authority, everything else in the system has to work twice as hard."),
                 ("LinkedIn content creation", "A mix of lead magnets and value posts.",
                  "Keeps you visible between DMs and builds trust before the first message ever lands, so outbound feels like a warm follow-up instead of a cold pitch."),
                 ("AI-powered outbound", "Hyper-targeted LinkedIn DMs.",
                  "AI narrows the list down to the people who actually match your ideal-client profile, so every message goes to someone worth messaging in the first place.")],
        included=[("Custom LinkedIn all-bound system", "Content and outbound designed as one system around your offer and ideal clients."),
                  ("Profile re-branding", "Headline, banner, about section and featured content rebuilt to convert visitors into calls."),
                  ("Daily LinkedIn content", "Lead magnets and value posts written in your voice and published consistently."),
                  ("4,000+ LinkedIn DMs monthly", "AI-targeted, personalised outreach to decision-makers who match your ideal-client profile."),
                  ("Weekly team update calls", "A clear view of what's working, what's booked and what we're testing next."),
                  ("A framework built to scale", "A system designed to take you past $100k and keep growing from there.")],
        steps=[("Free LinkedIn audit", "We review your profile, content and market, and see if working together makes sense."),
               ("Profile & strategy", "We re-brand your profile and map your ideal clients, offers and content angles."),
               ("Content & outbound live", "Daily content and AI-targeted DMs start running, so conversations begin within days."),
               ("Calls & scale", "Qualified calls land in your calendar and we keep scaling what converts.")],
        case_detail=dict(
            logo="keeyora", name="Keeyora", w=180, h=35,
            title="How Keeyora booked 40+ qualified meetings from LinkedIn",
            body="Keeyora, a talent communication platform, needed a consistent flow of conversations with the right SaaS prospects. We ran both sides of our framework around co-founder Brian Thompson's LinkedIn: inbound content that built authority and attracted leads, and AI-targeted outbound that started the right conversations.",
            stats=[("40+", "qualified meetings in a few months"), ("234k+", "impressions on the top 3 posts"),
                   ("6,400+", "comments on lead-magnet posts"), ("32.4%", "connection acceptance rate"),
                   ("10%", "reply rate on outbound"), ("22.9k", "followers on Brian's profile")],
            parts=[dict(label="Inbound", title="Content that drives results",
                        text="We turned Brian's profile into an authority channel. Alongside value posts, lead-magnet posts offered genuinely useful resources in exchange for a comment, turning attention into warm conversations. The top three posts alone reached 234k+ impressions and 6,400+ comments, so many prospects already knew Brian before any outreach began.",
                        images=[("posts", 900, 800, "Top performing lead-magnet posts: 106k, 66k and 61k impressions"),
                                ("brian-profile", 1200, 800, "Brian Thompson's LinkedIn profile, Co-Founder at Keeyora")]),
                   dict(label="Outbound", title="AI-targeted outreach",
                        text="In parallel, AI narrowed the target list down to SaaS decision-makers matching Keeyora's ideal-client profile, and personalised DM campaigns ran on top. With content already warming prospects up, the best campaign reached a 32.4% connection acceptance rate and a 10% reply rate.",
                        images=[("campaigns", 1440, 816, "Keeyora's LinkedIn outreach campaigns, with acceptance and reply rates highlighted")])],
            quote="brian"),
        offers=[dict(name="Done-For-You LinkedIn System", tag="Most popular", featured=True,
                     text="We'd rather build a real partnership than chase a one-off fee, so pricing is a setup cost plus a performance-based component.",
                     items=["Custom LinkedIn all-bound system", "Daily LinkedIn content", "Weekly team update calls", "Profile re-branding", "4,000+ LinkedIn DMs monthly", "A framework built to scale past $100k"],
                     cta="See if you qualify"),
                dict(name="LinkedIn 1:1 Consulting", tag="Done-with-you", featured=False,
                     text="Learn the exact system we use to book 40–50 calls a month. Ideal for solopreneurs or in-house teams who'd rather run it themselves.",
                     items=["Custom roadmap", "Masterclasses & guides", "Private 1:1 calls", "DM & content templates"],
                     cta="Book a call")],
        case=None, quotes=[],  # no testimonials section on this page
        faq=[("What's the process behind booking calls?", "It varies by niche and business model, but broadly we combine inbound (content and collaborations) with outbound (cold and warm DMs) to move the right people into your calendar."),
             ("How long does it take to start seeing results?", "With the right team and process in place, we've seen movement in as little as three to four days after onboarding."),
             ("Why LinkedIn and not Facebook or cold email?", "LinkedIn is still undersaturated for genuinely valuable content, and that window is closing over the next couple of years. It's noisy, but our approach is built to cut through that noise."),
             ("What makes your approach different?", "We treat content and outbound as one system, not two separate tactics. Book a call and we'll walk you through exactly how it works for your business.")],
    ),
    dict(
        slug="smart-outbound-framework", tone="brand",
        name="Smart Outbound Framework", title_a="Outbound that fills", title_b="your pipeline, not spam folders",
        icon='<path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4z"/>',
        summary="AI-targeted, multichannel outbound across email and LinkedIn that reaches the right decision-makers and turns replies into real pipeline.",
        intro="Most outbound fails because it goes to the wrong people with the wrong message. Our framework uses AI to find the prospects who actually match your ideal client, then runs personalised email and LinkedIn campaigns that start real sales conversations and build measurable pipeline.",
        best_for=["B2B companies that need more qualified meetings without hiring more SDRs",
                  "Teams whose current outbound gets ignored, bounced or marked as spam",
                  "Sales-led businesses that want pipeline they can forecast"],
        pillars_intro="Targeting, messaging and channels work together, so every touchpoint builds on the last instead of starting cold.",
        pillars=[("AI-powered targeting", "The right people, not just more people.",
                  "AI researches and filters your market down to decision-makers who match your ideal-client profile and show signs they're ready to buy."),
                 ("Multichannel sequences", "Email and LinkedIn, working together.",
                  "Personalised cold email and LinkedIn outreach run side by side, so prospects see you in more than one place and replies come from both channels."),
                 ("Pipeline handoff", "From reply to booked meeting.",
                  "Positive replies are routed fast, meetings land in your calendar and every opportunity is tracked in your CRM, so outbound shows up as real pipeline.")],
        included=[("Ideal-client & persona strategy", "A clear definition of who to target and the angles that will resonate with each persona."),
                  ("AI-researched prospect lists", "Verified decision-makers, enriched with the context we need to personalise every message."),
                  ("Email infrastructure & deliverability", "Domains, inboxes and warm-up set up properly so your emails land in the inbox."),
                  ("Personalised email sequences", "Multi-step campaigns written for each persona, tested and improved every week."),
                  ("LinkedIn outreach campaigns", "Connection requests and message sequences that run alongside email."),
                  ("Reply handling & reporting", "Fast follow-up on every positive reply, plus weekly numbers on replies, meetings and pipeline.")],
        steps=[("Audit & strategy", "We review your offer, past outreach and best customers to define targets and messaging."),
               ("Build", "We set up infrastructure, build AI-researched lists and write the first sequences for your approval."),
               ("Launch", "Email and LinkedIn campaigns go live, and replies start turning into booked meetings."),
               ("Optimise & scale", "We test angles, double down on what converts and expand to new segments.")],
        case_detail=dict(
            logo="aktive-clients", name="Aktive Clients", w=139, h=75, logo_class="h-16",
            title="How Aktive Clients built $1.2M in pipeline with smart outbound",
            body="Aktive Clients needed a reliable way to start conversations with the right prospects at scale. We ran the full Smart Outbound Framework for them: AI-targeted lists, personalised cold email and LinkedIn outreach working side by side, and every opportunity tracked through to pipeline.",
            stats=[("$1.2M", "in pipeline opportunity value"), ("10,000+", "prospects reached by email"),
                   ("Up to 94%", "email open rate"), ("669", "email replies, up to 6.7% reply rate"),
                   ("26%", "LinkedIn connection acceptance"), ("76", "replies from LinkedIn outreach")],
            parts=[dict(label="Email", title="Cold email that gets opened and answered",
                        text="Across two campaigns we reached more than 10,000 prospects. Strong deliverability and targeting kept open rates between 89% and 94%, and personalised sequences generated 669 replies, with the larger campaign reaching a 6.7% reply rate.",
                        images=[("email", 1600, 1067, "Email campaign analytics: 94% and 89% open rates, 5.8% and 6.7% reply rates")]),
                   dict(label="LinkedIn", title="LinkedIn outreach alongside email",
                        text="In parallel, LinkedIn campaigns reached the same kind of decision-makers from a second angle. 715 connection requests led to 187 new connections, a 26% acceptance rate, and 76 replies from 267 messages sent.",
                        images=[("linkedin", 1000, 540, "LinkedIn outreach statistics: 187 accepted connections and 76 replies")]),
                   dict(label="Pipeline", title="Replies turned into real pipeline",
                        text="Every positive reply was followed up and tracked, so outbound activity showed up where it matters: $1.2M in opportunity value across Aktive Clients' pipelines.",
                        images=[("pipeline", 1042, 208, "Opportunity value across all pipelines: $1.2M")])]),
        case=None, quotes=[],
        faq=[("Will cold email hurt our domain reputation?", "No. We send from separate, properly warmed domains and keep volumes within safe limits, so your main domain stays protected."),
             ("Why use email and LinkedIn together?", "Prospects who see you in more than one place are more likely to reply. Running both channels also means you're not dependent on a single platform."),
             ("Who writes the messages?", "We do, based on your input and our research. You approve the messaging before anything goes out."),
             ("How soon will we see replies?", "Once infrastructure is warmed up, most campaigns start producing replies within the first few weeks after launch.")],
    ),
    dict(
        slug="social-media-brand-growth", tone="brand",
        name="Social Media & Brand Growth", title_a="Social media that", title_b="grows your brand",
        icon='<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6"/>',
        summary="Done-for-you social media growth: competitor analysis, content ideation, management and weekly and monthly reporting across LinkedIn, Instagram and Facebook.",
        intro="We grow brands on social media from scratch. From competitor analysis and content ideation to daily management and clear weekly and monthly reporting, we handle everything, so your brand shows up consistently, builds an audience and turns attention into customers.",
        best_for=["B2B and product brands with little or inconsistent social presence",
                  "Teams that want to grow an audience without hiring in-house",
                  "Founders who want a brand that looks as strong as their product"],
        glance=dict(stats=[("Millions", "of impressions and views across our clients' channels"),
                           ("31K+", "combined followers across the brands we manage"),
                           ("704K", "views on a single Instagram reel"),
                           ("3", "platforms: LinkedIn, Instagram and Facebook")],
                    platforms=["LinkedIn", "Instagram", "Facebook"]),
        pillars_intro="Every brand we grow follows the same proven path, built from scratch around your market and audience.",
        pillars=[("Research", "Competitor and audience analysis.",
                  "We study your competitors, audience and platforms to find the content gaps and angles that will make your brand stand out."),
                 ("Create", "Content ideation and production.",
                  "We plan and produce posts, carousels and reels that educate, entertain and sell, all in your brand's voice and visual style."),
                 ("Grow & report", "Management with clear numbers.",
                  "We publish consistently, manage your channels and send weekly and monthly reports showing exactly what's growing and why.")],
        included=[("Competitor & audience analysis", "A clear picture of what works in your market and where your brand can win."),
                  ("Brand positioning & content strategy", "Content pillars, tone of voice and a plan built around your goals."),
                  ("Content ideation & creation", "Posts, carousels, reels and graphics designed and written for each platform."),
                  ("Social media management", "Scheduling, publishing and channel management handled end to end."),
                  ("Weekly & monthly reporting", "Reach, engagement, follower growth and what we're changing next."),
                  ("Ongoing optimisation", "We double down on the formats and topics that perform and drop what doesn't.")],
        steps=[("Audit & research", "We review your current channels, competitors and audience."),
               ("Strategy & content plan", "You get a content strategy and calendar tailored to each platform."),
               ("Create & publish", "We produce and publish content consistently, with your approval."),
               ("Report & optimise", "Weekly and monthly reports show results, and we keep improving.")],
        case_list_intro="Three brands, three platforms, built from scratch. Click through to see their channels live.",
        case_list=[
            dict(name="OERP Canada", logo="oerp-canada.webp", w=167, h=40, logo_class="h-9 w-auto", platform="LinkedIn",
                 url="https://www.linkedin.com/company/oerp-canada/", industry="IT services & ERP consulting · Odoo Gold Partner",
                 title="A LinkedIn presence that builds B2B trust",
                 body="For OERP Canada, an Odoo Gold Partner helping Canadian businesses run on ERP, we built a LinkedIn content engine that showcases their expertise, team and client results, strengthening brand visibility with the decision-makers they sell to.",
                 stats=[("148.7K", "impressions in 12 months"), ("2,826", "reactions"), ("2.9K", "followers")],
                 image=("social/oerp", 1600, 1200, "OERP Canada's LinkedIn company page and 12-month analytics: 148,750 impressions, 2,826 reactions and 172 comments")),
            dict(name="ParcelABC", logo="parcelabc.webp", w=169, h=39, logo_class="h-9 w-auto", platform="Facebook",
                 url="https://www.facebook.com/parcelabc", industry="Shipping & logistics platform",
                 title="From quiet page to 16K followers",
                 body="We grew ParcelABC's Facebook from scratch with educational carousels, carrier comparisons and promotional campaigns. Reach more than doubled and the page started bringing in inbound leads, not just likes.",
                 stats=[("16K", "Facebook followers"), ("287", "posts published"), ("2×", "reach, more than doubled")],
                 image=("social/parcelabc", 1600, 1200, "ParcelABC's Facebook page with 16K followers and 287 posts")),
            dict(name="Sonr Music", logo="sonr-music.webp", w=180, h=180, logo_class="h-14 w-14 rounded-full ring-1 ring-line", platform="Instagram",
                 url="https://www.instagram.com/sonr.music/", industry="Consumer electronics · waterproof music player",
                 title="Reels that made a product go viral",
                 body="Sonr makes a waterproof music player for swimmers. We built a reel-first Instagram strategy that shows the product in action in the pool, turning a niche product into scroll-stopping content that has generated millions of views across all reels.",
                 stats=[("704K", "views on the top reel"), ("Millions", "of views across all reels"), ("12.6K", "Instagram followers")],
                 image=("social/sonr", 1600, 1200, "Sonr Music's Instagram profile with 12.6K followers and reels with up to 704K views")),
        ],
        case=None, quotes=[],
        faq=[("Do you really start from scratch?", "Yes. Many of the brands we work with had little or no social presence. We start with competitor and audience analysis and build the strategy, content and channels from there."),
             ("Which platforms do you manage?", "LinkedIn, Instagram and Facebook. We recommend the platforms where your buyers actually spend time rather than trying to be everywhere."),
             ("Who creates the content?", "We do: ideation, copy and design. You review and approve before anything goes live, and we keep it in your brand's voice."),
             ("How do you report results?", "You get weekly updates and a monthly report covering reach, engagement, follower growth and leads, plus what we're changing next.")],
    ),
    dict(
        slug="ai-search-visibility", tone="sky",
        name="AI Search Visibility", title_a="Get recommended by", title_b="ChatGPT, Gemini and Google AI",
        icon='<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/><path d="M11 8v6M8 11h6"/>',
        summary="Generative engine optimisation (GEO) and answer engine optimisation (AEO) that make your brand the answer AI assistants and Google AI Overviews recommend.",
        intro="Your buyers now ask ChatGPT, Gemini, Perplexity and Google's AI Overviews before they ever visit a website. We optimise your site, content and brand signals so AI engines understand what you do, trust it, and recommend you when it matters.",
        best_for=["B2B companies whose buyers research with ChatGPT and Google AI",
                  "Brands with strong SEO that rarely appear in AI answers",
                  "Teams that want to stay ahead as search shifts from links to answers"],
        glance=dict(label="Why AI search matters now",
                    stats=[("25%", "forecast drop in traditional search volume by 2026"),
                           ("800M+", "people use ChatGPT every week"),
                           ("2B+", "monthly users see Google AI Overviews"),
                           ("+23 pts", "AEO score gained for OERP Canada")],
                    note='Sources: Gartner, Feb 2024 · OpenAI, Oct 2025 · Google, Jul 2025.'),
        pillars_intro="AI engines decide who to recommend based on how clearly they can read, trust and cite you. We improve all three.",
        pillars=[("Make it readable", "Technical and structured data.",
                  "Schema markup, clean metadata and AI-crawler access so engines like ChatGPT and Gemini can parse exactly who you are and what you offer."),
                 ("Make it quotable", "Answer-ready content.",
                  "Clear, factual pages and FAQs written in the question-and-answer format AI engines prefer to cite, with the stats and specifics they look for."),
                 ("Make it trusted", "Authority and brand signals.",
                  "Consistent entity information, reviews, mentions and third-party citations that give AI engines the confidence to recommend you over competitors.")],
        included=[("AI visibility audit", "AEO and GEO scoring of your key pages, plus how often AI assistants mention you versus competitors."),
                  ("Structured data & schema", "Organisation, service, FAQ and review markup that helps AI engines understand your business."),
                  ("Metadata & technical fixes", "Titles, descriptions, crawlability and AI-crawler access tuned for answer engines."),
                  ("Answer-ready content", "Pages and FAQs rewritten to answer the questions your buyers actually ask AI."),
                  ("Brand & citation building", "Consistent business information and mentions across the sources AI engines trust."),
                  ("Monthly visibility tracking", "Score changes and AI mentions across ChatGPT, Gemini, Perplexity and Google AI Overviews.")],
        steps=[("Audit", "We score your key pages for AEO and GEO and test how AI assistants describe your brand today."),
               ("Prioritise", "You get a clear list of fixes, ranked by impact on AI visibility."),
               ("Optimise", "We implement structured data, metadata and content improvements."),
               ("Measure & expand", "We re-score, track AI mentions monthly and extend the work across your site.")],
        case_detail=dict(
            logo="oerp-canada", name="OERP Canada", w=167, h=40,
            title="How OERP Canada raised its AI search scores by up to 23 points",
            body="OERP Canada, an Odoo Gold Partner with 14+ years of experience, 200+ projects delivered and a 4.9/5 Google rating, had all the credibility buyers look for. But its homepage wasn't structured for AI engines to read and cite it. We focused on the page-level signals AI search relies on: structured data, metadata and content.",
            stats=[("53 → 76", "AEO score out of 100"), ("64 → 82", "GEO score out of 100"),
                   ("+43%", "improvement in AEO score"), ("+28%", "improvement in GEO score")],
            parts=[dict(label="Starting point", title="Strong credentials, weak AI signals",
                        text="OERP's homepage already showed real proof: 14+ years of Odoo expertise, 200+ projects and a 4.9/5 rating. But AI engines struggled to extract it. Before our work, the homepage scored 53/100 for answer engine optimisation (AEO) and 64/100 for generative engine optimisation (GEO).",
                        images=[("homepage", 1546, 1106, "OERP Canada's homepage: Best Odoo Gold Partner in North America")]),
                   dict(label="Result", title="Clearer signals, higher scores", stack=True,
                        text="We improved the homepage's structured data, metadata and content so AI engines can understand who OERP serves, what they offer and why they're trusted. The AEO score rose from 53 to 76 and the GEO score from 64 to 82, putting the homepage solidly in the green on both.",
                        images=[("before", 1600, 427, "Before: AEO score 53/100, GEO score 64/100"),
                                ("after", 1600, 427, "After: AEO score 76/100, GEO score 82/100")])]),
        case=None, quotes=[],
        faq=[("What's the difference between SEO, AEO and GEO?", "SEO helps you rank in search results. AEO (answer engine optimisation) helps your content get pulled into direct answers, and GEO (generative engine optimisation) helps AI assistants like ChatGPT and Gemini understand, trust and recommend your brand."),
             ("Does this replace SEO?", "No, it builds on it. Strong SEO foundations help, but AI engines also need structured, quotable and consistent information to cite you."),
             ("Which AI platforms do you optimise for?", "ChatGPT, Gemini, Perplexity, Claude and Google AI Overviews. The fundamentals that help one engine understand you help them all."),
             ("How do you measure results?", "We score your pages for AEO and GEO before and after, and track how often and how accurately AI assistants mention your brand each month.")],
    ),
    dict(
        slug="website-design-development", tone="sky",
        name="Website Design & Development", title_a="A website that sells,", title_b="live in days, not months",
        icon='<rect x="2" y="3" width="20" height="16" rx="2"/><path d="M2 8h20M6 5.5h.01M9 5.5h.01"/>',
        summary="Custom, conversion-focused websites designed, written and launched in 1 to 5 days, with SEO and AI-search foundations built in.",
        intro="Your website is often the first thing a buyer checks before they book a call. We design, write and build custom websites that look premium, load fast and turn visitors into leads, and most go live in just 1 to 5 days.",
        best_for=["Startups and growing companies that need a premium website fast",
                  "Businesses whose current site looks dated or doesn't convert",
                  "Teams launching a new product, brand or market"],
        glance=dict(label="Website building at a glance",
                    stats=[("1–5 days", "from kickoff to a live website"),
                           ("6", "industries, from SaaS to home services"),
                           ("100%", "custom design, no generic templates"),
                           ("Mobile-first", "responsive on every screen size")]),
        pillars_intro="Speed doesn't mean shortcuts. Every site goes through the same focused process, compressed into days instead of months.",
        pillars=[("Strategy & copy", "Built to convert, not just to look good.",
                  "We map your audience, offer and goals, then write clear copy and structure every page around one job: turning visitors into leads."),
                 ("Design & build", "Custom, fast and responsive.",
                  "A design made for your brand, built to load fast and look sharp on phones, tablets and desktops."),
                 ("Launch & grow", "Ready to rank and capture leads.",
                  "SEO and AI-search foundations, analytics, booking and contact integrations, all set up before launch so your site starts working on day one.")],
        included=[("Custom design", "A unique look built around your brand, never a generic template."),
                  ("Conversion copywriting", "Clear headlines, proof and calls to action that move visitors to act."),
                  ("Responsive development", "Fast, mobile-first pages that work beautifully on every device."),
                  ("SEO & AI-search foundations", "Metadata, structured data and clean structure so Google and AI assistants understand your site."),
                  ("Integrations", "Booking calendars, contact forms, CRM, WhatsApp and analytics connected and tested."),
                  ("Launch & handover", "Domain, hosting and launch handled, plus a walkthrough so your team can update it.")],
        steps=[("Kickoff", "A short call to align on your goals, audience, offer and the look you want."),
               ("Design & copy", "We create the design and write the copy, and you review it quickly."),
               ("Build", "We develop the site, connect integrations and test it on every device."),
               ("Launch", "Your site goes live, typically within 1 to 5 days of kickoff.")],
        portfolio_intro="From crypto platforms to cleaning services, here are some of the websites we've designed and built. Click any of them to see it live.",
        portfolio=[
            dict(name="ABUZA", industry="Digital assets & crypto", url="https://www.abuza.pro/", image="abuza",
                 text="A premium, market-terminal style platform with live-style charts, wallet connection and a dark, cinematic design."),
            dict(name="Alkahf Technologies", industry="IT services · UAE", url="https://www.alkahf.ae/", image="alkahf",
                 text="A bold, modern site for a UAE technology company offering Tally software, cloud solutions, IT support and development."),
            dict(name="Mavuus", industry="CMO community & membership", url="https://www.mavuus.com/", image="mavuus",
                 text="A warm, community-led website helping CMOs connect and grow, with clear paths to join or hire a fractional CMO."),
            dict(name="Sparkling Cleaner Services", industry="Home & commercial cleaning", url="https://www.sparklingcleanerservicesd.com/", image="sparkling",
                 text="A fresh, trustworthy service-business site with clear services, testimonials and one-tap WhatsApp contact."),
            dict(name="Keeyora", industry="B2B SaaS · talent texting", url="https://www.keeyora.com/", image="keeyora",
                 text="A bright, product-led SaaS website that explains AI-powered candidate messaging in seconds."),
            dict(name="iWave Digital", industry="AI growth & marketing agency", url="https://www.iwave.digital/", image="iwave", badge="You're here",
                 text="Our own website: the one you're browsing right now, built with the same process we use for clients."),
        ],
        case=None, quotes=[],
        faq=[("Can you really build a website in 1 to 5 days?", "Yes. Most of our websites go live within 1 to 5 days of kickoff. Simpler sites can launch in a single day, and larger sites with more pages or integrations take closer to five."),
             ("Do you write the content too?", "Yes. We write conversion-focused copy based on a short kickoff call, so you don't have to start from a blank page. You review and approve everything before launch."),
             ("Will I be able to update the site myself?", "Yes. We hand over a site your team can edit, plus a walkthrough of how to make common updates."),
             ("Is the website optimised for Google and AI search?", "Every site includes SEO and AI-search foundations like metadata, structured data and clean page structure. For deeper optimisation, pair it with our AI Search Visibility service.")],
    ),
    dict(
        slug="growth-ai-advisory", tone="sky",
        name="Growth & AI Advisory", title_a="Build growth in-house,", title_b="with experts in your corner",
        icon='<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
        summary="Hands-on marketing and AI advisory for teams that want to run growth themselves: strategy, tools, copywriting, AI frameworks and automations, with as many calls as you need.",
        intro="Want to build marketing and AI capabilities inside your own team? We advise you on the strategies, tools and copy that work, and hand you ready-to-use AI frameworks, tools and automations, so your team has everything it needs to get going, with expert support on call whenever you need it.",
        best_for=["Teams that want to run marketing and AI in-house, with expert guidance",
                  "Founders and marketing leads unsure which tools and strategies to invest in",
                  "Companies starting with AI that want proven frameworks, not trial and error"],
        glance=dict(label="Advisory backed by real results",
                    stats=[("$5M+", "revenue generated for our clients"),
                           ("15+", "industries we've worked across"),
                           ("5+ years", "of hands-on AI and marketing"),
                           ("Unlimited", "advisory calls, as many as you need")]),
        pillars_intro="Two sides of growth, one team of advisors, and ongoing support so the work actually sticks.",
        pillars=[("Marketing advisory", "Strategy, tools and copy.",
                  "We help you choose the right channels, strategies and tools, review and improve your copywriting, and build a plan your team can execute."),
                 ("AI enablement", "Frameworks, tools and automations.",
                  "You get ready-to-use AI frameworks, tool recommendations, automation drafts and prompts, tailored to how your team actually works."),
                 ("Ongoing support", "Calls whenever you need them.",
                  "We stay on call as your team puts things into practice, with as many sessions as you need to get unstuck and keep moving.")],
        included=[("Marketing strategy & roadmap", "A clear plan covering channels, priorities and what to do first."),
                  ("Tool stack recommendations", "Honest advice on the marketing and AI tools worth paying for, and which to skip."),
                  ("Copywriting reviews", "Feedback and rewrites for your website, outreach, ads and content."),
                  ("AI frameworks & prompt library", "Proven frameworks and prompts your team can use from day one."),
                  ("AI tools & automation drafts", "Ready-to-adapt automations and workflows for marketing and sales tasks."),
                  ("Unlimited advisory calls", "Book as many sessions as you need while your team gets up and running.")],
        steps=[("Discovery call", "We learn your goals, team, current tools and where you're stuck."),
               ("Audit & roadmap", "We review your marketing and AI setup and map the highest-impact next steps."),
               ("Toolkit & sessions", "You get frameworks, tools, automation drafts and copy feedback, plus working sessions with your team."),
               ("Run it in-house", "Your team executes with confidence, and we stay on call whenever you need us.")],
        advisors_intro="You'll work directly with the people who build growth and AI systems for our clients every day.",
        advisors=[("nick", "Nick Gheorghita", "Founder & Head of Growth", "Marketing strategy, LinkedIn and outbound, copywriting and go-to-market."),
                  ("alex", "Alex Georgiu", "Co-Founder & Head of AI", "AI frameworks, tools and automations that save your team time."),
                  ("lina", "Lina Boicu", "Head of Content & Creativity", "Content strategy, social media and creative direction for your brand.")],
        case=None, quotes=[],
        faq=[("Who is advisory for?", "Teams that want to build marketing and AI capabilities in-house rather than outsource everything, from founders doing it themselves to marketing teams looking for an expert sounding board."),
             ("How many calls are included?", "As many as you need. We don't cap sessions, because the goal is for your team to get up and running with confidence."),
             ("What do we actually get?", "A marketing roadmap, tool recommendations, copywriting feedback, plus AI frameworks, prompts, tools and automation drafts your team can use right away."),
             ("Can you also implement things for us?", "Yes. If you'd rather hand parts of the work over, our other services like the LinkedIn Client Acquisition System or Smart Outbound Framework cover done-for-you execution.")],
    ),
]


def tone_classes(tone):
    return ("bg-brand-soft text-brand", "text-brand") if tone == "brand" else ("bg-sky-soft text-sky-dark", "text-sky-dark")


def icon_svg(inner, size=22):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{inner}</svg>'


def e(text):
    return escape(text, quote=True)


def header():
    home = "../index.html"
    links = [("Work", "#work"), ("About us", "#about"), ("Services", "#services"), ("Process", "#process"), ("Team", "#team"), ("FAQs", "#faq")]
    def nav_item(t, h):
        active = t == "Services"
        cls = "bg-white text-ink shadow-sm" if active else "text-muted"
        current = ' aria-current="true"' if active else ""
        return f'          <li><a href="{home}{h}" class="nav-link block rounded-full px-4 py-2 transition hover:text-ink {cls}"{current}>{t}</a></li>'
    desk = "\n".join(nav_item(t, h) for t, h in links)
    mob = "\n".join(f'        <li><a href="{home}{h}" class="block border-b border-line py-3">{t}</a></li>' for t, h in links)
    return f'''  <header id="top" class="sticky top-0 z-50 transition-colors" data-header>
    <div class="mx-auto flex max-w-site items-center justify-between gap-4 px-4 py-4 sm:px-6 lg:px-8">
      <a href="{home}" class="flex shrink-0 items-center">
        <img src="../assets/iwave-logo.png" alt="iWave Digital" width="101" height="48" class="h-10 w-auto sm:h-12" />
      </a>
      <nav aria-label="Primary" class="hidden lg:block">
        <ul class="flex items-center rounded-full border border-line bg-surface/80 p-1 text-[15px] backdrop-blur">
{desk}
        </ul>
      </nav>
      <div class="flex items-center gap-2">
        <a href="https://cal.com/iwave-digital/discovery-call" target="_blank" rel="noopener" class="group hidden items-center gap-3 rounded-full bg-ink py-1.5 pl-5 pr-1.5 text-[15px] font-medium text-white transition hover:bg-brand sm:inline-flex">
          Book a call
          <span class="flex h-9 w-9 items-center justify-center rounded-full bg-white text-ink transition group-hover:rotate-45" aria-hidden="true">{ARROW.format(s=14)}</span>
        </a>
        <button type="button" class="flex h-11 w-11 items-center justify-center rounded-full border border-line bg-white lg:hidden" aria-controls="mobile-menu" aria-expanded="false" aria-label="Open menu" data-menu-btn>
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
      </div>
    </div>
    <div id="mobile-menu" class="hidden border-t border-line bg-white px-4 pb-6 pt-2 lg:hidden" data-menu>
      <ul class="flex flex-col text-lg">
{mob}
      </ul>
      <a href="https://cal.com/iwave-digital/discovery-call" target="_blank" rel="noopener" class="mt-5 flex items-center justify-center rounded-full bg-ink py-3.5 font-medium text-white">Book a call</a>
    </div>
  </header>'''


def footer():
    home = "../index.html"
    links = [("Work", "#work"), ("About", "#about"), ("Services", "#services"), ("Process", "#process"), ("Team", "#team"), ("FAQs", "#faq"), ("Contact", "#contact")]
    items = "\n".join(f'          <li><a href="{home}{h}" class="hover:text-ink">{t}</a></li>' for t, h in links)
    return f'''  <footer class="border-t border-line">
    <div class="mx-auto flex max-w-site flex-col gap-8 px-4 py-12 sm:px-6 md:flex-row md:items-center md:justify-between lg:px-8">
      <div>
        <a href="{home}" class="inline-flex">
          <img src="../assets/iwave-logo.png" alt="iWave Digital" width="101" height="48" class="h-12 w-auto" loading="lazy" />
        </a>
        <p class="mt-3 max-w-xs text-[15px] text-muted">The AI growth and marketing partner for fast-moving B2B companies.</p>
      </div>
      <nav aria-label="Footer">
        <ul class="flex flex-wrap gap-x-6 gap-y-2 text-[15px] text-muted">
{items}
        </ul>
      </nav>
    </div>
    <div class="mx-auto max-w-site px-4 pb-10 text-sm text-muted sm:px-6 lg:px-8">© <span data-year></span> iWave Digital. All rights reserved.</div>
  </footer>'''


def case_card(key):
    c = CASES[key]
    return f'''          <article class="grid overflow-hidden rounded-3xl border border-line bg-white md:grid-cols-[0.9fr_1.1fr]">
            <div class="relative flex min-h-[240px] flex-col justify-end overflow-hidden {c["bg"]} p-8 text-white">
              <div class="absolute -right-16 -top-16 h-56 w-56 rounded-full bg-sky/50 blur-2xl" aria-hidden="true"></div>
              <p class="relative text-6xl font-semibold tracking-tight sm:text-7xl">{c["metric"]}</p>
              <p class="relative mt-1 text-white/85">{e(c["label"])}</p>
            </div>
            <div class="flex flex-col justify-center p-8 sm:p-10">
              <img src="../assets/logos/{c["logo"]}.webp" alt="{e(c["name"])}" width="{c["w"]}" height="{c["h"]}" class="h-8 w-auto self-start" loading="lazy" />
              <h3 class="mt-6 text-2xl font-semibold tracking-tight">{e(c["title"])}</h3>
              <p class="mt-3 leading-relaxed text-muted">{e(c["body"])}</p>
            </div>
          </article>'''


def avatar(key, name):
    if (ROOT / "assets" / "testimonials" / f"{key}.webp").exists():
        return f'<img src="../assets/testimonials/{key}.webp" alt="" width="40" height="40" class="h-10 w-10 shrink-0 rounded-full object-cover" loading="lazy" />'
    initials = "".join(w[0] for w in name.split()[:2])
    return f'<span class="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-brand-soft text-sm font-semibold text-brand" aria-hidden="true">{initials}</span>'


def quote_card(key):
    name, role, text = TESTIMONIALS[key]
    return f'''          <figure class="flex flex-col justify-between rounded-3xl border border-line bg-white p-8 shadow-lg shadow-brand/10">
            <blockquote class="leading-relaxed">{e(text)}</blockquote>
            <figcaption class="mt-6 flex items-center gap-3">
              {avatar(key, name)}
              <span><span class="block font-semibold leading-5 tracking-tight">{e(name)}</span><span class="mt-0.5 block text-sm leading-5 text-muted">{e(role)}</span></span>
            </figcaption>
          </figure>'''


def pillars_section(svc):
    if not svc.get("pillars"):
        return ""
    serif = '<span class="font-serif font-normal italic">'
    cards = "\n".join(f'''          <li class="flex flex-col rounded-3xl border border-line bg-white p-8">
            <span class="font-serif text-5xl italic text-brand">{i:02d}</span>
            <h3 class="mt-6 text-xl font-semibold tracking-tight">{e(t)}</h3>
            <p class="mt-1 font-medium text-ink/80">{e(sub)}</p>
            <p class="mt-4 leading-relaxed text-muted">{e(d)}</p>
          </li>''' for i, (t, sub, d) in enumerate(svc["pillars"], 1))
    return f'''
    <!-- ============ SYSTEM ============ -->
    <section class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl">
          <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">The {len(svc["pillars"])}-part system {serif}behind it</span></h2>
          <p class="mt-5 text-lg leading-relaxed text-muted">{e(svc.get("pillars_intro", ""))}</p>
        </div>
        <ol class="mt-12 grid gap-5 lg:grid-cols-3">
{cards}
        </ol>
      </div>
    </section>
'''


def case_detail_section(svc):
    c = svc.get("case_detail")
    if not c:
        return ""
    serif = '<span class="font-serif font-normal italic">'
    stats = "\n".join(f'''            <div class="rounded-2xl bg-surface p-5">
              <dd class="text-3xl font-semibold tracking-tight sm:text-4xl">{e(v)}</dd>
              <dt class="mt-1 text-sm text-muted">{e(l)}</dt>
            </div>''' for v, l in c["stats"])
    def fig(f, w, h, cap):
        return f'''              <figure>
                <div class="overflow-hidden rounded-2xl border border-line bg-white shadow-lg shadow-brand/10">
                  <img src="../assets/case-studies/{c["logo"]}/{f}.webp" alt="{e(cap)}" width="{w}" height="{h}" class="w-full" loading="lazy" />
                </div>
                <figcaption class="mt-3 text-sm text-muted">{e(cap)}</figcaption>
              </figure>'''
    def part(i, pt):
        flip = "lg:order-last" if i % 2 else ""
        grid = "lg:grid-cols-[1.2fr_0.8fr]" if i % 2 else "lg:grid-cols-[0.8fr_1.2fr]"
        cols = "sm:grid-cols-2" if len(pt["images"]) > 1 and not pt.get("stack") else ""
        figs = "\n".join(fig(*im) for im in pt["images"])
        return f'''          <div class="grid items-center gap-10 rounded-3xl bg-surface p-6 sm:p-10 {grid} lg:gap-14">
            <div class="{flip}">
              <span class="inline-flex rounded-full bg-brand-soft px-3 py-1 text-sm font-medium text-brand">{e(pt["label"])}</span>
              <h4 class="mt-5 text-2xl font-semibold tracking-tight">{e(pt["title"])}</h4>
              <p class="mt-4 leading-relaxed text-muted">{e(pt["text"])}</p>
            </div>
            <div class="grid items-start gap-6 {cols}">
{figs}
            </div>
          </div>'''
    imgs = "\n".join(part(i, pt) for i, pt in enumerate(c["parts"]))
    quote_html = ""
    if c.get("quote"):
        name, role, text = TESTIMONIALS[c["quote"]]
        quote_html = f'''
            <figure class="mt-8 border-l-2 border-brand pl-5">
              <blockquote class="font-serif text-2xl leading-snug">“{e(text)}”</blockquote>
              <figcaption class="mt-4 flex items-center gap-3">
                {avatar(c["quote"], name)}
                <span><span class="block font-semibold leading-5">{e(name)}</span><span class="mt-0.5 block text-sm leading-5 text-muted">{e(role)}</span></span>
              </figcaption>
            </figure>'''
    return f'''
    <!-- ============ CASE STUDY ============ -->
    <section id="case-study" class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">Case {serif}study</span></h2>
        <div class="mt-12 grid gap-10 lg:grid-cols-[1.1fr_1fr] lg:gap-16">
          <div>
            <img src="../assets/logos/{c["logo"]}.webp" alt="{e(c["name"])}" width="{c["w"]}" height="{c["h"]}" class="{c.get("logo_class", "h-9")} w-auto" loading="lazy" />
            <h3 class="mt-6 text-2xl font-semibold tracking-tight sm:text-3xl">{e(c["title"])}</h3>
            <p class="mt-4 text-lg leading-relaxed text-muted">{e(c["body"])}</p>{quote_html}
          </div>
          <dl class="grid grid-cols-2 content-start gap-3">
{stats}
          </dl>
        </div>
        <div class="mt-14 space-y-6">
{imgs}
        </div>
      </div>
    </section>
'''


def offers_section(svc):
    offers = svc.get("offers")
    if not offers:
        return ""
    serif = '<span class="font-serif font-normal italic">'
    def card(o):
        dark = o["featured"]
        wrap = "bg-ink text-white" if dark else "border border-line bg-white"
        sub = "text-white/70" if dark else "text-muted"
        tag = "bg-white/10 text-white" if dark else "bg-brand-soft text-brand"
        tick = "bg-white text-ink" if dark else "bg-brand text-white"
        btn = "bg-white text-ink hover:bg-brand hover:text-white" if dark else "bg-ink text-white hover:bg-brand"
        dot = "bg-ink text-white group-hover:bg-white group-hover:text-ink" if dark else "bg-white text-ink"
        items = "\n".join(f'              <li class="flex gap-3"><span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full {tick}" aria-hidden="true">{CHECK}</span><span>{e(i)}</span></li>' for i in o["items"])
        return f'''          <article class="relative flex flex-col overflow-hidden rounded-3xl p-8 sm:p-10 {wrap}">
            {'<div class="glow -right-24 -top-24 h-72 w-72 bg-brand/50" aria-hidden="true"></div>' if dark else ""}
            <div class="relative flex flex-1 flex-col">
              <span class="self-start rounded-full px-3 py-1 text-sm font-medium {tag}">{e(o["tag"])}</span>
              <h3 class="mt-6 text-2xl font-semibold tracking-tight sm:text-3xl">{e(o["name"])}</h3>
              <p class="mt-3 leading-relaxed {sub}">{e(o["text"])}</p>
              <ul class="mt-8 space-y-3">
{items}
              </ul>
              <a href="{BOOKING_URL}" target="_blank" rel="noopener" class="group mt-10 inline-flex items-center gap-4 self-start rounded-full py-2 pl-6 pr-2 font-medium transition {btn}">
                {e(o["cta"])}
                <span class="flex h-10 w-10 items-center justify-center rounded-full transition group-hover:rotate-45 {dot}" aria-hidden="true">{ARROW.format(s=14)}</span>
              </a>
            </div>
          </article>'''
    cards = "\n".join(card(o) for o in offers)
    return f'''
    <!-- ============ OFFERS ============ -->
    <section id="pricing" class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl">
          <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">Two ways to {serif}work with us</span></h2>
          <p class="mt-5 text-lg leading-relaxed text-muted">Book a free LinkedIn audit to see if working together makes sense. You'll walk away with something useful either way.</p>
        </div>
        <div class="mt-12 grid gap-6 lg:grid-cols-2">
{cards}
        </div>
      </div>
    </section>
'''


PLATFORM_ICONS = {
    "LinkedIn": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
    "Instagram": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6"/>',
    "Facebook": '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
}


def glance_section(svc):
    g = svc.get("glance")
    if not g:
        return ""
    items = "\n".join(f'''          <div class="py-6 sm:py-7 {"lg:border-l lg:border-line lg:pl-8" if i else ""}">
            <dd class="text-3xl font-semibold tracking-tight sm:text-4xl">{e(v)}</dd>
            <dt class="mt-1 text-sm text-muted">{e(l)}</dt>
          </div>''' for i, (v, l) in enumerate(g["stats"]))
    chips = "".join(f'<li class="inline-flex items-center gap-2 rounded-full border border-line bg-white px-3 py-1.5 text-sm font-medium"><span class="text-brand" aria-hidden="true">{icon_svg(PLATFORM_ICONS[p], 16)}</span>{p}</li>' for p in g.get("platforms", []))
    platforms = f'''
        <div class="flex flex-wrap items-center gap-3 border-t border-line py-5 text-sm text-muted">
          <span>{e(g.get("platforms_label", "Platforms we grow"))}</span>
          <ul class="flex flex-wrap gap-2 text-ink">{chips}</ul>
        </div>''' if chips else ""
    note = f'\n        <p class="border-t border-line py-4 text-xs leading-relaxed text-muted">{g["note"]}</p>' if g.get("note") else ""
    return f'''
    <!-- ============ AT A GLANCE ============ -->
    <section aria-label="{e(g.get("label", "Results at a glance"))}" class="border-y border-line bg-surface">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <dl class="grid grid-cols-2 gap-x-6 lg:grid-cols-4">
{items}
        </dl>{platforms}{note}
      </div>
    </section>
'''


def case_list_section(svc):
    cases = svc.get("case_list")
    if not cases:
        return ""
    serif = '<span class="font-serif font-normal italic">'
    def row(i, c):
        flip = "lg:order-last" if i % 2 else ""
        cols = "lg:grid-cols-[1.15fr_0.85fr]" if i % 2 else "lg:grid-cols-[0.85fr_1.15fr]"
        stats = "\n".join(f'''                <div>
                  <dd class="text-2xl font-semibold tracking-tight sm:text-3xl">{e(v)}</dd>
                  <dt class="mt-1 text-sm leading-snug text-muted">{e(l)}</dt>
                </div>''' for v, l in c["stats"])
        logo_cls = c.get("logo_class", "h-9 w-auto")
        f, w, h, alt = c["image"]
        return f'''          <article class="grid items-center gap-10 rounded-3xl bg-surface p-6 sm:p-10 {cols} lg:gap-12">
            <div class="{flip}">
              <div class="flex flex-wrap items-center gap-4">
                <img src="../assets/logos/{c["logo"]}" alt="{e(c["name"])}" width="{c["w"]}" height="{c["h"]}" class="{logo_cls}" loading="lazy" />
                <span class="inline-flex items-center gap-1.5 rounded-full bg-brand-soft px-3 py-1 text-sm font-medium text-brand"><span aria-hidden="true">{icon_svg(PLATFORM_ICONS[c["platform"]], 14)}</span>{e(c["platform"])}</span>
              </div>
              <p class="mt-6 text-sm font-medium text-muted">{e(c["industry"])}</p>
              <h3 class="mt-1 text-2xl font-semibold tracking-tight sm:text-3xl">{e(c["title"])}</h3>
              <p class="mt-4 leading-relaxed text-muted">{e(c["body"])}</p>
              <dl class="mt-8 grid grid-cols-3 gap-4 border-t border-line pt-6">
{stats}
              </dl>
              <a href="{c["url"]}" target="_blank" rel="noopener" class="group mt-8 inline-flex items-center gap-2 rounded-full border border-line bg-white px-5 py-2.5 text-[15px] font-medium transition hover:border-brand hover:text-brand">
                View {e(c["name"])} on {e(c["platform"])}
                <span class="transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5" aria-hidden="true">{ARROW.format(s=14)}</span>
                <span class="sr-only">(opens in a new tab)</span>
              </a>
            </div>
            <div class="overflow-hidden rounded-2xl">
              <img src="../assets/case-studies/{f}.webp" alt="{e(alt)}" width="{w}" height="{h}" class="w-full" loading="lazy" />
            </div>
          </article>'''
    rows = "\n".join(row(i, c) for i, c in enumerate(cases))
    return f'''
    <!-- ============ CASE STUDIES ============ -->
    <section id="case-studies" class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl">
          <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">Brands we've {serif}grown</span></h2>
          <p class="mt-5 text-lg leading-relaxed text-muted">{e(svc.get("case_list_intro", ""))}</p>
        </div>
        <div class="mt-12 space-y-6">
{rows}
        </div>
      </div>
    </section>
'''


def portfolio_section(svc):
    items = svc.get("portfolio")
    if not items:
        return ""
    serif = '<span class="font-serif font-normal italic">'
    def card(it):
        domain = it["url"].split("//", 1)[-1].rstrip("/").removeprefix("www.")
        badge = f'<span class="rounded-full bg-brand px-2.5 py-0.5 text-xs font-medium text-white">{e(it["badge"])}</span>' if it.get("badge") else ""
        return f'''          <a href="{it["url"]}" target="_blank" rel="noopener" class="group flex flex-col overflow-hidden rounded-3xl border border-line bg-white transition hover:-translate-y-1 hover:shadow-[0_24px_60px_-34px_rgba(85,77,241,.55)]">
            <div class="flex items-center gap-3 border-b border-line bg-surface px-4 py-2.5">
              <span class="flex gap-1.5" aria-hidden="true"><span class="h-2.5 w-2.5 rounded-full bg-line"></span><span class="h-2.5 w-2.5 rounded-full bg-line"></span><span class="h-2.5 w-2.5 rounded-full bg-line"></span></span>
              <span class="flex-1 truncate rounded-md bg-white px-3 py-1 text-center text-xs text-muted">{e(domain)}</span>
            </div>
            <div class="aspect-video overflow-hidden bg-surface">
              <img src="../assets/case-studies/websites/{it["image"]}.webp" alt="{e(it["name"])} homepage" width="1280" height="720" class="h-full w-full object-cover object-top transition duration-500 group-hover:scale-[1.03]" loading="lazy" />
            </div>
            <div class="flex flex-1 flex-col p-6">
              <div class="flex flex-wrap items-center gap-2">
                <h3 class="text-lg font-semibold tracking-tight">{e(it["name"])}</h3>{badge}
              </div>
              <p class="mt-1 text-sm font-medium text-brand">{e(it["industry"])}</p>
              <p class="mt-3 leading-relaxed text-muted">{e(it["text"])}</p>
              <span class="mt-auto inline-flex items-center gap-2 pt-5 text-[15px] font-medium">Visit website<span class="transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5" aria-hidden="true">{ARROW.format(s=14)}</span><span class="sr-only">(opens in a new tab)</span></span>
            </div>
          </a>'''
    cards = "\n".join(card(it) for it in items)
    return f'''
    <!-- ============ PORTFOLIO ============ -->
    <section id="portfolio" class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl">
          <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">Websites we've {serif}built</span></h2>
          <p class="mt-5 text-lg leading-relaxed text-muted">{e(svc.get("portfolio_intro", ""))}</p>
        </div>
        <div class="mt-12 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
{cards}
        </div>
      </div>
    </section>
'''


def advisors_section(svc):
    people = svc.get("advisors")
    if not people:
        return ""
    serif = '<span class="font-serif font-normal italic">'
    cards = "\n".join(f'''          <li class="overflow-hidden rounded-3xl border border-line bg-white">
            <div class="aspect-[4/3] overflow-hidden bg-brand-soft">
              <img src="../assets/team/{img}-wide.webp" alt="{e(name)}" width="1600" height="1000" class="h-full w-full object-cover object-bottom" loading="lazy" />
            </div>
            <div class="p-6">
              <h3 class="text-lg font-semibold tracking-tight">{e(name)}</h3>
              <p class="text-sm font-medium text-brand">{e(role)}</p>
              <p class="mt-3 leading-relaxed text-muted">{e(focus)}</p>
            </div>
          </li>''' for img, name, role, focus in people)
    return f'''
    <!-- ============ ADVISORS ============ -->
    <section id="advisors" class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl">
          <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">Advisors you'll {serif}work with</span></h2>
          <p class="mt-5 text-lg leading-relaxed text-muted">{e(svc.get("advisors_intro", ""))}</p>
        </div>
        <ul class="mt-12 grid gap-6 md:grid-cols-3">
{cards}
        </ul>
      </div>
    </section>
'''


def structured_data(svc):
    """Service, FAQ and breadcrumb schema so search engines and AI assistants can read the page."""
    url = f"{SITE}/services/{svc['slug']}.html"
    data = [
        {"@context": "https://schema.org", "@type": "Service", "name": svc["name"], "description": svc["summary"], "url": url,
         "provider": {"@type": "Organization", "name": "iWave Digital", "url": f"{SITE}/"}},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in svc["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Services", "item": f"{SITE}/#services"},
            {"@type": "ListItem", "position": 3, "name": svc["name"], "item": url}]},
    ]
    return "\n".join(f'  <script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in data)


def page(svc):
    icon_bg, accent = tone_classes(svc["tone"])
    best = "\n".join(f'''              <li class="flex gap-3"><span class="mt-0.5 flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-brand text-white" aria-hidden="true">{CHECK}</span><span>{e(b)}</span></li>''' for b in svc["best_for"])
    included = "\n".join(f'''          <li class="bg-white p-7">
            <span class="flex h-8 w-8 items-center justify-center rounded-full {icon_bg}" aria-hidden="true">{CHECK}</span>
            <h3 class="mt-5 font-semibold">{e(t)}</h3>
            <p class="mt-2 leading-relaxed text-muted">{e(d)}</p>
          </li>''' for t, d in svc["included"])
    steps = "\n".join(f'''          <li class="border-t border-white/20 pt-6">
            <p class="text-sm font-medium text-white/60">Step {i}</p>
            <h3 class="mt-3 text-xl font-semibold">{e(t)}</h3>
            <p class="mt-3 leading-relaxed text-white/70">{e(d)}</p>
          </li>''' for i, (t, d) in enumerate(svc["steps"], 1))
    proof_case = case_card(svc["case"]) if svc["case"] else ""
    quotes = "\n".join(quote_card(k) for k in svc["quotes"])
    qcols = "lg:grid-cols-3" if len(svc["quotes"]) >= 3 else ""
    serif = '<span class="font-serif font-normal italic">'
    results_heading = f"Results we've {serif}delivered</span>" if svc["case"] else f"What our {serif}clients say</span>"
    results_bg = "bg-surface" if svc.get("case_detail") else ""
    results_section = f'''    <!-- ============ RESULTS ============ -->
    <section class="{results_bg} py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <h2 class="max-w-2xl text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">{results_heading}</h2>
        <div class="mt-12 space-y-6">
{proof_case}
          <div class="grid gap-6 md:grid-cols-2 {qcols}">
{quotes}
          </div>
        </div>
      </div>
    </section>
''' if (svc["case"] or svc["quotes"]) else ""
    faq = "\n".join(f'''          <details class="group py-2"{" open" if i == 0 else ""}>
            <summary class="flex min-h-[56px] cursor-pointer items-center justify-between gap-6 py-3 text-lg font-semibold">
              {e(q)}
              <span class="faq-icon flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-line bg-surface transition" aria-hidden="true">{PLUS}</span>
            </summary>
            <p class="max-w-prose pb-5 leading-relaxed text-muted">{e(a)}</p>
          </details>''' for i, (q, a) in enumerate(svc["faq"]))
    others = "\n".join(f'''          <a href="{o["slug"]}.html" class="group flex items-center gap-4 rounded-2xl border border-line bg-white p-5 transition hover:border-brand/40 hover:bg-brand-soft/40">
            <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl {tone_classes(o["tone"])[0]}" aria-hidden="true">{icon_svg(o["icon"], 20)}</span>
            <span class="flex-1 font-semibold">{e(o["name"])}</span>
            <span class="text-muted transition group-hover:translate-x-0.5 group-hover:text-brand" aria-hidden="true">{ARROW.format(s=16)}</span>
          </a>''' for o in SERVICES if o["slug"] != svc["slug"])

    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(svc["name"])} — iWave Digital</title>
  <meta name="description" content="{e(svc["summary"])}" />
  <!-- Generated by tools/build_services.py — edit the content there and re-run the script. -->
  <link rel="canonical" href="{SITE}/services/{svc["slug"]}.html" />
  <meta name="theme-color" content="#554DF1" />
  <link rel="icon" href="../favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png" />
  <link rel="apple-touch-icon" href="../apple-touch-icon.png" />
  <link rel="manifest" href="../site.webmanifest" />

  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="iWave Digital" />
  <meta property="og:title" content="{e(svc["name"])} — iWave Digital" />
  <meta property="og:description" content="{e(svc["summary"])}" />
  <meta property="og:url" content="{SITE}/services/{svc["slug"]}.html" />
  <meta property="og:image" content="{SITE}/assets/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(svc["name"])} — iWave Digital" />
  <meta name="twitter:description" content="{e(svc["summary"])}" />
  <meta name="twitter:image" content="{SITE}/assets/og-image.jpg" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/tailwind.css" />
  <link rel="stylesheet" href="../assets/site.css" />
{structured_data(svc)}
</head>

<body class="bg-white font-sans text-ink">
  <a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:rounded-full focus:bg-ink focus:px-4 focus:py-2 focus:text-white">Skip to content</a>

{header()}

  <main id="main">
    <!-- ============ HERO ============ -->
    <section class="relative -mt-[76px] overflow-hidden pt-[76px]">
      <div class="glow left-[-10%] top-[10%] h-[480px] w-[480px] bg-brand/20" aria-hidden="true"></div>
      <div class="glow right-[-8%] top-[20%] h-[480px] w-[480px] bg-sky/20" aria-hidden="true"></div>
      <div class="relative mx-auto grid max-w-site gap-12 px-4 pb-20 pt-14 sm:px-6 sm:pt-20 lg:grid-cols-[1.35fr_1fr] lg:items-end lg:px-8">
        <div>
          <nav aria-label="Breadcrumb" class="text-sm text-muted">
            <ol class="flex flex-wrap items-center gap-2">
              <li><a href="../index.html" class="hover:text-ink">Home</a></li>
              <li aria-hidden="true">/</li>
              <li><a href="../index.html#services" class="hover:text-ink">Services</a></li>
              <li aria-hidden="true">/</li>
              <li class="text-ink" aria-current="page">{e(svc["name"])}</li>
            </ol>
          </nav>
          <span class="rise mt-10 flex h-14 w-14 items-center justify-center rounded-2xl {icon_bg}" aria-hidden="true">{icon_svg(svc["icon"], 26)}</span>
          <h1 class="rise rise-2 mt-6 text-[42px] font-semibold leading-[1.04] tracking-[-0.035em] sm:text-6xl lg:text-7xl">{e(svc["title_a"])} <span class="font-serif font-normal italic">{e(svc["title_b"])}</span></h1>
          <p class="rise rise-3 mt-6 max-w-2xl text-lg leading-relaxed text-muted sm:text-xl">{e(svc["intro"])}</p>
          <div class="rise rise-4 mt-9 flex flex-col gap-4 sm:flex-row sm:items-center">
            <a href="https://cal.com/iwave-digital/discovery-call" target="_blank" rel="noopener" class="group inline-flex items-center gap-4 self-start rounded-full bg-ink py-2 pl-7 pr-2 font-medium text-white shadow-[0_10px_30px_-10px_rgba(85,77,241,.55)] transition hover:bg-brand">
              Book a free growth call
              <span class="flex h-11 w-11 items-center justify-center rounded-full bg-white text-ink transition group-hover:rotate-45" aria-hidden="true">{ARROW.format(s=16)}</span>
            </a>
            <a href="#included" class="inline-flex h-11 items-center self-start rounded-full px-4 font-medium text-ink underline-offset-4 hover:underline sm:self-auto">See what's included</a>
          </div>
        </div>
        <aside class="rise rise-4 rounded-3xl border border-line bg-white/80 p-8 backdrop-blur">
          <h2 class="font-semibold">Best for</h2>
          <ul class="mt-5 space-y-4 leading-relaxed text-muted">
{best}
          </ul>
        </aside>
      </div>
    </section>

{glance_section(svc)}{pillars_section(svc)}
    <!-- ============ INCLUDED ============ -->
    <section id="included" class="bg-surface py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <h2 class="max-w-2xl text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">What's <span class="font-serif font-normal italic">included</span></h2>
        <ul class="mt-12 grid gap-px overflow-hidden rounded-3xl border border-line bg-line sm:grid-cols-2 lg:grid-cols-3">
{included}
        </ul>
      </div>
    </section>

    <!-- ============ HOW IT WORKS ============ -->
    <section class="relative overflow-hidden bg-ink py-24 text-white sm:py-28">
      <div class="glow -left-40 top-10 h-[420px] w-[420px] bg-brand/40" aria-hidden="true"></div>
      <div class="glow -right-40 bottom-0 h-[420px] w-[420px] bg-sky/30" aria-hidden="true"></div>
      <div class="relative mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <h2 class="max-w-2xl text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">How it <span class="font-serif font-normal italic">works</span></h2>
        <ol class="mt-14 grid gap-10 md:grid-cols-2 lg:grid-cols-4 lg:gap-8">
{steps}
        </ol>
      </div>
    </section>

{case_detail_section(svc)}{case_list_section(svc)}{portfolio_section(svc)}{advisors_section(svc)}
{results_section}
{offers_section(svc)}
    <!-- ============ FAQ ============ -->
    <section class="bg-surface py-24 sm:py-28">
      <div class="mx-auto grid max-w-site gap-12 px-4 sm:px-6 lg:grid-cols-[1fr_1.4fr] lg:gap-20 lg:px-8">
        <h2 class="text-4xl font-semibold tracking-[-0.03em] sm:text-5xl">Common <span class="font-serif font-normal italic">questions</span></h2>
        <div class="divide-y divide-line border-y border-line">
{faq}
        </div>
      </div>
    </section>

    <!-- ============ CONTACT ============ -->
    <section id="contact" class="py-24 sm:py-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <div class="relative overflow-hidden rounded-[32px] bg-gradient-to-br from-brand via-brand-dark to-sky-dark px-6 py-20 text-center text-white sm:px-12 sm:py-24">
          <div class="glow -left-20 -top-20 h-[360px] w-[360px] bg-sky/50" aria-hidden="true"></div>
          <div class="glow -bottom-24 -right-20 h-[360px] w-[360px] bg-white/20" aria-hidden="true"></div>
          <div class="relative">
            <h2 class="mx-auto max-w-3xl text-4xl font-semibold tracking-[-0.03em] sm:text-6xl">Let's talk about <span class="font-serif font-normal italic">{e(svc["name"].lower())}</span></h2>
            <p class="mx-auto mt-6 max-w-xl text-lg leading-relaxed text-white/85">Book a free 30-minute growth call. We'll look at where you are today and show you exactly what we'd build.</p>
            <div class="mt-10 flex flex-col items-center justify-center gap-5 sm:flex-row">
              <a href="{BOOKING_URL}" target="_blank" rel="noopener" class="group inline-flex items-center gap-4 rounded-full bg-white py-2 pl-7 pr-2 font-medium text-ink transition hover:bg-ink hover:text-white">
                Book a free discovery call
                <span class="flex h-11 w-11 items-center justify-center rounded-full bg-ink text-white transition group-hover:rotate-45 group-hover:bg-white group-hover:text-ink" aria-hidden="true">{ARROW.format(s=16)}</span>
              </a>
              <a href="mailto:{EMAIL}" class="inline-flex h-11 items-center rounded-full px-4 font-medium text-white underline-offset-4 hover:underline">{EMAIL}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ OTHER SERVICES ============ -->
    <section class="pb-24 sm:pb-28">
      <div class="mx-auto max-w-site px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-semibold tracking-[-0.03em] sm:text-4xl">Explore other <span class="font-serif font-normal italic">services</span></h2>
        <div class="mt-10 grid gap-4 md:grid-cols-2 lg:grid-cols-3">
{others}
        </div>
      </div>
    </section>
  </main>

{footer()}

  <script src="../assets/site.js"></script>
</body>
</html>
'''


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for svc in SERVICES:
        (OUT / f"{svc['slug']}.html").write_text(page(svc), encoding="utf-8")
        print(f"services/{svc['slug']}.html")
