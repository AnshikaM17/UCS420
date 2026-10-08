"""UCS420 Assignment 4: FAQ question matching with pandas."""

from pathlib import Path
import re

import pandas as pd


OUTPUT_FILE = Path(__file__).parent / "faq_qa.csv"
STOP_WORDS = {
	"a",
	"an",
	"and",
	"can",
	"do",
	"how",
	"i",
	"is",
	"my",
	"the",
	"to",
	"what",
}


def build_knowledge_base() -> pd.DataFrame:
	"""Create the initial FAQ knowledge base."""
	faq_entries = [
		{
			"question": "What is the annual fee?",
			"answer": "The annual fee is Rs 50.0.",
			"keywords": ["annual", "fee", "cost", "price", "charge"],
			"category": "billing",
		},
		{
			"question": "How do I reset my password?",
			"answer": "Go to Settings and select Reset Password.",
			"keywords": ["password", "login", "forgot", "reset"],
			"category": "account",
		},
		{
			"question": "How can I contact customer support?",
			"answer": "Contact support by email or through the Help section.",
			"keywords": ["support", "help", "contact", "email"],
			"category": "support",
		},
		{
			"question": "How long does delivery take?",
			"answer": "Standard delivery usually takes three to five business days.",
			"keywords": ["delivery", "shipping", "order", "days"],
			"category": "shipping",
		},
		{
			"question": "Can I get a refund?",
			"answer": "Refunds are available within 30 days of purchase.",
			"keywords": ["refund", "return", "money", "purchase"],
			"category": "billing",
		},
		{
			"question": "How do I update my account details?",
			"answer": "Open Settings, edit your account details, and save the changes.",
			"keywords": ["account", "profile", "details", "settings", "update"],
			"category": "account",
		},
	]
	return pd.DataFrame(faq_entries)


def tokenize(text: str) -> set[str]:
	"""Return lowercase word tokens, excluding punctuation."""
	return {
		token
		for token in re.findall(r"[a-z0-9]+", text.lower())
		if token not in STOP_WORDS
	}


def rank_faqs(query: str, knowledge_base: pd.DataFrame) -> pd.DataFrame:
	"""Return all matching FAQs ranked by a simple keyword confidence score."""
	query_tokens = tokenize(query)
	if not query_tokens:
		return pd.DataFrame(columns=[*knowledge_base.columns, "matched_keywords", "confidence"])

	scored_rows = []
	for _, entry in knowledge_base.iterrows():
		searchable_text = " ".join(
			[
				str(entry["question"]),
				str(entry["answer"]),
				" ".join(entry["keywords"]),
			]
		)
		matched_tokens = sorted(query_tokens & tokenize(searchable_text))
		if matched_tokens:
			result = entry.to_dict()
			result["matched_keywords"] = ", ".join(matched_tokens)
			result["confidence"] = round(len(matched_tokens) / len(query_tokens), 2)
			scored_rows.append(result)

	columns = [*knowledge_base.columns, "matched_keywords", "confidence"]
	return (
		pd.DataFrame(scored_rows, columns=columns)
		.sort_values(["confidence", "category"], ascending=[False, True])
		.reset_index(drop=True)
	)


def generate_and_score_hypothesis(
	query: str, knowledge_base: pd.DataFrame
) -> pd.DataFrame:
	"""Answer Q2 by returning every FAQ that matches the query."""
	return rank_faqs(query, knowledge_base)


def filter_by_category(category_name: str, knowledge_base: pd.DataFrame) -> pd.DataFrame:
	"""Return FAQs whose category matches category_name, ignoring case."""
	return knowledge_base[
		knowledge_base["category"].str.casefold() == category_name.casefold()
	].reset_index(drop=True)


def append_user_query(knowledge_base: pd.DataFrame) -> pd.DataFrame:
	"""Ask for a query, append it using the first FAQ as a sample answer, and save CSV."""
	try:
		user_query = input("\nQ4 - Enter a new FAQ query: ").strip()
	except EOFError:
		user_query = "What is the annual fee?"
	if not user_query:
		user_query = "What is the annual fee?"

	matching_entries = rank_faqs(user_query, knowledge_base)
	if matching_entries.empty:
		selected_entry = knowledge_base.iloc[0].copy()
	else:
		selected_question = matching_entries.iloc[0]["question"]
		selected_entry = knowledge_base[
			knowledge_base["question"] == selected_question
		].iloc[0].copy()
	selected_entry["question"] = user_query
	updated = pd.concat([knowledge_base, pd.DataFrame([selected_entry])], ignore_index=True)
	updated.to_csv(OUTPUT_FILE, index=False)
	return updated


def main() -> None:
	knowledge_base = build_knowledge_base()
	print("Q1 - FAQ knowledge base:\n", knowledge_base, sep="")

	query = "I forgot my password and cannot login"
	matches = generate_and_score_hypothesis(query, knowledge_base)
	print("\nQ2 - Ranked matches for:", query, "\n", matches, sep="")

	category = "billing"
	print(
		"\nQ3 - FAQs in the",
		category,
		"category:\n",
		filter_by_category(category, knowledge_base),
		sep="",
	)

	updated_knowledge_base = append_user_query(knowledge_base)
	print("\nQ4 - Knowledge base saved to", OUTPUT_FILE, ":\n", updated_knowledge_base, sep="")

	print("\nQ5 - Number of FAQs per category:\n", updated_knowledge_base["category"].value_counts(), sep="")

	final_query = "How do I reset a forgotten password?"
	final_matches = rank_faqs(final_query, updated_knowledge_base)
	print("\nQ6 - All matching FAQs for:", final_query, "\n", final_matches, sep="")
	if not final_matches.empty:
		print("\nQ6 - Top relevant FAQ:\n", final_matches.iloc[0], sep="")


if __name__ == "__main__":
	main()
