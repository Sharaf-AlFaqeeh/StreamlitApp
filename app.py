import streamlit as st

st.set_page_config("Short Report")
# إعداد الصفحات
def main_page():
    st.title("Home Page")
    st.write("____")
    # st.subheader("")
    col2,col1= st.columns(2)
    st.write("____")
    col1.subheader("Preview")
    col1.text("I am today a student")
    col1.text("I study AI in RU")
    col1.text("At the therd level")
    col1.text("so with help of Allah  ")
    col1.text("This site has builed  ")
    col1.text("from scratch by ")
    col1.text("Library streamlit")
    # st.subheader("")
    col2.image("images/profile.png", width= 200,output_format="PNG")  
    st.write("### Introdaction")
    st.write("""
          about me
    - **Name :** Sharaf Yahia Al-Faqeeh 
    - **Specialty :** AI
       - about this site
    - **Topic :** Short Report About Streamlit, MongoDB And Docker
    - **Supervision of :** 
    - **Eng :** محمد الشبلي
    """)
    st.write("___")
    st.write("### Contents Of Site")
    st.write("""
###  : المراجع 
- [الموقع الرسمي لـ Streamlit](https://streamlit.io) - Streamlit A faster way to build and share data apps
- [الموقع الرسمي لـ MongoDB](https://www.mongodb.com) - MongoDB NoSQL Experience the leading developer data platform 
                     that empowers developers to build global, multi-cloud applications at speed.
- [الموقع الرسمي لـ Docker](https://www.docker.com) - Docker Develop faster. Run anywhere. Build with the #1 most-used developer tool
""")

    # st.write(" ")
    st.write(" ")
    st.write("_________")

def streamlit_summary():
    st.title("Streamlit ملخص تعلّم ")
    st.write("""
**Streamlit** هي مكتبة مفتوحة المصدر تُستخدم لإنشاء تطبيقات ويب تفاعلية بسرعة وسهولة باستخدام لغة Python، وتُعد من الأدوات المهمة في مجال علم البيانات والذكاء الاصطناعي، حيث تمكن العلماء والمطورين من بناء واجهات تفاعلية لعرض النماذج والتصورات بسرعة كبيرة.

- **الأساسيات**:
  - **التعامل مع النصوص**:
    - `st.title("عنوان")`: لعرض عنوان رئيسي.
    - `st.header("عنوان فرعي")`: لعرض عنوان فرعي.
    - `st.subheader("عنوان فرعي أصغر")`: لعرض عنوان أصغر.
    - `st.write("نص عادي")`: لعرض نص عادي.
    - `st.markdown("نص بتنسيق Markdown")`: لعرض نصوص باستخدام تنسيق Markdown (لإضافة التنسيق مثل الغامق والمائل).
  - **إدخال البيانات**:
    - `st.text_input("أدخل نص")`: لإدخال نص.
    - `st.number_input("أدخل رقم")`: لإدخال أرقام.
    - `st.selectbox("اختر عنصرًا", ["خيار 1", "خيار 2"])`: لإنشاء قائمة منسدلة.
    - `st.slider("اختر قيمة", 0, 100)`: لإنشاء شريط تمرير للاختيار.
  - **التصورات**:
    - `st.line_chart(data)`: لإنشاء مخطط خطي.
    - `st.bar_chart(data)`: لإنشاء مخطط شريطي.
    - `st.map(data)`: لعرض بيانات جغرافية على خريطة.
  - **التفاعل مع المستخدم**:
    - `st.button("زر")`: لإضافة زر.
    - `st.checkbox("خيار")`: لإضافة صندوق اختيار.
    - `st.radio("اختر خيار", ["خيار 1", "خيار 2"])`: لإنشاء مجموعة خيارات.

- **أهمية المكتبة في علم البيانات والذكاء الاصطناعي**:
  - **عرض النماذج التفاعلية**: يمكن لمتخصصي علم البيانات والذكاء الاصطناعي استخدام Streamlit لعرض النماذج المدربة بشكل تفاعلي، مما يسهل عليهم مشاركة النماذج مع فريق العمل أو حتى العملاء.
  - **التصورات البيانية**: تسهل المكتبة إنشاء وعرض الرسوم البيانية والمخططات الإحصائية، مما يساعد على فهم البيانات بشكل أعمق.
  - **تطوير سريع**: بفضل سهولة الاستخدام، يمكن إنشاء تطبيقات تجريبية وتفاعلية في دقائق، مما يسهم في تسريع دورة تطوير المشاريع والنماذج.

- **أمثلة**:
  ```python
  import streamlit as st
  st.title("تطبيق بسيط")
  name = st.text_input("أدخل اسمك:")
  if st.button("عرض"):
      st.write(f"مرحبًا، {name}!")
  ```
    """)
    st.write("""
- **expender مثال عن انشاء**
  ```python
  with st.expander("more"):
    st.write("wellcom my friend Moh")
    st.text("Is this example good for these consepts ?")
    
    st.text_area("Comment",key="comment")
    clicked = st.button("send")
             
    if clicked :
        comment = str(st.session_state["comment"])
        if comment is None :
            st.write("No comment")
        else:   
             st.write(f"{comment}")

    if st.button("show image"):
        st.image("images/profile2.jpg")
  ```
    """)
    with st.expander("Results"):
        st.write("wellcom my friend Moh")
        st.text("Is this example good for these consepts ?")
        st.text_area("Comment",key="comment")
        clicked = st.button("send")
        if clicked :
            comment = str(st.session_state["comment"])
            if comment is None :
                st.write("No comment")
            else:   
                st.write(f"{comment}")
        if st.button("show image"):
            st.image("images/profile2.jpg")

