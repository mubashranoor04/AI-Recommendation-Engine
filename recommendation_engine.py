def calculate_jaccard_similarity(user_interests, item_tags):
    # Remove case-sensitivity and whitespace discrepancies
    set_user = set(tag.strip().lower() for tag in user_interests)
    set_item = set(tag.strip().lower() for tag in item_tags)

    intersection = set_user.intersection(set_item)
    union = set_user.union(set_item)

    if not union:
        return 0.0
    return len(intersection) / len(union)

def get_recommendations(user_interests, items, top_n=2):
    scored_items = []
    for item in items:
        score = calculate_jaccard_similarity(user_interests, item["tags"])
        scored_items.append((item, score))

    # Sort items based on the similarity score in descending order
    scored_items.sort(key=lambda x: x[1], reverse=True)

    # Return Top-N items that have a score greater than 0
    return [item for item, score in scored_items[:top_n] if score > 0]

if __name__ == "__main__":
    from dataset import ITEMS

    print("\tWelcome to the AI Recommendation Engine")
    user_input = input("Enter your skills/interests (comma-separated): ")
    user_interests = [tag.strip() for tag in user_input.split(",") if tag.strip()]

    recommendations = get_recommendations(user_interests, ITEMS)

    print("\n\tYour Top Recommendations")
    if recommendations:
        for idx, item in enumerate(recommendations, start=1):
            print(f"{idx}. {item['title']} (Tags: {', '.join(item['tags'])})")
    else:
        print("No matching items found. Try updating your interests!")