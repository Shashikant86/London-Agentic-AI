# Contributing to London Agentic AI Meetup Repository

Thank you for your interest in contributing to the London Agentic AI Meetup repository! We welcome contributions from our community members and external contributors alike.

## Ways to Contribute

### As a Speaker: Adding Your Demo/Talk

If you've presented at one of our meetups, we'd love to have your code and materials in this repository!

**Steps to contribute your demo/talk:**

1. **Fork this repository**
   - Click the "Fork" button on the top right of this repository
   - Clone your fork locally

2. **Create a new branch for your contribution**
   ```bash
   git checkout -b add-my-demo-[meetup-number]-[your-name]
   ```

3. **Add your code to the appropriate meetup directory**
   - Navigate to the relevant meetup folder (e.g., `1_Context_Engineering/`)
   - Create a new folder following the pattern: `[Your_Name]_[Topic]/`
   - Add your code, notebooks, and any supporting files

4. **Include a README with your demo**
   Your demo folder should include a README.md with:
   - **Brief description** of your demo/talk
   - **Setup instructions** (step-by-step)
   - **Dependencies** (requirements.txt, package.json, etc.)
   - **Usage examples** or how to run the demo
   - **Contact information** (optional but recommended)
   - **License information** (if different from repository default)

5. **Submit a pull request**
   - Push your changes to your fork
   - Create a pull request with a clear title and description
   - Reference the meetup session and your talk topic

**Example folder structure for speakers:**
```
2_Agent_Frameworks/
├── John_Doe_CrewAI_Demo/
│   ├── README.md
│   ├── requirements.txt
│   ├── demo.py
│   ├── agents/
│   └── examples/
```

### As an External Contributor: Improve Code

We welcome improvements and enhancements from the broader community!

**How to suggest improvements:**

1. **Create an issue first**
   - Go to the [Issues tab](https://github.com/[username]/London-Agentic-AI/issues)
   - Click "New Issue"
   - Describe the enhancement or improvement you'd like to suggest
   - Tag it with appropriate labels (enhancement, bug, documentation, etc.)

2. **Wait for discussion**
   - Allow the community and organizers to discuss your suggestion
   - This helps ensure your contribution aligns with the repository's goals

3. **Implement your improvement**
   - Fork the repository
   - Create a feature branch
   - Make your changes
   - Test thoroughly
   - Submit a pull request referencing the issue

**Types of improvements we welcome:**
- Bug fixes in existing demos
- Documentation improvements
- Code optimization and refactoring
- Additional examples or use cases
- Setup scripts or automation
- Testing frameworks for demos

## Contribution Guidelines

### Code Quality Standards

- **Documentation**: Ensure your code is well-documented with clear comments
- **Dependencies**: Clearly specify all requirements and versions
- **Setup Instructions**: Include step-by-step setup instructions
- **Testing**: Include examples of how to test or run your code
- **Clean Code**: Follow best practices for the language you're using

### Repository Standards

- **File Organization**: Follow the established directory structure
- **Naming Conventions**: Use clear, descriptive names for files and folders
- **README Requirements**: Every demo/talk folder must include a README.md
- **License Compliance**: Ensure your contributions are appropriately licensed

### Safety and Security

- **No Malicious Code**: Absolutely no malicious code or unsafe practices
- **API Keys**: Never commit API keys, secrets, or sensitive information
- **Dependencies**: Only include necessary and trusted dependencies
- **Security Best Practices**: Follow security best practices for AI/ML code

### Community Standards

- **Respectful Communication**: Be respectful in all interactions
- **Constructive Feedback**: Provide helpful and constructive feedback
- **Inclusive Environment**: Help maintain an inclusive environment for all
- **Knowledge Sharing**: Focus on learning and sharing, not commercial promotion

## Pull Request Process

### Before Submitting

1. **Test your code** thoroughly
2. **Update documentation** as needed
3. **Check for conflicts** with the main branch
4. **Review your changes** one final time

### Pull Request Template

When submitting a pull request, please include:

```markdown
## Description
Brief description of what this PR adds/changes

## Type of Contribution
- [ ] New demo/talk from meetup
- [ ] Bug fix
- [ ] Documentation improvement
- [ ] Code enhancement
- [ ] Other (please describe)

## Meetup Session
- Meetup number and theme: 
- Speaker name (if applicable):
- Talk title (if applicable):

## Testing
- [ ] I have tested this code locally
- [ ] I have included setup instructions
- [ ] I have verified all dependencies are listed

## Checklist
- [ ] My code follows the contribution guidelines
- [ ] I have added/updated documentation as needed
- [ ] I have not included any sensitive information
- [ ] I have used descriptive commit messages
```

### Review Process

1. **Community Review**: Other community members may review and provide feedback
2. **Organizer Review**: Repository maintainers will review for quality and alignment
3. **Testing**: We may test your contribution to ensure it works as expected
4. **Merge**: Once approved, your contribution will be merged

## Getting Help

### Questions About Contributing

- **GitHub Issues**: Use issues for contribution-related questions
- **Meetup Page**: Reach out through our [Meetup page](https://www.meetup.com/london-agentic-ai/)
- **Community Discord**: Join our Discord for real-time discussions (coming soon)
- **Direct Contact**: Contact Shashi Jagtap through Meetup or GitHub

### Technical Support

If you need help with:
- Setting up the development environment
- Understanding the repository structure
- Implementing a specific feature
- Troubleshooting issues

Don't hesitate to create an issue or reach out to the community!

## Recognition

We appreciate all contributions! Contributors will be:
- Listed in the repository's contributor section
- Acknowledged in meetup sessions (for speakers)
- Thanked in release notes (for significant improvements)

---

Thank you for helping make the London Agentic AI community a great place for learning and sharing! 🤖✨