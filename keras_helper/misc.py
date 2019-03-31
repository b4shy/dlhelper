def set_untrainable(model,up_to_what):

    for layer in model.layers:
        layer.trainable = True

    if up_to_what >= 0:
        for layer in model.layers[:-up_to_what]:
            if layer.__class__.__name__ is not "BatchNormalization":
                layer.trainable = False
    else:
        for layer in model.layers[:up_to_what]:
            if layer.__class__.__name__ is not "BatchNormalization":
                layer.trainable = False

