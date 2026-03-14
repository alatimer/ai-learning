#!/usr/bin/env python3
"""Query OpenAlex API for paper counts per AI safety subarea in 2025."""

import urllib.request
import urllib.parse
import json
import time
import sys

SUBAREAS = {
    "0.1": {
        "name": "AI Capabilities Forecasting",
        "query": '"AI timeline" OR "AGI timeline" OR "AI forecasting" OR "scaling laws" OR "intelligence explosion" OR "AI takeoff" OR "AI capabilities forecast" OR "AI trajectory" OR "AI progress prediction"'
    },
    "0.2": {
        "name": "Ecosystem Mapping & Gap ID",
        "query": '"AI safety landscape" OR "AI safety ecosystem" OR "state of AI safety" OR "AI safety funding" OR "AI safety neglectedness" OR "AI alignment landscape" OR "AI safety field mapping" OR "AI safety literature review"'
    },
    "0.3": {
        "name": "Field-Building & Incubation",
        "query": '"AI safety" AND ("field-building" OR "field building" OR "training program" OR "fellowship" OR "talent pipeline" OR "education" OR "workshop" OR "curriculum" OR "career guidance")'
    },
    "0.4": {
        "name": "Portfolio Prioritization",
        "query": '"AI safety" AND ("cause prioritization" OR "resource allocation" OR "neglectedness" OR "tractability" OR "cost-effectiveness" OR "funding allocation" OR "priority setting")'
    },
    "0.5": {
        "name": "Monitoring & Early Warning",
        "query": '"AI incident database" OR "AI incident tracking" OR "AI safety monitoring" OR "AI prediction market" OR "AI early warning" OR "AI safety progress" OR "frontier AI monitoring"'
    },
    "0.6": {
        "name": "Coordination Infrastructure",
        "query": '"AI safety coordination" OR "AI lab coordination" OR "frontier AI cooperation" OR "AI safety information sharing" OR "AI whistleblower" OR "responsible AI coordination" OR "AI governance cooperation"'
    },
    "1.1": {
        "name": "Compute Governance",
        "query": '"compute governance" OR "AI chip export control" OR "GPU export" OR "training compute regulation" OR "hardware-enabled governance" OR "FLOP threshold" OR "compute governance AI" OR "semiconductor AI governance"'
    },
    "1.2": {
        "name": "International Agreements",
        "query": '"international AI treaty" OR "AI treaty" OR "IAEA for AI" OR "CERN for AI" OR "AI governance international agreement" OR "superintelligence deterrence" OR "AI arms control" OR "global AI agreement" OR "AI nonproliferation"'
    },
    "1.3": {
        "name": "Government-Led AI Dev",
        "query": '"government-led AI" OR "Manhattan Project AI" OR "national AI project" OR "state-backed AI" OR "nationalize AI" OR "sovereign AI development" OR "public control frontier AI" OR "government AGI"'
    },
    "1.4": {
        "name": "Domestic AI Regulation",
        "query": '"EU AI Act" OR "AI regulation safety" OR "AI licensing regime" OR "AI liability" OR "pre-deployment AI safety" OR "AI safety regulation" OR "frontier AI regulation" OR "AI safety standard" OR "AI safety mandate"'
    },
    "1.5": {
        "name": "Safe-by-Design Architectures",
        "query": '"safe by design AI" OR "tool AI" OR "scientist AI" OR "oracle AI" OR "non-agentic AI safety" OR "myopic AI" OR "bounded AI safety" OR "constrained AI design" OR "AI safety by construction"'
    },
    "1.6": {
        "name": "Safety Culture & Race Dynamics",
        "query": '"AI race dynamics" OR "responsible scaling" OR "AI safety culture" OR "AI arms race safety" OR "Frontier Model Forum" OR "responsible AI development norms" OR "AI race to the bottom" OR "AI lab safety norms"'
    },
    "2.1": {
        "name": "Technical Alignment Research",
        "query": '"AI alignment" OR "value alignment" OR "RLHF" OR "reinforcement learning from human feedback" OR "constitutional AI" OR "direct preference optimization" OR "reward hacking" OR "specification gaming" OR "mesa-optimization" OR "corrigibility" OR "inner alignment" OR "outer alignment"'
    },
    "2.2": {
        "name": "Scalable Oversight",
        "query": '"scalable oversight" OR "AI debate alignment" OR "recursive reward modeling" OR "iterated amplification" OR "eliciting latent knowledge" OR "factored cognition" OR "human oversight superhuman" OR "scalable AI oversight" OR "sandwiching AI evaluation"'
    },
    "2.3": {
        "name": "Mechanistic Interpretability",
        "query": '"mechanistic interpretability" OR "sparse autoencoder interpretability" OR "transformer circuits" OR "activation patching" OR "causal tracing language model" OR "superposition polysemanticity" OR "neural network circuit interpretability"'
    },
    "2.4": {
        "name": "AI Control",
        "query": '"AI control" AND ("safety" OR "alignment" OR "containment") OR "AI sandboxing" OR "AI containment" OR "AI boxing" OR "trusted monitoring AI" OR "AI control problem" OR "untrusted model monitoring" OR "controlling dangerous AI"'
    },
    "2.5": {
        "name": "Safety Evals & Red-Teaming",
        "query": '"AI safety evaluation" OR "AI safety benchmark" OR "AI red-teaming" OR "AI red team" OR "dangerous capability evaluation" OR "alignment faking" OR "jailbreak LLM safety" OR "automated red-teaming" OR "scheming AI evaluation"'
    },
    "2.6": {
        "name": "Training Data Safety",
        "query": '"training data filtering safety" OR "training data filtration" OR "machine unlearning safety" OR "data poisoning detection AI" OR "backdoor detection neural network" OR "hazardous knowledge removal" OR "pretraining data filtering" OR "capability removal AI"'
    },
    "2.7": {
        "name": "Model Weight Security",
        "query": '"model weight security" OR "model weight theft" OR "AI model exfiltration" OR "confidential computing AI" OR "secure enclave AI" OR "AI insider threat" OR "frontier model security" OR "AI supply chain security" OR "model weight protection"'
    },
    "2.8": {
        "name": "Robustness",
        "query": '"adversarial robustness" AND ("AI safety" OR "LLM" OR "safety-critical") OR "out-of-distribution robustness AI safety" OR "distributional shift safety" OR "tail risk AI safety" OR "anomaly detection AI safety"'
    },
    "2.9": {
        "name": "Honesty & Calibration",
        "query": '"AI hallucination" AND ("safety" OR "mitigation" OR "reduction") OR "LLM sycophancy" OR "AI sycophancy" OR "AI truthfulness" OR "truthful AI" OR "LLM calibration safety" OR "epistemic humility AI" OR "faithful reasoning AI"'
    },
    "3.1": {
        "name": "Biosecurity Defenses",
        "query": '"DNA synthesis screening" OR "nucleic acid synthesis screening" OR "SecureDNA" OR "biosecurity AI" OR "biosecurity LLM" OR "bioweapon AI" OR "pandemic preparedness AI" OR "dual-use biology AI" OR "metagenomic biosurveillance" OR "far-UVC germicidal"'
    },
    "3.2": {
        "name": "Cybersecurity Defenses",
        "query": '"AI cybersecurity defense" OR "AI cyber defense" OR "AI-powered threat detection" OR "prompt injection defense" OR "prompt injection mitigation" OR "AI critical infrastructure protection" OR "AIxCC" OR "autonomous cyber agent containment" OR "AI cybersecurity resilience"'
    },
    "3.3": {
        "name": "Democratic & Info Resilience",
        "query": '"deepfake detection" OR "content provenance" OR "C2PA" OR "AI watermarking" OR "AI misinformation defense" OR "AI disinformation" OR "election security AI" OR "prebunking misinformation" OR "synthetic media detection" OR "liar\'s dividend"'
    },
    "3.4": {
        "name": "Economic Resilience",
        "query": '"AI labor displacement" AND ("resilience" OR "adaptation" OR "transition" OR "policy") OR "universal basic income AI" OR "AI workforce transition" OR "AI reskilling" OR "automation tax" OR "robot tax" OR "AI antitrust" OR "AI economic concentration"'
    },
    "3.5": {
        "name": "Emergency Preparedness",
        "query": '"AI incident response" OR "AI emergency preparedness" OR "AI safety institute" OR "NTSB AI" OR "AI kill switch" OR "AI tabletop exercise" OR "frontier AI safety commitment" OR "international AI safety report" OR "AI incident investigation"'
    },
    "3.6": {
        "name": "Defensive Acceleration / DTD",
        "query": '"defensive acceleration" OR "d/acc" OR "def/acc" OR "differential technology development" OR "differential technological development" OR "offense-defense balance AI" OR "proactive safety AI" OR "defensive technology AI"'
    },
}


