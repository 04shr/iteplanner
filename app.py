import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Smart India Itinerary Planner",
    page_icon="✈️",
    layout="wide"
)

# Title and introduction
st.title("✈️ Smart India Itinerary Planner")
st.markdown("Get a complete travel plan with suggested places, timings, commute options, and cultural highlights tailored to your preferences.")

# Sidebar for user inputs
with st.sidebar:
    st.header("Trip Details")
    
    destination = st.selectbox(
        "Destination",
        ["Delhi", "Mumbai", "Jaipur", "Agra", "Goa", "Varanasi", "Hampi", "Kerala", "Rishikesh", "Darjeeling"]
    )
    
    col1, col2 = st.columns(2)
    start_date = col1.date_input("Start Date", datetime.now() + timedelta(days=30))
    end_date = col2.date_input("End Date", datetime.now() + timedelta(days=35))
    
    num_travelers = st.number_input("Number of Travelers", min_value=1, value=2)
    
    st.header("Preferences")
    
    travel_pace = st.select_slider(
        "Travel Pace",
        options=["Relaxed", "Moderate", "Intensive"]
    )
    
    interests = st.multiselect(
        "Interests",
        ["History & Monuments", "Food & Dining", "Nature & Wildlife", 
         "Shopping & Crafts", "Temples & Spirituality", "Cultural Experiences", "Adventure"],
        default=["History & Monuments", "Food & Dining"]
    )
    
    budget_level = st.select_slider(
        "Budget Level",
        options=["Budget", "Moderate", "Luxury"]
    )
    
    accommodation_preference = st.radio(
        "Accommodation Preference",
        ["Hotel", "Hostel", "Homestay", "Resort"]
    )
    
    special_requirements = st.text_area("Any special requirements or accessibility needs?")
    
    generate_btn = st.button("Generate Itinerary", type="primary")

