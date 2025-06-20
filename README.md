🏠 Maharashtra Real Estate Price Estimator 

App Link:https://realapp-vansh.streamlit.app/


🔍 Overview
This project provides a user-friendly web application built with Streamlit to estimate real estate prices across major cities and districts in Maharashtra, India. The app allows users to select a city, choose a locality, and input the area of a property in square feet to get an instant price estimate based on pre-defined rates.

The tool is designed to serve prospective home buyers, sellers, and real estate agents by offering a quick, visually appealing, and interactive estimation experience.


🎯 Objectives
Provide an interactive UI for users to estimate real estate property prices.

Integrate district-wise and locality-wise rate mapping for Maharashtra.

Display dynamically calculated prices based on user inputs.

Style the app with professional visual themes and clear UI components.


🧩 Features
🌍 District and locality dropdowns for location selection.

📏 Area slider to enter property size.

💰 Instant price estimation based on fixed price-per-sqft.

🎨 Background with house/building image for real estate context.

🖍️ Clean, black, and bold text for maximum readability.

🪟 Semi-transparent layout to enhance visual appeal.



🔧 Steps Involved

1. Environment Setup

 2. App Design (Frontend)
Built entirely with Streamlit.

Injected custom CSS using st.markdown() to enhance aesthetics:

Background image relevant to real estate (e.g., house/building)

Black, bold, large text for improved readability

Light blur and soft transparency for visual clarity

3. Rate Mapping
Hardcoded a dictionary of city-wise and locality-wise property rates (₹/sqft) for:

Mumbai – Andheri, Bandra, Borivali, etc.

Pune – Kothrud, Wakad, Hinjewadi, etc.

Nagpur, Nashik, Solapur, Aurangabad – Key localities in each.

4. User Inputs
Select district from dropdown.

Select locality from corresponding options.

Enter property size using a slider (300–5000 sqft).

5. Price Calculation

 
 6. Output Display
Shows Rate per sqft

Shows Total estimated property price

Styled with black bold fonts and visibility-enhanced containers.


🧪 Example Use Case
Input	- Value
District - 	Pune
Area	- Wakad
Area (sqft) -	1200
Rate per sqft -	₹13,000
Estimated Price -	₹15,60,000


💾 Future Enhancements
Connect to a live real estate API or database for dynamic rate updates.

Add visualizations like price comparison across cities.

Enable CSV uploads for bulk estimation.

Integrate user authentication to save estimates.



✅ Conclusion
The Maharashtra Real Estate Price Estimator project showcases how Streamlit can be used to build powerful and beautiful web applications with minimal code. The app delivers value by enabling instant and intuitive property valuation, helping users make informed decisions.

By using a combination of interactive widgets, fixed rate logic, and clean UI design, this app serves as a great example of real-world utility with simple tools.

