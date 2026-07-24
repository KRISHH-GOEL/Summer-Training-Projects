
# CONSTANTS

# Churn Probability Thresholds
CRITICAL_RISK = 0.80
HIGH_RISK = 0.60
MEDIUM_RISK = 0.40

# Customer Tenure Thresholds
NEW_CUSTOMER = 12
LOYAL_CUSTOMER = 48


# Monthly Charges Thresholds
HIGH_MONTHLY_CHARGE = 80
VERY_HIGH_MONTHLY_CHARGE = 100

# Priority Levels
PRIORITY_CRITICAL = "Critical"
PRIORITY_HIGH = "High"
PRIORITY_MEDIUM = "Medium"
PRIORITY_LOW = "Low"

# Customer Segments
AT_RISK = "At-Risk Customer"
LOYAL_HIGH_VALUE = "Loyal High-Value Customer"
BUDGET_LOYAL = "Budget Loyal Customer"

# Recommendation Categories
CATEGORY_CONTRACT = "Contract"
CATEGORY_PRICING = "Pricing"
CATEGORY_SERVICE = "Service"
CATEGORY_LOYALTY = "Loyalty"
CATEGORY_RETENTION = "Retention"
CATEGORY_PAYMENT = "Payment"
CATEGORY_SECURITY = "Security"
CATEGORY_SUPPORT = "Support"
CATEGORY_ENGAGEMENT = "Engagement"
CATEGORY_GENERAL = "General"


# HELPER FUNCTIONS
def add_recommendation(
    recommendations,
    category,
    priority,
    message
):
    # Prevent duplicate recommendations
    existing_messages = {
        recommendation["Message"]
        for recommendation in recommendations
    }

    if message not in existing_messages:

        recommendations.append({
            "Category": category,
            "Priority": priority,
            "Message": message
        })


# RISK LEVEL

def get_risk_level(probability):

    if probability >= CRITICAL_RISK:
        return "Critical"
    elif probability >= HIGH_RISK:
        return "High"
    elif probability >= MEDIUM_RISK:
        return "Medium"
    else:
        return "Low"


# BUSINESS PRIORITY


def get_priority(probability):

    if probability >= CRITICAL_RISK:
        return "Immediate Action"
    elif probability >= HIGH_RISK:
        return "High"
    elif probability >= MEDIUM_RISK:
        return "Medium"
    else:
        return "Low"


# SORT RECOMMENDATIONS

def sort_recommendations(recommendations):
  
    priority_order = {
        "Critical": 0,
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    recommendations.sort(
        key=lambda recommendation:
        priority_order.get(
            recommendation["Priority"],
            99
        )

    )
    return recommendations


# CONTRACT RULES

def contract_rules(customer, recommendations):
   
    contract = customer.get("Contract", "")

    if contract == "Month-to-month":
        add_recommendation(
            recommendations,
            CATEGORY_CONTRACT,
            PRIORITY_CRITICAL,
            "Offer a discount for switching to a One-Year or Two-Year contract."
        )
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_HIGH,
            "Assign this customer to the retention campaign for contract conversion."
        )

    elif contract == "One year":
        add_recommendation(
            recommendations,
            CATEGORY_CONTRACT,
            PRIORITY_MEDIUM,
            "Promote a Two-Year contract with additional loyalty benefits."
        )

    elif contract == "Two year":
        add_recommendation(
            recommendations,
            CATEGORY_LOYALTY,
            PRIORITY_LOW,
            "Reward the customer with exclusive loyalty benefits."
        )


# TENURE RULES

def tenure_rules(customer, recommendations):
   
    tenure = customer.get("tenure", 0)

    if tenure < NEW_CUSTOMER:
        add_recommendation(
            recommendations,
            CATEGORY_LOYALTY,
            PRIORITY_HIGH,
            "Enroll customer in the New Customer Loyalty Program."
        )
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_MEDIUM,
            "Schedule a follow-up call during the first three months."
        )

    elif tenure >= LOYAL_CUSTOMER:

        add_recommendation(
            recommendations,
            CATEGORY_LOYALTY,
            PRIORITY_LOW,
            "Reward customer with VIP membership."
        )
        add_recommendation(
            recommendations,
            CATEGORY_LOYALTY,
            PRIORITY_LOW,
            "Offer early access to premium services."
        )


# PRICING RULES


