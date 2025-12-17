def create_feedback_report(sentences, faithfulness_labels, keyfacts, completeness_labels, conciseness_labels):
    """
    Create a comprehensive feedback report for summary evaluation.
    
    Args:
        sentences (list): List of summary sentences
        faithfulness_labels (list): Binary labels (1=faithful, 0=unfaithful) for each sentence
        keyfacts (list): List of key facts from the document
        completeness_labels (list): Binary labels (1=included, 0=missing) for each keyfact
        conciseness_labels (list): Binary labels (1=key content, 0=unnecessary) for each sentence
    
    Returns:
        str: Formatted feedback report containing all three dimensions
    """
    # Process faithfulness feedback
    faithfulness_feedback = []
    for idx, (sentence, label) in enumerate(zip(sentences, faithfulness_labels)):
        if label == 0:
            faithfulness_feedback.append({
                "sentence_id": idx + 1,
                "sentence": sentence,
            })
    
    # Process completeness feedback
    completeness_feedback = []
    for idx, (keyfact, label) in enumerate(zip(keyfacts, completeness_labels)):
        if label == 0:
            completeness_feedback.append({
                "missing_key_content_id": idx + 1,
                "keyfact": keyfact,
            })
    
    # Process conciseness feedback
    conciseness_feedback = []
    for idx, (sentence, label) in enumerate(zip(sentences, conciseness_labels)):
        if label == 0:
            conciseness_feedback.append({
                "sentence_id": idx + 1,
                "sentence": sentence,
            })
    
    # Generate reports
    faith_report = _create_faithfulness_report(faithfulness_feedback)
    comp_report = _create_completeness_report(completeness_feedback)
    conc_report = _create_conciseness_report(conciseness_feedback)
    
    # Combine all reports
    report_text = "\n\n".join([faith_report, comp_report, conc_report])
    
    return report_text


def _create_faithfulness_report(data):
    """Generate faithfulness feedback report."""
    report = "***Faithfulness Feedback***\n\n"
    if len(data) == 0:
        report += "All sentences are factually consistent with the Document.\n"
    else:
        report += "These summary sentences are factually inconsistent with the Document: \n"
        for entry in data:
            report += f"- Sentence {entry['sentence_id']}: {entry['sentence']}\n"
    return report


def _create_completeness_report(data):
    """Generate completeness feedback report."""
    report = "***Completeness Feedback***\n\n"
    if len(data) == 0:
        report += "All key contents are included in the summary.\n"
    else:
        report += "These key contents are missing in the summary: \n"
        for entry in data:
            report += f"Missing key content {entry['missing_key_content_id']}: {entry['keyfact']}\n"
    return report


def _create_conciseness_report(data):
    """Generate conciseness feedback report."""
    report = "***Conciseness Feedback***\n\n"
    if len(data) == 0:
        report += "All summary sentences contain key content.\n"
    else:
        report += "These summary sentences do not contain key content: \n"
        for entry in data:
            report += f"Sentence {entry['sentence_id']}: {entry['sentence']}\n"
    return report