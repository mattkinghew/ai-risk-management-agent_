import numpy as np
import pandas as pd
import json
# 假設我們有一個串接 LLM 的自訂模組
# from llm_service import generate_ai_insight 

class AIRiskAgent:
    def __init__(self, confidence_level=0.95):
        self.confidence_level = confidence_level
        self.alpha = (1.0 - confidence_level) * 100.0

    def _robust_var_calculation(self, stock_returns, weights):
        """
        【內部量化引擎】應用今天學到的「防彈邏輯」
        徹底剝離 Pandas 外衣，使用純 Numpy 運算防範 TypeError
        """
        try:
            # 1. 強制轉換為純數值矩陣
            rets_array = np.asarray(stock_returns)
            
            # 2. 強制壓平權重，對付來自 API 結構不明的 JSON/Dict
            if isinstance(weights, dict):
                w_array = np.array(list(weights.values())).flatten()
            else:
                w_array = np.asarray(weights).flatten()
                
            # 3. 核心運算
            port_ret = np.dot(rets_array, w_array).flatten()
            var_val = -np.percentile(port_ret, self.alpha)
            
            # 4. 取出純量並轉型，確保 JSON 序列化不報錯
            return float(var_val.item() if isinstance(var_val, np.ndarray) else var_val)
        
        except Exception as e:
            # AI Engineer 必備：系統崩潰時的優雅降級 (Graceful Degradation)
            return f"Error in quant engine: {str(e)}"

    def generate_risk_report(self, user_profile, stock_returns, weights):
        """
        【AI 代理大腦】結合量化數據與使用者語境
        """
        # 1. 呼叫底層引擎算出極端風險 (VaR)
        calculated_var = self._robust_var_calculation(stock_returns, weights)
        
        if isinstance(calculated_var, str): # 錯誤處理
            return {"status": "failed", "message": calculated_var}

        # 2. 建構給 LLM 的 Prompt (這就是 AI PM/Engineer 的 Prompt Engineering 功力)
        prompt = f"""
        你是一位專業且具備同理心的財富管理顧問。
        你的客戶是一位 {user_profile['age']} 歲的 {user_profile['risk_tolerance']} 型投資人。
        該客戶目前的投資組合，在 {self.confidence_level*100}% 的信心水準下，
        其單日最大可能虧損比例 (VaR) 高達 {calculated_var * 100:.2f}%。
        
        請用白話文（避免艱澀術語）向客戶解釋這個風險代表什麼意思，
        並給出 2 個具體的資產配置調整建議。
        """
        
        # 3. 呼叫 LLM (此處為示意)
        # ai_insight = generate_ai_insight(prompt)
        ai_insight = "AI 生成的白話文風險解釋與建議..." 
        
        return {
            "status": "success",
            "quantitative_metrics": {"VaR_95": calculated_var},
            "ai_advisor_insight": ai_insight
        }

# 商業應用測試
agent = AIRiskAgent()
user = {"age": 65, "risk_tolerance": "保守 (Conservative)"}
# 假設 student_stock_returns 和 mv_weights 已就緒
# report = agent.generate_risk_report(user, student_stock_returns, mv_weights)