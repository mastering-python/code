import plugins

plugins.PluginsThroughConfiguration.load(
    'plugins.spam',
    'plugins.eggs',
)

print(plugins.PluginsThroughConfiguration.get('spam'))
