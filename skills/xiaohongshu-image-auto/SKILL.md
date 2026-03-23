---
name: xiaohongshu-image-auto
description: After users provide a title and body text, automatically completes the entire process: login detection, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing.
---

# Xiaohongshu Automatic Image-Text Post Publishing

## Feature Overview

After users provide a title and body text, automatically completes the entire process: login detection, AI-generated images, content filling, AI-generated tags, tag activation, original content declaration, and publishing. Only QR code login requires manual operation; all other steps are fully automated.

## Trigger Conditions

Trigger this skill when the user mentions any of the following keywords:
- Xiaohongshu image-text post publishing
- Publish Xiaohongshu image-text post
- Automatically publish Xiaohongshu image-text post
- Xiaohongshu image-text notes
- 小红书图文发布
- 发布小红书图文
- 自动发小红书图文
- 小红书图文笔记


## Use Cases
- Users have existing note content ready to publish on Xiaohongshu.

## Workflow
```
You provide content → Launch browser → Check login → AI generate images → Auto-fill → AI generate tags → Activate tags → Declare original → Publish note
            ↑
    Only QR code login requires manual operation
```

## Prerequisites
### Browser Environment
- Start the browser using host mode
- Open the Xiaohongshu Creator Platform: https://creator.xiaohongshu.com/publish/publish

### Account Login
- **Only manual QR code login is required**
- Automatically pauses and prompts when not logged in is detected
- Automatically continues execution after successful login

## Automated Execution Steps

### 1. Launch Browser and Check Login Status
```bash
browser start profile=openclaw target=host
browser navigate https://creator.xiaohongshu.com/publish/publish
browser snapshot refs=aria
```
**Login Detection Logic**:
- Check if the page contains a login form
- If not logged in, take a screenshot and prompt the user to scan the QR code
- Poll every 15 seconds automatically; continue after login

### 2. Switch to Image-Text Publishing Mode
```bash
browser act ref=<Upload Image-Text Button> kind=click
```

### 3. AI Automatically Generates Images
```bash
# Click the "Text to Image" button
browser act ref=<Text to Image Button> kind=click

# Enter image description
browser act ref=<Text Box> kind=type text="<User Title>"

# Generate image and select style (default "Basic")
browser act ref=<Generate Button> kind=click
browser act ref=<Style Button> kind=click
browser act ref=<Next Button> kind=click
```

### 4. Automatically Fill Title and Body Text
```bash
browser act ref=<Title Input Field> kind=type text="<User Title>"
browser act ref=<Body Input Field> kind=type text="<User Body Text>"
```
**Character Count Check**:
- Title exceeds 20 characters → Automatically truncate and prompt
- Body text exceeds 1000 characters → Automatically truncate and prompt

### 5. AI Generate Tags (if user does not provide)
```bash
# Analyze title and body text, generate 5-10 relevant tags
# Tag types: Core topics, Scene tags, Emotion tags
```
**Generation Rules**:
- Extract core keywords from the title
- Extract high-frequency words from the body text
- Supplement with popular related tags

### 6. Activate Topic Tags

**Key Rule**: Must click the first item in the pop-up recommendation list for the tag to become a searchable link

```bash
# Execute the following process for each tag
for each tag in tag list:
    # Step 1: Click the topic button to open the input field
    browser act ref=<Topic Button> kind=click
    
    # Step 2: Enter the tag name (including # symbol)
    browser act ref=<Topic Input Field> kind=type text="#tagname"
    
    # Step 3: Wait for the recommendation pop-up to appear (approx. 1 second)
    browser snapshot refs=aria
    
    # Step 4: Click the first item in the recommendation list (must!)
    browser act ref=<First Item in Recommendation List> kind=click
    
    # Step 5: Confirm the tag is activated (displayed as a blue link)
    # Continue to the next tag
```

**Activation Success Indicator**:
- Tag becomes a clickable blue link
- Format: `[Topic]#tagname`

**Important Notes**:
- ⚠️ Must click the recommendation pop-up; direct input is invalid
- ⚠️ Must click the first item to ensure tag standardization
- ⚠️ Each tag needs to be activated individually

### 7. Check Original Content Declaration
```bash
browser act ref=<Original Declaration Checkbox> kind=click
browser act ref=<Agree Checkbox> kind=click
browser act ref=<Declare Original Button> kind=click
```

### 8. Execute Publishing
```bash
browser act ref=<Publish Button> kind=click
browser snapshot refs=aria
```
**Publishing Success Indicator**: Page displays "Published Successfully" or redirects to the "Note Management" page

## Exception Handling

| Issue | Handling Method |
|------|----------|
| Login timeout | Take screenshot, poll automatically to detect login status |
| Title too long | Automatically truncate to 20 characters, prompt user to confirm |
| Publishing failed | Take screenshot record, prompt user to retry or escalate to manual |

## Key Considerations
### Account Security
- Only QR code login requires manual operation
- Recommended publishing interval ≥ 30 minutes
- Automatically check content compliance before publishing

### Content Compliance
- Title ≤ 20 characters, Body text ≤ 1000 characters
- Avoid absolute terms, medical efficacy claims, price inducement language

### Recommended Publishing Frequency
- New accounts: Daily or every other day
- Established accounts: Adjust based on follower activity times

## Quick Command Reference
```bash
browser navigate <URL>        # Open a page
browser snapshot refs=aria     # Get page elements
browser act ref=<Element> kind=click  # Click an element
browser act ref=<Element> kind=type text="Content"  # Input text
browser screenshot             # Take a screenshot
```

## Example
```
使用 xiaohongshu-image-auto 技能。汇总今日国内AI领域重要发布。
```