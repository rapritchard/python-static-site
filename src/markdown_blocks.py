block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def check_for_headings(block):
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return True
    return False

def check_for_code_block(lines):
    return True if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```") else False

def check_for_quote(lines):
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def check_for_unordered_list(lines):
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            return False
    return True

def check_for_ordered_list(lines):
    for i, line in enumerate(lines):
        if not line.startswith(f"{i + 1}. "):
            return False
    return True

def block_to_block_type(block):
    lines = block.split("\n")

    if check_for_headings(block):
        return block_type_heading
    if check_for_code_block(lines):
        return block_type_code
    if check_for_quote(lines):
        return block_type_quote
    if check_for_unordered_list(lines):
        return block_type_unordered_list
    if check_for_ordered_list(lines):
        return block_type_ordered_list
    return block_type_paragraph

def markdown_to_blocks(markdown):
    filtered_blocks = []
    blocks = markdown.split("\n\n")

    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())

    return filtered_blocks