def pricing_rules(customer, recommendations):
    
    charges = customer.get("MonthlyCharges", 0)

    if charges >= VERY_HIGH_MONTHLY_CHARGE:
        add_recommendation(
            recommendations,
            CATEGORY_PRICING,
            PRIORITY_CRITICAL,
            "Offer a premium bundle discount immediately."
        )

    elif charges >= HIGH_MONTHLY_CHARGE:
        add_recommendation(
            recommendations,
            CATEGORY_PRICING,
            PRIORITY_HIGH,
            "Provide a personalized pricing offer."
        )
        add_recommendation(
            recommendations,
            CATEGORY_PRICING,
            PRIORITY_MEDIUM,
            "Recommend a more cost-effective service bundle."
        )


# PAYMENT METHOD RULES


def payment_rules(customer, recommendations):
    """
    Recommendations based on payment method.
    """

    payment = customer.get("PaymentMethod", "")

    if payment == "Electronic check":

        add_recommendation(
            recommendations,
            CATEGORY_PAYMENT,
            PRIORITY_MEDIUM,
            "Encourage Auto-Pay using Bank Transfer or Credit Card."
        )
        add_recommendation(
            recommendations,
            CATEGORY_PAYMENT,
            PRIORITY_LOW,
            "Provide cashback for switching to automatic payments."
        )



# INTERNET SERVICE RULES


def internet_rules(customer, recommendations):
   
    internet = customer.get("InternetService", "")

    if internet == "Fiber optic":
        add_recommendation(
            recommendations,
            CATEGORY_SERVICE,
            PRIORITY_MEDIUM,
            "Monitor service quality due to higher churn among Fiber customers."
        )

    elif internet == "DSL":
        add_recommendation(
            recommendations,
            CATEGORY_SERVICE,
            PRIORITY_LOW,
            "Offer speed upgrade packages."
        )



# TECH SUPPORT RULES


def tech_support_rules(customer, recommendations):
   
    if customer.get("TechSupport", "") == "No":
        add_recommendation(
            recommendations,
            CATEGORY_SUPPORT,
            PRIORITY_HIGH,
            "Provide a free 3-month Tech Support trial."
        )

# ONLINE SECURITY RULES

def security_rules(customer, recommendations):

    if customer.get("OnlineSecurity", "") == "No":
        add_recommendation(
            recommendations,
            CATEGORY_SECURITY,
            PRIORITY_HIGH,
            "Recommend the Online Security package."
        )

# ONLINE BACKUP RULES

def backup_rules(customer, recommendations):
   
    if customer.get("OnlineBackup", "") == "No":
        add_recommendation(
            recommendations,
            CATEGORY_SERVICE,
            PRIORITY_MEDIUM,
            "Offer discounted Online Backup services."
        )


# DEVICE PROTECTION RULES

def device_protection_rules(customer, recommendations):

    if customer.get("DeviceProtection", "") == "No":
        add_recommendation(
            recommendations,
            CATEGORY_SERVICE,
            PRIORITY_MEDIUM,
            "Promote Device Protection plans."
        )


# STREAMING RULES

def streaming_rules(customer, recommendations):

    tv = customer.get("StreamingTV", "")
    movies = customer.get("StreamingMovies", "")

    if tv == "No" and movies == "No":
        add_recommendation(
            recommendations,
            CATEGORY_ENGAGEMENT,
            PRIORITY_LOW,
            "Recommend an Entertainment Bundle with TV and Movies."
        )



# PAPERLESS BILLING RULES

def paperless_rules(customer, recommendations):

    if customer.get("PaperlessBilling", "") == "Yes":
        add_recommendation(
            recommendations,
            CATEGORY_ENGAGEMENT,
            PRIORITY_LOW,
            "Send personalized digital offers and loyalty emails."
        )


# SEGMENT RULES

def segment_rules(segment, recommendations):

    if segment == AT_RISK:
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_CRITICAL,
            "Assign customer to the Priority Retention Team immediately."
        )
        add_recommendation(
            recommendations,
            CATEGORY_PRICING,
            PRIORITY_HIGH,
            "Offer an exclusive loyalty discount."
        )
        add_recommendation(
            recommendations,
            CATEGORY_ENGAGEMENT,
            PRIORITY_HIGH,
            "Schedule a proactive customer care call."
        )

    elif segment == LOYAL_HIGH_VALUE:
        add_recommendation(
            recommendations,
            CATEGORY_LOYALTY,
            PRIORITY_LOW,
            "Reward customer with Premium Loyalty Membership."
        )
        add_recommendation(
            recommendations,
            CATEGORY_LOYALTY,
            PRIORITY_LOW,
            "Provide early access to new telecom plans."
        )

    elif segment == BUDGET_LOYAL:
        add_recommendation(
            recommendations,
            CATEGORY_PRICING,
            PRIORITY_MEDIUM,
            "Recommend affordable service upgrades."
        )
        add_recommendation(
            recommendations,
            CATEGORY_ENGAGEMENT,
            PRIORITY_LOW,
            "Promote value-for-money bundled plans."
        )


