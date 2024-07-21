import streamlit as st
st.image('rabbits.png')
st.title("Экономическая модель разведения кроликов при смешанном типе кормления")
# creates a horizontal line
st.write("---")
tab1, tab2 = st.tabs(["Неслучной период", "Случной период"])
with tab1:
    st.header("Крольчиха и самец в неслучной период")
    number = 33
    num1_1 = st.number_input(label="кол-во кормодней в году", value = number)
    number = 3.46
    num1_2 = st.number_input(label="концентраты", value=number)
    number = 1.19
    num1_3 = st.number_input(label="сено", value=number)
    number = 3.23
    num1_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 4.48
    num1_5 = st.number_input(label="зеленые корма", value=number)
with tab2:
    st.header("Крольчиха и самец в случной период")
    number = 32
    num2_1 = st.number_input(label="кол-во кормодней в году", value=number)
    number = 4.16
    num2_2 = st.number_input(label="концентраты", value=number)
    number = 1.44
    num2_3 = st.number_input(label="сено", value=number)
    number = 3.84
    num2_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 5.60
    num2_5 = st.number_input(label="зеленые корма", value=number)
st.write("---")
tab3, tab4 = st.tabs(["Крольчиха сукрольная", "Крольчиха лактирующая"])
with tab3:
    st.header("Крольчиха сукрольная")
    number = 120
    num3_1 = st.number_input(label="кол-во кормодней в году", value = number)
    number = 16.80
    num3_2 = st.number_input(label="концентраты", value=number)
    number = 6.0
    num3_3 = st.number_input(label="сено", value=number)
    number = 15.60
    num3_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 23.10
    num3_5 = st.number_input(label="зеленые корма", value=number)
with tab4:
    st.header("Крольчиха лактирующая (7-8 крольчат)")
    number = 180
    num4_1 = st.number_input(label="кол-во кормодней в году", value=number)
    number = 62.40
    num4_2 = st.number_input(label="концентраты", value=number)
    number = 21.10
    num4_3 = st.number_input(label="сено", value=number)
    number = 57.20
    num4_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 83.35
    num4_5 = st.number_input(label="зеленые корма", value=number)
st.write("---")
tab5, tab6, tab7 = st.tabs(["На одну голову молодняка", "На все головы молодняка", "Годовая потребность ремонтного молодняка"])
with tab5:
    st.header("На одну голову молодняка с 45 до 120 дней")
    number = 75
    num5_1 = st.number_input(label="кол-во кормодней в году", value=number)
    number = 10.14
    num5_2 = st.number_input(label="концентраты", value=number)
    number = 3.14
    num5_3 = st.number_input(label="сено", value=number)
    number = 11.97
    num5_5 = st.number_input(label="зеленые корма", value=number)
with tab6:
    st.header("Всего на 24 головы молодняка")
    number = 243.36
    num6_2 = st.number_input(label="концентраты", value=number)
    number = 75.36
    num6_3 = st.number_input(label="сено", value=number)
    number = 287.28
    num6_5 = st.number_input(label="зеленые корма", value=number)
with tab7:
    st.header("Годовая потребность ремонтного молодняка")
    number = 42
    num7_1 = st.number_input(label="кол-во кормодней в году", value=number)
    number = 5.25
    num7_2 = st.number_input(label="концентраты", value=number)
    number = 1.89
    num7_3 = st.number_input(label="сено", value=number)
    number = 5.67
    num7_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 8.19
    num7_5 = st.number_input(label="зеленые корма", value=number)
st.write("---")
tab8, tab9, tab10 = st.tabs(["Годовая потребность самца", "Доля самца на одну крольчиху", "На крольчиху с приплодом"])
with tab8:
    st.header("Годовая потребность самца")
    number = 365
    num8_1 = st.number_input(label="кол-во кормодней в году", value=number)
    number = 47.50
    num8_2 = st.number_input(label="концентраты", value=number)
    number = 16.40
    num8_3 = st.number_input(label="сено", value=number)
    number = 44.0
    num8_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 64.0
    num8_5 = st.number_input(label="зеленые корма", value=number)
with tab9:
    st.header("Доля самца на одну крольчиху (1:8)")
    number = 5.93
    num9_2 = st.number_input(label="концентраты", value=number)
    number = 2.05
    num9_3 = st.number_input(label="сено", value=number)
    number = 5.50
    num9_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 8.0
    num9_5 = st.number_input(label="зеленые корма", value=number)
with tab10:
    st.header("На крольчиху с приплодом")
    st.header("(24 головы до 4-х месячного возраста с долей самца 1:8 и 0,7 голов ремонтного молодняка)")
    number = 341.36
    num10_2 = st.number_input(label="концентраты", value=number)
    number = 109.03
    num10_3 = st.number_input(label="сено", value=number)
    number = 91.0
    num10_4 = st.number_input(label="силос, корнеплоды", value=number)
    number = 420.0
    num10_5 = st.number_input(label="зеленые корма", value=number)
st.header("Стоимость кормов, руб. за кг.")
number = 324.44
price_2 = st.number_input(label="концентраты:", value=number)
number = 176.5
price_3 = st.number_input(label="сено:", value=number)
number = 19.23
price_4 = st.number_input(label="силос, корнеплоды:", value=number)
number = 423.75
price_5 = st.number_input(label="зеленые корма:", value=number)
ans1 = 0
ans2 = 0
ans3 = 0
ans4 = 0
ans = 0
def calculate():
    ans1 = num10_2 * price_2
    ans2 = num10_3 * price_3
    ans3 = num10_4 * price_4
    ans4 = num10_5 * price_5
    ans = ans1 + ans2 + ans3 + ans4
    st.success(f"Стоимость концентратов: {round(ans1,2)} руб.")
    st.success(f"Стоимость сена: {round(ans2,2)} руб.")
    st.success(f"Стоимость силоса, корнеплодов: {round(ans3,2)} руб.")
    st.success(f"Стоимость зеленых кормов: {round(ans4,2)} руб.")
    st.success(f"Итого: {round(ans,2)} руб.")
st.header("Расчет общей стоимости кормов на год")
if st.button("Рассчитать итоговую стоимость"):
    calculate()