# Sample data for different Indian destinations
destinations_data = {
    "Delhi": {
        "attractions": [
            "Red Fort", "Qutub Minar", "Humayun's Tomb", 
            "India Gate", "Lotus Temple", "Akshardham Temple", 
            "Jama Masjid", "Chandni Chowk", "Rajpath", 
            "National Museum", "Lodhi Gardens", "Raj Ghat"
        ],
        "restaurants": [
            "Karim's", "Bukhara", "Paranthe Wali Gali", 
            "Indian Accent", "Saravana Bhavan", "Andhra Bhavan", 
            "Khan Chacha", "Gulati", "Dilli Haat Food Stalls", "Moti Mahal"
        ],
        "transportation": ["Metro", "Auto Rickshaw", "Taxi", "Bus", "Walking"],
        "cultural_tips": [
            "Dress modestly when visiting religious sites",
            "Remove shoes before entering temples and homes",
            "Use your right hand for eating and giving/receiving items",
            "Head wobble can mean 'yes' or acknowledgment",
            "Haggling is expected in local markets",
            "Be cautious of crowded areas, especially as a tourist"
        ]
    },
    "Mumbai": {
        "attractions": [
            "Gateway of India", "Marine Drive", "Elephanta Caves", 
            "Chhatrapati Shivaji Terminus", "Juhu Beach", "Haji Ali Dargah", 
            "Sanjay Gandhi National Park", "Siddhivinayak Temple", "Kanheri Caves", "Colaba Causeway"
        ],
        "restaurants": [
            "Trishna", "Leopold Cafe", "Britannia & Co.", 
            "Bademiya", "Swati Snacks", "Cafe Madras", 
            "The Bombay Canteen", "Pav Bhaji at Juhu Beach", "Chetana", "Khyber"
        ],
        "transportation": ["Local Train", "Metro", "Bus", "Taxi", "Auto Rickshaw", "Ferry"],
        "cultural_tips": [
            "Mumbai locals are usually in a rush - try to keep up with the pace",
            "Local trains have separate compartments for women",
            "During monsoon (June-September), carry an umbrella",
            "The 'Bombay time' means people might be 15-30 minutes late",
            "Street food is popular but choose hygienically prepared options",
            "Avoid wearing flashy jewelry in crowded areas"
        ]
    },
    "Jaipur": {
        "attractions": [
            "Amber Fort", "Hawa Mahal", "City Palace", 
            "Jantar Mantar", "Jal Mahal", "Albert Hall Museum", 
            "Nahargarh Fort", "Jaigarh Fort", "Birla Mandir", "Galtaji Temple"
        ],
        "restaurants": [
            "Laxmi Misthan Bhandar", "Suvarna Mahal", "Chokhi Dhani", 
            "Niros", "Peacock Rooftop Restaurant", "Handi", 
            "Lakshmi Mishthan Bhandar", "Rawat Misthan Bhandar", "Four Seasons", "Tadka Restaurant"
        ],
        "transportation": ["Auto Rickshaw", "Taxi", "E-Rickshaw", "City Bus", "Rental Bike"],
        "cultural_tips": [
            "Jaipur is known as 'Pink City' - many buildings in old city are terracotta pink",
            "Bargaining is expected in markets, start at 50% of quoted price",
            "Traditional Rajasthani attire is colorful - appreciate local fashion",
            "Respect cows on streets as they are considered sacred",
            "Summer days can be extremely hot - stay hydrated",
            "Try local Rajasthani cuisine like Dal Baati Churma"
        ]
    },
    "Agra": {
        "attractions": [
            "Taj Mahal", "Agra Fort", "Fatehpur Sikri", 
            "Mehtab Bagh", "Itimad-ud-Daulah", "Akbar's Tomb", 
            "Kinari Bazaar", "Jama Masjid", "Anguri Bagh", "Ram Bagh"
        ],
        "restaurants": [
            "Pind Balluchi", "Dasaprakash", "Esphahan", 
            "Pinch of Spice", "Joney's Place", "Sheroes Hangout", 
            "Taj Terrace", "El Clasico", "The Silk Route", "Jhankar"
        ],
        "transportation": ["Auto Rickshaw", "Cycle Rickshaw", "Taxi", "Tempo", "Walking"],
        "cultural_tips": [
            "Visit Taj Mahal during sunrise for best views and fewer crowds",
            "Dress modestly when visiting religious sites",
            "Be prepared for persistent touts and guides",
            "Carry small denomination notes for small purchases",
            "Agra's famous sweet is Petha - try the different varieties",
            "The city can get very hot in summer, plan indoor activities during peak heat"
        ]
    },
    "Goa": {
        "attractions": [
            "Calangute Beach", "Baga Beach", "Basilica of Bom Jesus", 
            "Fort Aguada", "Dudhsagar Falls", "Anjuna Flea Market", 
            "Chapora Fort", "Palolem Beach", "Spice Plantations", "Old Goa Churches"
        ],
        "restaurants": [
            "Thalassa", "Fisherman's Wharf", "Gunpowder", 
            "Mum's Kitchen", "Britto's", "Vinayak", 
            "Martin's Corner", "Curlies", "Infantaria", "Souza Lobo"
        ],
        "transportation": ["Rented Scooter/Bike", "Taxi", "Auto Rickshaw", "Local Bus", "Ferry"],
        "cultural_tips": [
            "Goa has a relaxed lifestyle - locals call it 'Susegad'",
            "Respect beach cleanliness rules and marine life",
            "Trance parties are common in certain beaches - check local listings",
            "Try Feni, the local cashew/coconut spirit",
            "Cover up when visiting churches despite beach atmosphere",
            "Water sports have designated areas - avoid unofficial operators"
        ]
    },
    "Varanasi": {
        "attractions": [
            "Dashashwamedh Ghat", "Kashi Vishwanath Temple", "Sarnath", 
            "Manikarnika Ghat", "Assi Ghat", "Ramnagar Fort", 
            "Tulsi Manas Temple", "Evening Ganga Aarti", "Bharat Mata Temple", "Alamgir Mosque"
        ],
        "restaurants": [
            "Varanasi Chaat", "Blue Lassi Shop", "Dosa Cafe", 
            "Kashi Chat Bhandar", "Brown Bread Bakery", "Pizzeria Vaatika Cafe", 
            "Aadha-Aadha", "Keshari Restaurant", "Bana Lassi", "Canton Royale"
        ],
        "transportation": ["Auto Rickshaw", "Cycle Rickshaw", "Boat", "Walking", "E-Rickshaw"],
        "cultural_tips": [
            "Varanasi is one of the world's oldest living cities",
            "Photography at cremation ghats is disrespectful",
            "Morning boat ride on Ganges is a must-do experience",
            "City layout can be confusing - use maps or guides",
            "Expect crowds at religious sites and ghats",
            "Try the famous Banarasi Paan (betel leaf preparation)"
        ]
    },
    "Hampi": {
        "attractions": [
            "Virupaksha Temple", "Vittala Temple", "Hampi Bazaar", 
            "Queen's Bath", "Elephant Stables", "Lotus Mahal", 
            "Hemakuta Hill Temples", "Achyutaraya Temple", "Matanga Hill", "Royal Enclosure"
        ],
        "restaurants": [
            "Mango Tree", "Laughing Buddha", "Gopi Island", 
            "Suresh Hotel", "Chill Out Bamboo Hut", "The Goan Corner", 
            "Ravi's Rose Restaurant", "Swapna Mousumi", "Funky Monkey", "New Shanthi"
        ],
        "transportation": ["Auto Rickshaw", "Rented Bicycle", "Rented Scooter", "Coracle", "Walking"],
        "cultural_tips": [
            "Hampi is a UNESCO World Heritage Site with ruins from 14th century",
            "Dress modestly when visiting temples",
            "Bouldering and rock climbing are popular activities",
            "Area is divided into Sacred Centre and Royal Centre",
            "Take adequate water when exploring as it gets hot",
            "Sunrise/sunset views from Matanga Hill or Hemakuta Hill are spectacular"
        ]
    },
    "Kerala": {
        "attractions": [
            "Alleppey Backwaters", "Fort Kochi", "Munnar Tea Gardens", 
            "Varkala Beach", "Periyar Wildlife Sanctuary", "Wayanad", 
            "Kovalam Beach", "Athirappilly Falls", "Bekal Fort", "Kumarakom"
        ],
        "restaurants": [
            "Grand Pavilion", "History Restaurant", "Chakara", 
            "Dal Roti", "Fusion Bay", "Dhe Puttu", 
            "Kayees Rahmathullah Hotel", "Paragon", "Malabar Junction", "Spice Village"
        ],
        "transportation": ["KSRTC Bus", "Ferry", "Auto Rickshaw", "Taxi", "Houseboat"],
        "cultural_tips": [
            "Kerala is known as 'God's Own Country'",
            "Traditional Kerala cuisine is served on banana leaf",
            "Ayurvedic treatments are popular - research centers before booking",
            "Monsoon (June-August) offers special 'green' experience but limits some activities",
            "Kathakali performances are unique cultural experience",
            "The state has higher literacy rate and different pace of life than some parts of India"
        ]
    },
    "Rishikesh": {
        "attractions": [
            "Laxman Jhula", "Ram Jhula", "Triveni Ghat", 
            "Beatles Ashram", "Neelkanth Mahadev Temple", "Parmarth Niketan", 
            "Rajaji National Park", "Kunjapuri Temple", "Ganga Aarti", "Neer Garh Waterfall"
        ],
        "restaurants": [
            "Little Buddha Cafe", "Chotiwala", "Bistro Nirvana", 
            "Ganga Beach Restaurant", "Freedom Cafe", "Oasis Cafe", 
            "Ramana's Organic Cafe", "Pyramid Cafe", "Ganga View", "Tulsi Restaurant"
        ],
        "transportation": ["Auto Rickshaw", "Taxi", "Walking", "Local Bus", "Rented Bicycle"],
        "cultural_tips": [
            "Rishikesh is known as the 'Yoga Capital of the World'",
            "It's a holy city - alcohol and non-vegetarian food are prohibited",
            "Whitewater rafting is popular between September-June",
            "Evening Ganga Aarti at Parmarth Niketan is a spiritual experience",
            "Many ashrams offer yoga and meditation courses",
            "Respect the spiritual atmosphere of the town"
        ]
    },
    "Darjeeling": {
        "attractions": [
            "Tiger Hill", "Darjeeling Himalayan Railway", "Batasia Loop", 
            "Peace Pagoda", "Happy Valley Tea Estate", "Padmaja Naidu Himalayan Zoological Park", 
            "Himalayan Mountaineering Institute", "Observatory Hill", "Ghoom Monastery", "Mall Road"
        ],
        "restaurants": [
            "Glenary's", "Keventer's", "Kunga Restaurant", 
            "Sonam's Kitchen", "Nathmull's Tea Room", "Lunar Restaurant", 
            "Hot Stimulating Cafe", "Dekevas", "Tom & Jerry's", "Park Restaurant"
        ],
        "transportation": ["Shared Jeep", "Taxi", "Walking", "Toy Train", "Cycle Rickshaw"],
        "cultural_tips": [
            "Darjeeling is famous for its tea - visit a tea garden and try tea tasting",
            "Sunrise view of Kanchenjunga from Tiger Hill is magnificent",
            "Toy Train (DHR) is a UNESCO World Heritage Site",
            "Weather can change quickly - carry layers even in summer",
            "Local Tibetan and Nepali influence in culture and cuisine",
            "Darjeeling has early sunrise/sunset times - plan accordingly"
        ]
    }
}