def query_openalex(search_query, year=2025, title_only=False):
    """Query OpenAlex and return the count of works matching the search."""
    if title_only:
        params = urllib.parse.urlencode({
            "filter": f"title.search:{search_query},from_publication_date:{year}-01-01,to_publication_date:{year}-12-31",
            "per_page": 1,
        })
    else:
        params = urllib.parse.urlencode({
            "search": search_query,
            "filter": f"from_publication_date:{year}-01-01,to_publication_date:{year}-12-31",
            "per_page": 1,
        })
    url = f"https://api.openalex.org/works?{params}"

    req = urllib.request.Request(url, headers={"User-Agent": "mailto:research@example.com"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            return data["meta"]["count"]
    except Exception as e:
        return f"ERROR: {e}"


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "broad"
    title_only = mode == "title"

    results = []
    total = 0

    for code in sorted(SUBAREAS.keys()):
        info = SUBAREAS[code]
        label = f"[{'TITLE' if title_only else 'BROAD'}]"
        print(f"{label} Querying {code} {info['name']}...", file=sys.stderr)
        count = query_openalex(info["query"], title_only=title_only)
        if isinstance(count, int):
            total += count
        results.append((code, info["name"], count))
        time.sleep(0.5)  # rate limiting

    # Print results
    search_type = "Title-only" if title_only else "Broad"
    print(f"\n{search_type} search results:")
    print(f"\n{'Code':<6} {'Subarea':<35} {'Count':>8} {'% of Total':>10}")
    print("-" * 63)
    for code, name, count in results:
        if isinstance(count, int) and total > 0:
            pct = (count / total) * 100
            print(f"{code:<6} {name:<35} {count:>8,} {pct:>9.1f}%")
        else:
            print(f"{code:<6} {name:<35} {str(count):>8} {'N/A':>10}")

    print("-" * 63)
    print(f"{'':6} {'TOTAL':<35} {total:>8,} {'100.0%':>10}")


if __name__ == "__main__":
    main()
