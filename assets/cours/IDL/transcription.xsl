<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output omit-xml-declaration="yes" indent="no"/>



  
  <xsl:template match="/" >
    <html>
      <body>
	<table>
          <xsl:for-each select="Trans/Episode/Section/Turn">
	    <tr>
	      <td>
		<xsl:value-of select="@startTime"/>s
		- 
		<xsl:value-of select="@endTime"/>s
	      </td>
	      <xsl:choose>
		<xsl:when test="@speaker='FRA2019_0100'">
		  <td bgcolor="lightpink">
		    <xsl:for-each select="text()">
		      <!-- pour chaque élément de texte brut 
			   on commence par vérifier si ce n'est
			   pas des caractères blancs uniquement
			   (voir en fin de fichier)
		      -->
		      <xsl:if test="(normalize-space(.))">
			 <!-- affichage du texte suivi d'un 
			      retour à la ligne (<br/>)
			 -->
			<xsl:value-of select="." /><br/>
		      </xsl:if>
		    </xsl:for-each>
		  </td>
		</xsl:when>
		
		<xsl:otherwise>
		  <td bgcolor="lightgreen">
		    <xsl:for-each select="text()">
		      <xsl:if test="(normalize-space(.))">
			<xsl:value-of select="." /><br/>
		      </xsl:if>
		    </xsl:for-each>
		  </td>
		</xsl:otherwise>
              </xsl:choose>
	    </tr>
            
	  </xsl:for-each>
	</table>
	
	
      </body>
    </html>
  </xsl:template>


    

</xsl:stylesheet>

 <!-- 
Ce test permet de savoir si le contenu de la balise
contient autre chose que des caractères invisibles :
"Contains text other than whitespace: (normalize-space(.))"

<xsl:if test="(normalize-space(.))"> -->
