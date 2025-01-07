def can_build(env, platform):
    return env.editor_build

def get_opts(platform):
    from SCons.Variables import BoolVariable

    return [
        BoolVariable("tinyexr_export_templates", "Enable loading OpenEXR images in export template builds (increases binary size)", False),
    ]

def configure(env):
    pass
