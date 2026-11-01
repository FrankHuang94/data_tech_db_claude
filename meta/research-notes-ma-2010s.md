# Research notes: data-infrastructure M&A, 2010-2019

Companion to `data/staging/ma_2010_2019.csv` (47 deals, announced 2010-01-01 to 2019-12-31). Retrieved 2026-11-01. Values in USD millions. "Disclosed" means the acquirer or target published it (press release or SEC filing). "Press-reported" means the number came from media citing sources. Undisclosed values are left blank, not estimated.

## Caveats and judgment calls

- **HP-Autonomy:** HP set the price in sterling (GBP 25.50/share, about GBP 7.1B fully diluted). The $10.3B figure is the USD value in press reports, so the row is marked press-reported.
- **Cloudera-Hortonworks:** $5.2B is the combined equity value of the merged company. It is not a price paid.
- **VMware-Pivotal:** $2.7B is enterprise value. VMware expected to pay out only about $0.8B in net cash, because Dell already owned much of Pivotal.
- **TIBCO-Jaspersoft:** the press reported $185M. TIBCO's 10-Q shows a total purchase price of about $188M.
- **IBM-Red Hat:** this is not a data deal in the narrow sense. It is included because of its open-source and hybrid-cloud relevance, and is labelled "open-source infrastructure".
- **Ad/marketing data deals:** BlueKai, Datalogix and Moat are included as data-asset deals.
- **Estimates not used as values:** EMC-Greenplum (analyst guess $300-400M), Hitachi-Pentaho (outside estimate $500-600M) and Google-Alooma (Globes, $100-150M unconfirmed) are mentioned only in the outcome text. Their value fields are blank.
- **Announcement-date judgment calls:**
  - Apple-FoundationDB uses 2015-03-24, the date TechCrunch reported it. Apple never issued a release.
  - Snowflake-Numeracy uses 2019-03-26, from Snowflake's blog and a CB Insights listing.
  - Twitter-Gnip uses 2014-04-15, from a Reuters report cited secondhand.
- **Outcomes stated from background knowledge, not re-fetched this sweep:** HP's $8.8B Autonomy impairment (Nov 2012), Oracle's 2024 exit from advertising, the 2021 Cloudera take-private, the 2021 Informatica re-IPO and 2025 Salesforce agreement, MongoDB deprecating Atlas Device Sync (2024), and Syncsort being renamed Precisely (2020). The integrator should spot-check these.

## Sources

