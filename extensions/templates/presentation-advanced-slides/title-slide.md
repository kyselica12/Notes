---
css:[css/layout.css,css/custom_layout.css]
---

<% content %>
	
<grid drag="94 94" drop="3 3">

<grid drag="100 30" drop="-2 -73"align="left" pad="0px 0px">
![[extensions/templates/presentation-advanced-slides/images/FMFI_logo_text_ENG_black.png]]
</grid>



<grid drag="100 40" drop="0 25" align="left" pad="0 0px" class="title">
<% title %>
</grid>

<grid drag="100 10" drop="0 55" align="left" pad="0 0px" class="event">
<% event %>
</grid>

<grid drag="100 10" drop="0 65" align="left" pad="0 0px">
<% author %>
</grid>

<grid drag="50 10" drop="0 90"  align="left" pad="0 0px" class="footer">
<% footer %>
</grid>

<grid drag="50 10" drop="50 90" align="right" pad="0 0px" >
<% date %>
</grid>

</grid>
