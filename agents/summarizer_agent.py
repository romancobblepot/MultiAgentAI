# -*- coding: utf-8 -*-
"""Summarizer_agent.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RGJ4HefhFsVGOqGoVu6744WwYbC7HbPj
"""

from .agent_base import AgentBase

class SummarizeTool(AgentBase):
  def __init__(self,max_retries=3,verbose=True):
    super().__init__(name="SummarizeTool", max_retries=max_retries, verbose=verbose)

  def execute(self,text):
    messages = [
        {"role": "system", "content": "You are an AI assistant that summarizes medical texts."},
        {
            "role": "user",
            "content": (
                "Please provide a concise summary of the following medical text:\n\n"
                f"{text}\n\nSummary:"
            )
        }
    ]
    summary = self.call_openai(messages,max_tokens=300)
    return summary