def mongodb_summary():
    st.title("ملخص تعلّم MongoDB")
    st.write("""
    **MongoDB** هي قاعدة بيانات NoSQL تُستخدم لتخزين البيانات غير المهيكلة مثل الوثائق.
    - **الاتصال بقاعدة البيانات**:
      - استخدام مكتبة `pymongo` للاتصال بـ MongoDB.
      - مثال للاتصال:
        ```python
        from pymongo import MongoClient
        client = MongoClient("mongodb://localhost:27017/")
        db = client["mydatabase"]
        collection = db["mycollection"]
        ```
    - **إضافة واسترجاع البيانات**:
      - **إضافة**:
        ```python
        collection.insert_one({"name": "Ali", "age": 25})
        ```
      - **استرجاع**:
        ```python
        data = collection.find()
        for item in data:
            print(item)
        ```
    - ** Dete السحابية NoSql مثال كامل مع استخدام  **:
      - **app.py**:
        ```python
        import streamlit as st 
        import plotly.graph_objects as go 
        import calendar 
        from datetime import datetime
        from streamlit_option_menu import option_menu
        import database as db

        incomes=["Salary","Blog","Other Income"]
        expenses=["Rent","Utilities","Groceries","Car","Other Expenses","Saving"]
        currency = "USD"

        page_title = "Income and Expenses Tracker"
        page_icon = ":money_with_wings:"
        layout = "centered"

        st.set_page_config(page_title=page_title, page_icon= page_icon, layout= layout)
        st.title(page_title + " "+page_icon)

        years = [datetime.today().year , datetime.today().year + 1]
        months = list(calendar.month_name[1:])
        # 
        def get_all_periods():
            items = db.fetch_all_periods()
            periods = [item["key"] for item in items]
            return periods
        # 
        hide_st_style = """

        """
        st.markdown(hide_st_style, unsafe_allow_html=True)
        # 
        selected=option_menu(
            menu_title= None,
            options= ["Data Entry","Data Visualization"],
            icons=["pencil-fill", "bar-chart-fill"],
            orientation= "horizontal",
        )
        # 
        if selected == "Data Entry":
            st.header("Data Entry in "+currency)
            with st.form("entry_form",clear_on_submit=False):
            # with st.form("entry_form",clear_on_submit=True):
                col1 , col2 = st.columns(2)
                col1.selectbox("Select Month",months,key="month")
                col2.selectbox("Select Year",years,key="year")

                with st.expander("Income"):
                    for income in incomes:
                        st.number_input(f"{income}:", min_value=0 , format="%i", step=10, key=income)
                        
                with st.expander("EXpenses"):
                    for expense in expenses:
                        st.number_input(f"{expense}:", min_value=0 , format="%i", step=10, key=expense)
                    st.write("---------------")
                with st.expander("Comment"):
                    comment=st.text_area("",placeholder="Enter a comment her ...")
                
                submitted = st.form_submit_button("Save Data")

                if submitted :
                    period = str(st.session_state["year"])+ "_"+str(st.session_state["month"]) 
                    incomes = {income : st.session_state[income] for income in incomes}
                    expenses = {expense : st.session_state[expense] for expense in incomes}
                    # insert value into database
                    # st.write(f"incomes: {incomes}")
                    # st.write(f"expenses: {expenses}") #replaced by fellowing
                    db.insert_period(period=period, incomes=incomes, expenses=expenses, comment=comment)
                    st.success("Data saved")

        if selected == "Data Visualization":   
            st.header("Data Visualization")
            with st.form("saved_periods"):
                period = st.selectbox("Select Period:", get_all_periods())
                submitted = st.form_submit_button("Plot Period")
                if submitted:
                    # comment = " some cmment"
                    # incomes = {'salary':1500, 'Blog':50 , 'Other income':200}
                    # expenses = {'Rent':1500, 'Utilities':50 ,'Groceries':30,'Car':50, 'Other Expenses':200} 
                    # change to following :
                    period_data = db.get_period(period=period)
                    comment = period_data.get("comment")
                    expenses = period_data.get("expenses")
                    incomes = period_data.get("incomes")

                    total_income= sum(incomes.values())
                    total_expense= sum(expenses.values())
                    remaining_budget = total_income -total_expense

                    col1 ,col2 ,col3 =st.columns(3)
                    col1.metric("Total Income", f"{total_income} {currency}")
                    col2.metric("Total Expense", f"{total_expense} {currency}")
                    col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
                    st.text(f"Comment: {comment}")

                    # _______________
                    label = list(incomes.keys())+ ["Total Income"] + list(expenses.keys())
                    source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
                    # source =[0,1,2,2]
                    target = [len(incomes)] * len(incomes)+ [label.index(expense) for expense in expenses]
                    # target =[2,2,3,4]
                    value = list(incomes.values()) + list(expenses.values())
                    # Data Visualization
                    # Data to dict, dict to sankey
                    link = dict(source=source, target=target, value=value)
                    # Select Period
                    node = dict(label=label, pad=20, thickness=30, color="#E694FF")
                    data = go.Sankey(link=link, node=node)
                    # Plot Period
                    fig = go.Figure(data)
                    # Total Income
                    fig.update_layout(margin=dict(l=0, r=0, t=5, b=5)) 
                    st.plotly_chart(fig, use_container_width=True)

        ```
      - **database.py**:
        ```python
        import os
        from deta import Deta # pip install deta
        from dotenv import load_dotenv # to store the key  to be hidden
        # dete site key 
        # load environment variables
        load_dotenv(".env")
        # DETA_KEY = "my_deta_key" #this will be change to bellow
        DETA_KEY = os.getenv("DETA_KEY") #this DETA_KEY variable is in the dotenv file .env

        deta =Deta(DETA_KEY) 


        db = deta.Base("monthly_reports")

        def insert_period(period,incomes, expenses, comment):
            #Return the report on a successful creation, otherwise raises an error
            return db.put({"key":period ,"incomes":incomes, "expenses":expenses, "commint":comment})

        def fetch_all_periods():
            # Return a dict of all period
            res = db.fetch()
            return res.items

        def get_period(period):
            #If not found, the function will return None
            return db.get(period)
        ```
      - **.streamlit**:
        - **config.toml**:
            ```toml
            [theme]
            primaryColor = "#d33682"
            backgroundColor = "#002b36"
            secondaryBackgroundColor = "#586e75"
            textColor = "#fafafa"
            font = "sans serif"
            ```
      - **.env**:
        ```env
        DETA_KEY = "my_deta_key"
        ```
    """)
    with st.expander("Show Results"):
        # st.text("")
        st.write("Sory ! It Is In Development")
        st.text("What To Learn ?")
        import example
        pass

