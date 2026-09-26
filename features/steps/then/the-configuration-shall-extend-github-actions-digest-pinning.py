from behave import then

@then(u'the configuration shall extend GitHub Actions digest pinning')
def step_impl(context):
    config = getattr(context, "renovate_config", {})
    extends = config.get("extends", [])
    assert "helpers:pinGitHubActionDigests" in extends, f"Expected 'helpers:pinGitHubActionDigests' in extends: {extends}"
