# importing libraries
import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 


st.title("مونوبولي")
st.text("")
st.text("")
st.text("أعرفكم عن نفسي أنا فايز بكتب وبنفس الوقت بسولف معكم عن قصتنا")
st.write("أول واحد هذا انا ومن بعدي بالترتيب مؤيد وهلال")
st.image("fayez.jpg")
st.image("mu.png")
st.image("helal.png")
st.text("")
st.text("")
st.text("")
st.text("")
st.write("ربع جينا من الديرة ندور على لقمة العيش في الرياض")
st.write("وعايشين حاليا في هالكرفان دبرة لين نحصل سكن")
st.image("caravan.png")
st.write("قررنا احنا الثلاثة نروح إلى مكتب أحد هوامير العقار بالرياض الي هو أبو حمود")
st.write()
st.image("abu.png")
st.write("ابو حمود نقدر نقول انه عنده اكبر وادق داتابيس للعقار حصرية في الرياض.. علشان تفهمون ابو حمود هو انسان منظم ودقيق جدا نشاطه")
st.write("محسوب بدقة توازي دقة ساعة سويسرية لامجال عنده للارتجال والعشوائية")
st.write("جلس فايز (ممثل عن اصحابه ) مع أبو حمود ( ممثل عن الرأسمالية ) على طاولة المفاوضات")
st.image("disc.png")
st.write("أبو حمود :  خلني اعطيك نظرة شاملة على السوق كامل")
st.image("general.png")

st.write("فايز: أحترم رأيك عزيزي ابو حمود بس اشوف انه معلومات مظللة تعرض ليي الرياض بمختلف مناطقها في متوسط اسعار واحد ! وانت سيد العارفين الشمال لها افرج معين والشرق والجنوب كذلك قارن ليي متوسط سعر العقارات في  الحي نفسه مع بعض  ")
st.image("reject.png")
st.write("ابو حمود:  تمام")


st.write("معليش لو قاطعتك")
st.write(" يالربع ايه انت الي تقرا .. وش رايكم نخليه يستعرض لنا أي جهة بالرياض افضل ودنا ناخذ افضل منطقتين؟ من حيث اسعار وجودة حياة وخدمات وبنية تحتية؟ ")

option = st.radio("Salect", ['شمال الرياض', 'شرق الرياض', 'جنوب الرياض', "غرب الرياض", "وسط الرياض"])
if option == "شمال الرياض": 
    st.success("صح عليك.. رأينا أيضا نفس الشي")
elif option == "شرق الرياض": 
    st.success("صح عليك.. رأينا أيضا نفس الشي")
elif option == 'جنوب الرياض': 
    st.warning("امممم ، مانتوقع :(")
elif option == 'وسط الرياض': 
    st.warning("امممم ، مانتوقع :(")
elif option == 'غرب الرياض': 
    st.warning("امممم ، مانتوقع :(")

st.text("تمام الشرق أو الشمال ")
st.image("northLand.png")
st.image("northV.png")
st.image("eastLand.png")
st.image("eastV.png")
st.image("northA.png")

st.write("يلا ياشباب خلينا نروح ونشوف المنطقة")
btn = st.button("يلا بسم الله")
if btn:
    st.image("dislike north.png")
    st.write("هذي هي شمال الرياض؟ ليه كذا وسط بر مافيها شي من خدمات بنية تحتية.. بس الزين فيها قلة الزحمة وتركز أهم الشركات فيها")
    st.write("طيب على أي اساس صارت كذا غالية؟ وش أكثر شي يأثر بالأسعار؟")
    st.image("heat.png")
    st.write("اوه طلع أكثر شي هو")

st.write("وانتم وش رايكم عجبتكم؟")
like = st.radio("Salect", ['ايه عجبنا', 'لا '])
st.write(' هلال : اسمعو انا اقول نسوي قطة نقسم راس مالنا لثلاث اسهم والسهم الرابع للبنك نطلب قرض من البنوك بحيث يكون شريك معنا ونشتري ارض بالشمال كاستثمار وعوائد الاستثمار نعطيها للبنك ونشتري مقابلها حصة من اسهم البنك لين تصير ملكية العقار لنا %100')
st.write('وجهة نظري شمال الرياض ممتازة للاستثمار غالبا')
st.write('شوف تحليل شركة بيداس لحلول الاعمال في نمو الأسعار بالشمال كيف')
st.image("lands.jpg")

st.write("وجلست افكار كثيرة تشتت فكر فايز")
st.write("فايز: يارب ينجح المشروع وتتوسع أعمالي لين تصير عندي سيولة عالية")
st.write("فايز وهو يحلم انه غرقان بالسيولة")
st.image("cash.jpg")
st.write(" بعدين رجعو لمكتب العقاري وصار نقاش ")
st.write("حاد على الشقة الي يبونها ويتفقون امهم يختارو شقة أقل شي فيها ثلاث غرف وثلاث حمامات وتكون مؤثثة ومساحتها  ")
st.write("لاتقل عن 200 متر ")

st.write("ابو حمود: تمام تمام الي تبونه عندي تفضلو")
st.image("final.png")
st.write("بالنهاية اتفق الاصحاب الثلاثة للأسف على أن لايتفقو.. اختلاف بسبب الاراء والاسعار انتهى المطاف أنه رجع كل شخص لمنطقته")
st.image("ff.jpg")





