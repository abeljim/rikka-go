from threading import Thread
import time
import grpc
import random

import rikka_pb2
import rikka_pb2_grpc

PASSAGE = "In meteorology, precipitation is any product of the condensation of atmospheric water vapor that falls under gravity. The main forms of precipitation include drizzle, rain, sleet, snow, graupel and hail... Precipitation forms as smaller droplets coalesce via collision with other rain drops or ice crystals within a cloud. Short, intense periods of rain in scattered locations are called “showers”."
QUESTION = "What is another main form of precipitation besides drizzle, rain, snow, sleet and hail?"
PASSAGE2 = "The Norman dynasty had a major political, cultural and military impact on medieval Europe and even the Near East. The Normans were famed for their martial spirit and eventually for their Christian piety, becoming exponents of the Catholic orthodoxy into which they assimilated. They adopted the Gallo-Romance language of the Frankish land they settled, their dialect becoming known as Norman, Normaund or Norman French, an important literary language. The Duchy of Normandy, which they formed by treaty with the French crown, was a great fief of medieval France, and under Richard I of Normandy was forged into a cohesive and formidable principality in feudal tenure. The Normans are noted both for their culture, such as their unique Romanesque architecture and musical traditions, and for their significant military accomplishments and innovations. Norman adventurers founded the Kingdom of Sicily under Roger II after conquering southern Italy on the Saracens and Byzantines, and an expedition on behalf of their duke, William the Conqueror, led to the Norman conquest of England at the Battle of Hastings in 1066. Norman cultural and military influence spread from these new European centres to the Crusader states of the Near East, where their prince Bohemond I founded the Principality of Antioch in the Levant, to Scotland and Wales in Great Britain, to Ireland, and to the coasts of north Africa and the Canary Islands."
QUESTION2 = "In what country is Normandy located?"

PASSAGE3= """displayed a willingness to subjugate outsiders first Indians, who were nearly annihilated through war and disease, and then Africans, who were brought in chains to serve as slave labor, especially on the tobacco, rice, and indigo plantations of the southern colonies. But if the settlement experience gave people a common stock of values, both good and bad, it also divided them. The thirteen colonies were quite different from one another. Puritans carved tight, pious, and relatively democratic communities of small family farms out of rocky-soiled New England. Theirs was a homogeneous world in comparison to most of the southern colonies, where large landholders, mostly Anglicans, built plantations along the coast from which they lorded over a labor force of black slaves and looked down upon the poor white farmers who settled the backcountry. Different still were the middle colonies stretching from New York to Delaware. There diversity reigned. Well-to-do merchants put their
stamp on New York City, as Quakers did on Philadelphia, while out in the countryside sprawling estates were interspersed with modest homesteads. Within individual colonies, conflicts festered over economic interests, ethnic rivalries, and religious practices. All those clashes made it difficult for colonists to imagine that they were a single people with a common destiny, much less that they ought to break free from Britain. The American colonists in fact had little reason to complain about
Britain. Each of the thirteen colonies enjoyed a good deal of self-rule. Many colonists profited from trade within the British Empire. But by the 1760s, this stable arrangement began to crumble, a victim of the imperial rivalry between France and Britain. Their struggle for supremacy in North America began in the late seventeenth century and finally dragged in the colonists during the French and Indian War from 1756 to 1763. That war in one sense strengthened ties with Britain, since colonial
militias fought triumphantly alongside the British army against their mutual French and Indian enemies. But once the French were driven from the North American continent, the colonists no longer needed Britain for protection. More important still, after 1763 a financially overstretched British government made the fateful choice of imposing taxes on colonies that had been accustomed to answering mainly to their own colonial assemblies. By the 1770s issues of taxation, self-rule, and trade
restrictions brought the crisis of imperial authority to a head. Although as late as 1775 most people in the colonies clung to the hope of some kind of accommodation short of outright independence, royal intransigence soon thrust the colonists into a war of independence that neither antagonist could have anticipated just a few years before. Eight years of revolutionary war did more than anything in the colonial past to bring Americans together as a nation. Comradeship in arms and the struggle to
shape a national government forced Americans to subdue their differences as best they could. But the spirit of national unity was hardly universal. One in five colonists sided with the British as Loyalists, and a generation would pass before the wounds of this first American civil war fully healed. Yet in the end, Americans won the Revolution, with no small measure of help from the French, because in every colony people shared a firm belief that they were fighting for the unalienable rights of
life, liberty, and the pursuit of happiness, in the words of Thomas Jefferson's magnificent Declaration of Independence. Almost two hundred years of living a new life had prepared Americans to found a new nation. Philadelphia, Corner of Second and High Streets Delegates to the Constitutional Convention in 1787 gathered in Philadelphia, the largest city in North America, a vivid symbol of the rise of American society from its precarious beginnings at Jamestown and Plymouth nearly two centuries
earlier."""
QUESTION3 = "Where did the middle colonies stretch from?"
NUM_REQUESTS = 10
SLEEP_COUNT = 0.05

channel = grpc.insecure_channel('localhost:50051')
rikka_stub = rikka_pb2_grpc.RikkaStub(channel)
mai_request = rikka_pb2.QueryRequest(passage=PASSAGE3, question=QUESTION3)
sum_request = rikka_pb2.SummaryRequest(passage=PASSAGE3)
rui_request = rikka_pb2.QuestionRequest(passage=PASSAGE, term="test")


def call_infer_endpoint(n):
    response = rikka_stub.Query(mai_request)
    print(response.answer, ",", response.score)
    response = rikka_stub.Summarize(sum_request)
    print(response.summary)
    response = rikka_stub.GenerateQuestion(rui_request)
    print(response.question)


threads = []
start_time = time.time()

for i in range(0, NUM_REQUESTS):
    t = Thread(target=call_infer_endpoint, args=(i,))
    threads.append(t)
    t.daemon = True
    t.start()
    time.sleep(SLEEP_COUNT)

for x in threads:
    x.join()

print("--- %s seconds ---" % (time.time() - start_time))
