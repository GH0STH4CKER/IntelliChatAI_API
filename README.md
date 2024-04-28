<article id="6881c6d3-df1c-4980-ab4c-858010234edb" class="page sans"><header><img class="page-cover-image" src="https://i.ibb.co/VwFRGQ2/Intellichatlogobanner.png" style="object-position:center 50%"/><h1 class="page-title">IntelliChat API Docs</h1><p class="page-description"></p></header><div class="page-body"><h2 id="76aafaa5-e727-40f1-96fc-f5b14506d578" class="">Description</h2><p id="756ca6af-a126-4be7-8c6d-b0a98dbe79d2" class="">This is an API of a chatbot that responds to your messages</p><h2 id="a0b580b6-d926-4f64-8698-75d1edfa6a39" class="">Base URL</h2><p id="fb881f70-a9a4-400a-ae97-89abe501edef" class="">The base URL for all API requests is:</p><p id="efd9506f-3e1a-406a-91c9-403bb5a91655" class=""><code>https://intelli-chat-ai.vercel.app</code></p><h2 id="63ac0751-77c6-4d22-90d9-8c8d70d4a085" class="">Endpoints</h2><h3 id="ab32ce92-e17a-4ccd-9e04-22e2e485b508" class=""><code>POST /chat</code></h3><p id="764b9e3f-4e87-4710-a1ab-de3d9e7e6445" class="">Returns JSON response </p><h3 id="ecab4a75-373d-4a77-a0eb-7f5fece701e8" class="">Parameters</h3><ul id="ccc290ba-75f8-47af-9881-417235683c8a" class="bulleted-list"><li style="list-style-type:disc"><code>user-input</code>: The message you send to chatbot</li></ul><h3 id="0ccc7b95-4394-44de-b4eb-d85ccae6193b" class="">Response</h3><p id="649ecc7f-ec4f-4ac6-816a-723863a9e244" class="">Returns a JSON object with the following properties:</p><ul id="326f1250-1dfd-4c61-bf7a-d8f31fb08ea7" class="bulleted-list"><li style="list-style-type:disc"><code>response</code>: Chatbot’s response</li></ul><h3 id="10bef76f-5051-487f-93fa-0ab671e89b16" class="">Example</h3><p id="a6fa1b12-ed24-467d-b518-d48ade185be0" class="">Request:</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="cb9ae2b9-06e2-4661-b13f-d8040db39a03" class="code"><code class="language-Python" style="white-space:pre-wrap;word-break:break-all">import requests

url = &#x27;https://intelli-chat-ai.vercel.app/chat&#x27;

data = {
    &#x27;user_input&#x27;: &#x27;Hi&#x27;
}

response = requests.post(url, data=data)

if response.status_code == 200:

    print(response.text)
else:

    print(&quot;Error:&quot;, response.status_code, response.text)
</code></pre><p id="23b57652-84ca-4299-ac3b-5c9f360bf2bb" class="">Response:</p><script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" integrity="sha512-7Z9J3l1+EYfeaPKcGXu3MS/7T+w19WtKQY/n+xzmw4hZhJ9tyYmcUS+4QqAlzhicE5LAfMQSF3iFTK9bQdTxXg==" crossorigin="anonymous" referrerPolicy="no-referrer"></script><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.min.css" integrity="sha512-tN7Ec6zAFaVSG3TpNAKtk4DOHNpSwKHxxrsiw4GHKESGPs5njn/0sMCUMl2svV4wo4BK/rCP7juYz+zx+l6oeQ==" crossorigin="anonymous" referrerPolicy="no-referrer"/><pre id="33f02e4d-160f-46ba-9f8d-b2f972b49b7e" class="code"><code class="language-JSON" style="white-space:pre-wrap;word-break:break-all">{&quot;response&quot;:&quot;Hi! Welcome to IntelliChat. How may I help?&quot;}</code></pre><h2 id="c10dd7c1-071e-4629-8053-1b498ea38685" class="">Errors</h2><p id="1c88de16-a351-41b0-9694-0b88b542e152" class="">This API uses the following error codes:</p><ul id="b4c1715b-7302-4781-9b70-f9e0bfd92960" class="bulleted-list"><li style="list-style-type:disc"><code>400 Bad Request</code>: The request was malformed or missing required parameters.</li></ul><ul id="a75fccad-4b28-4dfb-8f51-81d367518f27" class="bulleted-list"><li style="list-style-type:disc"><code>404 Not Found</code>: The requested resource was not found.</li></ul><ul id="b841638d-5829-43b0-a415-e1022d1f3798" class="bulleted-list"><li style="list-style-type:disc"><code>500 Internal Server Error</code>: An unexpected error occurred on the server.</li></ul><p id="10450d7a-9b6e-4b9c-861e-a0ee0518ad0e" class="">
</p><h2 id="79f50fac-79da-4197-9dd9-9826c2e5eb28" class="">Pricing</h2><p id="0892ae4f-f9e0-4928-bb9f-c254f54b70a3" class="">This API is completely free to use. If you find it helpful and would like to support the developer, you can buy a coffee for him. </p><p id="d6245833-88a0-4c35-8ca9-01c5bf1d323d" class=""><a href="https://emojipedia.org/hot-beverage"><strong>☕ </strong></a><a href="https://ko-fi.com/dimuthdezoysa">https://ko-fi.com/dimuthdezoysa</a> </p><p id="8154bf6b-4974-4b46-880f-c0e73f1748c9" class=""><a href="https://emojipedia.org/hot-beverage"><strong>☕ </strong></a><a href="https://buymeacoffee.com/dimuthdezoysa/membership">https://buymeacoffee.com/dimuthdezoysa</a></p><h2 id="c24d6489-d99a-46a2-9957-978d227ce03e" class="">Contact</h2><p id="2966badd-e8a0-410d-bd6a-b9f7756bb1bd" class="">If you encounter any issues or have any questions regarding the API, please feel free to reach out to our support team at <code>dimuthsakya@protonmail.com</code></p><p id="3db63f3f-f9a7-4a44-b88d-02302baa5df1" class="">
</p></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span>
