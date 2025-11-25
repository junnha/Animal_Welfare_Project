import google.generativeai as genai
from google.generativeai import types

context_data = """
58       2015-06-15 02:13:00 2015-06-15 03:40:00        rest            88
59       2015-06-15 03:41:00 2015-06-15 03:42:00      normal             2
60       2015-06-15 03:43:00 2015-06-15 03:55:00        rest            13
61       2015-06-15 03:56:00 2015-06-15 04:01:00      normal             6
62       2015-06-15 04:02:00 2015-06-15 04:12:00        rest            11
63       2015-06-15 04:13:00 2015-06-15 04:23:00      normal            11
64       2015-06-15 04:24:00 2015-06-15 06:59:00        rest           156
65       2015-06-15 07:00:00 2015-06-15 07:06:00      normal             7
66       2015-06-15 07:07:00 2015-06-15 09:02:00        rest           116
67       2015-06-15 09:03:00 2015-06-15 10:05:00      normal            63
68       2015-06-15 10:06:00 2015-06-15 10:06:00        rest             1
69       2015-06-15 10:07:00 2015-06-15 10:33:00      normal            27
70       2015-06-15 10:34:00 2015-06-15 10:34:00        rest             1
"""

prompt = f"""
You are an AI assistant that summarizes animal activity patterns for visitors.
Based on the data below, provide a concise and human-readable explanation.

[Data]
{context_data}
[Arbitrarily Set]
"""

response = model.generate_content(prompt)
print(response.text)