| # | Publisher | Title (paraphrased where untitled) | URL | Published | Retrieved |
|---|---|---|---|---|---|
| 1 | SAP | SAP to acquire Sybase (ad-hoc release) | https://www.sap.com/investors/en/financial-news/ad-hoc-news/2010/05/934992.html | 2010-05-12 | 2026-11-01 |
| 2 | EMC (Dell Technologies newsroom) | EMC to acquire Greenplum | https://corporate.delltechnologies.com/en-us/newsroom/announcements/2010/07/20100706-01.htm | 2010-07-06 | 2026-11-01 |
| 3 | WilmerHale | Netezza to be acquired for $1.7 billion in cash | https://www.wilmerhale.com/en/insights/news/netezza-to-be-acquired-for-1-7-billion-in-cash-september-22-2010 | 2010-09-22 | 2026-11-01 |
| 4 | TechCrunch | HP acquires Vertica | https://techcrunch.com/2011/02/14/hp-acquires-data-management-and-real-time-analytics-company-vertica/ | 2011-02-14 | 2026-11-01 |
| 5 | SEC / Teradata | Form 8-K, Aster Data merger agreement | https://www.sec.gov/Archives/edgar/data/0000816761/000119312511054332/d8k.htm | 2011-03-03 | 2026-11-01 |
| 6 | The Register | HP completes Autonomy acquisition | https://www.theregister.com/2011/10/04/hp_buys_autonomy/ | 2011-10-04 | 2026-11-01 |
| 7 | VentureBeat | Actian buys ParAccel | https://venturebeat.com/2013/04/25/actian-buys-paraccel | 2013-04-25 | 2026-11-01 |
| 8 | Washington Technology | IBM bolsters cloud services with Cloudant | https://washingtontechnology.com/articles/2014/02/25/ibm-cloudant-acquisition.aspx | 2014-02-25 | 2026-11-01 |
| 9 | IAPP | Oracle to buy BlueKai for $400M | https://iapp.org/news/a/oracle-to-buy-bluekai-for-400m | 2014-02-24 | 2026-11-01 |
| 10 | SEC / Twitter | 10-Q Q2 2014 (Gnip consideration) | https://www.sec.gov/Archives/edgar/data/0001418091/000156459014003474/twtr-10q_20140630.htm | 2014-08-07 | 2026-11-01 |
| 11 | GlobeNewswire / TIBCO | TIBCO Software acquires Jaspersoft | https://www.globenewswire.com/news-release/2014/04/28/1051677/0/en/TIBCO-Software-Acquires-Jaspersoft.html | 2014-04-28 | 2026-11-01 |
| 12 | BigDATAwire | Teradata acquires Revelytix, Hadapt | https://bigdatawire.com/2014/07/22/teradata-acquires-revelytix-hadapt | 2014-07-22 | 2026-11-01 |
| 13 | SiliconANGLE | Teradata buys Think Big | https://siliconangle.com/2014/09/04/teradata-buys-out-the-hottest-hadoop-consultancy-in-silicon-valley/ | 2014-09-04 | 2026-11-01 |
| 14 | Financier Worldwide | Vista Equity acquires TIBCO for $4.3bn | https://financierworldwide.com/vista-equity-acquires-tibco-for-43bn | 2014-09 | 2026-11-01 |
| 15 | Bloomberg | Google buys Firebase | https://www.bloomberg.com/news/articles/2014-10-21/google-buys-firebase-to-add-cloud-computing-mobile-tools | 2014-10-21 | 2026-11-01 |
| 16 | AdExchanger | Oracle to acquire Datalogix | https://adexchanger.com/platforms/oracle-to-acquire-data-solutions-giant-datalogix | 2014-12-22 | 2026-11-01 |
| 17 | PCWorld | Microsoft to acquire Revolution Analytics | https://www.pcworld.com/article/431469/microsoft-to-acquire-r-language-powerhouse-revolution-analytics.html | 2015-01-23 | 2026-11-01 |
| 18 | Hitachi Vantara | HDS announces intent to acquire Pentaho | https://hitachivantara.com/en-us/news/gl150210a | 2015-02-10 | 2026-11-01 |
| 19 | Elastic | Packetbeat on Found (blog) | https://www.elastic.co/blog/packetbeat-on-found | 2015 | 2026-11-01 |
| 20 | MacRumors (citing TechCrunch) | Apple acquires FoundationDB | https://macrumors.com/2015/03/24/apple-acquires-foundationdb | 2015-03-24 | 2026-11-01 |
| 21 | Permira | Informatica agreement to be acquired | https://www.permira.com/news-and-insights/news/informatica-announces-agreement-to-be-acquired-by-the-permira-funds-and-canada-pension-plan-investment-board/ | 2015-04-07 | 2026-11-01 |
| 22 | Microsoft | Microsoft acquires Datazen | https://blogs.microsoft.com/blog/2015/04/14/microsoft-acquires-mobile-business-intelligence-leader-datazen/ | 2015-04-14 | 2026-11-01 |
| 23 | Elastic | Elastic acquires Packetbeat | https://www.elastic.co/about/press/elastic-acquires-packetbeat | 2015-05-27 | 2026-11-01 |
| 24 | Thoma Bravo | Thoma Bravo to acquire Qlik | https://www.thomabravo.com/press-releases/thoma-bravo-to-acquire-qlik | 2016-06-02 | 2026-11-01 |
| 25 | Workday | Workday to acquire Platfora | https://blog.workday.com/en-us/2016/workday-to-acquire-platfora.html | 2016-07-21 | 2026-11-01 |
| 26 | CNBC | Apple buys machine-learning startup Turi | https://www.cnbc.com/2016/08/05/apple-buys-machine-learning-startup-turi.html | 2016-08-05 | 2026-11-01 |
| 27 | TechCrunch | Google confirms acquisition of Kaggle | https://techcrunch.com/2017/03/08/google-confirms-its-acquisition-of-data-science-community-kaggle/ | 2017-03-08 | 2026-11-01 |
| 28 | SiliconANGLE | Oracle snaps up Moat | https://siliconangle.com/2017/04/18/oracle-snaps-digital-measurement-firm-moat-fill-marketing-cloud/ | 2017-04-18 | 2026-11-01 |
| 29 | Enterprise Times | Infor acquires cloud-native BI (Birst) | https://www.enterprisetimes.co.uk/2017/04/26/infor-acquires-cloud-native-bi/ | 2017-04-26 | 2026-11-01 |
| 30 | Salesforce | Salesforce signs definitive agreement to acquire MuleSoft | https://investor.salesforce.com/news/news-details/2018/Salesforce-Signs-Definitive-Agreement-to-Acquire-MuleSoft/default.aspx | 2018-03-20 | 2026-11-01 |
| 31 | Calcalist | Salesforce buys Datorama for over $800M | https://www.calcalistech.com/ctech/articles/0,7340,L-3742414,00.html | 2018-07-16 | 2026-11-01 |
| 32 | TechCrunch | Cloudera and Hortonworks announce $5.2B merger | https://techcrunch.com/2018/10/03/cloudera-and-hortonworks-announce-5-2-billion-merger | 2018-10-03 | 2026-11-01 |
| 33 | VentureBeat | MongoDB to acquire mLab for $68M | https://venturebeat.com/ai/mongodb-to-acquire-cloud-database-provider-mlab-for-68-million | 2018-10-09 | 2026-11-01 |
| 34 | SEC / IBM | 8-K, completion of Red Hat acquisition | https://www.sec.gov/Archives/edgar/data/51143/000095014219001515/eh1900893_8k.htm | 2019-07-09 | 2026-11-01 |
| 35 | BigDATAwire | Talend buys Stitch for $60M | https://bigdatawire.com/2018/11/07/21615 | 2018-11-07 | 2026-11-01 |
| 36 | Microsoft | Microsoft acquires Citus Data | https://blogs.microsoft.com/blog/2019/01/24/microsoft-acquires-citus-data-re-affirming-its-commitment-to-open-source-and-accelerating-azure-postgresql-performance-and-scale/ | 2019-01-24 | 2026-11-01 |
| 37 | TechCrunch | Google acquires Alooma | https://techcrunch.com/2019/02/19/google-acquires-cloud-migration-platform-alooma/ | 2019-02-19 | 2026-11-01 |
| 38 | SEC / Attunity | 6-K exhibit 99.1, Qlik agreement | https://www.sec.gov/Archives/edgar/data/893821/000117891319000661/exhibit_99-1.htm | 2019-02-21 | 2026-11-01 |
| 39 | Snowflake | Numeracy: investing in our query UI | https://snowflake.com/blog/numeracy-investing-in-our-query-ui/ | 2019-03 | 2026-11-01 |
| 40 | MongoDB | MongoDB strengthens mobile offerings with Realm | https://investors.mongodb.com/news-releases/news-release-details/mongodb-strengthens-mobile-offerings-acquisition-realm | 2019-04-24 | 2026-11-01 |
| 41 | SEC / Elastic | 8-K, Endgame merger agreement | https://www.sec.gov/Archives/edgar/data/1707753/000119312519166177/d573056d8k.htm | 2019-06-05 | 2026-11-01 |
| 42 | TechCrunch | Google closes $2.6B Looker acquisition | https://techcrunch.com/2020/02/13/google-closes-2-6b-looker-acquisition/ | 2020-02-13 | 2026-11-01 |
| 43 | Cooley | Tableau enters agreement to sell to Salesforce for $15.7B | https://www.cooley.com/news/coverage/2019/2019-06-10-tableau-enters-agreement-to-sell-to-salesforce-for-15-billion | 2019-06-10 | 2026-11-01 |
| 44 | HPE | HPE acquires MapR business assets | https://hpe.com/us/en/newsroom/press-release/2019/08/hpe-advances-its-intelligent-data-platform-with-acquisition-of-mapr-business-assets.html | 2019-08-05 | 2026-11-01 |
| 45 | SEC / Splunk | 8-K exhibit 99.1, SignalFx | https://www.sec.gov/Archives/edgar/data/1353283/000110465919046819/a19-17469_1ex99d1.htm | 2019-08-21 | 2026-11-01 |
| 46 | SEC / VMware | 8-K exhibit 99.1, Pivotal agreement | https://www.sec.gov/Archives/edgar/data/1124610/000119312519226898/d778820dex991.htm | 2019-08-22 | 2026-11-01 |
| 47 | SEC / Pitney Bowes | 8-K exhibit 99.1, sale of Software Solutions to Syncsort | https://www.sec.gov/Archives/edgar/data/78814/000095015719000934/ex99-1.htm | 2019-08-26 | 2026-11-01 |

