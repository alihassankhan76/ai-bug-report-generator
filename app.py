import streamlit as st
from report_gen import generate_report

st.set_page_config(page_title="AI Bug Report Generator")

st.title("🛡️ AI Bug Bounty Report Generator")

with st.form("bug_form"):
    vuln_type = st.selectbox("Vulnerability Type", [
        "IDOR", "2FA Bypass", "OAuth Misconfiguration", "Business Logic", "Privilege Escalation"
    ])
    scope = st.text_input("Scope / Asset URL")
    steps = st.text_area("Steps to Reproduce")
    impact = st.text_area("Impact")
    fix = st.text_area("Suggested Fix (Optional)", "")
    
    submitted = st.form_submit_button("Generate Report")

if submitted:
    with st.spinner("Generating report..."):
        result = generate_report(vuln_type, scope, steps, impact, fix)
        st.success("✅ Report Generated!")
        st.code(result, language='markdown')