# CHURN PREDICTION RULES

def churn_rules(churn_prediction,
                churn_probability,
                recommendations):
   
    if churn_prediction == 1:
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_CRITICAL,
            "Contact the customer within the next 24 hours."
        )
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_HIGH,
            "Create a personalized retention campaign."
        )

    if churn_probability >= CRITICAL_RISK:
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_CRITICAL,
            "Escalate the customer to the Senior Retention Team."
        )

    elif churn_probability >= HIGH_RISK:
        add_recommendation(
            recommendations,
            CATEGORY_RETENTION,
            PRIORITY_HIGH,
            "Monitor customer activity closely over the next 30 days."
        )

    elif churn_probability >= MEDIUM_RISK:
        add_recommendation(
            recommendations,
            CATEGORY_ENGAGEMENT,
            PRIORITY_MEDIUM,
            "Send personalized promotional offers."
        )


# MAIN RETENTION ADVISOR

def retention_advisor(
    customer,
    churn_prediction,
    churn_probability,
    segment
):
    recommendations = []

    # Risk Assessment
    risk_level = get_risk_level(churn_probability)

    business_priority = get_priority(churn_probability)


    # Execute Business Rules
    contract_rules(customer, recommendations)
    tenure_rules(customer, recommendations)
    pricing_rules(customer, recommendations)
    payment_rules(customer, recommendations)
    internet_rules(customer, recommendations)
    tech_support_rules(customer, recommendations)
    security_rules(customer, recommendations)
    backup_rules(customer, recommendations)
    device_protection_rules(customer, recommendations)
    streaming_rules(customer, recommendations)
    paperless_rules(customer, recommendations)
    segment_rules(segment, recommendations)
    churn_rules(
        churn_prediction,
        churn_probability,
        recommendations
    )

    # Sort Recommendations

    recommendations = sort_recommendations(
        recommendations
    )


    # Default Recommendation
    if len(recommendations) == 0:
        add_recommendation(
            recommendations,
            CATEGORY_GENERAL,
            PRIORITY_LOW,
            "No immediate retention action required."
        )



    # Final Business Report
    
    report = {

        "Risk Level": risk_level,
        "Business Priority": business_priority,
        "Customer Segment": segment,
        "Churn Prediction":
        "Likely to Churn"
        if churn_prediction == 1
        else
        "Not Likely to Churn",
        "Churn Probability (%)":
        round(churn_probability * 100, 2),
        "Total Recommendations":
        len(recommendations),
        "Recommendations":
        recommendations

    }
    return report



# # =====================================================================
# # TESTING SECTION
# # =====================================================================

# if __name__ == "__main__":

#     print("\n")
#     print("=" * 70)
#     print("      TELECOM CUSTOMER INTELLIGENCE SYSTEM")
#     print("            RETENTION ADVISOR TEST")
#     print("=" * 70)

#     # ==============================================================
#     # SAMPLE CUSTOMER 1
#     # High Risk Customer
#     # ==============================================================

#     customer_1 = {

#         "gender": "Male",

#         "SeniorCitizen": 0,

#         "Partner": "No",

#         "Dependents": "No",

#         "tenure": 4,

#         "PhoneService": "Yes",

#         "MultipleLines": "No",

#         "InternetService": "Fiber optic",

#         "OnlineSecurity": "No",

#         "OnlineBackup": "No",

#         "DeviceProtection": "No",

#         "TechSupport": "No",

#         "StreamingTV": "No",

#         "StreamingMovies": "No",

#         "Contract": "Month-to-month",

#         "PaperlessBilling": "Yes",

#         "PaymentMethod": "Electronic check",

#         "MonthlyCharges": 105,

#         "TotalCharges": 420

#     }

#     report = retention_advisor(

#         customer=customer_1,

#         churn_prediction=1,

#         churn_probability=0.91,

#         segment=AT_RISK

#     )

