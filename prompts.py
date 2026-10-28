#!/usr/bin/env python3
"""PromptPlaybook-Urdu — bilingual prompt library by use-case."""
import argparse
PROMPTS = {
 "sales": [
  ("Write a short sales message for [product] for [audience]. Keep it friendly and under 60 words.",
   "[product] ke liye [audience] ko ek chhota sales message likho, friendly tone mein, 60 words se kam."),
  ("List 3 benefits of [product] in simple words a first-time buyer would understand.",
   "[product] ke 3 faide simple words mein likho, jo pehli dafa khareedne wala bhi samajh sake."),
 ],
 "support": [
  ("Reply politely to a customer who says: [complaint]. Apologise, explain the fix, and offer next steps.",
   "Customer ki shikayat [complaint] ka polite jawab do, maazrat karo, hal batayo aur agla step do."),
  ("Write a short FAQ answer: how do I track my order? Keep it under 40 words.",
   "FAQ jawab likho: order kaise track karein? 40 words se kam, simple Urdu/English mein."),
 ],
 "social": [
  ("Write a social post about [topic] with a hook in the first line and a call to action at the end.",
   "[topic] par social post likho, pehli line hook ho aur aakhir mein call to action ho."),
  ("Turn this idea into 3 short post captions: [idea].",
   "Is idea [idea] ko 3 chhoti post captions mein badlo."),
 ],
}
def main():
    p = argparse.ArgumentParser(); p.add_argument("--list", action="store_true"); p.add_argument("--use-case", default="")
    a = p.parse_args()
    if a.list: print("Use-cases: " + ", ".join(PROMPTS)); return
    if a.use_case in PROMPTS:
        for en, ur in PROMPTS[a.use_case]:
            print(f"EN: {en}\nUR (Roman): {ur}\n")
    else: print("Use --list, or --use-case sales|support|social")
if __name__ == "__main__": main()
