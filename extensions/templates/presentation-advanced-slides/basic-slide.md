---
css:[css/layout.css,css/custom_layout.css]
---

<grid drag="94 98" drop="3 -6">

<grid drag="17 17" drop="80 0"  align="right" pad="0 0px">
 ![[FMFI_logo_black.png]]
</grid>

<grid drag="85 10" drop="0 0" align="left" pad="0px 20px" class="title">
<% title %>
</grid>

<grid drag="85 5" drop="0 10" align="left" pad="0px 20px" class="subtitle">
<% subTitle %>
</grid>

<grid drag="94 0" drop="2 20" class="horizontal_line">
</grid>

<grid drag="100 70" drop="0 20" align="left" pad="20px 20px">
<% content %>
</grid>



<grid drag="100 0" drop="2 -7" align="left" pad="20px 20px" class="footer">
<% footer %>
</grid>
</grid>
