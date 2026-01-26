<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h1 style="color: purple;" align="center">Pokédex</h1>
                <table border="2" align="center">
                    <tr style="color: purple;">
                        <th>Pokémon</th>
                        <th>Nom</th>
                        <th>Type(s)</th>
                        <th>Points de vie</th>
                        <th>Talent(s)</th> <!--Select if talent caché = en italique-->
                        <th>Description</th> <!--sort by num-->
                    </tr>
                    <xsl:for-each select="pokedex/pokemon">
                        <tr>
                            <td><xsl:apply-templates select="image"/></td>
                            <td><xsl:value-of select="nom"/></td>
                            <td><xsl:value-of select="types"/></td>
                            <td><xsl:value-of select="points_de_vie"/></td>
                            <td>
                                <xsl:for-each select="talents/talent">
                                    <xsl:choose>
                                        <xsl:when test="@type='caché'">
                                            <i><xsl:value-of select="."/></i>
                                        </xsl:when>
                                        <xsl:otherwise>
                                            <p><xsl:value-of select="."/></p>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </xsl:for-each>
                            </td>
                            <td>
                                <xsl:for-each select="descriptions/description">
                                    <xsl:sort select="@numero" order="descending"/>
                                    <p><xsl:value-of select="."/></p>
                                </xsl:for-each>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
                <br/><br/>
                <h2 style="color: purple;" align="center">Région de Kanto (Première génération)</h2>
                <table border="2" align="center">
                    <tr style="color: purple;">
                        <th>Pokémon</th>
                        <th>Nom</th>
                    </tr>
                    <xsl:for-each select="pokedex/pokemon">
                        <tr>
                        <xsl:choose>
                            <xsl:when test="@id &lt; 151">
                                <td><xsl:apply-templates select="image"/></td>
                                <td><xsl:value-of select="nom"/></td>
                            </xsl:when>
                        </xsl:choose>
                        </tr>
                    </xsl:for-each>
                </table>
                <br/><br/>
                <h2 style="color: purple;" align="center">Région de Johto (Deuxième génération)</h2>
                <table border="2" align="center">
                    <tr style="color: purple;">
                        <th>Pokémon</th>
                        <th>Nom</th>
                    </tr>
                    <xsl:for-each select="pokedex/pokemon">
                        <tr>
                        <xsl:choose>
                            <xsl:when test="@id[. &gt; 152 and . &lt; 252]">
                                <td><xsl:apply-templates select="image"/></td>
                                <td><xsl:value-of select="nom"/></td>
                            </xsl:when>
                        </xsl:choose>
                        </tr>
                    </xsl:for-each>
                </table>
                <br/><br/>
                <h2 style="color: purple;" align="center">Région d'Alola (Septième génération)</h2>
                <table border="2" align="center">
                    <tr style="color: purple;">
                        <th>Pokémon</th>
                        <th>Nom</th>
                    </tr>
                    <xsl:for-each select="pokedex/pokemon">
                        <tr>
                        <xsl:choose>
                            <xsl:when test="@id[. &gt; 722 and . &lt; 807]">
                                <td><xsl:apply-templates select="image"/></td>
                                <td><xsl:value-of select="nom"/></td>
                            </xsl:when>
                        </xsl:choose>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="image">
        <img src="{@url}" width="150"/>
    </xsl:template>

</xsl:stylesheet>
