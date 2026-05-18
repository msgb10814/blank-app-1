import streamlit as st

# 앱 제목 및 설명 (주석으로 달아주신 핵심 논리를 화면에 표시합니다)
st.title("🔢 가장 큰 수 찾기 앱")
st.markdown("### 💡 알고리즘 원리")
st.info("""
세 개의 정수 중에서 가장 큰 수를 찾으려면 **최소 두 번의 비교**가 필요합니다.
1. 먼저 첫 번째 수와 두 번째 수를 비교하여 둘 중 더 큰 값을 찾습니다. (1회 비교)
2. 그 다음, 거기서 찾은 큰 값과 세 번째 수를 비교하여 최종적으로 가장 큰 값을 찾습니다. (1회 비교)
            
따라서 **총 두 번의 비교**를 통해 가장 큰 수를 알아낼 수 있습니다.
""")

st.write("---") # 구분선

# 1. 원래의 input()을 스트림릿의 입력창으로 변경 (원래 변수명 유지)
num1 = st.number_input('첫 번째 수:', value=0, step=1)
num2 = st.number_input('두 번째 수:', value=0, step=1)
num3 = st.number_input('세 번째 수:', value=0, step=1)

# '결과 확인' 버튼을 누르면 비교 로직이 실행됩니다.
if st.button("가장 큰 수 찾아보기"):
    st.subheader("📊 비교 결과")
    
    # 2. 원래 작성하신 if-else 구조를 단 한 글자도 바꾸지 않고 그대로 유지했습니다.
    # (print문만 웹 화면 출력을 위해 st.write로 변경)
    if num1 > num2:
        if num1 > num3:
            st.success(f"가장 큰 수는 **{num1}**입니다. (1번 숫자가 가장 큼)")
        else: 
            st.success(f"가장 큰 수는 **{num3}**입니다. (3번 숫자가 가장 큼)")
    else:
        if num2 > num3:
            st.success(f"가장 큰 수는 **{num2}**입니다. (2번 숫자가 가장 큼)")
        else:
            st.success(f"가장 큰 수는 **{num3}**입니다. (3번 숫자가 가장 큼)")