def docker_summary():
    st.title("ملخص تعلّم Docker")
    st.write("""
    **Docker** هو نظام أساسي يستخدم لحزم التطبيقات في حاويات مع جميع متطلباتها.
    - **المفاهيم الأساسية**:
      - **حاوية (Container)**: وحدة معزولة لتشغيل التطبيقات.
      - **صورة (Image)**: نموذج يُستخدم لإنشاء الحاويات.
    - **أوامر أساسية**:
      - `docker build -t myapp .`: إنشاء صورة.
      - `docker run -p 8501:8501 myapp`: تشغيل حاوية.
      - `docker-compose up`: تشغيل مجموعة من الخدمات.
    - **مزايا Docker**:
      - قابلية النقل بين الأنظمة.
      - سهولة إدارة الاعتماديات.
    - **Docker**:
      -Build
        Spin up new environments quickly
        Accelerate your development by building Docker images locally 
        or in the cloud with Docker Build Cloud. Create multiple containers
        using Docker Compose without the hassle of local build constraints.
        Integrate with your existing tools
        Docker seamlessly integrates with your development tools, such as
        VS Code, CircleCI, and GitHub. Meanwhile, Docker Build Cloud fast-tracks 
        build times, resulting in an enhanced workflow without disruption.
        Containerize applications for consistency
        Ensure consistent application performance across any environment, whether 
        it’s on-premises Kubernetes or cloud platforms like AWS ECS, Azure ACI, and 
        Google GKE.
    """)
    st.subheader("Why use Docker?")
    st.write("""
        Trusted by developers. Chosen by Fortune 100 companies. Docker provides a suite of development 
        tools, services, trusted content, and automations, used individually or together, 
        to accelerate the delivery of secure applications.[ Read more customer stories ](https://www.docker.com/customer-stories)   
""")
    
# صفحة التنقل
page_names_to_funcs = {
    "الصفحة الرئيسية": main_page,
    "ملخص Streamlit": streamlit_summary,
    "ملخص MongoDB": mongodb_summary,
    "ملخص Docker": docker_summary
}

# st.image("images/profile2.jpg",width=200)
# st.title("Hello")

selected_page = st.sidebar.selectbox("اختر صفحة", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

# if st.sidebar.button("mongodb"):
#     mongodb_summary()
# if st.sidebar.button("docker"):
#     docker_summary()
# if st.sidebar.button("streamlit_summary"):
#     streamlit_summary()
# for row in page_names_to_funcs :
#     btn=st.sidebar.button(row)
#     if btn :
#         page_names_to_funcs[row]()