#     print("\n")
#     print("=" * 70)
#     print("CUSTOMER 1")
#     print("=" * 70)

#     print(f"Segment              : {report['Customer Segment']}")
#     print(f"Risk Level           : {report['Risk Level']}")
#     print(f"Business Priority    : {report['Business Priority']}")
#     print(f"Prediction           : {report['Churn Prediction']}")
#     print(f"Probability          : {report['Churn Probability (%)']}%")
#     print(f"Recommendations      : {report['Total Recommendations']}")

#     print("\nRecommended Actions\n")

#     for i, rec in enumerate(report["Recommendations"], start=1):

#         print(f"{i}. [{rec['Priority']}] {rec['Category']}")

#         print(f"   {rec['Message']}\n")



#     # ==============================================================
#     # SAMPLE CUSTOMER 2
#     # Loyal Customer
#     # ==============================================================

#     customer_2 = {

#         "gender": "Female",

#         "SeniorCitizen": 0,

#         "Partner": "Yes",

#         "Dependents": "Yes",

#         "tenure": 72,

#         "PhoneService": "Yes",

#         "MultipleLines": "Yes",

#         "InternetService": "Fiber optic",

#         "OnlineSecurity": "Yes",

#         "OnlineBackup": "Yes",

#         "DeviceProtection": "Yes",

#         "TechSupport": "Yes",

#         "StreamingTV": "Yes",

#         "StreamingMovies": "Yes",

#         "Contract": "Two year",

#         "PaperlessBilling": "No",

#         "PaymentMethod": "Bank transfer (automatic)",

#         "MonthlyCharges": 94,

#         "TotalCharges": 6900

#     }

#     report = retention_advisor(

#         customer=customer_2,

#         churn_prediction=0,

#         churn_probability=0.08,

#         segment=LOYAL_HIGH_VALUE

#     )

#     print("\n")
#     print("=" * 70)
#     print("CUSTOMER 2")
#     print("=" * 70)

#     print(f"Segment              : {report['Customer Segment']}")
#     print(f"Risk Level           : {report['Risk Level']}")
#     print(f"Business Priority    : {report['Business Priority']}")
#     print(f"Prediction           : {report['Churn Prediction']}")
#     print(f"Probability          : {report['Churn Probability (%)']}%")
#     print(f"Recommendations      : {report['Total Recommendations']}")

#     print("\nRecommended Actions\n")

#     for i, rec in enumerate(report["Recommendations"], start=1):

#         print(f"{i}. [{rec['Priority']}] {rec['Category']}")

#         print(f"   {rec['Message']}\n")



#     # ==============================================================
#     # SAMPLE CUSTOMER 3
#     # Budget Loyal
#     # ==============================================================

#     customer_3 = {

#         "gender": "Female",

#         "SeniorCitizen": 0,

#         "Partner": "Yes",

#         "Dependents": "No",

#         "tenure": 30,

#         "PhoneService": "Yes",

#         "MultipleLines": "No",

#         "InternetService": "DSL",

#         "OnlineSecurity": "No",

#         "OnlineBackup": "No",

#         "DeviceProtection": "No",

#         "TechSupport": "No",

#         "StreamingTV": "No",

#         "StreamingMovies": "No",

#         "Contract": "One year",

#         "PaperlessBilling": "Yes",

#         "PaymentMethod": "Credit card (automatic)",

#         "MonthlyCharges": 55,

#         "TotalCharges": 1650

#     }

#     report = retention_advisor(

#         customer=customer_3,

#         churn_prediction=0,

#         churn_probability=0.32,

#         segment=BUDGET_LOYAL

#     )

#     print("\n")
#     print("=" * 70)
#     print("CUSTOMER 3")
#     print("=" * 70)

#     print(f"Segment              : {report['Customer Segment']}")
#     print(f"Risk Level           : {report['Risk Level']}")
#     print(f"Business Priority    : {report['Business Priority']}")
#     print(f"Prediction           : {report['Churn Prediction']}")
#     print(f"Probability          : {report['Churn Probability (%)']}%")
#     print(f"Recommendations      : {report['Total Recommendations']}")

#     print("\nRecommended Actions\n")

#     for i, rec in enumerate(report["Recommendations"], start=1):

#         print(f"{i}. [{rec['Priority']}] {rec['Category']}")

#         print(f"   {rec['Message']}\n")

#     print("=" * 70)
#     print("Retention Advisor Test Completed Successfully")
#     print("=" * 70)