# Function to generate itinerary
def generate_itinerary(destination, start_date, end_date, interests, travel_pace, budget_level):
    # Calculate number of days
    num_days = (end_date - start_date).days + 1
    
    # Determine number of activities per day based on travel pace
    activities_per_day = {
        "Relaxed": 3,
        "Moderate": 4,
        "Intensive": 6
    }[travel_pace]
    
    # Get destination data
    if destination in destinations_data:
        dest_data = destinations_data[destination].copy()
    else:
        # Fallback to Delhi if destination not found
        dest_data = destinations_data["Delhi"].copy()
    
    # Generate itinerary
    itinerary = []
    
    # Create copies of attractions and restaurants to avoid modifying the original
    attractions = dest_data["attractions"].copy()
    restaurants = dest_data["restaurants"].copy()
    
    current_date = start_date
    for day in range(num_days):
        daily_schedule = []
        
        # Morning activity
        start_time = datetime.strptime("09:00", "%H:%M").time()
        if attractions:
            attraction = random.choice(attractions)
            attractions.remove(attraction)  # Remove to avoid duplicates
        else:
            # If we run out of attractions, refill the list
            attractions = dest_data["attractions"].copy()
            attraction = random.choice(attractions)
            attractions.remove(attraction)
            
        daily_schedule.append({
            "time": start_time.strftime("%H:%M"),
            "activity": f"Visit {attraction}",
            "category": "Attraction",
            "transportation": random.choice(dest_data["transportation"]),
            "duration": "2 hours"
        })
        
        # Lunch
        start_time = datetime.strptime("12:00", "%H:%M").time()
        if restaurants:
            restaurant = random.choice(restaurants)
            restaurants.remove(restaurant)  # Remove to avoid duplicates
        else:
            # If we run out of restaurants, refill the list
            restaurants = dest_data["restaurants"].copy()
            restaurant = random.choice(restaurants)
            restaurants.remove(restaurant)
            
        daily_schedule.append({
            "time": start_time.strftime("%H:%M"),
            "activity": f"Lunch at {restaurant}",
            "category": "Dining",
            "transportation": random.choice(dest_data["transportation"]),
            "duration": "1.5 hours"
        })
        
        # Afternoon activities (1-2 based on pace)
        afternoon_activities = min(activities_per_day - 2, len(attractions))
        start_time = datetime.strptime("14:00", "%H:%M").time()
        
        for i in range(afternoon_activities):
            if attractions:
                attraction = random.choice(attractions)
                attractions.remove(attraction)  # Remove to avoid duplicates
                
                # Calculate time (simple approach)
                hour = 14 + i*2
                time_str = f"{hour:02d}:00"
                start_time = datetime.strptime(time_str, "%H:%M").time()
                
                daily_schedule.append({
                    "time": start_time.strftime("%H:%M"),
                    "activity": f"Explore {attraction}",
                    "category": "Attraction",
                    "transportation": random.choice(dest_data["transportation"]),
                    "duration": "2 hours"
                })
            else:
                # If we run out of attractions, refill the list
                attractions = dest_data["attractions"].copy()
        
        # Dinner
        start_time = datetime.strptime("19:00", "%H:%M").time()
        if restaurants:
            restaurant = random.choice(restaurants)
            restaurants.remove(restaurant)  # Remove to avoid duplicates
        else:
            # If we run out of restaurants, refill the list
            restaurants = dest_data["restaurants"].copy()
            restaurant = random.choice(restaurants)
            restaurants.remove(restaurant)
            
        daily_schedule.append({
            "time": start_time.strftime("%H:%M"),
            "activity": f"Dinner at {restaurant}",
            "category": "Dining",
            "transportation": random.choice(dest_data["transportation"]),
            "duration": "2 hours"
        })
        
        # Evening activity (if intensive pace)
        if travel_pace == "Intensive" and attractions:
            start_time = datetime.strptime("21:30", "%H:%M").time()
            if "Cultural Experiences" in interests:
                activity = "Evening cultural performance" 
            else:
                attraction = random.choice(attractions)
                attractions.remove(attraction)
                activity = f"Evening visit to {attraction}"
                
            daily_schedule.append({
                "time": start_time.strftime("%H:%M"),
                "activity": activity,
                "category": "Entertainment",
                "transportation": random.choice(dest_data["transportation"]),
                "duration": "2 hours"
            })
        
        # Add the daily schedule to the itinerary
        itinerary.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "day": f"Day {day + 1}",
            "schedule": daily_schedule
        })
        
        # Move to next day
        current_date += timedelta(days=1)
    
    return itinerary, dest_data["cultural_tips"]

