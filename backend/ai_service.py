
import os
import json
import httpx
from typing import List, Dict, Optional, Any

class KimiService:
    """Service to interact with Kimi K2 (Moonshot AI) via Direct API (Async)"""
    
    def __init__(self):
        # Priority: Env Var > .env File > Config File
        self.api_key = os.getenv('KIMI_API_KEY')
        
        # Manually load .env if not found (backend root)
        if not self.api_key:
            try:
                env_path = os.path.join(os.path.dirname(__file__), '.env')
                if os.path.exists(env_path):
                    with open(env_path, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.strip().startswith('KIMI_API_KEY='):
                                self.api_key = line.strip().split('=', 1)[1].strip('"\'')
                                os.environ['KIMI_API_KEY'] = self.api_key
                                break
            except Exception as e:
                print(f"Warning: Could not load .env file: {e}")

        self.base_url = 'https://api.moonshot.cn/v1'
        self.model = 'moonshot-v1-128k'
        
    def _get_headers(self):
        if not self.api_key:
            raise ValueError("KIMI_API_KEY not configured")
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    async def chat(self, messages: List[Dict[str, str]], temperature: float = 0.7) -> str:
        """Send message to Kimi (Async)"""
        try:
            payload = {
                'model': self.model,
                'messages': messages,
                'temperature': temperature,
            }
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f'{self.base_url}/chat/completions', 
                    headers=self._get_headers(), 
                    json=payload,
                    timeout=60.0
                )
                response.raise_for_status()
                return response.json()['choices'][0]['message']['content']
        except Exception as e:
            raise Exception(f"Error connecting to Kimi AI: {str(e)}")

    async def solve_math_problem(self, problem: str, show_steps: bool = True) -> Dict[str, Any]:
        """
        Resolver problema matemático con razonamiento paso a paso.
        Retorna un diccionario estructurado.
        """
        system_prompt = f"""Eres un asistente matemático experto de Aldra's Team (Binary EquaLab AI).

Resuelve el siguiente problema {'mostrando TODOS los pasos' if show_steps else 'directamente'}.

Responde ESTRICTAMENTE en formato JSON con esta estructura:
{{
  "solution": "Respuesta final matemática (LaTeX/texto)",
  "steps": ["Paso 1: ...", "Paso 2: ..."],
  "reasoning": "Explicación breve del enfoque",
  "difficulty": "fácil|medio|difícil",
  "concepts": ["Concepto 1", "Concepto 2"]
}}"""
        
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': problem}
        ]
        
        try:
            response_text = await self.chat(messages, temperature=0.3)
            # Limpiar markdown
            cleaned = response_text.replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return {
                "solution": response_text,
                "steps": ["No se pudo parsear la respuesta estructurada."],
                "reasoning": "Respuesta directa del modelo.",
                "difficulty": "desconocido",
                "concepts": []
            }
        except Exception as e:
             return {
                "solution": "Error de conexión",
                "steps": [str(e)],
                "reasoning": "Error del servidor",
                "difficulty": "error",
                "concepts": []
            }

    async def explain_concept(self, concept: str, level: str = 'intermedio') -> str:
        """Explicación pedagógica de conceptos"""
        system_prompt = f"""Eres un profesor de matemáticas apasionado de Aldra's Team.
        Explica el concepto solicitado para un nivel {level}.
        Usa analogías, claridad y rigor."""
        
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f"Explícame: {concept}"}
        ]
        return await self.chat(messages, temperature=0.5)

    async def generate_exercises(self, topic: str, count: int = 5, difficulty: str = 'medio') -> List[Dict[str, Any]]:
        """Generar ejercicios de práctica"""
        system_prompt = f"""Genera {count} ejercicios de {topic} con dificultad {difficulty}.
        
        Responde ESTRICTAMENTE en formato JSON (Array de objetos):
        [
          {{
            "problem": "Enunciado",
            "solution": "Respuesta",
            "steps": ["Paso 1", "Paso 2"],
            "concepts": ["Concepto A"]
          }}
        ]"""
        
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': "Genera los ejercicios."}
        ]
        
        try:
            response_text = await self.chat(messages, temperature=0.7)
            cleaned = response_text.replace('```json', '').replace('```', '').strip()
            return json.loads(cleaned)
        except Exception:
            return []

# Singleton
kimi_service = KimiService()
