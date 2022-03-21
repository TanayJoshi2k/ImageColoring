<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="Image_Colorization_with_Encoders__0"></a>Image Colorization with Encoders 🎨</h1>
<hr>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="Description_2"></a>Description</h3>
<ul>
<li class="has-line-data" data-line-start="3" data-line-end="4">This fun project colorizes a grayscale image (to RGB) using Encoders.</li>
<li class="has-line-data" data-line-start="4" data-line-end="5">All images are resized to (224, 224, 3).</li>
<li class="has-line-data" data-line-start="5" data-line-end="6">The training images are converted from RGB to LAB format where <em>L</em> is the luminosity of the image and <em>AB</em> are the channels.</li>
<li class="has-line-data" data-line-start="6" data-line-end="7">Each image is split into two matrices: the grayscale channel (<em>L</em>) and AB channels.</li>
<li class="has-line-data" data-line-start="7" data-line-end="8">The above step is repeated for all images.</li>
<li class="has-line-data" data-line-start="8" data-line-end="9">The grayscale channel (<em>L</em>) of all such images is called <em>X</em> and the <em>AB</em> channels is called <em>y</em>.</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">The shape of <em>X</em> is (None, 224, 224, 1) and that of <em>y</em> is (None, 224, 224, 2)</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">The model is trained on <em>X</em> and loss (MSE) is calculated on model predictions and <em>y</em></li>
<li class="has-line-data" data-line-start="11" data-line-end="13">Model(<em>X</em>) =&gt; <em>preds</em> =&gt; MSE(<em>preds</em>, <em>y</em>)</li>
</ul>
<h4 class="code-line" data-line-start=13 data-line-end=14 ><a id="To_run_the_script__13"></a>To run the script ▶️</h4>
<ul>
<li class="has-line-data" data-line-start="14" data-line-end="15">Clone the repo</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">Install the requirements:  <code>pip install requirements.txt</code></li>
<li class="has-line-data" data-line-start="16" data-line-end="17">Navigate inside the sript dir</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">The script expects a string image path argument</li>
<li class="has-line-data" data-line-start="18" data-line-end="20">Run the script: <code>python ImageColoring.py &lt;image_path&gt;</code></li>
</ul>
<h4 class="code-line" data-line-start=20 data-line-end=21 ><a id="Train_your_own_encoder_20"></a>Train your own encoder</h4>
<p class="has-line-data" data-line-start="21" data-line-end="22">I have attached the script that trains the encoder from scratch. Change the path to your data and hyperparameters as per your need.</p>