# Main content
if "itinerary" not in st.session_state:
    st.session_state.itinerary = None
    st.session_state.cultural_tips = None

# When the user clicks "Generate Itinerary"
if generate_btn or st.session_state.itinerary is not None:
    if generate_btn:
        with st.spinner("Generating your perfect itinerary..."):
            st.session_state.itinerary, st.session_state.cultural_tips = generate_itinerary(
                destination, 
                start_date, 
                end_date, 
                interests, 
                travel_pace, 
                budget_level
            )
    
    # Display trip summary
    st.header(f"Your {destination} Adventure")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Duration", f"{(end_date - start_date).days + 1} days")
    col2.metric("Travelers", num_travelers)
    col3.metric("Pace", travel_pace)
    
    # Trip overview
    st.subheader("Trip Overview")
    st.info(f"Discover {destination} with this customized itinerary tailored to your interests in {', '.join(interests)}. "
            f"Your {travel_pace.lower()}-paced trip focuses on experiencing the best of {destination} "
            f"while keeping within a {budget_level.lower()} budget.")
    
    # Cultural tips
    if st.session_state.cultural_tips:
        with st.expander("Cultural Tips & Local Customs", expanded=True):
            for i, tip in enumerate(st.session_state.cultural_tips):
                st.markdown(f"- {tip}")
    
    # Detailed itinerary
    st.subheader("Daily Itinerary")
    
    # Tabs for each day
    day_tabs = st.tabs([day["day"] for day in st.session_state.itinerary])
    
    for i, tab in enumerate(day_tabs):
        with tab:
            day_data = st.session_state.itinerary[i]
            st.subheader(f"{day_data['day']} - {datetime.strptime(day_data['date'], '%Y-%m-%d').strftime('%A, %b %d')}")
            
            # Create a table for the day's schedule
            schedule_df = pd.DataFrame(day_data["schedule"])
            st.dataframe(
                schedule_df[["time", "activity", "transportation", "duration"]],
                hide_index=True,
                use_container_width=True
            )
            
            # Map placeholder (in a real app, this would be an actual map)
            st.subheader("Daily Route Map")
            st.info("Interactive map would display here, showing the route between today's destinations.")
    
    # Download button (would generate a PDF in a real app)
    st.download_button(
        label="Download Itinerary PDF",
        data="Sample PDF content",
        file_name=f"{destination}_Itinerary.pdf",
        mime="application/pdf",
    )
    
    # Reset button
    if st.button("Create New Itinerary"):
        st.session_state.itinerary = None
        st.session_state.cultural_tips = None
        st.rerun()

else:
    # Show sample itinerary screenshot or instructions
    st.info("Fill in your trip details in the sidebar and click 'Generate Itinerary' to get started!")
    
    # Sample image or features explanation
    st.subheader("Features")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("- **Personalized day-by-day planning**")
        st.markdown("- **Local transportation suggestions**")
        st.markdown("- **Dining recommendations**")
    
    with col2:
        st.markdown("- **Cultural tips and insights**")
        st.markdown("- **Flexible pace options**")
        st.markdown("- **Downloadable itineraries**")