## Pattern observations (2010-2019)

1. **2010-11: incumbents bought MPP analytic databases.** Sybase, Greenplum, Netezza, Vertica and Aster all sold to SAP, EMC, IBM, HP and Teradata within about 12 months. Nearly every analytic-database startup of the 2000s was absorbed by a systems or apps vendor. Few of those engines survived as category leaders once cloud warehouses arrived.
2. **Storage and hardware vendors kept buying up-stack.** EMC bought Greenplum, Hitachi bought Pentaho, HP bought Vertica and Autonomy, and HPE bought MapR. Results were mixed or poor. Greenplum ended up in Pivotal, then VMware, then Broadcom; Vertica went to Micro Focus; Autonomy became an $8.8B writedown. For a storage acquirer, the lesson is that owning the data engine did not reliably pull through hardware.
3. **The Hadoop cycle ran from boom to merger to distressed sale within the decade.** Teradata bought Hadoop add-ons (Hadapt, Think Big) in 2014. Cloudera and Hortonworks then merged in 2018 to stop competing on price, and MapR's assets went to HPE in 2019 after a near shutdown. Open-source distributions without a managed-cloud product lost pricing power.
4. **Private equity became the exit for slow-growth public data vendors.** TIBCO ($4.3B), Informatica ($5.3B) and Qlik ($3.0B) were all taken private, often after activist pressure. Their PE owners then used them to roll up smaller companies (Qlik bought Attunity; Syncsort bought Pitney Bowes Software and became Precisely).
5. **Late-decade price peaks came from application vendors buying data layers.** Salesforce bought MuleSoft ($6.5B), Datorama (~$0.8B reported) and Tableau ($15.7B). Workday bought Platfora and Infor bought Birst. Apps vendors paid the most because analytics and integration deepen account lock-in.
6. **Hyperscalers mostly made small, undisclosed tuck-ins rather than big database buys.** Examples are Google-Firebase, Kaggle, Alooma and Looker ($2.6B, the exception), plus Microsoft-Citus, Datazen and Revolution, and Apple-FoundationDB. They built their core engines in-house (Redshift, BigQuery, Cosmos DB) and acquired for developer reach or migration on-ramps.
7. **Database companies moved users from self-managed to managed cloud services through M&A.** MongoDB bought mLab, its largest third-party host, to move users onto Atlas, and Elastic bought Found, which became Elastic Cloud. Buying the hosting resellers of your own open-source project was a repeatable play.
8. **Disclosure is thin.** About 43% of the rows (20 of 47) have no disclosed price, and 7 more rely on press reports. Undisclosed deals cluster in sub-$500M tuck-ins by Apple, Google and Microsoft, and in asset deals.
9. **At the end of the decade, observability and security pulled the search engines away from pure data infrastructure.** Splunk bought SignalFx ($1.05B) and Elastic bought Endgame ($234M), pointing Elastic and Splunk toward security and observability rather than general analytics. That set up Cisco's 2024 purchase of Splunk.
